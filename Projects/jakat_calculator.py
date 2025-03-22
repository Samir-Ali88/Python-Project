print("------Welcome to Zakat Calculator-------")
print("""To become Eligable for Zakat you must have 
Gold Nisab = 87.48 grams of gold
Silver Nisab = 612.36 grams of silver
Cash & Savings = Must be equal to the value of 87.48g gold or 612.36g silver""")
while True:
    user=input("For Calculating press (c) \nFor quiting press (q)\nEnter the value:  ").lower()
    if user=="q":
        print("Exiting Calculator....")
        break
    elif  user=="c":
        amount=float(input("Enter the amount of Nisab amount you have (Must be in money) : "))
        zakat= 2.5/100 * amount
        print(f"You need to pay {zakat} taka Zakat")
    
    else:
        print("Invalid value")    