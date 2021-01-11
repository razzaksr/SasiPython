from pymysql import *

try:
    con=connect(host='localhost',database='sasikumar',user='root',passwd='')
    print('Connection opened')

    cur = con.cursor()

    reg=input("Enter the vehicle registration number: ")

    many=input('Tell us what are all you wish to update by ,(pick_date,cust_name,cust_contact,issues,expected,exp_bill)')
    many=list(many.split(','))

    for x in many:
        if x=='cust_contact' or x=='expected':
            value = int(input("tell us the value for:" + x))
            qry = "update jobs set %s = %d where regnum='%s'" % (x, value, reg)
        elif x=='exp_bill':
            value = float(input("tell us the value for:" + x))
            qry = "update jobs set %s = %f where regnum='%s'" % (x, value, reg)
        else:
            value = input("tell us the value for:" + x)
            qry = "update jobs set %s = '%s' where regnum='%s'" % (x, value, reg)
        ack = cur.execute(qry)
        if ack != 0:
            print(ack, "vehicle updated into records")
        else:
            print("can't update the vehicle")
    '''
    pick=input("Tell us Picking date in YYYY-MM-DD: ")
    name=input("TEll us  Customer name: ")
    contact=int(input("Tell us customer contact: "))
    probs=input("Tell us issues you have in this vehicle(seperate issues by ,): ")
    expDay=int(input("Tell us expected delivery duration: "))
    expBill=float(input("Approximatly expected bill: "))
    #issue=probs.split(",")
    '''
    '''qry="""insert into jobs(regnum,pick_date,cust_name,cust_contact,issues,expected,exp_bill) values('%s','%s','%s',%d,'%s',%d,%f)"""\
        %(reg,pick,name,contact,probs,expDay,expBill)'''
    con.autocommit(True)
except Exception as e:
    print(e)
    con.rollback()

finally:con.close()