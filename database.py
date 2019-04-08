import pymysql

"""INSIEME DI FUNZIONI DI LIBRERIA"""


def showtasks():
    sql = "select * from todo order by task asc"
    conn = pymysql.connect(user="root", password="root", host="localhost", database="todo")
    cursor = conn.cursor()
    cursor.execute(sql)
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return tasks


def newTask(task):
    sql2 = "insert into todo(task) values(%s)"
    ok = "ok"
    conn2 = pymysql.connect(user="root", password="root", host="localhost", database="todo")
    cursor2 = conn2.cursor()
    cursor2.execute(sql2, (task,))
    conn2.commit()
    cursor2.close()
    conn2.close()


def removeTask(id):
    sql_delete = "delete from todo where id=%s"
    conn3 = pymysql.connect(user="root", password="root", host="localhost", database="todo")
    cursor3 = conn3.cursor()
    cursor3.execute(sql_delete, (id,))
    conn3.commit()
    cursor3.close()
    conn3.close()


