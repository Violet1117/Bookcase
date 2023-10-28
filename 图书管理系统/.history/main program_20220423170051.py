from flask import Flask, url_for, redirect, render_template, request
from create_db import *
import time

DATABASE1 = 'user information.db'
DATABASE2 = 'basic information.db'
book = []
for i in range(1,6):
    book.append(seekbook(i,DATABASE2)[0])

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html',book=book)

@app.route('/index', methods=['GET', 'POST'])
def index():
    time1 = time.time()
    return render_template('index.html',time=time1)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        global username,password,sign
        password = request.form['password']
        username = request.form['username']
        if username!='' and password!='':
            try:
                if seekuser(username,DATABASE1)[0][1]==password:
                    sign = '借阅'
                    return redirect(url_for('check'))
                else:
                    return render_template('login.html',warn='false',message='不会记住自己的密码嘛:(  ')
            except:
                return render_template('login.html',warn='false',message='你还没有注册哦:)  ')
        else:
            return render_template("login.html",warn='false',message='不能输入用户名或密码嘛:(')
    return render_template('login.html',warn='')

@app.route('/lend', methods=['GET', 'POST'])
def lend():
    if request.method == 'POST':
        global checkname
        checkname = request.form['lend'][5:-1]
        return redirect(url_for('login'))
    return render_template('lend.html')

@app.route('/return', methods=['GET', 'POST'])
def returning():
    return render_template('return.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        global username,password
        password = request.form['password']
        username = request.form['username']
        if username!='' and password!='':
            try:
                adduser([username,password],DATABASE1)
                return redirect(url_for('login'))
            except:
                return render_template("register.html",warn='false',message='不会取自己独特的名字嘛:(')
        else:
            return render_template("register.html",warn='false',message='不能输入用户名或密码嘛:(')
    return render_template('register.html',warn='')

@app.route('/check', methods=['GET', 'POST'])
def check():
    return render_template('check.html',sign=sign,checkname=checkname,username=username)

if __name__ == '__main__':
    app.run(use_reloader=False,debug=True)