# handling multiple exception

history=(20,120,50,70,0,300,60,10)
try:
    liters = int(input("Tell us liters you filled: "))
    pos = int(input("Tell us index to find travelled km to calculate fuel consumption: "))
    kms = history[pos]
    print("fuel consumed per km", (liters / kms))
except ValueError as verror:
    print(verror,"\nData are should be numeric")
    liters = int(input("Tell us liters you filled: "))
    pos = int(input("Tell us index to find travelled km to calculate fuel consumption: "))
    kms = history[pos]
    print("fuel consumed per km", (liters / kms))
except IndexError as ierror:
    print(ierror,"\nSelect position within",len(history))
    pos = int(input("Tell us index to find travelled km to calculate fuel consumption: "))
    kms = history[pos]
    print("fuel consumed per km", (liters / kms))
except ZeroDivisionError as zerror:
    print(zerror,"\nplease select index within",len(history),"and besides 4")
    pos = int(input("Tell us index to find travelled km to calculate fuel consumption: "))
    kms = history[pos]
    print("fuel consumed per km", (liters / kms))
except Exception as error:
    print(error)
finally:
    print("Fuel consumption calculation done")