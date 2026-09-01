n=int(input("Enter the number of rows"))
def pattern(n):
    if(n==0):
        return "its zero"
    else:
        print("*"*n)
        pattern(n-1)
a=pattern(n)
print(a)
