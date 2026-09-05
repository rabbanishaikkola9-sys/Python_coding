f=open("hello.txt")
reading=f.read()
# print(reading)
f.close()
text="hey there this is this and that is that luffy will become the king of the pirates and I will be master of python "
with open ("hello.txt","w") as f:
    reading=f.write(text)