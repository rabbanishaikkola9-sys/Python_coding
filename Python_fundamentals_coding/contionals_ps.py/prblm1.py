# 1. Write a program to find the greatest of four numbers entered by the user.
a1=int(input("Enter the number1"))
a2=int(input("Enter the number2"))
a3=int(input("Enter the number3"))
a4=int(input("Enter the number4"))
print(f"The numbers are{a1},{a2},{a3},{a4}")
if(a1>a2 and a1>a3 and a1>a4):
    print(f"{a1} is the greatest number:\n")
elif(a2>a1 and a2>a3 and a2>a4):
    print(f"{a2} is the greatst")
elif(a3>a1 and a3>a2 and a3>a4):
    print(f"{a3} is the greatest")
elif(a1==a2 and a2==a3 and a3==a4):
    print("Everthing is same")
else:
    print(f"{a4} is the greatest")
    
# end of ladder
print("\t End of the program")