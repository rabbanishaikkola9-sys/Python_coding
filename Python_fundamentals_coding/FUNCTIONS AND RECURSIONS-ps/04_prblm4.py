n=int(input("Enter the number"))
def fact(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        return n+fact(n-1)
res=fact(n)
print(res)