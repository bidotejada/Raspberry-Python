import RPi.GPIO as GPIO
import time

LED = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # GPIO names
# GPIO.setmode(GPIO.BOARD) # pin names
GPIO.setup(LED, GPIO.OUT, initial=1)  # initial (0 or 1)

for i in range(60):
    GPIO.output(LED, GPIO.LOW)
    time.sleep(.1)
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(.3)

# clean up on exit
'''
	Useful if GPIO pin stays on.
	Turns it back of.
'''
GPIO.cleanup()
