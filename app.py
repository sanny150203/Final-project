from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)

# Создаем таблицу бронирований при запуске приложения
database.create_table_bookings()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bron', methods=['GET', 'POST'])
def bron():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        date = request.form['date']
        time = request.form['time']

        # Вставляем данные бронирования в базу данных
        database.insert_booking(name, email, date, time)

        return redirect('/')

    return render_template('bron.html')

if __name__ == '__main__':
    app.run(debug=True)


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}