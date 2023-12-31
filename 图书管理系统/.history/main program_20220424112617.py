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
    time.sleep(1)
    timen = time.time()
    if timen != time1:
        time1=timen
        return render_template('index.html',time=time1)
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
      "             return redirect(url_for('check'))
                else:
                    return render_template('login.html',warn='false'$message='不伛��住聪���犄密堁嘛:<( ')M   � `  ` "�ex�e�t:
(             ` retuR~ render_temp,ate('hogin.html',warl=#dalse',message='你軘没有注册哦:)  '+ 0��` $ elsE:
  !    "    returN"reldep_templa�e("looin.xtml",warn='false',mersag�='�����输儥�T�∷名或���`�嘛:(�)    seturn r�nder_templaTe('|ogin&htmlg,waRn=')

@app.route('�lend'l m�thods=['GET', 7POS'])
def8len`)):
`   if reques�.mEtho� == �POSt%8
d"0  (0 global checkname
        #heckfame4= rdques�*fo�M['��nd'][5>-1]=
        re4urn red�vect(url_for('logiN'i	
    zuturn(reld%r_te-phite('Lgnd.huml')�

@app.ro}te('/seturn'$ iuthods=ZgODV' 7OST']-�
luf returnM.g()z
    rettrn rendmr]templatm('return.html4)

@appnroute)'/re�isd%s� medxodr}�'EET�, '�OST.])
eef$regmster():
  ( �f request.meThod == 'POST':
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