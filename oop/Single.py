# Single Inheritance

class Account:
    accountNo=0
    accountBal=0.0
    accountHolder=""
    def __str__(self):
        return str(self.accountNo)+" "+self.accountHolder+" "+str(self.accountBal)+"\n"
#single
class Card(Account):
    cardNumber=0
    def __init__(self,cn=0,anum=0,ahold="",abal=0.0):
        self.cardNumber=cn
        self.transactions=[]
        self.accountNo=anum
        self.accountHolder=ahold
        self.accountBal=abal
    def __add__(self,amt):
        self.accountBal+=amt
        print(amt,"deposited to",self.accountHolder)
        self.transactions.append('Credit')
    def __sub__(self, draw):
        if self.accountBal>=draw:
            self.accountBal-=draw
            print(draw,"has been withdrawn from ",self.accountHolder)
            self.transactions.append('Debit')
        else:print("Insufficient account balance")
    def countTrans(self):
        creCount=self.transactions.count('Credit')
        debCount = self.transactions.count('Debit')
        charges=0
        if creCount>=5:
            charges+=(creCount-5)*10
        if debCount>=3:
            charges+=(debCount-3)*20
        print("Total charges on transaction count is",charges)
        self.accountBal-=charges
        print("Charges debited in your account")
    def __str__(self):
        return str(super(Card, self).__str__())+"\n"+str(self.cardNumber)+" "+str(self.accountBal)+"\n"
'''a1=Account()
a1.accountNo=98765678;a1.accountHolder="Sasi";a1.accountBal=23400.9
print(a1)'''

c1=Card(12347383478347,9876787,"Sasi",879.6)
c1+4000
#print(c1)
c1-1800
#print(c1)
c1-200
c1+1000
c1-100
c1-500
c1+10000
c1-100
c1+4000
print(c1)
c1.countTrans()
