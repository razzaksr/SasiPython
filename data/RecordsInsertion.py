from pymysql import *

try:
    con=connect(host='localhost',database='sasikumar',user='root',passwd='')
    print('Connection opened')
    reg=input("Enter the vehicle registration number: ")
    pick=input("Tell us Picking date in YYYY-MM-DD: ")
    name=input("TEll us  Customer name: ")
    contact=int(input("Tell us customer contact: "))
    probs=input("Tell us issues you have in this vehicle(seperate issues by ,): ")
    expDay=int(input("Tell us expected delivery duration: "))
    expBill=float(input("Approximatly expected bill: "))
    #issue=probs.split(",")

    qry="""insert into jobs(regnum,pick_date,cust_name,cust_contact,issues,expected,exp_bill) values('%s','%s','%s',%d,'%s',%d,%f)"""\
        %(reg,pick,name,contact,probs,expDay,expBill)
    cur=con.cursor()
    ack=cur.execute(qry)
    con.autocommit(True)
    if ack!=0:print(ack,"vehicle added into records")
    else:print("can't add the vehicle")
except Exception as e:
    print(e)
    con.rollback()

finally:con.close()