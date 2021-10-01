import math

def findSecondLargest(array):
    min = math.inf
    max = 0
    second_largest = 0
    
    for i in range(len(array)):
        
        if array[i] < min: 
            min = array[i]
        if array[i] > max:
            second_largest = max #second largest equals current max replaced by the new max
            max = array[i]
             
    print ("{}".format(second_largest))

findSecondLargest([7,28, 1,2000,3,4])

