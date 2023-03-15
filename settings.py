import sqlite3 as sl

con = sl.connect("chess.db")

# Создает БД для хранения данных
def set_settings(con):
  with con:
      con.execute("""
          CREATE TABLE IF NOT EXISTS board (
              id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              position INTEGER,
              cell_size INTEGER
          );
      """)

# Получает и записывает позицию шахматной доски
def get_board_position(con):
  sql = 'INSERT INTO board (name, position) values(?, ?)'
  data = [
      ('x', 150),
      ('y', 210),
      ('board', 800),
  ]

  with con:
      con.executemany(sql, data)

set_settings(con)


