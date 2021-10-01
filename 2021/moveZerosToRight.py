def MoveZerosToRight(arr):
    #count how many zero's we have, then do a second pass from right to left to move values up to count
    i = len(arr) - 1
    count = 0
    end_pointer = len(arr) - 1
    
    while i >= 0 or end_pointer >=0:
        if arr[i] == 0:
            count += 1
        else:
            if i >= 0:
                arr[end_pointer] = arr[i]
            else:
                arr[end_pointer] = 0
            end_pointer -= 1
        i-= 1
    
        
    return arr
    
# Driver code
if __name__ == "__main__":
    arr = [1, 10, 20, 0, 59, 63, 0, 88, 0]
    print("Input array: {}".format(arr))
    print("Zero's moved to beginnig of the list:{}".format(MoveZerosToRight(arr)))