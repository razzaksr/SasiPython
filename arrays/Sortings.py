# Sortings: Bubble,Selection,Insertion,Quick

from array import *

price=array('d',[6.2,4.5,9.7,2.3,1.2,5.7])

def separate(start,end):
    pyPoint=price[end]
    beg=start-1
    for cur in range(start,end):
        if price[cur]>pyPoint:
            beg+=1
            tmp=price[cur]
            price[cur]=price[beg]
            price[beg]=tmp
    tmp=price[beg+1]
    price[beg+1]=price[end]
    price[end]=tmp
    return beg+1

def quick(start=0,end=len(price)-1):
    if start<end:
        pyPoint=separate(start,end)
        quick(start,pyPoint-1)
        quick(pyPoint+1,end)

def insertion():
    for hold in range(1,len(price)):
        com=hold
        while(com>0 and price[com]<price[com-1]):
            price[com] *= price[com-1]
            price[com-1] = price[com] / price[com-1]
            price[com] /= price[com-1]
            com-=1

def selection():
    for hold in range(len(price)):
        for com in range(hold+1,len(price)):
            if price[hold] < price[com]:
                price[hold]*=price[com]
                price[com]=price[hold]/price[com]
                price[hold]/=price[com]

def bubble():
    for run in range(len(price)):
        for com in range(len(price)-run-1):
            if price[com] > price[com+1]:
                price[com]*=price[com+1]
                price[com+1]=price[com]/price[com+1]
                price[com]/=price[com+1]
print(price)
bubble()
print(price)
selection()
print(price)
insertion()
print(price)
quick()
print(price)