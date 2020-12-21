# Multiple Inheritance: two or more base class for one derived

# hybrid: combination of more than one form of inheritance

# here Hierarchy and multiple

# s>> c
# s>> d
# u>>c,d

from array import *

class Source:
    def __init__(self):
        self.transactions = array('f', [])
    def __str__(self):
        strs=""
        for hai in self.transactions:strs+=str(hai)+"\n"
        return strs

class Credit(Source):
    def __init__(self):
        super(Credit, self).__init__()
    def __add__(self, other):
        self.transactions.append(other)
    def __mul__(self, other):
        if len(self.transactions)>=8:
            extra=self.transactions[len(self.transactions) - 1] * other / 100
            new=self.transactions[len(self.transactions)-1]+extra
            self.transactions.append(new)
            print(extra,"added to your account for the interest of",other)
        else:print("Interest can't apply")
class Debit(Source):
    def __init__(self):
        super(Debit, self).__init__()
    def __sub__(self, other):
        self.transactions.append(other)
    def __mul__(self, other):
        if len(self.transactions)>=5:
            reduce=self.transactions[len(self.transactions)-1]*other/100
            new=self.transactions[len(self.transactions)-1]-reduce
            self.transactions.append(new)
            print(reduce,"debited from your account for the interest of",other)
        else:print("Interest can't apply")

class User(Debit,Credit):
    def check(self):
        print("User function called")


u=User()
u.check()
u+100
u-90
u+2000
u+3000
u+100
u+569.8
u+12900
u-300
u+700
u-450
u-120
u-320
u+9000
u*5.8
print(u)
'''s=Source()
print(s)'''

'''c=Credit()
c+12000
c+4500
c+6000
c+7800
c+100
c+50
c+1300
c+600
c+780
c+2000
c+13000
c*5.9
print(c)'''

'''deb=Debit()
deb-9700
deb-800
deb-1200
deb-100
deb-2400
deb-400
deb-200
deb-1000
deb*6.1
print(deb)'''