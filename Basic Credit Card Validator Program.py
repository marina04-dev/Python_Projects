''' Python Credit Card Validator Program '''
''' 1. Remove any '-' or ' ' 
    2. Add all digits in the odd places from right to left
    3. Double every second digit from right to left 
        (If result is a two-digit number, add the two-digit number
        together to get a single digit)
    4. Sum the totals of steps 2 & 3
    5. If sum is divisable by 10, the credit card is valid '''
        
# Step 1     
card = input("Enter a credit card number: ")
card = card.replace("-","")
card = card.replace(" ","")
card = card[::-1]

# Step 2 
sum_odd_digits = 0 
sum_even_digits = 0 
for x in card[::2]:
    sum_odd_digits += int(x)
    
# Step 3 
for x in card[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x 
        
# Step 4 
total = sum_even_digits + sum_odd_digits

# Step 5
if total % 10 == 0:
    print("Valid Credit Card Number!")
else:
    print("Not Valid Credit Card Number")
    
