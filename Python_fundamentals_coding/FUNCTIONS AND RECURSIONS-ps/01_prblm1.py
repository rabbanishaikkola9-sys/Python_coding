def great(greet="Thankyou"):
    a=int(input("Enter the number"))
    b=int(input("Enter the number"))
    c=int(input("Enter the number"))
    if (a>b and a>c):
        print(f"{a} is the greatest {greet}")
    elif(b>a and b>c):
        print(f"{b} is the greatest {greet}")
    else:
        print(f"{c} is the greatest {greet}")
great()