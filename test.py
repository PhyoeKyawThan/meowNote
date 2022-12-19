import sqlite3

connect = sqlite3.connect("minds.db")
cursor = connect.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS texts(_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,texts TEXT NOT NULL)''')
cursor.execute("DELETE FROM texts")
connect.commit()
# cursor.execute("INSERT INTO texts(")
# datas = cursor.execute("SELECT * FROM texts")


connect.close()
