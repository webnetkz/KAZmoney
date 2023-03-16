import sqlite3 as sl
import subprocess
import time

def board_position():
  con = sl.connect("./board/chess.db")

  with con:
      try:
        data = con.execute("SELECT * FROM board")
        rows = data.fetchall()
        if not rows:
            print("Результат запроса пустой")
        else:
            return rows
      except:
          # Первый запуск, данные о положение шахматной доске не найдены
          # Запускает получение данных и перезапускает текущий скрипт
          subprocess.run(['python3', 'set_settings.py'])
          time.sleep(2)
          subprocess.run(['python3', 'get_data.py'])


    

