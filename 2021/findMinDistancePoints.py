import math
class Point:
    def    __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

def computeDistance(p1, p2):
    return math.sqrt( (p2.x - p1.x)**2 + (p2.y - p1.y)**2 )

def findMinDistance(arr):
    #pointers for our dynamic programming approach to solving the mind distance problem
    p1 = 0
    p2 = 1 
    
    if len(arr) == 0 or len(arr) == 1:
        return None
    elif len(arr) == 2:
        return computeDistance(arr[p1], arr[p2])
    
    #we have more than 2 points if we are here
    
    min = math.inf
    min_points = (arr[p1], arr[p2])
    
    while p1 < len(arr):
        
        while p2 < len(arr):
            dist = computeDistance(arr[p1], arr[p2])
            if dist < min:
                min = dist
                min_points = (arr[p1], arr[p2])
            p2 += 1
        
        p1 += 1
        p2 = p1 + 1
        
    return min_points
    

# Driver code
if __name__ == "__main__":
    
    arr = [Point(1,1), Point(-1,-1), Point(3,4), Point(6,1), Point(-1,-6), Point(-4,-3)]
    for point in findMinDistance(arr):
        print (point, end = " ")