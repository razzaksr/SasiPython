from pymysql import *
try:
    var = connect(host="localhost", user="root", passwd="")
    qry = "create database sasikumar"
    cur = var.cursor()
    cur.execute(qry)
except:
    var.rollback()
finally:
    var.close()
    print("Database created")