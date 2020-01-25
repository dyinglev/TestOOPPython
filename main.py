from libs.EnterForm import EnterForm
from libs.Db import DataBase
from tkinter import messagebox


def check_app():
    """Проверка приложения"""
    db = DataBase()
    if not db.check_db(): # Проверка БД на доступность
        messagebox.showerror('Ошибка', 'Нет соединения с удаленной базой данных!\nПрограмма будет закрыта!')
    else:
        # Запуск формы входа
        EnterForm()


check_app()
