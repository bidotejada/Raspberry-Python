import RPi.GPIO as GPIO
import time


def main():
    LED = 18

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED, GPIO.OUT, initial=0)

    while True:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(' - Interrupted')  # if CTRL+C is pressed, exit cleanly
        GPIO.cleanup()  # clean up all GPIO
        # pwm.stop() # stop PWM
