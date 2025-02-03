# Password Generator
import random
complete = True

print("Welcome To Your Password Generator!")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@$%^&*().,?'
while complete:
    number = input("Enter the number of passwords you want to generate or press 0 to exit: ")
    if number.isalpha() or number == "":
        print("Wrong Input! Enter a number or press 0 to exit!")
    else:
        number = int(number)
        if number == 0:
            print("Exit Of The Program!")
            break 
        else:
            while complete:
                length = input("Enter the passwords length in numbers: ")
                if length == "" or length.isalpha():
                    print("Please enter a valid length for your passwords!")
                else:
                    length = int(length)
                    print("\nHere are your passwords:")
                    for pwd in range(number):
                        passwords = ''
                        for c in range(length):
                            passwords += random.choice(chars)
                        print(passwords)
                    complete = False 
            
