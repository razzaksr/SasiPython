# type error

height=int(input("Tell us height from ocean level that the place you visited: "))
place=input("Tell us the place that you visited: ")
try:
    print(height + " " + place)
except TypeError as terror:
    print(terror,"Casting need to be done")
    print(str(height)+" "+place)
finally:
    print("Place has registered in our records")