from tkinter import *
# from tkinter.ttk import *
from tkinter.messagebox import showinfo
from os.path import exists
from time import sleep
from gpiozero import RGBLED
# from signal import pause
import json

import digitalio
import board
import adafruit_matrixkeypad

# LED GPIO pins
RED = 17
GREEN = 27
BLUE = 22

cols = [digitalio.DigitalInOut(x) for x in (board.D26, board.D20, board.D21)]
rows = [digitalio.DigitalInOut(x) for x in (
    board.D5, board.D6, board.D13, board.D19)]

keys = ((1, 2, 3, 'A'),
        (4, 5, 6, 'B'),
        (7, 8, 9, 'C'),
        ("*", 0, "#", 'D'))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

while True:
    keys = keypad.pressed_keys
    if keys:
        print("Pressed: ", keys)
    sleep(0.1)

