from flask import Flask, request, redirect, render_template, url_for, session
import sqlite3

app = Flask(__name__)
connect = sqlite3.connect("minds.db", check_same_thread=False)
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS texts(_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,texts TEXT NOT NULL)''')
datas = cursor.execute("SELECT * FROM texts")
check_datas = []

for data in datas:
    add_ = (data[1], data[2])
    check_datas.append(add_)


@app.route('/')
def index():
    datas = cursor.execute("SELECT * FROM texts")
    return render_template('main.html', showalert=datas)

@app.route('/index', methods=["POST", "GET"])
def add_minds():
    if request.method == 'POST':
        name = request.form['name']
        text = request.form['text']
        data = (name, text)
        if (name, text) not in check_datas:
            cursor.execute("INSERT INTO texts(name, texts) VALUES(?, ?)", data)
            connect.commit()
        alertxt = "Written, Successful <3"
        return redirect(url_for('index'))

    else:
        return render_template('index.html')


@app.route('/show')
def show_data():
    return render_template('show.html')

if __name__ == '__main__':
    app.run(debug=True)