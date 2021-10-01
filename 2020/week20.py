import random

def rand7():
    
    return random.randrange(1, 7)
    
    
def rand5():
    
    matrix = [
        [1,2,3,4,5,1,2],
        [3,4,5,1,2,3,4],
        [5,1,2,3,4,5,1],
        [2,3,4,5,1,2,3],
        [4,5,1,2,3,4,5],
        [1,2,3,4,5,1,2],
        [3,4,5,None,None,None,None]
    ]
    
    rand5 = None
    
    while rand5 is None:
        x = rand7()
        y = rand7()
        rand5 = matrix[x][y]
        
    return rand5
    
# Driver program to test above function 
if __name__=='__main__': 
    
    print (rand7())
    print (rand5())