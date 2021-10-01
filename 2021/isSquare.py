import math

def isSquare(points):
    #base case where we don't have enough points
    if len(points) != 4:
        return False
        
    #let's init our distance by using two points. If all the x distances and all the y distances are the same, then it's a square
    distance = (points[0].x - points[3].x)**2 + (points[0].y - points[3].y)**2 
    previous = points[0]
    
    
    for i in range(1, len(points)):
        if (points[0].x - points[3].x)**2 + (points[0].y - points[3].y)**2  != distance:
            return False
            
        previous = points[i]

    return True
    
    
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "{}:{}".format(self.x, self.y)

points = [Point(20, 10), Point(10, 20), Point(20, 20), Point(10, 10)]

print (isSquare(points))


