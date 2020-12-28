file=open("D:\\jpgms\\2020-09-16.doc","r")

print(file.read(100))

#tells the current cursor position
print(file.tell())

#redirect cursor to specified number of character by offset and rediretion based on by whence
file.seek(10,0)

print(file.tell())

print("After position changed to 10 from beginning",file.read())

file.close()

print("Content from",file.name,"has been read successfully")