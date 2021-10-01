def Sort012(arr):
    count1 = 0
    count2 = 0
    count3 = 0
    
    for element in arr:
        if element == 0:
            count1 += 1
        elif element == 1:
            count2 += 1
        else:
            count3 += 1
    
    r = []
    
    for i in range(count1):
        r.append(0)
    
    for i in range (count2):
        r.append(1)
        
    for i in range(count3):
        r.append(2)
        
    return r


print(Sort012([0, 1,1,2,0, 1, 2, 0, 1, 1]))