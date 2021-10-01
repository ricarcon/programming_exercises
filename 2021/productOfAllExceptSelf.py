def productOfAllExceptSelfNaive(arr):
    
    temp = []
    
    for i in range(len(arr)):
        product = 1
        
        for j in range (len(arr)):
            if i != j:
                product *= arr[j]
        
        temp.append(product)
    
    return temp
    
    
def productOfAllExceptSelf(arr):
    
    prod = 1
    flag = 0
    
    for i in range(len(arr)):
        if arr[i] == 0:
            flag += 1
        else:
            prod *= arr[i]
            
    prod_arr = [0 for i in range(len(arr))]
    
    if flag > 1:
        return prod_arr
    
    for i in range(len(arr)):
        if flag == 0:
            prod_arr[i] = prod // arr[i]
            
        elif flag == 1 and a[i] != 0:
            continue
        else:
            prod_arr[i] = prod
    return prod_arr
    
# Driver code
if __name__ == "__main__":
 
    arr = [10, 3, 5, 6, 2]
    
    print(productOfAllExceptSelfNaive(arr))
    
    print(productOfAllExceptSelf(arr))