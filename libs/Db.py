import pymysql
from libs.Config import Config


class DataBase:
    def __init__(self):
        c = Config()
        self.db_config = c.get_config()

    def db_connect(self):
        return pymysql.connect(self.db_config['server'], self.db_config['username'], self.db_config['password'],
                               self.db_config['db_name'])

    def print_db_version(self):
        with self.db_connect():
            cur = self.db_connect().cursor()
            cur.execute("SELECT VERSION()")
            version = cur.fetchone()
        return "Database version: {}".format(version[0])
