import RPi.GPIO as GPIO
from time import sleep
from random import randint


class Color:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    RED = 17
    GREEN = 27
    BLUE = 22

    FREQ = 100

    GPIO.setup(RED, GPIO.OUT, initial=0)
    GPIO.setup(GREEN, GPIO.OUT, initial=0)
    GPIO.setup(BLUE, GPIO.OUT, initial=0)

    pwm1 = GPIO.PWM(RED, FREQ)
    pwm2 = GPIO.PWM(GREEN, FREQ)
    pwm3 = GPIO.PWM(BLUE, FREQ)

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def display_color(self):
        Color.pwm1.start(self.red)
        Color.pwm2.start(self.green)
        Color.pwm3.start(self.blue)

    @staticmethod
    def turn_off():
        Color.pwm1.stop()
        Color.pwm2.stop()
        Color.pwm3.stop()


def main():
    while True:
        red = randint(1, 100)
        green = randint(1, 100)
        blue = randint(1, 100)
        print(f'red: {red}\ngreen: {green}\nblue: {blue}\n\n')
        color_red = Color(red, green, blue)
        color_red.display_color()
        sleep(.5)

        # color_green = Color(1, 100, 1)
        # color_green.display_color()
        # sleep(2)

        # color_blue = Color(1, 1, 100)
        # color_blue.display_color()
        # sleep(2)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        Color.turn_off()
        print(' - Interrupted')
    finally:
        GPIO.cleanup()
