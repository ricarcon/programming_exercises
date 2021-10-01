def findDupes(arr):
    
    seen = {}
    
    for i in range(len(arr)):
        if arr[i] in seen:
            seen[arr[i]] += 1
            return True
        else:
            seen[arr[i]] = 1
            
    return False
    
arr = [1, 2, 3, 4, 5, 6, 4]

print (findDupes(arr))