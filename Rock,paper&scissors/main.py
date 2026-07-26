'''
rock :0
paper:1
scissor :-1
'''
import random
import sys

computer = random.choice([0, 1, -1])

youdict = {"r": 0, "p": 1, "s": -1}
reverseddict = {0: "rock", 1: "paper", -1: "scissor"}

youstr = input("Enter choice (r/p/s): ").lower()

if youstr not in youdict:
    print("Invalid input! Please enter r, p, or s.")
    sys.exit()

you = youdict[youstr]

print(f"You chose {reverseddict[you]} and computer chose {reverseddict[computer]}")

if you == computer:
    print("It's a draw!")
elif ((you == 0 and computer == -1) or 
      (you == 1 and computer == 0) or 
      (you == -1 and computer == 1)):
    print("You win!")
else:
    print("Computer wins, you lose!")
