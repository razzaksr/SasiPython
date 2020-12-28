from sqlite3.dbapi2 import Date

from handling.Custom import SasiError
from handling.Entity import Jobcard


class ServiceAdmin:
    def __init__(self):
        self.records=[]
    def __add__(self,obj):
        self.records.append(obj)
        print(obj.custName,"with",obj.vehicleNumber,"has added to service records")
    def __sub__(self, other):
        try:
            if other not in self.records:
                raise SasiError
            if self & other == True:
                self.records.remove(other)
                print(other.vehicleNumber, "has delivered successfully")
            else:
                print("Pay your Bill in order to get your vehicle")
        except SasiError as serror:
            print(serror,"\nPlease add",other,"first in records")
            if input("Do you wish to add "+str(other.vehicleNumber)+" into our records: ") == 'yes':
                self+other
            else:print("Try to deliver valid job")
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
    def __or__(self, other):
        try:
            for job in self.records:
                if other == job.jobNumber:
                    self*job
                    return job
            else:
                raise SasiError
        except SasiError as serror:
            print(serror,other)
            other=int(input("Please enter valid job number: "))
            return self|other

s=ServiceAdmin()
job1=Jobcard(9987656,Date(2020,12,18),"Razak Mohamed",8667002959,['Engines sieze','General service','break'],0,0,"TN54L4192")
job2=Jobcard(567876567,Date(2020,7,25),"Sabarinathan",8765567765,['General service'],0,0,"TN54M0635")
job3=Jobcard(45678332,Date(2019,3,31),"Manikandan",9876556732,['break'],0,0,"TN54F7832")
job4=Jobcard(12321212,Date(2018,2,11),"Sheik",8767878832,['General service','milage check'],0,0,"TN54R8923")
job5=Jobcard(566636363,Date(2011,5,1),"Mohamed",9778777873,['disc oil'],0,0,"TN54S1222")
s+job1
s+job2

s-job3

s+job3
s+job4
s+job5
s-job1
print(s)
print(s|1111111)
#print(Date(year=2020,month=9,day=10))