n=int(input("Enter the number"))
product=1
for i in range(1,n+1):
    product=product*i
print(f"The factorial of {n} is {product}")
# Using while loop
n=int(input("Enter the number"))

i=1
res=1
while(i<=n):
    res=res*i
    i+=1
print(f"The factorial of {n} is {res}")