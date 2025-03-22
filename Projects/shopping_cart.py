foods=[]
prices=[]
total=0
while True:
    user=input("Enter Food name or q to quit: ")
    if user.lower()=="q":
        print("Quiting the program....")
        break
    else:
        price=float(input("Enter The price of food: "))
        foods.append(user)
        prices.append(price)
        total +=price
print(f"Your items are: {foods}")
print(f"price are: {prices}") 
print(f"Total amount is: {total}")       