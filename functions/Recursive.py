# Recursive: function call by itself: repeatation, data structures algorithm

def count(number,sum=0):
    if number>0:
        print(number)
        sum+=number
        return count(number-1,sum)
    else:return sum

def facting(number,ft=1):
    if number>0:
        ft*=number
        return facting(number-1,ft)
    else:return ft

num=int(input("Tell us number: "))

fact=1
'''for n in range(num,0,-1):
    fact*=n'''
fact=facting(num)
print("Factorial",fact,"is for",num)

print("Sum of the series ",count(num))

limit=int(input("Tell us limit of ending sum of the series: "))

def sumOfSeries(number,sum=0):
    if number<=limit:
        print(number)
        sum+=number
        return sumOfSeries(number+num,sum)
    else:print(sum)

print("Sum of the",num,"series is")
sumOfSeries(num)