def waveArray(arr):
    for i in range(0, len(arr), 2):
        if i + 1 < len(arr):
            temp = arr[i + 1]
            arr[i + 1] = arr[i]
            arr[i] = temp
    return arr

# Driver code
if __name__ == "__main__":
    
    print(waveArray([1,2,3,4,5]))
    print(waveArray([2,4,7,8,9,10]))