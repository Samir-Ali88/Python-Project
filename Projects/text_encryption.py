import random
import string

chars=string.ascii_letters + string.digits + string.punctuation +" " #this linr of code iimports all the letters alphabets
chars=list(chars) #this  line adds all letters in a list for better visiulization
keys=chars.copy() #copys everything chars
random.shuffle(keys)#shuffles the elements from chars

# print(f"char;{chars}")
# print(f"keys:{keys}")

#-----Encryption-----
text=input("Enter the text you want to encrypt: ")
cipher=""
for letters in text:    
    ind=chars.index(letters) #finds the letter in index
    cipher += keys[ind] #use the letter from index


print(f"Your Plain text is : {text}")
print(f"Your encrypted text is: {cipher}")
print("-----Encryption Done-----")