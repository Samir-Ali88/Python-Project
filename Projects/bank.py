print("------Welcome to LALA BANK----")
print("""1.For opening account type (open)
2.For checking money type (check)
3.For diposit more money type(diposit)
4.For withdrawin money type (withdraw)
5.For exiting type(exit) """)
amount={} #total bank data

while True:
    user=input("Enter type what do you want?: ").lower() #what user want to do
    if user=="open": #if user want to open account
        name_user=input("Enter Your Name: ").capitalize()
        money_user=int(input("How much money do you want to save :"))
        amount[name_user]=money_user #this indicates money
        print(f"Account is opened for {name_user} with the balance of : {amount[name_user]}") #amount[name_user] is indicate as money in the account
    elif user=="check": #if user want to check his amount
        name_user=input("Enter your name :").capitalize()
        if name_user in amount :
            print(f"{name_user} Current balance is : {amount[name_user]}")
        else:
            print("No user found try again with correct name")    
    elif user=="diposit": #if user want to diposit money
        name_user=input("Enter You name: ").capitalize()
        if name_user in amount: #confirms if user exists in bank🤣🤣
            diposit_user=int(input("How much money do you want to add: "))
            amount[name_user] +=diposit_user
            print(f"Your deposted amount {diposit_user} has been added sucessfully\nCurrent Balance is: {amount[name_user]}") #amour[name_user ] is the balance       
        else:
            print("No user found try again with correct name")    
    elif user=="withdraw": #if user wants to withdraw the money
        name_user=input("Enter Your name: ").capitalize()
        if name_user in amount:
            withdraw_user=int(input("Enter the amount you want to withdraw: "))
            if withdraw_user>amount[name_user]:
                print("Not enough balance")
            elif withdraw_user==0:
                print("No money was withdrawn")
            elif withdraw_user<=amount[name_user]:
                amount[name_user] -= withdraw_user
                print(f"Your withdrawn amount {withdraw_user} has been deducted sucessfully\nCurrent Balance is: {amount[name_user]}")
            else:
                print("Invalid value")    

    elif user=="exit":
        print("Exiting....")
        break    
    else:
        print("Invalid value")
print("Thanks for using my bank")        
