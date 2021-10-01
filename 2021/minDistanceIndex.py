import math
def minDistance(arr, x, y):
    min_distance = math.inf
    x_index = -1
    y_index = -1 
    
    for i in range(len(arr)):
        temp = math.inf
        if arr[i] == x:
            temp = computeDistance(i, y_index)
            if temp == math.inf:
                x_index = i
        elif arr[i] == y:
            temp = computeDistance(x_index, i)
            if temp == math.inf:
                y_index = i
        
        if temp < min_distance:
            min_distance = temp
            
    if min_distance == math.inf:
        min_distance = -1
        
    return min_distance

def computeDistance(x, y):
    if y == -1 or x == -1:
        return math.inf
    return abs(y - x)
    
# Driver code
if __name__ == "__main__":
    
    print (minDistance([1, 2, 3, 2], 1, 2))
    print (minDistance([86, 39, 90, 67, 84, 66, 62], 42, 12))