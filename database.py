import sqlite3

# Создание базы данных
def create_table_bookings():
    connection = sqlite3.connect('bookings.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

# Вставка данных бронирования в базу данных
def insert_booking(name, email, date, time):
    connection = sqlite3.connect('bookings.db')
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO bookings (name, email, date, time) VALUES (?, ?, ?, ?)
    ''', (name, email, date, time))
    connection.commit()
    connection.close()
