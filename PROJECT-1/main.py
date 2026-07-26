#*************** *************** FIRST PROJECT   ******************************  #
'''
1 for snake
-1 for water
0 for gun
'''
"""
 Snake drinks/beats Water, Water douses/beats Gun, and Gun shoots/beats Snake


"""
import random

computer = random.choice([0, 1, -1])
# print(num)
youip=input("Enter your choice (s/w/g): ").lower()
youdict={
    "s":1,
    "w":-1,
    "g":0
}
reverseddict={
    1:"Snake",
    -1:"Water",
    0:"Gun"
}

if youip not in youdict:
    print("Invalid choice! Please enter s, w, or g.")
else:
    you=youdict[youip]
    print(f"You chose {reverseddict[you]}, Computer chose {reverseddict[computer]}")
    
    if(you==computer):
        print("Its draw!!")
    else:
        if(you==1 and computer==-1):
            print("You won!!") # Snake beats Water
        elif(you ==-1 and computer==1):
            print("You lose and computer wins!!")
        elif(you==0 and computer==1):
            print("You won!!") # Gun beats Snake
        elif(you==0 and computer==-1):
            print("You lose and computer wins!!") # Water beats Gun
        elif(you==1 and computer==0):
            print("you lost") # Snake loses to Gun
        elif(you==-1 and computer==0):
            print("You won!!") # Water beats Gun
        else:
            print("Something went wrong")

'''
if(computer-you==1 or computer-1==-2):
    print('You won')
    else:
    print('You lost')
'''

