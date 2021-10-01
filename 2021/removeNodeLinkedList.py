def SortOddDescEvenAsc(arr):

    odd = []
    even = []
    
    for element in arr:
        if element % 2 == 0:
            even.append(element)
        else:
            odd.append(element)
            
    
    odd.sort(reverse=True)
    even.sort()
    
    odd.extend(even)
    
    return (odd)
    
    
print(SortOddDescEvenAsc([1, 2, 3, 5, 4, 7, 10]))