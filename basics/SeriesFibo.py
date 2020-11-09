# Fibonacci series: 0 1 1 2 3 5 8 13 21 ,,,,,


num1=0
num2=1
print(num1,num2,end=" ")
for temp in range(2,int(input("Tell us count of fibonacci: "))):
    sum = num1 + num2
    num1=num2
    num2=sum
    print(num2,end=" ")