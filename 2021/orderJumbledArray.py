def orderArray(order):
    count = 0
    result = [None] * len(order)
    max = len(order) - 1
    
    for i in range(len(order) - 1, 0 - 1, -1):
        if order[i] == "-":
            result[i] = count
            count += 1
        else:
            result[i] = max
            max -= 1
    
    return result
    
# Driver code
if __name__ == "__main__":
    
    print(orderArray([None, "+", "+", "-", "+"]))
    print(orderArray([None, "-", "+", "-", "+", "-", "-", "+", "+", "+"]))
    
    
    """
        [None, -, +, -, +, -, -, +, +, +]
        
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        
        [4,3,5,2,6,1,0,7,8,9]
    """