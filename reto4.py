import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ledR=2
ledG=3
GPIO.setup(ledR, GPIO.OUT)
GPIO.setup(ledG, GPIO.OUT)
GPIO.output(ledR, False)
GPIO.output(ledG, False)
a=[0,0,0]
b=[0,0,0,0,0]

while True:
    for i in range(len(a)):
        GPIO.output(ledR,True)
        time.sleep(0.5)
        GPIO.output(ledR,False)
        time.sleep(0.5)
    for i in range(len(b)):
        GPIO.output(ledG, True)
        time.sleep(0.5)
        GPIO.output(ledG, False)
        time.sleep(0.5)