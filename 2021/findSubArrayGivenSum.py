def findSubArrayGivenSum(arr, sum):
    start = 0
    current = 1
    current_sum = arr[start]
    
    while current < len(arr):
        while current_sum > sum and start < current - 1:
            current_sum = current_sum - arr[start]
            start += 1
            
        if current_sum == sum:
            return (start, current-1)
            
        if current < len(arr):
            current_sum += arr[current]
            
        current += 1
    return (0, 0)
    
'''
tbd
'''

# Driver code
if __name__ == "__main__":
 
    arr = [1, 4, 20, 3, 10, 5]
    sum = 33
    print(findSubArrayGivenSum(arr, sum))