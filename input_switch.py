import RPi.GPIO as GPIO
import time

LED = 18
SWITCH = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SWITCH, GPIO.IN)
# GPIO.setup(SWITCH, GPIO.IN,  pull_up_down = GPIO.PUD_DOWN) # input with pull-down
# GPIO.setup(SWITCH, GPIO.IN,  pull_up_down = GPIO.PUD_UP)   # input with pull-up


# pull-up resistor configuration
while True:
    # Read status of input GPIO pin (logic level 0 or 1 "True" "False")
    if GPIO.input(SWITCH):
        # if switch is not pressed
        GPIO.output(LED, GPIO.LOW)
    else:
        ## switch is pressed
        GPIO.output(LED, GPIO.HIGH)
