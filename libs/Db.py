import pymysql
from libs.Config import Config


class DataBase:
    """Класс для работы с БД"""

    def __init__(self):
        """Получение данных для соединения с БД"""
        c = Config()
        self.db_config = c.get_config()

    def db_connect(self):
        """Соединение с БД"""
        return pymysql.connect(host=self.db_config['server'], user=self.db_config['username'],
                               password=self.db_config['password'],
                               db=self.db_config['db_name'], cursorclass=pymysql.cursors.DictCursor)

    def select(self, query):
        """Выбор данных по запросу :query из БД"""
        with self.db_connect().cursor() as c:
            c.execute(query)
            result = c.fetchone()
        return result if result else False

    def print_db_version(self):
        """Вывод версии MySQL"""
        with self.db_connect().cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
        return "Database version: {}".format(version[0])
