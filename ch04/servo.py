import RPi.GPIO as GPIO
from time import sleep

import servo

pin = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

def setAngle(angle):
    duty = 2.5 + 10 * angle / 180
    print(f"degree : {angle} to {duty}(duty)")
    servo.ChangeDutyCycle(duty)

if __name__ == "__main__":
    servo.start(0)
    setAngle(0)
    sleep(1)
    setAngle(90)
    sleep(1)
    setAngle(50)
    sleep(1)
    setAngle(120)
    sleep(1)
    setAngle(180)
    sleep(1)
    servo.stop()
    GPIO.cleanup()