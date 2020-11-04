# Logicals

print("-------Welcome to Loan agency-----")
salary=int(input("Tell us monthly salary: "))
file=bool(input("Are you paying your tax properly: "))
print("Are you eligible for personal loan of 1L: ",((salary>=15000) or (file==True)))
print("Are you eligible for business loan of 10L: ",((salary>=50000) and (file==True)))
print("Are you eligible for home loan of 5L: ",((salary>=20000 and salary<=40000)))
print("Are you eligible for loan against property: ",((not file==False)))