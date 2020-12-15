# Hierarchy
from oop.Multilevel import GPay
from oop.Single import Card


class Flipkart(Card):
    profile=""
    def __init__(self,cn=0,anum=0,ahold="",abal=0.0,mine={}):
        super(Flipkart, self).__init__(cn,anum,ahold,abal)
        self.profile=ahold
        self.kart=mine
    def __add__(self, other):
        self.kart[other[0]]=other[1]
        print(other[0],"added to kart")
    def __sub__(self, other):
        if other in self.kart.keys():
            owe=self.kart[other]
            valid=int(input("Enter the card number once again to validate: "))
            if valid == self.cardNumber:
                if owe <= self.accountBal:
                    self.accountBal-=owe
                    self.kart.pop(other)
                    print("order placed successfully with",owe,"for the product",other)
                else:print("Insufficient amount")
            else:print("Unauthorized access")
        else:print("Product",other,"not found in kart")
    def list(self):
        sum=0
        for key,value in self.kart.items():
            print(key,value)
            sum+=value
        print("Kart value is",sum)

f=Flipkart(98765432111,76864,"Mohamed",8700.5,{"RedmiWatch6":2999,"MotoTV":15500})
f.list()
f+["iBallBeanBag",6200]
f.list()
f-"MotoTV"
f-"RedmiWatch6"
f.list()

g1=GPay(112233,87656789876,9888888,"Sasikumar",7600.5)
g1+400
print(g1)

