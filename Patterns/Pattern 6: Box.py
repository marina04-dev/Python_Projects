# Pattern 6 - Box 
rows6 = 5 
for i in range(rows6):
    if i == 0 or i == rows6-1:
        print('*' * rows6)
    else:
        print('*' + ' ' * (rows6-2) + '*')

print("\n\n\n\n")
