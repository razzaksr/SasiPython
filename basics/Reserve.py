# bus reservation

seats=1
while seats<=10:
    fare = int(input("Enter the amount: "))
    if fare >= 250 and fare < 600:
        print("You can travel @ seater class in the bus ",seats)
        seats+=1
    elif fare >= 600:
        print("You can travel @ sleeper class in the bus ",seats)
        seats+=1
    else:
        print("Insufficient amount to travel in this bus")
else:
    print("Bus has started its journey")