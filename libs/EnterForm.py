from tkinter import Tk, Label, Button
from tkinter import ttk
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
        # Центрироване окна
        self.sign_in_form.geometry(f'300x180+{width // 2 - 150}+{height // 2 - 100}')

        self.user = User()

        # Объявление виджетов
        self.label_enter = Label(self.sign_in_form, text='Войдите в Yogify', bg='#1e90ff', fg='#fff', font=15, width=34, pady=10)
        self.label_login = Label(self.sign_in_form, text='Логин')
        self.login = ttk.Entry(self.sign_in_form, width=30)
        self.login.focus_set()
        self.label_password = Label(self.sign_in_form, text='Пароль')
        self.password = ttk.Entry(self.sign_in_form, width=30)
        self.btn_sign_in = ttk.Button(self.sign_in_form, text='Войти', command=self.check_userdata, width='14')

        # Расстановка виджетов
        self.label_enter.place(relx=0.5, anchor='n')
        self.label_login.place(x=75, y=70, anchor='e')
        self.login.place(x=80, y=70, anchor='w')
        self.label_password.place(x=75, y=100, anchor='e')
        self.password.place(x=80, y=100, anchor='w')
        self.btn_sign_in.place(relx=0.5, y=130, anchor='n')

        self.sign_in_form.mainloop()

    def check_userdata(self):
        """Проверка введенных данных пользователя"""
        user = self.user.get_test_user()
        if user['login'] == self.login.get():
            self.sign_in_form.destroy()
            MainWindow()
        else:
            print(user['login'])
