import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
un=2
do=3
tre=4
cua=27
cinc=17
btnizq=22
btnder=14
GPIO.setup(btnizq, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btnder, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(un, GPIO.OUT)
GPIO.setup(do, GPIO.OUT)
GPIO.setup(tre, GPIO.OUT)
GPIO.setup(cua, GPIO.OUT)
GPIO.setup(cinc, GPIO.OUT)
i=0

def cero():
    GPIO.output(un, False)
    GPIO.output(do, False)
    GPIO.output(tre, False)
    GPIO.output(cua, False)
    GPIO.output(cinc, False)

def uno():
    GPIO.output(un, True)
    GPIO.output(do, False)
    GPIO.output(tre, False)
    GPIO.output(cua, False)
    GPIO.output(cinc, False)

def dos():
    GPIO.output(un, False)
    GPIO.output(do, True)
    GPIO.output(tre, False)
    GPIO.output(cua, False)
    GPIO.output(cinc, False)

def tres():
    GPIO.output(un, False)
    GPIO.output(do, False)
    GPIO.output(tre, True)
    GPIO.output(cua, False)
    GPIO.output(cinc, False)

def cuatro():
    GPIO.output(un, False)
    GPIO.output(do, False)
    GPIO.output(tre, False)
    GPIO.output(cua, True)
    GPIO.output(cinc, False)

def cinco():
    GPIO.output(un, False)
    GPIO.output(do, False)
    GPIO.output(tre, False)
    GPIO.output(cua, False)
    GPIO.output(cinc, True)

while True:
    time.sleep(0.5)
    estado1 = GPIO.input(btnizq)
    estado2 = GPIO.input(btnder)
    if (estado1 == False):
        i=i+1
    if (estado2 == False):
        i=i-1
    if(i == -1):
        i=0
    if(i == 0):
        cero()
    if (i == 1):
        uno()
    if (i == 2):
        dos()
    if (i == 3):
        tres()
    if (i == 4):
        cuatro()
    if (i == 5):
        cinco()
    if (i == 6):
        i=0