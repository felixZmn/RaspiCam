from numpy import interp
import RPi.GPIO as GPIO
import time
minValue = 4
midValue = 7.2
maxValue = 10


class Servo:
    def __init__(self, servoPIN):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)
        self.p = GPIO.PWM(servoPIN, 50)
        self.p.start(midValue)

    def __del__(self):
        self.p.stop()
        GPIO.cleanup()

    def move(self, position):
        value = interp(position, [0, 100], [minValue, maxValue])
        self.p.ChangeDutyCycle(value)
        time.sleep(0.1)
