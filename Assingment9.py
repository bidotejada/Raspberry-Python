from tkinter import *
# from tkinter.ttk import *
from tkinter.messagebox import showinfo

# main window
root = Tk()

root.geometry('425x300')

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

# save functions frame
frame3 = Frame(root)
frame3.pack(side=BOTTOM)

save_val = Button(frame3, text='Save values', command=lambda: print(
    red.get(), green.get(), blue.get()))
save_val.pack(side=LEFT)

display_saved = Button(frame3, text='Display Saved', command=lambda: showinfo(
    title='Saved Vals', message=f'Red: {red.get()}\nGreen: {green.get()}\nBlue: {blue.get()}'))
display_saved.pack(side=RIGHT)

# launch main window
root.mainloop()
