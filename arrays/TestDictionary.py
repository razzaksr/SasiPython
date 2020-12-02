# Dictionary:{key:value}

laptops={"Vostro":32400,"Inspiron":45600,"Compaq":32400,"Pavilion":42090,"Studio":56900,"Vaio":81000,"NoteBook":37600,"MacBook":92400}

print(laptops)

for x,y in laptops.items():
    print(x,y)

laptops['BusinessBook']=84500
laptops['Vostro']=27600

for x in laptops.values():
    print(x)
print(laptops)

print(laptops.keys())

#print(laptops[input("Tell us model to get price: ")])

laptops.popitem()

del laptops['Inspiron']

laptops.pop('Compaq')

print(laptops)
