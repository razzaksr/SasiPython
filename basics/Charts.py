# $#

chart=""
for row in range(1,3):
    for seat in range(1,5):
        amt=int(input("Enter amount: "))
        if amt>=350:chart+="$"
        else:chart+="#"
        if seat % 2 == 0: chart += " "
    chart+="\n"
print(chart)