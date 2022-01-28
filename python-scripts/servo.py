from numpy import interp
import RPi.GPIO as GPIO
import PCA9685 as servoDriver
import time
minValue = 900
maxValue = 2100
midValue = minValue + (maxValue -minValue)



class Servo:
    def __init__(self, servoChannel):
        self.servoChannel = servoChannel
        servo = servoDriver(0x40)
        servo.setPWMFreq(50)
        servo.setPWm(servoChannel, 0, 1024)
        servo.setServoPulse(servoChannel, midValue)  # 1500 is centered
        self.servo = servo
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(servoChannel, GPIO.OUT)
        #self.p = GPIO.PWM(servoChannel, 50)
        #self.p.start()
        

    def __del__(self):
        #self.p.stop()
        #GPIO.cleanup()
        return 0

    def move(self, position):
        value = interp(position, [0, 100], [minValue, maxValue])
        self.servo.setServoPulse(self.servoChannel, value)
        #self.p.ChangeDutyCycle(value)
        time.sleep(0.1)
