from tkinter import *
from tkinter.ttk import *

# launch a windowwith the object name of canvas(window)

canvas = Tk()
canvas.geometry('500x500')

# naming the main canvas
canvas.title('test gui window')

# add a label to the canvas
label = Label(canvas, text='Hello, world!').pack()

frame = Frame(canvas)
# geometry method
frame.pack()

# create a button with a label
# terminates window
button = Button(frame, text='click me!', command=canvas.destroy)
button.pack()

# create a label
label1 = Label(frame, text='you won\'t')
label1.pack()
entry = Entry(frame, text='yes').pack()
# call the main loop to run the program
canvas.mainloop()
