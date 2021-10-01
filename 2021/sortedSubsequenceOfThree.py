import sys
def sortedSub3(nums):
    
    # If number of elements < 3
    # then no triplets are possible
    if (len(nums) < 3):
        print("No such triplet found", end = '')
        return
       
    # Track best sequence length
    # (not current sequence length)
    seq = 1
    
    # min number in array
    min_num = nums[0]
    
    max_seq = -sys.maxsize -1 
    
    # Save arr[i]
    store_min = min_num
    
    # Iterate from 1 to nums.size()
    for i in range(1, len(nums)):
        print ("---------------------------------------------------------------------------------------------------------------------------------------------------")
        print ("Current element: {} - MinNum: {} - Seq: {} - MaxSeq: {} - store_min: {}".format(nums[i], min_num, seq, max_seq, store_min))
        
        if (nums[i] == min_num):
            continue
        elif (nums[i] < min_num):
            min_num = nums[i]
            continue
        
        # This condition is only hit
        # when current sequence size is 2
        elif (nums[i] < max_seq):
        
            # Update best sequence max number
            # to a smaller value
            # (i.e. we've found a
            # smaller value for arr[j])
            max_seq = nums[i]
            
            # Store best sequence start value
            # i.e. arr[i]
            store_min = min_num
            
        # Increase best sequence length &
        # save next number in our triplet
        elif (nums[i] > max_seq):
            if seq == 1:
                store_min = min_num
            seq += 1
           
            # We've found our arr[k]!
            # Print the output
            if (seq == 3):
                print("Triplet: " + str(store_min) +  ", " + str(max_seq) + ", " + str(nums[i]))
                return
           
            max_seq = nums[i]
        print ("Current element: {} - MinNum: {} - Seq: {} - MaxSeq: {} - store_min: {}".format(nums[i], min_num, seq, max_seq, store_min))
    # No triplet found
    print("No such triplet found", end = '')
    

# Driver code
if __name__ == "__main__":
    
    sortedSub3([12, 11, 10, 5, 6, 2, 30])