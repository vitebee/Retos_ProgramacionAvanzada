import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pwmPin=18
GPIO.setup(pwmPin,GPIO.OUT)
pwm = GPIO.PWM(pwmPin,100)
pwm.start(0)

while True:
        count = 1
        while count < 100:
            pwm.ChangeDutyCycle(count)
            time.sleep(0.01)
            count=count+1
        while count>1:
            pwm.ChangeDutyCycle(count)
            time.sleep(0.01)
            pwm.ChangeDutyCycle(count)
            time.sleep(0.01)
            count=count-1