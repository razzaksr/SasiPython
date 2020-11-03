# operations: arithmetic, shorthand, member, identity , bitwise, relational, logicals

# Convertors:

'''cent=float(input("Tell us cent value"))
acre=cent/100;
print("Acre wise ",cent," is ",acre)'''


# possible to withdraw or not
'''amt=int(input("Tell us desired amount to withdraw: "))
hai=(amt%500==0)
denom=(int)(amt/500)
print("Is withdraw possible",hai)
print("No of cureencies: ",denom)'''

# FD calculator:
'''deposit=int(input("Tell us amount to open FD: "))
intrest=6.8
profit=(deposit*intrest)/100
maturity=deposit+profit
print("Maturity is: ",maturity)
print("Intrest is: ",profit)
print("Yearly wise outline",profit)
print("Yearly twise outline",profit/2)
print("Yearly four times outline",profit/3)
print("Each month: ",profit/12)'''

# swap two numbers
num1=int(input("Tell us number one: "))# 30
num2=int(input("Tell us number two: "))# 89
print("Number 1",num1,"number 2",num2)
num1*=num2#num1=num1*num2
num2=num1/num2
num1/=num2#num1=num1/num2
print("Number 1",num1,"number 2",num2)
