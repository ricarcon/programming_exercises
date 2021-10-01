def getSingle(arr, n): 
    ones = 0
    twos = 0
      
    for i in range(n): 
        print ("i: {}".format(i))
        print ("\tValue: {}".format(arr[i]))
        # one & arr[i]" gives the bits that 
        # are there in both 'ones' and new 
        # element from arr[]. We add these 
        # bits to 'twos' using bitwise OR 
        twos = twos | (ones & arr[i])
        print ("\t\ttwos:  {}".format(twos))
          
        # one & arr[i]" gives the bits that 
        # are there in both 'ones' and new 
        # element from arr[]. We add these 
        # bits to 'twos' using bitwise OR 
        ones = ones ^ arr[i] 
        print ("\t\tones:  {}".format(ones))
          
        # The common bits are those bits  
        # which appear third time. So these 
        # bits should not be there in both  
        # 'ones' and 'twos'. common_bit_mask 
        # contains all these bits as 0, so 
        # that the bits can be removed from 
        # 'ones' and 'twos' 
        print ("\t\tones and twos: {}".format(ones & twos))
        common_bit_mask = ~(ones & twos) 
        print ("\t\tcommon_bit_mask:  {}".format(common_bit_mask))
          
        # Remove common bits (the bits that  
        # appear third time) from 'ones' 
        ones &= common_bit_mask 
          
        # Remove common bits (the bits that 
        # appear third time) from 'twos' 
        twos &= common_bit_mask 
        
        print ("\t\tOnes: {}".format(ones))
        print ("\t\tTwos: {}".format(twos))
        
    return ones 
      
# driver code 
arr = [3, 3, 2, 3] 
n = len(arr) 
print("The element with single occurrence is ", 
        getSingle(arr, n)) 