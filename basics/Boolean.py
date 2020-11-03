# relational: > < == != >= <=
# logicals: and or not

entry=int(input("Tell us amount you have: "))
print("Are you able to enter into themepark: ",entry>=300)
print("Are you allowed to have free lunch: ",(entry>700))
print("Are you able to watch 3D show: ",(entry<=500))
print("Are you eligible for random gift holder: ",(entry%6==0))
print("Are you eligible to get free travel pass: ",(entry%4==0))