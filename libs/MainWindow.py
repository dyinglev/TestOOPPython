from tkinter import *
from libs.EnterForm import EnterForm


class MainWindow:
    def __init__(self):
        self.root = Tk()

        EnterForm(self.root)

        self.label1 = Label(self.root, text="This is your main window and you can input anything you want here")
        self.label1.pack()

        self.root.withdraw()
        self.root.mainloop()

    def start_program(self):
        print('hello')
