# List: []

from array import *

price=array('d',[6.2,4.5,9.7,2.3,1.2,5.7])

data=(1.2,'Sasikumar',9,True,89,76,'Zealous')

record=list(price)
print(record)

record.sort()
print(record)

record.extend(list(data))
print(record)

for y in record:print(y)

print(record.count(1.2))
print(record.index(True))

nums=record.copy()
print(nums)
nums.reverse()
print(nums)

tup=tuple(record)
print(tup)