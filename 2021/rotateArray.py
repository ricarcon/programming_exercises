import math

def rotateArray(array, n):
    result = []
    
    i = n
    count = 0
    while count < len(array):
        
        if n >= len(array):
            n = 0
        result.append(array[n])
        
        n += 1
        count += 1
             
    print (result)

rotateArray([7,28, 1,2000,3,4], 2)

