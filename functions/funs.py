# functions

kart={"Mi TV":24666,"Realme":19800,"Samsung":12000,"LG":17600,"TCL":65000}

def filter():
    bud=int(input("Tell us budget: "))
    for each in kart.keys():
        if kart[each]<=bud:
            print(each,kart[each])

def showAll():
    for every in kart.items():
        print(every)

def discount(per):
    for single in kart.keys():
        kart[single]-=(kart[single]*per)/100

def hai():
    print("Simply function")

print("Main execution")
hai()
showAll()
discount(10)
showAll()
#filter()
#filter()


