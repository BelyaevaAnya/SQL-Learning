import sqlite3

# Connect to the database
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER
    )
''')
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
# cursor.execute("INSERT INFO Users (username, email, age) VALUES (?, ?, ?)", "(newuser, exp@gmail.com), '28'")
# for i in range(30):
#     cursor.execute(f"INSERT INTO Users (username, email, age) VALUES ('newuser{i}', '{i}exp@gmail.com', '28')")
# cursor.execute(f"UPDATE Users SET age = ? WHERE username = ?", (29, "newuser0"))
cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser0', ))
connection.commit()
connection.close()
