import sqlite3


def print_fetchall():
    users = cursor.fetchall()
    for user in users:
        print(user)


connection = sqlite3.connect('database.db')
cursor = connection.cursor()
# for i in range(1, 30):
#     cursor.execute(f"UPDATE Users SET age = ? WHERE username = ?", (29 + i, f"newuser{i}"))
cursor.execute("SELECT * FROM Users ")
print(f'Вывод всех пользователей:')
print_fetchall()

cursor.execute("SELECT username, age  FROM Users WHERE age > ?", (39,))
print(f'Вывод всех пользователей с их возрастом + старше 39:')
print_fetchall()
print(f'Вывод всех возрастов')
cursor.execute("SELECT username,age FROM Users GROUP BY AGE")
print_fetchall()
cursor.execute("SELECT username,age FROM Users ORDER BY AGE")
print_fetchall()
connection.commit()
connection.close()
