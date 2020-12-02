# Tuple: index,count
# CRUDL

data=(1.2,'Sasikumar',9,True,89,76,'Zealous')
nums=(1.2,3.4,6,8.9,12.5,3.4)

print(len(data))
print(max(nums))
print(min(nums))
print(sum(nums))
print(data)
print(data[2])
print(data[2:5])

#data[3]='Razak Mohamed'

for h in nums:print(h)

from array import *

arr=array('d',nums)
print(arr)

arr.append(5.6)
arr.insert(2,8.9)

arr[0]*=7

arr.pop(4)

nums=tuple(arr)
print(nums)

print(nums.count(3.4))

print(nums.index(12.5))