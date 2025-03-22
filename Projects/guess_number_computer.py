import random
def play(x):
    random_number= random.randint(1,x)
    play=0
    while play!=random_number:

        play=int(input("Enter a number: "))

        if play>random_number:
            print("Your Number is too high")
        elif play<random_number:
            print("Your number is low") 
    print(f"Your Number is correct:{random_number}")
play(500)               