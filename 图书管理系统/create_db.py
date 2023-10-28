import sqlite3
def seekbook(number,database):
    db = sqlite3.connect(database)
    cur = db.cursor()
    cur.execute("SELECT*FROM book_sql WHERE number=?",[number])
    data = cur.fetchall()
    cur.close()
    db.close()
    return data
def addbook(bookinfo,database):
    db = sqlite3.connect(database)
    cur = db.cursor()
    insert_book_sql = "insert into book_sql(number,bookname,authername)values(?,?,?)"
    try:
        cur.execute(insert_book_sql,(bookinfo[0],bookinfo[1],bookinfo[2]))
        db.commit()
        print("数据插入成功")
    except Exception as error:
        print(error)
        db.rollback()
        print("数据插入失败")
    finally:
        cur.close()
        db.close()
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