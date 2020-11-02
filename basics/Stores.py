# Shopping kart
# input>> str
# type conversion: casting

holder=input("Tell us account holder: ")#"Sasi kumar"

contact=int(input("Tell us contact number: "))#9876545676

items=[]
items.append(int(input("Tell us product price: ")))#[1200,5600,9888,10999,4500,5100]
items.append(int(input("Tell us product price: ")))#[1200,5600,9888,10999,4500,5100]
items.append(int(input("Tell us product price: ")))#[1200,5600,9888,10999,4500,5100]

print(type(holder),type(contact),type(items))

print(holder," holding ",items," to be purchased with sum of",sum(items),"by the contact ",contact)