import math

def reverseArray(array):
    result = []
    
    i = len(array) - 1
    while i >= 0:
        result.append(array[i])
        i-= 1
             
    print (result)

reverseArray([7,28, 1,2000,3,4])

