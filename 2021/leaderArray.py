def leader(arr):
    results = []
    size = len(arr)
    max_from_right = arr[size-1]
    results.insert(0, max_from_right)
    for i in range(size-2, -1, -1):
        if max_from_right < arr[i]:
            results.insert(0,arr[i])
            max_from_right = arr[i]
    return results
# Driver code
if __name__ == "__main__":
    
    print (leader([16, 17, 4, 3, 5, 2]))