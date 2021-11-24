from posixpath import commonpath
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo
import json
import os
from os.path import exists
from time import sleep
from gpiozero import LED
from signal import pause

led = LED(17)

LED_state = True


def LED_toggle():
    if LED_state == True:
        led.off()
        LED_state = False
    else:
        led.on()
        LED_state = True


# config file configuration
settings_file_name = 'LED_saved_values.json'

root = Tk()
root.geometry('500x500')
root.title('LED Toggle GUI')

label1 = Label(root, text='Press the buttons for magic')
label1.pack()

btn1 = Button(root, text='Turn on LED', command=lambda: print('LED on'))
btn1.pack()

btn2 = Button(root, text='Turn off LED', command=lambda: print('LED off'))
btn2.pack()

btn1.configure(text='changed text')

root.mainloop()
