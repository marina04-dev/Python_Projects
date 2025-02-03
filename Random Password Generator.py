# Random Password Generator
import random 

# A function do shuffle all the characters of a string 
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)
    
    
# Main program starts here
upperCaseLetter1 = chr(random.randint(65,90)) # Generate a random UpperCase Letter
upperCaseLetter2 = chr(random.randint(65,90)) # Generate a random UpperCase Letter 
upperCaseLetter3 = chr(random.randint(65,90)) # Generate a random UpperCase Letter 
upperCaseLetter4 = random.randint(0,9) # Generate a random digit
upperCaseLetter5 = random.randint(0,9) # Generate a random digit
upperCaseLetter6 = chr(random.randint(65,90)).lower() # Generate a random LowerCase Letter 
upperCaseLetter7 = chr(random.randint(65,90)).lower() # Generate a random LowerCase Letter 
upperCaseLetter8 = chr(random.randint(65,90)).lower() # Generate a random LowerCase Letter 

# Generate password using all the characters in random order
password = upperCaseLetter8 + upperCaseLetter7 + upperCaseLetter6 + str(upperCaseLetter5) + str(upperCaseLetter4) + upperCaseLetter2 + upperCaseLetter3 + upperCaseLetter1
password = shuffle(password)

print(password)
