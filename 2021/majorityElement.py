def majorityElement(arr):
    maxCount = 0
    maxElement = -1
    numCount = {}
    
    for element in arr:
    
        if element in numCount:
            numCount[element] += 1
        else:
            numCount[element] = 1
            
        if numCount[element] > maxCount and numCount[element] > 1:
            maxElement = element
            maxCount = numCount[element]
    
    return maxElement

# Driver code
if __name__ == "__main__":
    
    print(majorityElement([3, 1, 3, 3, 2]))
    print(majorityElement([1,2,3]))