# Yogify
Yogify - помощник, задачник, бухгалтер
***
### Внимание!
Чтобы у вас работало подключение с ВАШЕЙ БД, вам нужно:
1. Создать в папке libs файл Config.py
2. Написать в нем следующий код:
```python
class Config:
    def get_config(self):
        return {
            'username': 'Lev', # Имя пользователя
            'db_name': 'MyDataBase', # Имя базы данных
            'password': 'qwerty12', # Пароль пользователя
            'server': 'siteonmysql.com', # Адрес БД (localhost, если на вашем компьютере)
            'port': 'p0rt your DB', # Порт (необязательно, если нет)
        }
```
