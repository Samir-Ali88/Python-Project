import random

def play():
    user=input("For head H \nFor tale T\nEnter Vlaue: ").upper()
    computer= random.choice(["H","T"])
    print(f"Computer output {computer}")
    if user==computer:
        return"You Win the toss"
    return "You loss"   
print(play()) #it will exicute return value