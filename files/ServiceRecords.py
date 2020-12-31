# Service logs
from sqlite3.dbapi2 import Date

from handling.Entity import Jobcard
from handling.FrontOffice import ServiceAdmin
from pickle import *



class Logs(ServiceAdmin):
    def __init__(self):
        super(Logs, self).__init__()
        #print(self.log)
    def __xor__(self, other):
        self+other
        self.pickle()
        #print(self.records)
    def pickle(self):
        self.log = open("D:\\jpgms\\sasi.doc", "wb")
        dump(self.records, self.log)
        self.log.close()
        print("Record dumped")
    def unpickle(self):
        self.log = open("D:\\jpgms\\sasi.doc", "rb")
        print("Gonna load from dumped file")
        for x in load(self.log):
            print(x)
        self.log.close()
    def __gt__(self,other):
        self-other
        self.pickle()
    def __str__(self):
        self.unpickle()
        return ""

l1=Logs()
job1=Jobcard(9987656,Date(2020,12,18),"Razak Mohamed",8667002959,['Engines sieze','General service','break'],0,0,"TN54L4192")
job2=Jobcard(567876567,Date(2020,7,25),"Sabarinathan",8765567765,['General service'],0,0,"TN54M0635")
job3=Jobcard(45678332,Date(2019,3,31),"Manikandan",9876556732,['break'],0,0,"TN54F7832")
job4=Jobcard(12321212,Date(2018,2,11),"Sheik",8767878832,['General service','milage check'],0,0,"TN54R8923")
job5=Jobcard(566636363,Date(2011,5,1),"Mohamed",9778777873,['disc oil'],0,0,"TN54S1222")

l1^job1
l1^job2
l1^job4
l1^job3

print(l1)

l1>job1
l1>job5

print(l1)


