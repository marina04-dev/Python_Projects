''' Problem J5: Tandem Bicycle
Problem Description: 
Since time immemorial, the citizens of Dmojistan and Pegland have been a war.
Now they have finally signed a truce. They have decided to participate in a 
tandem bicycle ride to celebrate the truce. There are N citizens
from each country. They must be assigned to pairs so that each pair contains
one person from Dmojistan and one person from Pegland.

Each citizen has a cycling speed. In a pair, the fastest person will always operate the tandem
bicycle while the slower person simply enjoys the ride. In other words,
if the members of a pair have speeds a and b, then the bike speed of the pair
is max(a,b). The total speed is the sum of the N individual bike speeds.

For this problem, in each test case, you will be asked to answer one of two questions:
    - Question 1: what is the minimum total speed, out of all possible assignments into pairs?
    - Question 2: what is the maximum total speed, out of all possible assignments into pairs?'''
    
    
# Solution 
q = int(input(("Enter the question's number (1 or 2): "))
n = int(input("Enter the amount of citizens from each country: "))

dmoj = list(map(lambda x: int(x), input("Enter Dmojistan citizens speed with a space between each person: ").split(" ")))
peg = list(map(lambda x: int(x), input("Enter Pegland citizens speed with a space between each person: ").split(" ")))

speed = 0 
dmoj.sort()
peg.sort()

if q == 1:
    # min total speed 
    for i in range(n):
        speed += max(dmoj[i], peg[i])
        
else:
    # max total speed 
    dmoj = dmoj[::-1]
    for i in range(n):
        speed += max(dmoj[i], peg[i])
        
print(speed)
