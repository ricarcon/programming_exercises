import math

def removeDupes(array):
    
    if len(array) == 0:
        print(result)
        return
    
    previous = array[0]
    result = [previous]
    
    for i in range(1, len(array)):
        if array[i] != previous:
            result.append(array[i])
            previous = array[i]
    
    print (result)

removeDupes([2,2,2,2, 2, 2])

