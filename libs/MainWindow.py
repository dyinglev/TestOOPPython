from tkinter import *


class MainWindow:
    def __init__(self):
        main_win = Tk()

        l = Label(main_win, text='Hola')
        l.pack()
        main_win.mainloop()
