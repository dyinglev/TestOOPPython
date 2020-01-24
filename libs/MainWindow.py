from tkinter import *
from libs.EnterForm import EnterForm


class MainWindow:
    def __init__(self, root):
        self.root = root
        EnterForm(self.root, self.start_program)

        self.label1 = Label(self.root, text="This is your main window and you can input anything you want here")
        self.label1.pack()

    def start_program(self, q):
        print('hello')


root = Tk()
mw = MainWindow(root)
root.withdraw()
root.mainloop()
