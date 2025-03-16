""" This Function given a string of alphabetical characters returns a new string with
the characters in alphabetical order. The string might contains both capital and
lowercase letters. There will be no spaces in the string. Capital Letters 
appear before the same lowercase letter in part b. Part a works only for 
lowercase. """
# Alphabet Soup Part A
def alphabetSoup(string):
    li = sorted(list(string))
    newString = ''
    for char in li:
        newString += char 
    return newString
    
word = input("Please enter a word: ")
print(alphabetSoup(word))



# Alphabet Soup Part B
def alphabetSoup(string):
    li = sorted(list(string))
    lowerLi = sorted(list(string.lower()))
    caps = []
    newString = ''
    for char in li:
        if char.isupper():
            caps.append(char)
            
    for letter in lowerLi:
        if caps.count(letter.upper()) != 0:
            newString += letter.upper()
            caps.pop(caps.index(letter.upper()))
        else:
            newString += letter
    return newString

word = input("Please enter a word: ")
print(alphabetSoup(word))
