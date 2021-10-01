import math

class Point():
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        
    def __str__(self):
        return "{}:{}".format(self.x, self.y)
        
class PointDistance(Point):
    def __init__(self, point):
        self.x = point.x
        self.y = point.y
        self.distance = None
        
def kClosestPoints(arr, k):
    
    #base case
    if len(arr) <= k:
        return arr
    
    origin = Point(0, 0)
    
    result = []
    
    for i in range(len(arr)):
        p = PointDistance(arr[i])
        p.distance = Distance(origin, arr[i])
        
        result.append(p)
    
    #now sort by distance and pick the k elements
    result.sort(key = lambda x: x.distance)
    
    return result[:k]
    
    
def Distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
'''
tbd
'''

# Driver code
if __name__ == "__main__":
    arr = [Point(3,3), Point(5, -1), Point(-2, 4)]
    k = 5
    
    for item in kClosestPoints(arr, k):
        print(item, end = "|")