from tkinter import *
from libs.User import User
from libs.MainWindow import MainWindow


class EnterForm:
    """Работа с формой входа"""

    def __init__(self):
        """Инициализация формы входа"""
        self.sign_in_form = Tk()
        self.sign_in_form.title('Вход')
        self.sign_in_form.resizable(False, False)
        width = self.sign_in_form.winfo_screenwidth()
        height = self.sign_in_form.winfo_screenheight()
        self.sign_in_form.geometry(f'300x150+{width // 2 - 150}+{height // 2 - 85}')  # Центрироване окна

        self.user = User()

        self.label_enter = Label(self.sign_in_form, text='Войдите в Yogify', bg='#1e90ff', fg='#fff', font=15, width=34, pady=10)

        self.label_login = Label(self.sign_in_form, text='Логин')
        self.login = Entry(self.sign_in_form)
        self.label_password = Label(self.sign_in_form, text='Пароль')
        self.password = Entry(self.sign_in_form)
        self.btn_sign_in = Button(self.sign_in_form, text='Enter', command=self.check_userdata)

        self.label_enter.place(relx=0.5, anchor='n')
        # self.label_login.place(row=1, column=0)
        # self.login.place(row=1, column=1)
        # self.label_password.place(row=2, column=0)
        # self.password.place(row=2, column=1)
        # self.btn_sign_in.place(row=3, column=0, columnspan=2)

        self.sign_in_form.mainloop()

    def check_userdata(self):
        """Проверка введенных данных пользователя"""
        user = self.user.get_test_user()
        if user['login'] == self.login.get():
            self.sign_in_form.destroy()
            MainWindow()
        else:
            print(user['login'])
