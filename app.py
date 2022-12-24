from flask import Flask, request, redirect, render_template, url_for, session
import sqlite3

app = Flask(__name__)
connect = sqlite3.connect("minds.db", check_same_thread=False)
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS texts(name TEXT NOT NULL,texts TEXT NOT NULL)''')

@app.route('/view')
def view():
    return f'h1'

@app.route('/')
def index():
    alert = "Added successful!!!!"
    return render_template('main.html', alertxt=alert)

@app.route('/index', methods=["POST", "GET"])
def add_minds():
    txt = ""
    if request.method == 'POST':
        name = request.form['name']
        text = request.form['text']
        data = (name, text)
        check = ('', '')

        if data==check:
            txt = "Must not be empty value!!"
            return render_template('index.html', alertxt=txt)
        else:
            if data in cursor.execute("SELECT * FROM texts"):
                txt = "Already added!!!"
                return render_template('index.html',  alertxt=txt)
            else:
                cursor.execute("INSERT INTO texts(name, texts) VALUES(?, ?)", data)
                connect.commit()
                return redirect(url_for('index'))
    else:
        return render_template('index.html')


@app.route('/show')
def show_data():
    datas = cursor.execute("SELECT * FROM texts")
    return render_template('show.html', datas=datas)

if __name__ == '__main__':
    app.run(debug=True)