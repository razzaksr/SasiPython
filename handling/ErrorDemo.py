# Error Handling demo

try:
    empName = input("Tell us your name: ")
    empSalary = float(input("Tell us your annual salary: "))
    if empSalary >= 4 and empSalary <= 8:
        print("We'll offer 2Lacks limited Credit card", empName)
    elif empSalary > 8:
        print("We'll offer 3Lacks limited Credit card", empName)
    else:
        print("No credit card offer available for you", empName)
except ValueError as verror:
    print(verror,"\nSalary should be numerical data")
    empSalary = float(input("Tell us your annual salary: "))
    if empSalary >= 4 and empSalary <= 8:
        print("We'll offer 2Lacks limited Credit card", empName)
    elif empSalary > 8:
        print("We'll offer 3Lacks limited Credit card", empName)
    else:
        print("No credit card offer available for you", empName)
finally:
    print("Enquiry Done")
