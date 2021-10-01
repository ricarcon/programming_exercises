import time
def intersection(arr1, arr2):
    
    if len(arr1) > len(arr2):
        temp = arr1
        arr1 = arr2
        arr2 = temp
        
    #we want arr1 to be the smaller one, so let's sort it to perform binSearch on it from arr2
    arr1.sort()
    result = ""
    for i in range(len(arr2)):
        if binarySearch(arr2[i], arr1):
            result += str(arr2[i]) + " " 
            
    return result
    
def binarySearch(element, arr):
    
    mid = (len(arr) - 1) // 2
    
    if element == arr[mid]:
        return True
        
    if len(arr) == 1:
        return False
        
    if element < arr[mid]:
        #the result is (if present) on the left side of the array
        return binarySearch(element, arr[:mid + 1])
    else:
        #result, if present, is oon the right of the array
        return binarySearch(element, arr[mid+1:])
    

# Driver code
if __name__ == "__main__":
    arr1 = [7, 1, 5, 2, 3, 6]
    arr2 = [3, 8, 6, 20, 7]
    
    print("Intersection points are: {}".format(intersection(arr1, arr2)))