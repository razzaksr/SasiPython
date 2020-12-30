from pickle import *
class alpha:
    def __init__(self,mod="",amt=0):
        self.model=mod
        self.price=amt
    def __str__(self):return self.model+" "+str(self.price)+"\n"


store=[]

a=alpha("Realme5s",14500)
b=alpha("Motorolazx2",15500)
c=alpha("Nokia6.1Puls",13100)
d=alpha("Honor9Lite",8100)

'''
store.append(a)
store.append(b)
store.append(c)
store.append(d)
'''

#pickling
store=dumps([a,b,c,d])

for x in store:
    print(x)

#unpickling
hai=loads(store)

for x in hai:
    print(x)