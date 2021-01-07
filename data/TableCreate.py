from pymysql import *
try:
    var = connect(host="localhost",user='root', passwd='',database='sasikumar')
    qry1 = "create table jobs(number int(4) not null, regnum varchar(50) not null,pick_date date not null, cust_name varchar(50) not null, cust_contact bigint(10) not null, issues text not null, expected int(4) not null, exp_bill double not null)"
    qry2="ALTER TABLE jobs ADD PRIMARY KEY ( number )"
    qry3="ALTER TABLE jobs CHANGE number number INT( 4 ) NOT NULL AUTO_INCREMENT"
    cur = var.cursor()
    cur.execute(qry1)
    cur.execute(qry2)
    cur.execute(qry3)
except Exception as e:
    print(e)
    var.rollback()
finally:
    var.close()
    print("Table created")