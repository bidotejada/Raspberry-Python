from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo

root = Tk()
root.geometry('500x500')

f_name = StringVar()
l_name = StringVar()
display_gender = StringVar()

root.title('Submit User Info')
title_frame = Frame(root)
title_frame.pack()

label = Label(title_frame, text='Hello, world!', anchor=W)
label.pack(side=LEFT)

label2 = Label(title_frame, text='and galaxy', anchor=E)
label2.pack(side=RIGHT)


name_frame = Frame(root)
name_frame.pack()

gender_frame = Frame(root)
gender_frame.pack()


button = Button(root, text='Exit window...', command=root.destroy)
button.pack(side=BOTTOM)

fname_label = Label(name_frame, text='First name:')
fname_label.pack()

fname_entry = Entry(name_frame, textvariable=f_name)
fname_entry.pack()

lname_label = Label(name_frame, text='Last name:')
lname_label.pack()

lname_entry = Entry(name_frame, textvariable=l_name)
lname_entry.pack()

gender_label = Label(gender_frame, text='Gender:')
gender_label.pack()


genders = [['Male', 'M'],
           ['Female', 'F']]

for gender in genders:
    btn = Radiobutton(
        gender_frame,
        text=gender[0],
        value=gender[1],
        variable=display_gender
    )
    btn.pack(fill='x', padx=5, pady=5)

submit_frame = Frame(root)
submit_frame.pack()

submit_btn = Button(submit_frame,
                    text='Submit info',
                    command=lambda: showinfo(
                        title='Submit message',
                        message=f'First name: {f_name.get()}\nLast name: {l_name.get()}\nGender: {display_gender.get()}'
                    )
                    )
submit_btn.pack()

root.mainloop()
