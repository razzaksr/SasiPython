#  array:
'''import array
var=array.array('i',[12,34,56])'''
'''import array as a
var=a.array('f',[1.2,4.5,6.7])'''
from array import *
var=array('i',[1,3,6,12,8,7,1,19])

var.append(26)
print(var)

var.insert(4,17)
print(var)

#reading:
print(var[8])
#Slicing operator:
print(var[:])
print(var[0:2])
print(var[4:10])
print(var[::-1])
print(var[9:2:-1])
#update
var[5]=82
print(var)
var[0:4]=array('i',[0,0,0])
print(var)
#delete
var.remove(7)
print(var)
var.pop()
print(var)
var.pop(3)
print(var)
del var[5]
print(var)

print(var.count(0))
print(var.index(1))
print(var.itemsize)
print(len(var))