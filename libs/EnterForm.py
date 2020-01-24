from tkinter import *
from libs.User import User
from libs.MainWindow import MainWindow


class EnterForm:
    def __init__(self):
        self.sign_in_form = Tk()
        self.user = User()

        self.login = Entry(self.sign_in_form)
        self.password = Entry(self.sign_in_form)
        self.btn_sign_in = Button(self.sign_in_form, text='Enter', command=self.check_userdata)
        self.login.pack()
        self.password.pack()
        self.btn_sign_in.pack()

        self.sign_in_form.mainloop()

    def check_userdata(self):
        user = self.user.get_test_user()
        if user['login'] == self.login.get():
            self.sign_in_form.destroy()
            MainWindow()
        else:
            print(user['login'])