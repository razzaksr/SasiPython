# Multi level: Account->Card->Wallet
from oop.Single import Card, Account


class GPay(Card):
    upi_Pin=0
    def __init__(self,pin,cn=0,anum=0,ahold="",abal=0.0):
        self.upi_Pin=pin
        super(GPay, self).__init__(cn,anum,ahold,abal)
    def __mul__(self, other):
        amount=int(input("Enter the amount to transfer: "))
        validate = int(input("Enter the UPI pin once again: "))
        if validate==self.upi_Pin:
            if amount<=self.accountBal:
                self.accountBal-=amount
                other.accountBal+=amount
                print("Fund",amount,"Transferred successfully to",other.accountHolder)
            else:print("Insufficient amount")
        else:print("Transaction Failed due to invalid PIN")
    def __str__(self):
        validate = int(input("Enter the UPI pin once again: "))
        if validate == self.upi_Pin:
            return str(self.accountNo)+" "+self.accountHolder+" "+str(self.accountBal)+"\n"
        else:
            return "Invalid Pin"

'''g1=GPay(112233,87656789876,9888888,"Sasikumar",7600.5)
g2=GPay(999999,6567567666,11110000023,"Kumar",900.5)

g2+400
print(g2)

g1*g2

print(g2)
print(g1)'''


