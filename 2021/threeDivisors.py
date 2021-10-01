import math

def countSquares(n):
    
    done = False
    i = 1
    while not done:
        if i * i < n:
            i += 1
        else:
            done = True
    
    return i - 1
        
        
print(countSquares(3))
print(countSquares(9))
print(countSquares(10))
print(countSquares(16))
print(countSquares(25))
print(countSquares(36))



