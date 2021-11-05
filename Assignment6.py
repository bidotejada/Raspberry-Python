import RPi.GPIO as GPIO
from time import sleep

red_led = 23
green_led = 24
PHOTOCELL_PIN = 18
SERVO_PIN = 17
FREQ = 50

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(PHOTOCELL_PIN, GPIO.IN)

SERVO_OUTPUT = GPIO.PWM(SERVO_PIN, FREQ)
SERVO_OUTPUT.start(2.5)

try:
    while True:
        print(f'input: {GPIO.input(PHOTOCELL_PIN)}')
        if GPIO.input(PHOTOCELL_PIN):

            SERVO_OUTPUT.ChangeDutyCycle(2.5)
            GPIO.output(red_led, GPIO.HIGH)
            sleep(1)
            GPIO.output(red_led, GPIO.LOW)

        else:

            SERVO_OUTPUT.ChangeDutyCycle(12.5)
            GPIO.output(green_led, GPIO.HIGH)
            sleep(1)
            GPIO.output(green_led, GPIO.LOW)

except KeyboardInterrupt:
    SERVO_OUTPUT.stop()
finally:
    GPIO.cleanup()
