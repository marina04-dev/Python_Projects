# Pattern 11 - X Letter
rows11 = 5 
for i in range(1, rows11+1):
    for j in range(1, rows11+1):
        if i == j or i + j == rows11 + 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print("\n\n\n\n")
