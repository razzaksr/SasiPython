# default and + arguments

teck=[12,23,56,99,12,90,11,56,78,67,56,23]

def findOut(element=0):
    print(element,"is existing in following positions")
    for pos in range(len(teck)):
        if element == teck[pos]:
            print(pos)
def findSum(beg=0,end=len(teck)):
    sum=0
    for pos in range(beg,end):
         sum+=teck[pos]
    print("sum value between",beg,"and",end,"is",sum)

#findOut()
findSum()
findSum(3,9)
findSum(end=11,beg=5)
findSum(end=5)