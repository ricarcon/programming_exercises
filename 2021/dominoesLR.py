def dominoPositions(dominoes):
    
    temp = []
    for index, entry in enumerate(dominoes):
        if entry != '.':
            temp.append((entry, index))
            
    index = 0
    result = []
    start = 0
    
    while index < len(temp):
        
        try:
            stop = temp[index][1] + 1
            next = temp[index][0]
            
            for i in range(start, stop):
                if temp[index][0] == "L" and index == 0:
                    result.append("L")
                elif i == (stop - start):
                    result.append(".")
                elif i < (stop - start) and temp[index][0] == "L":
                    result.append("L")
                elif i > (stop - start) and next == "R":
                    result.append("R")
               
            start = stop
            index += 1
            
        except:
            break
            
    return result

str = ".L.R....L"
print(dominoPositions(str))
