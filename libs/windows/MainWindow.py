from tkinter import *
from tkinter import ttk
from libs.Config.Settings import Settings
from libs.Classes.Db import DataBase


class MainWindow:
    """Главное окно программы"""

    def __init__(self, active_user):
        """Инициализация главного окна"""
        self.user = active_user

        # Инициализация главного окна
        self.main_win = Tk()
        self.main_win.title(Settings().TITLE + ' Version: ' + Settings().VERSION)
        self.main_win.iconbitmap(Settings().FAVICON)
        self.main_win.resizable(False, False)

        # Центрироване окна
        width = self.main_win.winfo_screenwidth()
        height = self.main_win.winfo_screenheight()
        self.main_win.geometry(f'700x500+{width // 2 - 350}+{height // 2 - 250}')

        # Меню
        self.menubar = Menu(self.main_win)
        self.main_win.config(menu=self.menubar)
        # Файл
        file_menu = Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="Сменить пользователя", command=self.change_user)
        file_menu.add_command(label="Выйти", command=self.on_exit)
        self.menubar.add_cascade(label="Файл", menu=file_menu)

        # Вкладки
        rows = 0
        while rows < 50:
            self.main_win.rowconfigure(rows, weight=1)
            self.main_win.columnconfigure(rows, weight=1)
            rows += 1
        tabs = ttk.Notebook(self.main_win)
        tabs.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

        # Вкладка Список дел
        todo_win = ttk.Frame(tabs)
        tabs.add(todo_win, text='Список дел')
        todo_win_rows = 0
        while todo_win_rows < 50:
            todo_win.rowconfigure(todo_win_rows, weight=1)
            todo_win.columnconfigure(todo_win_rows, weight=1)
            todo_win_rows += 1
        tabs_todo = ttk.Notebook(todo_win)
        tabs_todo.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
        current_task = ttk.Frame(tabs_todo)
        # Текущие
        tabs_todo.add(current_task, text='Текущие')

        # Выполненные
        done_task = ttk.Frame(tabs_todo)
        tabs_todo.add(done_task, text='Выполненные')
        tasks = self.get_tasks_by_user_id(10)
        task_y = 10
        task_i = 1
        for task in tasks:
            text = str(task_i) + '. ' + task['text'][:30]
            if len(task['text']) > 30:
                text += '...'
            l = Label(current_task, text=text).place(x=10, y=task_y)
            task_y += 30
            task_i += 1

        # Вкладка Бухгалтер
        accountant_win = ttk.Frame(tabs)
        tabs.add(accountant_win, text='Финансы')

        # Запуск
        self.main_win.mainloop()

    def get_tasks_by_user_id(self, count):
        query = 'SELECT * FROM `tasks` WHERE `user_id` = ' + str(self.user['id']) + ' LIMIT ' + str(count)
        return DataBase().select(query, 'all')

    def on_exit(self):
        self.main_win.destroy()

    def change_user(self):
        from libs.windows.EnterForm import EnterForm
        del self.user
        self.main_win.destroy()
        EnterForm()
