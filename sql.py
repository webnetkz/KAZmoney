import sqlite3

# Устанавливаем соединение с базой данных или создаем новую, если она не существует
connection = sqlite3.connect("mydatabase.db")

# Создаем курсор (объект для выполнения SQL-запросов)
cursor = connection.cursor()

# Пример создания таблицы
create_table_sql = """
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY,
    email TEXT,
    lichess TEXT,
    code TEXT
)
"""

cursor.execute(create_table_sql)
connection.commit()  # Сохраняем изменения

# Пример вставки данных
insert_data_sql = "INSERT INTO user (email, lichess, code) VALUES (?, ?, ?)"
data = ("user@example.com", "zhora", '123qwer123')

cursor.execute(insert_data_sql, data)
connection.commit()  # Сохраняем изменения

# Пример выборки данных
select_data_sql = "SELECT * FROM user"
cursor.execute(select_data_sql)
data = cursor.fetchall()

for row in data:
    print(row)

# Закрываем соединение с базой данных
connection.close()
