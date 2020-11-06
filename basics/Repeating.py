# repeatation

stock=50
invoice=0
timing=11.00
profit=0

while stock>0 and timing<=11.40:
    required = int(input("Tell us how many quantity you want: "))
    if stock >= required:
        stock -= required
        invoice+=1
        profit+=8999*required
        print("Your order has placed for ",required," items")
    else:
        print("Product went insufficient for your requirement")
    timing+=0.05
else:
    print("Out of stock/ sale over; total invoices are: ",invoice)
    print("Total profit out of this sale: ",profit)