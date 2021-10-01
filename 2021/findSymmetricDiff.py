def findDiff(arrays):
    map = {}
    for array in arrays:
        map = seen(map, array)
    result = []
    
    for key in map:
        if map[key] == 1:
            result.append(key)
    return result

def seen(map, array):
    
    for element in array:
        if element in map:
            map[element] += 1
        else:
            map[element] = 1
    
    return map
    
    
# Driver code
if __name__ == "__main__":
    
    arr1 = [1, 2, 3]
    arr2 = [5, 2, 1, 4]
    print(findDiff([arr1, arr2]))
    