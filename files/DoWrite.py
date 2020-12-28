file=open("sasifirstfile.txt","w")

#writing content
file.write(input("Tell us something to record: "))

file.close()

print("content written successfully in",file.name)