from tkinter import *


def sign_in():
    sign_in_form = Tk()

    login = Entry(sign_in_form)
    password = Entry(sign_in_form)
    btn_sign_in = Button(sign_in_form, text='Enter', command=lambda: check_userdata(login.get(), password, sign_in_form))
    login.pack()
    password.pack()
    btn_sign_in.pack()

    sign_in_form.mainloop()


def check_userdata(log, pw, root):
    user = get_user()
    if user['login'] == log:
        root.destroy()
        main_win = Tk()

        l = Label(main_win, text='Hola')
        l.pack()
        main_win.mainloop()
    else:
        print(False)


def get_user():
    return {
        'login': 'user',
        'password': 'pass'
    }


sign_in()
