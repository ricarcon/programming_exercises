def PrintPattern(num, count = 0, reverse = False):
    
    print (num)
    
    if num >= 0 and not reverse:
        if (num - 5 <= 0):
            PrintPattern(num-5, count + 1, reverse=True)
        else:
            PrintPattern(num-5, count + 1)
    elif count > 0 and reverse:
        PrintPattern(num + 5, count - 1, reverse=True)
        
    return
    
    
#driver program
PrintPattern(16)