topCarModels=['fortuner','thar','xylo','innova','swift','waggenor','xuv','triber','creta','ertica']
try:
    position = int(input("Tell us position to know car model: "))
    print(topCarModels[position])
except ValueError as verror:
    print(verror,"\nPlease enter the position only numeric: ")
    position = int(input("Tell us position to know car model: "))
    print(topCarModels[position])
except IndexError as ierror:
    print(ierror,"\nPlease enter the position within",len(topCarModels))
    position = int(input("Tell us position to know car model: "))
    print(topCarModels[position])
except Exception as error:
    print(error)
finally:
    print("Thanks for having us")