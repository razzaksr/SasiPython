# returntypes: return

def square(num,pow):
    if pow==0:return 0
    else:
        temp=1
        for times in range(pow):
            temp*=num
        return temp

got=square(4,0)
print(got)
print(square(9,2))

