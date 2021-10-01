def Unique2(n):
    
    n = 5
    m = 2
    L = [[None]*(n+1) for i in range(m+1)]
    print(L)
    return None
    
    unique = []
    unique.append([1])
    unique[0].append(1)
    unique.append([2])
    
    #start at 2 since we already have base cases defined
    for i in range(2, n):
        
        print(unique)
        
        for j in range(i):
            if i % 2 == 0:
                unique[i].append(2)
            else:
                unique[i].append(1)
        
    print (unique)
        
        

def UniqueSteps(n, s):
    
    if n > 0:
        
        unique_steps = [0 for x in range(n)]
        #set base cases
        unique_steps[0] = 1
        unique_steps[1] = 1
        
        for i in range(2,n):
            j = 1
            
            while j <= len(s) and j <= i:
                unique_steps[i] = unique_steps[i] + unique_steps[i-j]
                j += 1
                
        return (unique_steps[n-1])
    
    return []
    
def main():

    #number of steps
    n = 4
    
    #unique ways we can climb the steps (e.g. 1 or 2 steps)
    s = [1, 2]
    
    #print (UniqueSteps(n+1, s))
    print(Unique2(n))
    
    '''
    N = 3
    1, 1, 1
    2, 1
    1, 2
    
    ########################################################
    
    N = 4
    
    f(3) + 1
    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    
    f(2) + 2
    1, 1, 2
    2, 2
    
    ########################################################
    N = 5
    
    (1, 1, 1, 1) + 1
    (2, 1, 1) + 1
    (1, 2, 1) + 1
    (1, 1, 2) + 1
    (2, 2) + 1
    
    
    ########################################################
    N = 6
    
    f(N-1) + 1
    (1, 1, 1, 1 + 1) + 1
    (2, 1, 1 + 1) + 1
    (1, 2, 1 + 1) + 1
    (1, 1, 2 + 1) + 1
    (2, 2 + 1) + 1
    
    f(N-2) + 2
    2, 1, 1 + 2
    1, 1, 1, 1 + 2
    1, 2, 1 + 2
    1, 1, 2 + 2
    2, 2 + 2
    
    
    '''
    
if __name__=="__main__":main()