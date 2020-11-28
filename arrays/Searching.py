# Binary:sorted,Linear: Unsorted

from array import *


house=array('i',[3,4,14,21,28,32,46,54,68,128,256,1024])

def binary(data,start=0,end=len(house)-1):
    if start<=end:
        mid = int((start + end) / 2)
        if house[mid] == data:return mid
        elif house[mid] > data:return binary(data, start, mid)
        else:return binary(data, mid+1 , end)
    else:
        return -1


users=int(input("Tell us data want to search: "))
pos=binary(users)
if pos!=-1:print(users,"found @",pos)
else:print(users,"not found anywhere")


'''def linear(data):
    print(data,"searched by linear way")
    for index in range(len(var)):
        if var[index]==data:
            return index
    else:return -1
var=array('d',[1.2,4.5,6.7,8.9,2.3,5.8,1.9,11.9,45.8,3.4])
users=float(input("Tell us data want to search: "))
pos=linear(users)
if pos!=-1:print(users,"found @",pos)
else:print(users,"not found anywhere")'''

