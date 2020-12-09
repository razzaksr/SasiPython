# class with constructor and inner creation

# Contructors:
# priority to execute before any other functions to be called
# it will be initiated while creating object itself
# to initialise members

#__str__,__del__,operator overloading,.....

class Loan:
    __loanAmt=0.0
    __loanNumber=0
    __loanIntrest=0.0
    __loanNeedToPay=0.0
    __loanBorrower=""
    __loanDuration=0
    #Constructor
    def __init__(self,name="",num=0,dur=0,it=0.0,amt=0):
        print("Initiated")
        self.__loanBorrower=name;self.__loanNumber=num;self.__loanDuration=dur
        self.__loanIntrest=it;self.__loanAmt=amt;
        calc = self.getLoanAmt() * (self.getLoanIntrest()) / 100
        calc *= self.getLoanDuration()
        calc += self.getLoanAmt()
        self.__loanNeedToPay=calc
    def __del__(self):
        print("Object released from memory")
    def __str__(self):
        return str(self.__loanNumber)+" "+self.__loanBorrower+" "+str(self.__loanDuration)+" "+str(self.__loanIntrest)+" "+str(self.__loanAmt)+" "+str(self.__loanNeedToPay)+"\n"
    def __add__(self,data=0):
        calc = self.getLoanAmt() * (self.getLoanIntrest()) / 100
        calc *= self.getLoanDuration()
        calc += self.getLoanAmt()
        self.__loanNeedToPay = calc
    def __xor__(self,data=""):
        return str(self.__loanNumber) + " " + self.__loanBorrower + " " + str(self.__loanDuration) + " " + str(
            self.__loanIntrest) + " " + str(self.__loanAmt) + " " + str(self.__loanNeedToPay) + "\n"
    def setLoanAmt(self,amt):self.__loanAmt=amt
    def getLoanAmt(self):return self.__loanAmt
    def setLoanNumber(self,num):self.__loanNumber=num
    def getLoanNumber(self):return self.__loanNumber
    def setLoanIntrest(self,it):self.__loanIntrest=it
    def getLoanIntrest(self): return self.__loanIntrest
    def getLoanNeedToPay(self):return self.__loanNeedToPay
    def setLoanNeedToPay(self, pay): self.__loanNeedToPay = pay
    def setLoanBorrower(self,borr):self.__loanBorrower=borr
    def getLoanBorrower(self):return self.__loanBorrower
    def setLoanDuration(self,years):self.__loanDuration=years
    def getLoanDuration(self):return self.__loanDuration

l1=Loan()
l1.setLoanAmt(50000);l1.setLoanBorrower("Mohamed");l1.setLoanDuration(3)
l1.setLoanIntrest(4.1);l1.setLoanNumber(9876787676);
l1+1
'''calc=l1.getLoanAmt()*(l1.getLoanIntrest())/100
calc*=l1.getLoanDuration()
calc+=l1.getLoanAmt()
l1.setLoanNeedToPay(calc)'''
#print(l1.getLoanNumber(),l1.getLoanBorrower(),l1.getLoanIntrest(),l1.getLoanAmt(),l1.getLoanNeedToPay())
print(l1)

l2=Loan("Razak",9876788632,3,13.1,99800)
#print(l2.getLoanAmt(),l2.getLoanNumber(),l2.getLoanNeedToPay())
print(l2^"hai")
#print(l2)

l3=Loan(amt=113000,it=13.8,num=876567894,dur=4,name="Sabari")
print(l3)