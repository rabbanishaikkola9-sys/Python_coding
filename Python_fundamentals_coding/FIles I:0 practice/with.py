# f=open("hello.txt")
# print(f.read())
# f.close()
with open("hello.txt") as f:
    print(f.read())
# you have to explicitly close the file