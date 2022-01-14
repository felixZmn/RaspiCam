# Web streaming example
# Source code from the official PiCamera package
# http://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming

import io
from lib2to3.pgen2.token import NUMBER
from tokenize import Double
import picamera
import logging
import socketserver
from threading import Condition
from http import server
from urllib import parse
from servo import Servo

servo1 = Servo(18)


class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)


class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header(
                'Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning('Removed streaming client %s: %s',
                                self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()

    def do_POST(self):
        if self.path.startswith('/servo/'):
            id = int(self.path[7])
            degrees = float(parse.parse_qs(
                parse.urlparse(self.path).query)['degrees'][0])

            if id != 0 and id != 1 or (degrees < 0 or degrees > 100):
                self.send_response(400)
                self.end_headers()
                return
            print("move motor to: ", degrees)

            servo1.move(degrees)
            self.send_response(200)
            self.end_headers()

        else:
            self.send_error(404)
            self.end_headers()


class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


with picamera.PiCamera(resolution='1920x1080', framerate=30) as camera:
    output = StreamingOutput()
    # Uncomment the next line to change your Pi's Camera rotation (in degrees)
    camera.rotation = 180
    camera.start_recording(output, format='mjpeg')
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        camera.stop_recording()
