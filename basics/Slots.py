# Giant Wheel
for cabin in range(1,6):
    print("Filling cabin no:",cabin)
    seat=1
    while seat<=4:
        age=int(input("Tell us age: "))
        if age>=14:
            print("Seat ",seat," filled @ cabin",cabin)
            seat+=1