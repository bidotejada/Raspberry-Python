import RPi.GPIO as GPIO
from time import sleep


def main():
    LED = 18

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)  # GPIO names
    # GPIO.setmode(GPIO.BOARD) # pin names
    GPIO.setup(LED, GPIO.OUT, initial=1)  # initial (0 or 1)

    for i in range(15):
        GPIO.output(LED, GPIO.LOW)
        sleep(.1)
        GPIO.output(LED, GPIO.HIGH)
        sleep(.3)


# clean up on exit
'''
	Useful if GPIO pin stays on.
	Turns it back of.
'''
if __name__ == '__main__':
    try:
        main()
        GPIO.cleanup()
    except KeyboardInterrupt:
        print(' - Interrupted')  # if CTRL+C is pressed, exit cleanly
        GPIO.cleanup()  # clean up all GPIO
