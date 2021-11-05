import RPi.GPIO as GPIO
from time import sleep
from random import randint, uniform


def blink_interval():
    """
    This function returns a float between 0 and 1 with 3 decimals
    of precision.
    """
    blink_time = round(uniform(0.000, 1.000), 3)  # 0.000 <= N <= 1.000
    print(f'{blink_time:.3f}', end=' | ')
    return blink_time


def main():
    """
    This is the main function. In here, a button is assigned to GPIO23 and an
    led is assigned to GPIO24 on a raspberry pi (40-pin variant). The internal
    pull-up resistor is used, enabled by software.

    The purpose of this program is to press the button and the led will blink
    a random amount of times and at a random blink-interval rate.
    """
    BUTTON = 23
    LED = 24

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED, GPIO.OUT, initial=0)

    # using internal pull-up resistor
    GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        flash_time = randint(5, 10)  # 5 <= N <= 10

        # if button is not pressed
        if GPIO.input(BUTTON):
            GPIO.output(LED, GPIO.LOW)
        # if button is pressed
        else:
            print(f'\nn flashes: {flash_time}')

            for i in range(flash_time):

                GPIO.output(LED, GPIO.HIGH)
                print(f'{i + 1}  | on time:', end=' ')
                sleep(blink_interval())

                GPIO.output(LED, GPIO.LOW)
                print('off time:', end=' ')
                sleep(blink_interval())
                print()
            print()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(' - Interrupted')
        GPIO.cleanup()
    finally:
        GPIO.cleanup()  # ensures clean exit (clears GPIO pins)
