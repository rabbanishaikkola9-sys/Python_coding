f=open("peoms.txt")
reading=f.read()
if("twinkle " in reading):
    print("twinkle is present in the txt")
else:
    print("Twinkle is not present in the txt")
f.close()