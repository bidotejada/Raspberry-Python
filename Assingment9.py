from tkinter import *
from os.path import exists
from gpiozero import RGBLED
import json

# BCM GPIOs used by gpiozero module
# gpiozero is a higher level implementation of the RPi.GPIO module
# that has an overall cleaner code and provides easy access to GPIO pins.

RED = 17
GREEN = 27
BLUE = 22

# assigning pins to RGB LED
led = RGBLED(RED, GREEN, BLUE)

# creating save file
settings_file_name = "LEDToggleConfig.json"
rt_vars = dict()
if exists(settings_file_name):
    # Load configuration information if it exists
    file = open(settings_file_name, 'r')
    rt_vars_text = file.read()
    rt_vars = json.loads(rt_vars_text)
    led.color = (rt_vars['LEDState'][0], rt_vars['LEDState']
                 [1], rt_vars['LEDState'][2])
else:
    # Initialize Default Values
    rt_vars["LEDState"] = (0, 0, 0)
    # save Default Values
    rt_vars_json = json.dumps(rt_vars)
    file = open(settings_file_name, "w")
    file.write(rt_vars_json)
    file.close()

# this function puts the users input to action
# turning LED different colors


def activate_color():
    global rt_vars
    global led
    LEDState = rt_vars["LEDState"]
    led.color = (red.get()/100, green.get()/100, blue.get()/100)
    rt_vars['LEDState'] = (red.get()/100, green.get()/100, blue.get()/100)
    print(
        f'Activated color: {rt_vars["LEDState"]}')

# this function saves current state to save file
# and exits the GUI


def save_exit():
    global rt_vars
    print(f'Saved values: {rt_vars}')
    file = open(settings_file_name, "w")
    rt_vars_json = json.dumps(rt_vars)
    file.write(rt_vars_json)
    file.close()
    root.destroy()


# main window
root = Tk()

# starting window size
root.geometry('425x300')

# window title
root.title('LED light show')

title_label = Label(text='Move sliders to change the LED color')
title_label.pack(side=TOP)

# label frame
frame1 = Frame(root)
frame1.pack(side=TOP)

red_label = Label(frame1, text='Red')
red_label.pack(side=LEFT, padx=10, pady=10)

green_label = Label(frame1, text='Green')
green_label.pack(side=LEFT, padx=10, pady=10)

blue_label = Label(frame1, text='Blue')
blue_label.pack(side=LEFT, padx=10, pady=10)

# sliders frame
frame2 = Frame(root)
frame2.pack(side=TOP)

red = Scale(frame2, from_=100, to=0, orient=VERTICAL)
red.pack(padx=5, pady=10, side=LEFT)

green = Scale(frame2, from_=100, to=0, orient=VERTICAL)
green.pack(padx=5, pady=10, side=LEFT)

blue = Scale(frame2, from_=100, to=0, orient=VERTICAL)
blue.pack(padx=5, pady=10, side=LEFT)

# sets initial value if any was saved
# if not sets default starting value of 0 (zero)
red.set(rt_vars['LEDState'][0]*100)
green.set(rt_vars['LEDState'][1]*100)
blue.set(rt_vars['LEDState'][2]*100)

activate_btn = Button(text='Activate..', command=lambda: activate_color())
activate_btn.pack()

# save/exit functions frame
frame3 = Frame(root)
frame3.pack(side=BOTTOM)

save_val = Button(frame3, text='Save & Exit', command=lambda: save_exit())
save_val.pack(side=LEFT)

# launch main window
root.mainloop()
