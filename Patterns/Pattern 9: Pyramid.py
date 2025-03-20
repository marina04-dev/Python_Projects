# Pattern 9 - Pyramid 
rows9 = 5 
for i in range(1, rows9+1):
    if i == rows9:
        print('*' * (2*i-1))
    else:
        print(' ' * (rows9-i) + '*' + ' ' * (2*i-3) + ('*' if i>1 else ''))
    
print("\n\n\n\n") 
