import RPi.GPIO as GPIO
import time
# servoPIN = 18

minValue = 4
midValue = 7.2
maxValue = 10
# servoPositions = [4, 7.2, 10]


def setServoCycle(p, position):
    p.ChangeDutyCycle(position)
    # eine Pause von 0,5 Sekunden
    time.sleep(0.5)


class Servo:
    def __init__(self, servoPIN):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)
        self.p = GPIO.PWM(servoPIN, 250)
        self.p.start(midValue)

    def __del__(self):
        self.p.stop()
        GPIO.cleanup()

    def move(self, position):
        # use position range from 0%-100% or -06 to 60
        if position < minValue or position > maxValue:
            return
        setServoCycle(self.p, position)
