def FindMax(array):
    max = 0
    for value in array:
        if value > max:
            max = value
    return max

def FindMin(array):
    
    max = FindMax(array)
    missing_number = [0]*max
    
    for value in array:
        if value > 0:
            missing_number[value - 1] = 1
    #print (missing_number)
    
    if len(missing_number) > 0:
        missing = 0
        for i in range(len(missing_number)):
            if missing_number[i] == 0:
                return i + 1
            i += 1
            missing = i
        #if here, we're at the end of the list, return i + 1
        return missing + 1
        
    #if we're here, we didn't find a positive value, so just return 1
    return 1
    

def main():
    
    min = 0 #minimum positive value init to zero
    array = [1,0,2]
    array2 = [2, 3, 7, 6, 8, -1, -10, 15]
    array3 = [2, 3, -7, 6, 8, 1, -10, 15]
    array4 = [1, 1, 0, -1, -2]
    
    #print(array)
    print (FindMin(array))
    #print(array2)
    print (FindMin(array2))
    #print(array3)
    print (FindMin(array3))
    #print(array4)
    print (FindMin(array4))

if __name__=="__main__":main()