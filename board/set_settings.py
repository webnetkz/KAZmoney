import sqlite3 as sl
from board.find_board import get_start_position


con = sl.connect("chess.db")

# Создает БД для хранения данных
def set_settings(con):
  with con:
      con.execute("""
          CREATE TABLE IF NOT EXISTS board (
              id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              result INTEGER
          );
      """)

# Получает и записывает позицию шахматной доски
def set_board_position(con):
  # Получает координаты
  position_board = get_start_position()
  # Доска не обнаружена
  if not position_board:
     print("Шахматная доска не найдена")
     exit()
  
  # Проверяем наличие данных
  data = con.execute("SELECT * FROM board")
  rows = data.fetchall()
  if not rows:
    # Формируем\Добавляем данные в БД
    BOARD_SIZE = position_board[2]-4
    CELL_SIZE = int(BOARD_SIZE / 8)
    BOARD_TOP_COORD = position_board[1]+4
    BOARD_LEFT_COORD = position_board[0]+3

    sql = 'INSERT INTO board (name, result) values(?, ?)'
    data = [
        ('x', BOARD_LEFT_COORD),
        ('y', BOARD_TOP_COORD),
        ('board', BOARD_SIZE),
        ('cell_size', CELL_SIZE),
    ]

    with con:
        con.executemany(sql, data)

set_settings(con)
set_board_position(con)


