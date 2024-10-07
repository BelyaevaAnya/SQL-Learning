import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
''')

for i in range(1, 11):
    cursor.execute(
        f"INSERT INTO Users (username, email, age, balance) VALUES ('User{i}', 'example{i}@gmail.com', '{i * 10}','1000')")

for i in range(1, 11, 2):
    cursor.execute(f"UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i}"))

for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}',))

cursor.execute("SELECT username, email, age, balance  FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

cursor.execute('DELETE FROM Users WHERE username = ?', ('User6', ))
cursor.execute('SELECT COUNT(*) FROM Users')
count_users = cursor.fetchone()[0]
print(f'Кол-во записей: {count_users}')
cursor.execute('SELECT SUM(balance) FROM Users')
sum_balance = cursor.fetchone()[0]
print(f'Сумма балансов: {count_users}')
print(f'Средняя сумма на балансе: ', sum_balance/count_users)
cursor.execute('SELECT AVG(balance) FROM Users')
avg_balance = cursor.fetchone()[0]
print(f'Средняя сумма на балансе через sql-запрос: ', avg_balance)
connection.commit()
connection.close()
