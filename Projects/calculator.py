print("This is homemade calculator🤣🤣")
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
o=input("Enter an operator(+,_,*,/) : ")
if o=="+":
    print(f"{a} + {b} =",a+b)
elif o=="-":
    print(f"{a} - {b} =",a-b) 
elif o=="*":
    print(f"{a} * {b} =",a*b)
elif o=="/":
    try:
        print(f"{a} / {b} =",a/b)    
    except ZeroDivisionError:
        print("Cannot divdided by Zero 😒😒")
else:
    print("Invalid  operator ☹️ ☹️")            