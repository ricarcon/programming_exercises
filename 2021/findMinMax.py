import math

def findMinMax(array):
    min = math.inf
    max = 0
    
    for i in range(len(array)):
        
        if array[i] < min: 
            min = array[i]
        if array[i] > max:
            max = array[i]
            
    print ("Min: {} & Max: {}".format(min, max))
findMinMax([7, 1,2000,3,4])

