from tkinter import *
# from tkinter.ttk import *
from tkinter.messagebox import showinfo
from os.path import exists
from time import sleep
from gpiozero import RGBLED
# from signal import pause
import json
import RPi.GPIO as GPIO
import sys
import digitalio
import board
import adafruit_matrixkeypad
from cryptography.fernet import Fernet
import base64

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# LED BCM/GPIO pins
RED = 17
GREEN = 27
BLUE = 22

led = RGBLED(RED, GREEN, BLUE)
led.color = (0, 0, 1)

# creating save file
settings_file_name = "encrypted_password.json"
rt_vars = dict()
if exists(settings_file_name):
    # Load configuration information if it exists
    file = open(settings_file_name, 'r')
    rt_vars_text = file.read()
    rt_vars = json.loads(rt_vars_text)
    # led.color = (rt_vars['LEDState'][0], rt_vars['LEDState']
    #              [1], rt_vars['LEDState'][2])
    led.color = rt_vars["LEDState"]
    password = rt_vars["passcode"]
    lock_state = rt_vars["lock_state"]
else:
    # Initialize Default Values
    rt_vars["LEDState"] = (0, 0, 1)
    rt_vars["passcode"] = "0000"
    rt_vars["lock_state"] = "locked"
    # save Default Values
    rt_vars_json = json.dumps(rt_vars)
    file = open(settings_file_name, "w")
    file.write(rt_vars_json)
    file.close()

# LED flash red, turn green, or turn blue


def led_action(type):
    if type == "error":
        led.color = (1, 0, 0)
        sleep(.5)
        led.color = (0, 0, 0)
        sleep(.5)
        led.color = (1, 0, 0)
        sleep(.5)
        led.color = (0, 0, 0)
    elif type == "good":
        pass
    elif type == "wait":
        pass
    else:
        pass


def btn_action(option):
    if option == "lock":
        if rt_vars["lock_state"] == 'locked':
            print('The safe is already locked!!')
        else:
            led.color = (0, 0, 1)
    elif option == "unlock":
        if rt_vars["lock_state"] == 'unlocked':
            print('The safe is already unlocked!!')
        else:
            led.color = (0, 1, 0)
    elif option == "change":
        led.color = (0, 0, 0)
    else:
        pass


# encryption section
key = b'Q19rhxzv0FxMzg0o_E8SA_5rTl8__t1ZgN7XdI_L_6I='
# cipher suite
fernet = Fernet(key)
password = "0000"
encrypted_password = fernet.encrypt(password.encode())
decrypted_password = fernet.decrypt(encrypted_password).decode()


cols = [digitalio.DigitalInOut(x) for x in (10, 9, 11, 5)]
rows = [digitalio.DigitalInOut(x) for x in (6, 13, 19, 26)]

keys = ((1, 2, 3, "A"),
        (4, 5, 6, "B"),
        (7, 8, 9, "C"),
        ("*", 0, "#", "D"))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

code_entered = list()
while True:
    keys = keypad.pressed_keys
    if keys:
        code_entered.append(keys)
        print("Pressed: ", keys)
        if len(code_entered) == 4:
            break
    sleep(0.1)

actions = ['lock', 'unlock', 'change', 'error', 'good', 'wait']

root = Tk()

root.geometry('425x300')
root.title("Lock Security System (Encrypted)")

label1 = Label(root, text='Press the buttons to perform an action of the lock')
label1.pack()

# lock_btn = Button(root, text='Lock', command=lambda: lock())
# lock_btn.pack()
# unlock_btn = Button(root, text='Unlock', command=lambda: unlock())
# unlock_btn.pack()
# code_btn = Button(root, text='Change Passcode',
#                   command=lambda: change_passcode())
# code_btn.pack()

lock_btn = Button(root, text='Lock', command=lambda: btn_action(actions[0]))
lock_btn.pack()
unlock_btn = Button(root, text='Unlock',
                    command=lambda: btn_action(actions[1]))
unlock_btn.pack()
code_btn = Button(root, text='Change Passcode',
                  command=lambda: btn_action(actions[2]))
code_btn.pack()


root.mainloop()
