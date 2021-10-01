def findAndReplaceNumWithTwoNums(number, search_num):
    
    digits = list(str(number))
    
    new_num = []
    
    for digit in digits:
        if int(digit) == search_num:
            new_num.append(str(int(digit) - 1))
        else:
            new_num.append(digit)
    
    int_num = int("".join(new_num))
    
    return (number - int_num, int_num)
    
print(findAndReplaceNumWithTwoNums(153, 5))