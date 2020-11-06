# even number series

limit=int(input("Tell us end point of even series: "))
'''for num in range(2,limit+1,+2):
    print(num,end=" ")'''

for num in range(1,limit+1):
    if num%2==0:print(num,end=" ")