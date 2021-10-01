ASC = "ASC"
DESC = "DESC"

def iterations(num):
    count = 1
    target = 6174
    current_num = num
    
    while current_num != target:
        
        desc_num = sort(current_num, DESC)
        asc_num = sort(current_num, ASC)
        
        current_num = desc_num - asc_num
        count += 1
        
    return count - 1
    
def sort(num, direction=ASC):
    
    result = []
    for digit in str(num):
        result.append(digit)
        
    if direction == ASC:
        result.sort()
    else:
        result.sort(reverse=True)
        
    new_num = int("".join(result))
    return new_num
    
# Driver code
if __name__ == "__main__":
    
    print (iterations(1234))