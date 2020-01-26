from libs.Classes.Db import DataBase


class User:
    """Класс для работы с пользователями"""

    def get_test_user(self):
        """Возвращает тестового пользователя"""
        return {
            'login': 'user',
            'password': 'pass'
        }

    def get_user_by_login_and_password(self, login, password):
        """Возвращает  пользователя по логину и паролю из БД"""
        db = DataBase()
        query = 'SELECT * FROM `users` WHERE `username` = "' + login + '" AND `password` = "' + password + '"'
        return db.select(query, 'one')
