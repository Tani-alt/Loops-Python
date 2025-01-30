#Power calculator
base=float(input("Enter the base number number"))
exponent=float(input("Enter the exponent number"))
result=(base, exponent)
print(f"{base} raised to the power of {exponent} is : {result}")
continue_choice=input("Do you want to calculte another power ? (yes/no) :")
if continue_choice!='yes' :
    print("Goodbye !")
