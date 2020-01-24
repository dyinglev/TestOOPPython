from tkinter import *
import sys

class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.top = Toplevel()

        self.entry1 = Entry(self.top)
        self.entry2 = Entry(self.top)
        self.button1 = Button(self.top, text="Login", command=lambda: self.command1())
        self.button2 = Button(self.top, text="Cancel", command=lambda: self.command2())
        self.label1 = Label(self.root, text="This is your main window and you can input anything you want here")
        self.entry1.pack()
        self.entry2.pack()
        self.button1.pack()
        self.button2.pack()
        self.label1.pack()

        self.root.withdraw()
        self.root.mainloop()

    def command1(self):
        if self.entry1.get() == "user" and self.entry2.get() == "password":
            self.root.deiconify()
            self.top.destroy()

    def command2(self):
        self.top.destroy()
        self.root.destroy()
        sys.exit()


