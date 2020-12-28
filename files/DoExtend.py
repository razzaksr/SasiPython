file=open("sasisecondfile.txt","a")

#gets=['hai','hello',9.8,7.9,12,9,67]
#file.write(str(gets))
file.write(input("Tell us new content to be written in file: "))

file.close()

print("content written in",file.name)