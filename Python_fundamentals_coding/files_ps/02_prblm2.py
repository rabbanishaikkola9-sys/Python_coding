import random
def game():
    print("You are playng the game")
    score=random.randint(1,100)
    # fetch the hiscore
    with open("hiscore.txt","r") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)  # Throws ValueError because empty string '' cannot be converted to int
        else:
            hiscore=0             # Resets valid scores (e.g. "50") back to 0

    print(f"Your score is {score}")
    if(score > hiscore):
        #write the hiscore here
        with open("hiscore.txt","w") as f:
            f.write(str(hiscore))
    return score
game()
