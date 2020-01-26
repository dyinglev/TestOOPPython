from tkinter import *
from libs.Config.Settings import Settings


class MainWindow():
    """Главное окно программы"""

    def __init__(self, active_user):
        """Инициализация главного окна"""
        self.user = active_user

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

        l = Label(self.main_win, text=self.user['username']).pack()

        self.main_win.mainloop()

    def on_exit(self):
        self.main_win.destroy()

    def change_user(self):
        from libs.windows.EnterForm import EnterForm
        del self.user
        self.main_win.destroy()
        EnterForm()
