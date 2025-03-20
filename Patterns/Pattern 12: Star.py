# Pattern 12 - Star
import math 

def main():
    q = math.tan(math.pi * 0.4)
    w = math.tan(math.pi * 0.2)
    
    n = float(input("Enter the size: \n"))
    
    for j in range(math.ceil(n * q), -1, -1):
        for i in range(-math.ceil(0.55*n*q/w-n), math.ceil(0.55*n*q/w-n)):
            if ((j<= 0.55 *n*q and j >= (i+n) * w and j >= (n-i) *w ) or (j>=(i+n) *w and j <= (i+n) * q and j <= (n-i) * q) or (j<=(n-i) * q and j >= (n-i) * w and j <=(i+n) * q)):
                print("*", end='')
            else:
                print(" ", end='')
        print()
    if __name__ == "__main__":
        main()
        
main()
