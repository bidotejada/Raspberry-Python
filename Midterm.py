import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime


red_led = 17
green_led = 27
blue_led = 22
buzzer = 25
button1 = 23
button2 = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)

GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(buzzer, GPIO.OUT)


lights = [red_led, green_led, blue_led]
while True:
    times_pressed = 0
    timing = 0
    if GPIO.input(button1):
        GPIO.output(buzzer, GPIO.LOW)
    else:
        GPIO.output(buzzer, GPIO.HIGH)
        sleep(.8)
        GPIO.output(buzzer, GPIO.LOW)

        initial_time = float(datetime.now().time().strftime('%S'))
        end_time = float(datetime.now().time().strftime('%S'))
        time_elapsed = 0
        while True:
            if GPIO.input(button2):
                pass
            else:
                times_pressed += 1
            end_time = float(datetime.now().time().strftime('%S'))
            time_elapsed = (end_time-initial_time)
            print(f'time elapsed: {time_elapsed}')
            if time_elapsed > 5:
                time_elapsed = 0
                break
            sleep(.18)

        GPIO.output(buzzer, GPIO.HIGH)
        sleep(.8)
        GPIO.output(buzzer, GPIO.LOW)

    light = 0
    print(f'times pressed: {times_pressed}')
    for _ in range(times_pressed):
        if light > 2:
            light = 0
        GPIO.output(lights[light], GPIO.HIGH)
        sleep(.6)
        GPIO.output(lights[light], GPIO.LOW)
        sleep(.4)
        light += 1


GPIO.cleaup()
