import RPi.GPIO as GPIO
import time
servoPIN = 18

# min 4
# mid 7.5
# max 10
servoPositions = [4, 5, 7.5, 10]


def setServoCycle(p, position):
    p.ChangeDutyCycle(position)
    # eine Pause von 0,5 Sekunden
    time.sleep(1)


try:
    # damit wir den GPIO Pin ueber die Nummer referenzieren koennen
    GPIO.setmode(GPIO.BCM)
    # setzen des GPIO Pins als Ausgang
    GPIO.setup(servoPIN, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50)  # GPIO als PWM mit 50Hz
    pos = 4
    p.start(pos)
    setServoCycle(p, pos)
except KeyboardInterrupt:
    p.stop()
    # alle Pins zuruecksetzen
    GPIO.cleanup()
