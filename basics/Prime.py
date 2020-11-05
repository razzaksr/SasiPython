
# prime :80%

num=int(input("Tell us number to verify its prime or not: "))

if num==2 or num==3 or num==5 or num==7 or num%2!=0  and num%3!=0 and num%5!=0 and num%7!=0:
    print("Given ",num," is prime")
else:
    print("Given ",num," is not prime")