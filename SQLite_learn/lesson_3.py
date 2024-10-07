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
cursor.execute('SELECT SUM(age) FROM Users')
total1 = cursor.fetchone()[0]
print(total1)
cursor.execute('SELECT COUNT(*) FROM Users')
total2 = cursor.fetchone()[0]
print(total2)
print(f'Средний возраст: {total1/total2}')
cursor.execute('SELECT AVG(age) FROM Users')
avg_age = cursor.fetchone()[0]
print(f'AVG AGE from sql func: {avg_age}')
cursor.execute('SELECT MIN(age) FROM Users')
min_age = cursor.fetchone()[0]
print(f'Min age: {min_age}')
cursor.execute('SELECT MAX(age) FROM Users')
max_age = cursor.fetchone()[0]
print(f'Max age: {max_age}')
connection.commit()
connection.close()