START_TIME = 0
END_TIME = 1

def mergeTimes(arr):
    if len(arr) < 2 or arr is None:
        return arr
    
    result = [arr[0]]
    previous = result[0]
    curr_index = 0
    
    for element in arr:
    
        start_time = previous[START_TIME]
        end_time = element[END_TIME]
        
        if element[START_TIME] <= previous[END_TIME]:
            if element[START_TIME] < previous[START_TIME]:
                start_time = element[START_TIME]
            if element[END_TIME] < previous[END_TIME]:
                end_time = previous[END_TIME]
            result[curr_index] = (start_time, end_time)
        else:
            result.append(element)
            curr_index += 1
            
        previous = result[curr_index]
            
    return result
    
# Driver code
if __name__ == "__main__":
    arr1 = [(0,1), (3,5), (4,8), (10, 12), (9,10)]
    print(mergeTimes(arr1))
    print(mergeTimes([(1,2), (2, 3)]))
    