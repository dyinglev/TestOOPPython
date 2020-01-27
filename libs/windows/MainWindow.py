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

        # Текущие
        current_task = ttk.Frame(tabs_todo)
        tabs_todo.add(current_task, text='Текущие')
        btn_add_task = ttk.Button(current_task, text='Добавить задачу', command=self.add_task)
        btn_add_task.grid(row=0, column=0, pady=20, padx=10, sticky=N)
        tasks_listbox = Listbox(current_task)
        tasks = self.get_tasks_by_user_id(10)
        if not tasks:
            Label(current_task, text='Задач пока нет...').grid(row=1, column=0, columnspan=2)
        else:
            task_i = 1
            for task in tasks:
                text = str(task_i) + '. ' + task['text'][:30]
                if len(task['text']) > 30:
                    text += '...'
                if task['priority'] == 1:
                    text = '* ' + text
                tasks_listbox.insert(END, text)
                task_i += 1
            tasks_listbox.grid(row=1, column=0, sticky=N+S+W+E)
            tasks_listbox.bind("<<ListboxSelect>>", self.edit_task)
        textarea_task = Text(current_task)
        textarea_task.grid(row=0, rowspan=2, column=1, columnspan=3, sticky=N+S+W+E)
        btn_save = ttk.Button(current_task, text='Сохранить')
        btn_delete = ttk.Button(current_task, text='Удалить')
        btn_complete = ttk.Button(current_task, text='Выполнено')
        btn_save.grid(row=2, column=1)
        btn_delete.grid(row=2, column=2)
        btn_complete.grid(row=2, column=3)

        # Выполненные
        done_task = ttk.Frame(tabs_todo)
        tabs_todo.add(done_task, text='Выполненные')

        # Вкладка Бухгалтер
        accountant_win = ttk.Frame(tabs)
        tabs.add(accountant_win, text='Финансы')

        # Запуск
        self.main_win.mainloop()

    def edit_task(self):
        pass

    def add_task(self):
        pass

    def get_tasks_by_user_id(self, count):
        query = 'SELECT * FROM `tasks` WHERE `user_id` = ' + str(
            self.user['id']) + ' AND `status` = "in_progress" ORDER BY `priority` DESC'
        return DataBase().select(query, 'all')

    def on_exit(self):
        self.main_win.destroy()

    def change_user(self):
        from libs.windows.EnterForm import EnterForm
        del self.user
        self.main_win.destroy()
        EnterForm()
