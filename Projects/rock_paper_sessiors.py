import random

def play():
    user = input("r for rock ,p for paper,s for sissors: ").lower()
    computer= random.choice(["r","p","s"])
    print(f"Computer output:{computer}")

    if user==computer :
        return'Its a tie'
    if win (user,computer):
        return'You win'
    return 'You lose'    

def win(player,computer):
    if (player=="r" and computer =="s") or \
       (player=="s" and computer=="p") or \
       (player=="p" and computer=="r" ):
        return True    
print(play())   
