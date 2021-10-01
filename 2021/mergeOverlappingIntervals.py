START = 0
END = 1

def MergeOverlappingIntervals(arr):
    if arr is None:
        return None
    elif len(arr) == 1:
        return arr
    elif len(arr) > 1:
    
        result = [arr[0]]   #init what we'll return to the caller with our merged results
        
        index = 1
        
        while index < len(arr):
            previous = result[-1]
            current = arr[index]    #track current element to compare against the previous merged results
            if previous[END] <= current[START]:
                start = previous[START]
                end = current[END]
                
                if previous[END] > current[END]:
                    end = previous[END]
                
                #replace current entry in the tip of results with the new merged result
                result[-1] = (start, end)
                
            index += 1
                
        return result
        
# Driver code
if __name__ == "__main__":
    arr = [(1,5), (3,7), (4,6), (6,8)]
    print("Input array: {}".format(arr))
    print("Merged list:{}".format(MergeOverlappingIntervals(arr)))
    
    arr = [(10,12), (12,15)]
    print("Input array: {}".format(arr))
    print("Merged list:{}".format(MergeOverlappingIntervals(arr)))