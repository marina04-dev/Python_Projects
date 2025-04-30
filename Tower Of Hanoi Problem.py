# Tower of Hanoi Problem
''' Tower of Hanoi consists of three pegs or towers 
with n disks placed one over the other.

The objective of the puzzle is to move the stack to 
another peg following these simple rules:
    1. Only one disk can be moved at a time.
    2. No disk can be placed on top of the smaller disk.'''
    
def tower(n, first, median, dest):
    if n == 1:
        print("Move disc 1 from ", first, " to ",dest, "\n")
    else:
        tower(n-1, first, median, dest)
        print("Move disc ", n," from ", first, " to ",dest, "\n")
        tower(n-1, median, dest, first)
        
        
tower(4,'A', 'B', 'C')
            
