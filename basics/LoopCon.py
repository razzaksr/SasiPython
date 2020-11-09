# continue, break

seat=1
while seat<=10:
    if seat%3==0:
        print("Booked by online already")
        seat+=1
        break
    else:
        print("can be booked as open ticket")
        seat+=1