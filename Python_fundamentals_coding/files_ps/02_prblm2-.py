import random
def game():
    print("You are playing game..")
    score=random.randint(1,100)
    # fetch the hiscore
    print(f"Your score is {score}")
    with open("hiscore.txt") as f :
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    if(score>hiscore):
        with open("hiscore.txt"):
            f.write(str(hiscore))
    return score
game()