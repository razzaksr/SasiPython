from sqlite3.dbapi2 import Date

from handling.Entity import Jobcard


class ServiceAdmin:
    def __init__(self):
        self.records=[]
    def __add__(self,obj):
        self.records.append(obj)
        print(obj.custName,"with",obj.vehicleNumber,"has added to service records")
    def __sub__(self, other):
        if self&other==True:
            self.records.remove(other)
            print(other.vehicleNumber,"has delivered successfully")
        else:
            print("Pay your Bill in order to get your vehicle")
    def __mod__(self, other):
        for hai in self.records:
            for each in hai.issues:
                print(each)
    def __mul__(self, other):
        labour=len(other.issues)*200
        print(labour,"for labour alone")
        spares=len(other.issues)*150
        print(spares,"for spare parts")
        labour+=(labour*0.18)
        print(labour,"labour after GST")
        spares += (spares * 0.18)
        print(spares,"Spares after GST")
        other.expectedBill=labour+spares
    def __and__(self, other):
        self*other
        amount=int(input("Pay your bill: "+str(other.expectedBill)))
        if amount>=other.expectedBill:
            return True
        else:return False
    def __str__(self):
        data=""
        for x in self.records:
            data+=str(x)+"\n"
        return data

s=ServiceAdmin()
job1=Jobcard(9987656,Date(2020,12,18),"Razak Mohamed",8667002959,['Engines sieze','General serice','break'],0,0,"TN54L4192")
#s+job1
s-job1
print(s)
#print(Date(year=2020,month=9,day=10))