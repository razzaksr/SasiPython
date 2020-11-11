# patterns: 8 basic:
'''
12345
12345
12345
12345
12345
'''
'''for step in range(1,6):
    num=1
    for stone in range(1,6):
        print(num,end="")
        num+=1
    print()'''

'''
Floyds: left upper
a
ab
abc
abcd
abcde
'''

'''for step in range(1,6):
    let=97
    for stone in range(1,step+1):
        print(chr(let),end="")
        let+=1
    print()'''

'''
Floyd: right upper
             5
          3  6
      10 15 20
   9  12 15 18
25 30 35 40 45
'''

'''five=5
three=3
for step in range(1,6):
    for space in range(5,step,-1):
        print(" ",end="")
    for data in range(1,step+1):
        #print("#",end="")
        if step%2==0:
            print(three,end="")
            three+=3
        else:
            print(five,end="")
            five+=5
    print()'''

'''
Pascal: upper
      z
     z e
    z e a
   z e a l
  z e a l o
 z e a l o u 
z e a l o u s
'''
'''data="zealous"
for step in range(1,8):
    for space in range(7,step,-1):
        print(" ",end="")
    for stone in range(0,step):
        print(data[stone]+" ",end="")
    print()'''

'''
Pyramid: upper
   z
  zea
 zealo
zealous
'''
'''data="zealous"
limit=1
for step in range(1,5):
    for space in range(4,step,-1):
        print(" ",end="")
    for stone in range(0,limit):
        print(data[stone],end="")
    limit+=2
    print()'''

'''
pyramid:lower
zealous
 zealo
  zea
   z
'''
'''data="zealous"
limit=7
for step in range(4,0,-1):
    for space in range(4,step,-1):
        print(" ",end="")
    for stone in range(0,limit):
        print(data[stone],end="")
    limit-=2
    print()'''

'''
pascal:lower
z e a l o u s
 z e a l o u
  z e a l o
   z e a l
    z e a
     z e
      z
'''

'''data="zealous"
for step in range(7,0,-1):
    for space in range(7,step,-1):
        print(" ",end="")
    for stone in range(0,step):
        print(data[stone]+" ",end="")
    print()'''

'''
Floyd:right lower
45 40 35 30 25
   18 15 12  9
      20 15 10
          6  3
             5
'''
'''five=45
three=18
for step in range(5,0,-1):
    for space in range(5,step,-1):
        print(" ",end="")
    for data in range(1,step+1):
        #print("#",end="")
        if step%2==0:
            print(three,end="")
            three-=3
        else:
            print(five,end="")
            five-=5
    print()'''

'''
Floyd: left lower
abcde
abcd
abc
ab
a
'''
for step in range(5,0,-1):
    let=97
    for stone in range(1,step+1):
        print(chr(let),end="")
        let+=1
    print()