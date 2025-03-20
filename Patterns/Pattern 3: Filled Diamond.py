# Pattern 3 - Diamond Filled
rows3 = 5 
# Upper Half
for i in range(1, rows3+1):
    print(' ' * (rows3-i) + '*' * (2*i-1))
    
# Lower Half 
for i in range(rows3, 0, -1):
    print(' ' * (rows3-i) + '*' * (2*i-1))

print("\n\n\n\n")
