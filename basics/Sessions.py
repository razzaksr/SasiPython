# training session

skill=input("Tell us skillset you wish to get trained: ")
timing=float(input("Tell us timing you wish: "))
if timing>10.00 and timing < 12.30:
    if skill=="java" or skill=="spring" :
        print(skill,"Training happening @ CSE block")
    else:print(skill,"not available in",timing)
elif skill=="python" or skill=="flask":
    if timing>13.00 and timing<16.40:
        print(skill,"Training happening @ MCA block")
    else:
        print(skill, "not available in", timing)
elif skill=="dotnet" and timing>16.00:
    if timing<20.00:
        print(skill,"Training happening @ IT block")
    else:
        print(skill, "not available in", timing)
else:print("requested ",skill,"not offered by placement")