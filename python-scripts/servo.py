from numpy import interp
from PCA9685 import PCA9685 as servoDriver
import time
minValue = 350
maxValue = 2700
midValue = minValue + (maxValue - minValue)


class Servo:
    def __init__(self, servoChannel):
        self.servoChannel = servoChannel
        servo = servoDriver(0x40)
        servo.setPWMFreq(50)
        servo.setPWM(servoChannel, 0, 1024)
        servo.setServoPulse(servoChannel, midValue)  # 1500 is centered
        self.servo = servo

    def move(self, position):
        value = interp(position, [0, 100], [minValue, maxValue])
        self.servo.setServoPulse(self.servoChannel, value)
