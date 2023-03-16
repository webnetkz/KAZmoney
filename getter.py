import sqlite3 as sl

con = sl.connect("chess.db")

with con:
    data = con.execute("SELECT * FROM board")
    rows = data.fetchall()
    if not rows:
        print("Результат запроса пустой")
    else:
        for row in rows:
            print(row)
