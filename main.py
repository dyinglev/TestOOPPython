from tkinter import *
import sys

root = Tk()
top = Toplevel()

entry1 = Entry(top)
entry2 = Entry(top)
button1 = Button(top, text="Login", command=lambda:command1())
button2 = Button(top, text="Cancel", command=lambda:command2())
label1 = Label(root, text="This is your main window and you can input anything you want here")

def command1():
    if entry1.get() == "user" and entry2.get() == "password":
        root.deiconify()
        top.destroy()

def command2():
    top.destroy()
    root.destroy()
    sys.exit()


entry1.pack()
entry2.pack()
button1.pack()
button2.pack()
label1.pack()

root.withdraw()
root.mainloop()