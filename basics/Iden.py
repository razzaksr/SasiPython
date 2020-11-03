# identity operator: is, is not

con=98.2

print(con,id(con))

hify=98.3

print(hify,id(hify))

top="Mukesh"
secondTop="Richard"

print(top is secondTop)

secondTop="Mukesh"

print(top is not secondTop)