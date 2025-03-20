# Pattern 4 - Butterfly 
rows4 = 5 
# Upper Part 
for i in range(1, rows4+1):
    print('*' * i + ' ' * (2 *(rows4-i)) + '*' * i)
    
# Lower Part
for i in range(rows4, 0, -1):
    print('*' * i + ' ' * (2 *(rows4-i)) + '*' * i)
    
    
print("\n\n\n\n")
