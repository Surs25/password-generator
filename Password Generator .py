import random 
chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
length= int(input("Enter length of the password: "))
passwd=""
for i in range(length):
    passwd += random.choice(chars)
op=input("do you wish to add Symbols[Y/N]: ")

if op=="Y" or op=="y":  
    s_amount=int(input("Enter How many symbols you want: "))
    Symbols="!@#$%^&*()_+-={}[]|\':;.<,>?/~`"
    for j in range(s_amount):
        passwd += random.choice(Symbols)
    print("Your password is", passwd)
elif op=="N" or op=="n":
    print("Your password is", passwd)
else:
    print("Invalid option")



