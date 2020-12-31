from pickle import *
class alpha:
    def __init__(self,mod="",amt=0):
        self.model=mod
        self.price=amt
    def __str__(self):return self.model+" "+str(self.price)+"\n"


a=alpha("Realme5s",14500)
b=alpha("Motorolazx2",15500)
c=alpha("Nokia6.1Puls",13100)
d=alpha("Honor9Lite",8100)

file=open("D:\\jpgms\\secret.doc","wb")


store=[a,b,c,d]
dump(store,file)# Pickling

file.close()

print("Objects are dumped into file",file.name)

file=open("D:\\jpgms\\secret.doc","rb")

#unpickling
for x in load(file):
    print(x)


file.close()
print("Object are loaded from file",file.name)