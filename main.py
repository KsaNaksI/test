from flask import Flask, request, render_template, redirect

from data import db_session
from data.users import User

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        db_session.global_init("db/blogs.db")
        db_sess = db_session.create_session()
        email = request.form['email']
        password = request.form['password']
        surname = request.form['surname']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        speciality = request.form['speciality']
        address = request.form['address']
        user = User()
        user.surname = surname
        user.name = name
        user.age = age
        user.position = position
        user.speciality = speciality
        user.address = address
        user.email = email
        db_sess.add(user)

        db_sess.commit()

        # После обработки данных можно выполнить любые другие действия, например, запись в базу данных

        # После обработки данных можно перенаправить пользователя на другую страницу
        return "Вы зарегестрированы"
    return render_template('reg.html')

if __name__ == '__main__':
    app.run(debug=True)