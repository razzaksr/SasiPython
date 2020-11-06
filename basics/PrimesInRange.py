# prime series in given length

start=int(input("Tell us start range: "))
limit=int(input("Tell us prime end point: "))
if limit>=start:
    for num in range(start,limit+1):
        if num==2 or num ==3 or num==5 or num==7 or num%2!=0 and num%3!=0 and num%5!=0 and num %7!=0:
            print(num,end=" ")
else:
    print("Invalid start and limit")