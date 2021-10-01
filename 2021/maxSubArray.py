import sys
def maxSubArray(nums):
    min_index = 0
    max_index = 0
    current_min_index = 0
    current_max_index = 0
    maxsum = 0
    current_sum = 0
    
    for i in range(len(nums)):
        if nums[i] > 0:
            current_sum += nums[i]
            current_max_index = i
        elif current_sum > maxsum:
            maxsum = current_sum
            max_index = i
        else:
            min_index = i 
    
    return nums[min_index:max_index + 1]

# Driver code
if __name__ == "__main__":
    
    print(maxSubArray([12, 11, -1, 10, 5, 6, 2, 30]))