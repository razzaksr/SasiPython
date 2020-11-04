# denomination

t2000s=10
f500s=20
t200s=10
o100s=30

cash=int(input("Tell us amount required: "))
denom=""

if t2000s>0:
    req=int(cash/2000)
    actualAmt=t2000s*2000
    if cash<=actualAmt:
        t2000s-=req
        cash-=req*2000
        denom="2000 x "+str(req)+"\n"
    else:
        denom="2000 x "+str(t2000s)+"\n"
        cash-=actualAmt
        t2000s=0
if cash>0:
    req = int(cash / 500)
    actualAmt = f500s * 500
    if cash <= actualAmt:
        f500s -= req
        cash -= req * 500
        denom += "500 x " + str(req)+"\n"
    else:
        denom += "500 x " + str(f500s)+"\n"
        cash -= actualAmt
        f500s = 0
if cash>0:
    req = int(cash / 200)
    actualAmt = t200s * 200
    if cash <= actualAmt:
        t200s -= req
        cash -= req * 200
        denom += "200 x " + str(req)+"\n"
    else:
        denom += "200 x " + str(t200s)+"\n"
        cash -= actualAmt
        t200s = 0
if cash>0:
    req = int(cash / 100)
    actualAmt = o100s * 100
    if cash <= actualAmt:
        o100s -= req
        cash -= req * 100
        denom += "100 x " + str(req)+"\n"
    else:
        denom += "100 x " + str(o100s)+"\n"
        cash -= actualAmt
        o100s = 0
if cash==0:
    print(denom)
else: print("Unable to dispense the cash")