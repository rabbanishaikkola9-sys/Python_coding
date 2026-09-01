def result():
    f=int(input("Enter the temp in F")) 
    c=5*(f-32)/9
    return c
res=result()
print(round(res,2))