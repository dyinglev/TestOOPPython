from tkinter import *
from tkinter import ttk
from libs.Config.Settings import Settings


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

        # Определение вкладок
        nb = ttk.Notebook(self.main_win)
        nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

        # Вкладка Список дел
        todo_win = ttk.Frame(nb)
        nb.add(todo_win, text='Список дел')
        # Вертикальные вкладки
        style = ttk.Style(todo_win)
        style.configure('lefttab.TNotebook', tabposition='ws')
        notebook = ttk.Notebook(todo_win, style='lefttab.TNotebook')
        f1 = todo_win.Frame(notebook, bg='red', width=200, height=200)
        f2 = todo_win.Frame(notebook, bg='blue', width=200, height=200)
        notebook.add(f1, text='Frame 1')
        notebook.add(f2, text='Frame 2')
        notebook.pack()

        # Вкладка Бухгалтер
        accountant_win = ttk.Frame(nb)
        nb.add(accountant_win, text='Финансы')

        # Запуск
        self.main_win.mainloop()

    def on_exit(self):
        self.main_win.destroy()

    def change_user(self):
        from libs.windows.EnterForm import EnterForm
        del self.user
        self.main_win.destroy()
        EnterForm()
