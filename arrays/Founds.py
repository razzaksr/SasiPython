# additional fundamental operations

from array import *


def all():
    print("Listing the array")
    for x in var: print(x,end=" ")
    print()
var=array('i',[17,3,6,21,8,7,1,19])

def show(index):
    if index<len(var):
        print(var[index],end=" ")
        index+=1
        show(index)
    else:return

def second():
    print("Finding Second Minimum,Maximum")
    fmin=var[0]
    fmax=var[0]
    smin=var[0]
    smax=var[0]
    for x in var:
        if fmin>x:
            smin=fmin
            fmin=x
        if smin>x and fmin!=x:
            smin=x
        if fmax<x:
            smax=fmax
            fmax=x
        if smax<x and fmax!=x:
            smax=x
    print("Second Min is: ",smin)
    print("Second Max is: ", smax)

def recurSecond(index,fmin=var[0],smin=var[0],fmax=var[0],smax=var[0]):
    if index<len(var):
        if fmin>var[index]:
            smin=fmin
            fmin=var[index]
        if smin>var[index] and var[index]!=fmin:
            smin=var[index]
        if fmax<var[index]:
            smax=fmax
            fmax=var[index]
        if smax<var[index] and var[index]!=fmax:
            smax=var[index]
        index+=1
        recurSecond(index,fmin,smin,fmax,smax)
    else:
        print("Through recursive Second Min: ",smin,"\nSecond max is ",smax)
        return

print(min(var))
print(max(var))

all()
show(0)
second()
recurSecond(0)