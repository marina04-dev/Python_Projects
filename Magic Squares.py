# Magic Squares 
""" A magic square is a 2D matrix composed of n^2 integers
where n is the length of one row/column. In a magic square
each row, each column and the 2 diagonals must sum to the 
same value. """

""" This Function given a 2D matrix the function determimes 
if the square is magic or not and displays "magic" or "not magic" 
accordingly """

""" The program takes an input n, representing the length of one 
row of the matrix. It will then take n lines of input containing
n integers seperated by spaces. """


""" Magic Squares """
matrix = []
n = int(input("Enter the length of one row: "))

# Array Insertion
for _ in range(n):
    nums = input("Enter: ")
    matrix.append([int(x) for x in nums.split()])

# Goal's calculation (summary of the first row)
magic_sum = sum(matrix[0])

# Checking rows and preparing columns
columns = [[] for _ in range(n)]
for row in matrix:
    if sum(row) != magic_sum:
        print("Not Magic!")
        exit()
    for j, elem in enumerate(row):
        columns[j].append(elem)

# Columns Checking
for col in columns:
    if sum(col) != magic_sum:
        print("Not Magic!")
        exit()

# Diagonals Checking
main_diagonal = sum(matrix[i][i] for i in range(n))
anti_diagonal = sum(matrix[i][n - 1 - i] for i in range(n))

if main_diagonal != magic_sum or anti_diagonal != magic_sum:
    print("Not Magic!")
else:
    print("Magic!")

