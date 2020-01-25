from libs.EnterForm import EnterForm
from libs.Db import DataBase
from tkinter import messagebox


def check_app():
    db = DataBase()
    if not db.check_db():
        messagebox.showerror('Ошибка', 'Нет соединения с интернетом!\nПрограмма будет закрыта!')
    else:
        # Запуск формы входа
        EnterForm()


check_app()
