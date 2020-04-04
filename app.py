#  from: https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/
from flask import Flask, flash, redirect, render_template, \
     request, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/edit_account', methods=['GET', 'POST'])
def edit_account():
    error = None
    if request.method == 'GET':
        request.form.username = "foo"
        request.form.password = "bar"
    elif request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('Account updated')
            return redirect(url_for('index'))
    return render_template('edit_account.html', error=error)