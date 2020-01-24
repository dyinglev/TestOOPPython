from tkinter import *
from libs.MainWindow import MainWindow


class EnterForm:
    def __init__(self, parent_root):
        self.top = Toplevel()
        self.parent_root = parent_root

        # Создаем 2 поля ввода и 2 кнопки
        self.login = Entry(self.top)
        self.password = Entry(self.top)
        self.btn_sign_in = Button(self.top, text="Login", command=lambda: self.sign_in())
        self.btn_cancel = Button(self.top, text="Cancel", command=lambda: self.exit_program())

        # Размещаем все это
        self.login.pack()
        self.password.pack()
        self.btn_sign_in.pack()
        self.btn_cancel.pack()

    def sign_in(self):
        if self.login.get() == "user" and self.password.get() == "password":
            self.parent_root.deiconify()
            self.top.destroy()
            MainWindow.start_program()

    def exit_program(self):
        self.top.destroy()
        self.parent_root.destroy()
        sys.exit()
