import sqlite3
def seekuser(user,database):
    db = sqlite3.connect(database)
    cur = db.cursor()
    cur.execute("SELECT*FROM user_sql WHERE user=?",[user])
    data = cur.fetchall()
    cur.close()
    db.close()
    return data
def adduser(data,database):
    db = sqlite3.connect(database)
    cur = db.cursor()
    insert_user_sql = "insert into user_sql(user,password)values(?,?)"
    try:
        cur.execute(insert_user_sql,(data[0],data[1]))
        db.commit()
    except Exception as error:
        db.rollback()
        raise Exception
    finally:
        cur.close()
        db.close()

DATABASE = 'user information.db'
db = sqlite3.connect(DATABASE)
cur = db.cursor()
user_sql = '''create table user_sql(user varchar(50) primary key,password varchar(50))'''
try:
    cur.execute(user_sql)
    print("创建表成功")
except Exception as error:
    print(error)
    print("创建表失败")
finally:
    cur.close()
    db.close()

adduser(['11','11'],DATABASE)
print(seekuser('11',DATABASE))
