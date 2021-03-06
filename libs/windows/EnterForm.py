from tkinter import Tk, Label, ttk, messagebox
from libs.Classes.User import User
from libs.windows.MainWindow import MainWindow
from libs.Config.Settings import Settings


class EnterForm:
    """Работа с формой входа"""

    def __init__(self):
        """Инициализация класса"""
        # Объекты необходимых классов
        self.user = User()

        # Инициализация формы входа
        self.sign_in_form = Tk()
        self.sign_in_form.title('Вход')
        self.sign_in_form.iconbitmap(Settings().FAVICON)
        self.sign_in_form.resizable(False, False)

        # Центрироване окна
        width = self.sign_in_form.winfo_screenwidth()
        height = self.sign_in_form.winfo_screenheight()
        self.sign_in_form.geometry(f'300x170+{width // 2 - 150}+{height // 2 - 100}')

        # Объявление виджетов
        self.label_enter = Label(self.sign_in_form, text='Войдите в Yogify', bg='#1e90ff', fg='#fff', font=15, width=34,
                                 pady=10)
        self.label_login = Label(self.sign_in_form, text='Логин')
        self.login = ttk.Entry(self.sign_in_form, width=30)
        self.login.focus_set()
        self.label_password = Label(self.sign_in_form, text='Пароль')
        self.password = ttk.Entry(self.sign_in_form, width=30, show='*')
        self.btn_sign_in = ttk.Button(self.sign_in_form, text='Войти', command=self.check_userdata, width='14')

        # Расстановка виджетов
        self.label_enter.place(relx=0.5, anchor='n')
        self.label_login.place(x=75, y=70, anchor='e')
        self.login.place(x=80, y=70, anchor='w')
        self.label_password.place(x=75, y=100, anchor='e')
        self.password.place(x=80, y=100, anchor='w')
        self.btn_sign_in.place(relx=0.5, y=130, anchor='n')

        # Запуск
        self.sign_in_form.mainloop()

    def check_userdata(self):
        """Проверка введенных данных пользователя"""
        # user = self.user.get_test_user()
        if self.login.get == '' or self.password.get() == '':
            messagebox.showerror('Ошибка входа', 'Заполните оба поля!')
        else:
            user = self.user.get_user_by_login_and_password(self.login.get(), self.password.get())
            if not user:
                messagebox.showerror('Ошибка входа', 'Неправильное имя пользователя или пароль')
            else:
                if user['username'] == self.login.get() and user['password'] == self.password.get():
                    self.sign_in_form.destroy()
                    MainWindow(user)
                else:
                    messagebox.showerror('Ошибка входа', 'Неправильное имя пользователя или пароль')
