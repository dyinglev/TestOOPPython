from tkinter import *


class MainWindow:
    """Главное окно программы"""

    def __init__(self):
        """Инициализация главного окна"""
        main_win = Tk()

        l = Label(main_win, text='Hola')
        l.pack()
        main_win.mainloop()
