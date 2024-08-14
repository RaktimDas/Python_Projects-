from flask import Flask, redirect, render_template, url_for, request, session
from flask_mysqldb import MySQL
import MySQLdb
app = Flask(__name__)
app.secret_key = 'raktimdas9854'
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "123456"
app.config["MYSQL_DB"] = 'login'

db = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT * FROM logininfo WHERE email=%s AND password=%s", (username, password))
        info = cursor.fetchone()
        if info is not None:
            if info['email'] == username and info['password'] == password:
                session['loginsuccess'] = True
                return redirect(url_for('profile'))
        else:
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        if 'one' in request.form and 'two' in request.form and 'three' in request.form:
            name = request.form['one']
            email = request.form['two']
            password = request.form['three']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(
                "INSERT INTO login.logininfo(name, email ,password)VALUES(%s,%s,%s)", (name, email, password))
            db.connection.commit()
            return redirect(url_for('index'))
    return render_template('register.html')


@app.route('/register/profile')
def profile():
    if session['loginsuccess'] == True:
        return render_template('profile.html')


@app.route('/register/logout')
def logout():
    session.pop('loginsuccess', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
