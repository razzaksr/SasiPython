# Control statements

print("*************Welcome to TNSTC*************")
dest=input("Tell us place you wish to travel: ")
if dest=="Chennai":
    busType = input("Tell us bus class you wish to travel: ")
    if busType == "Ordinary":
        ticket = int(input("Enter the amount: "))
        if ticket >= 240:
            print("Yeah You can travel in ordinary bus")
        else:
            print("Insufficient amount to get ticket")
    elif busType == "Ultra delux":
        ticket = int(input("Enter the amount: "))
        if ticket >= 320:
            print("Yeah You can travel in UL bus")
        else:
            print("Insufficient amount to get ticket")
    elif busType == "Sleeper":
        ticket = int(input("Enter the amount: "))
        if ticket >= 510:
            print("Yeah You can travel in Sleeper bus")
        else:
            print("Insufficient amount to get ticket")
    else:
        print("Bus service not available")
elif dest=="Coimbatore":
    busType = input("Tell us bus class you wish to travel: ")
    if busType == "Ordinary":
        ticket = int(input("Enter the amount: "))
        if ticket >= 150:
            print("Yeah You can travel in ordinary bus")
        else:
            print("Insufficient amount to get ticket")
    elif busType == "Ultra delux":
        ticket = int(input("Enter the amount: "))
        if ticket >= 220:
            print("Yeah You can travel in UL bus")
        else:
            print("Insufficient amount to get ticket")
    elif busType == "Sleeper":
        ticket = int(input("Enter the amount: "))
        if ticket >= 710:
            print("Yeah You can travel in Sleeper bus")
        else:
            print("Insufficient amount to get ticket")
    else:
        print("Bus service not available")