import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT, initial=0)

pwm = GPIO.PWM(18, 1000)
pwm.start(75)

time.sleep(2)

pwm.ChangeDutyCycle(5)

time.sleep(2)

pwm.stop()

time.sleep(2)

GPIO.output(18, GPIO.HIGH)
time.sleep(1)

GPIO.cleanup()
