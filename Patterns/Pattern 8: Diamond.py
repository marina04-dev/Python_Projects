# Pattern 8 - Diamond
rows8 = 5 
# Upper Part
for i in range(1, rows8+1):
    print(' ' * (rows8-i) + '*' + ' '* (2*i-3) + ('*' if i > 1 else ''))
    
# Lower Part 
for i in range(rows8-1, 0, -1):
    print(' ' * (rows8-i) + '*' + ' ' * (2*i-3) + ('*' if i > 1 else ''))


print("\n\n\n\n")
