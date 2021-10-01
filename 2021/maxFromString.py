import re
def maxFromString(str):
    results = []
    num_start = True
    temp = ""
    for char in list(str):
        if re.match("[0-9]", char):
            num_start = True
            temp += char
        else:
            num_start = False
            if temp != "":
                results.append(int(temp))
            temp = ""
    if temp != "":
        results.append(int(temp))
    results.sort()
    return results[-1:].pop()
    
# Driver code
if __name__ == "__main__":
    
    print (maxFromString("100fed200exe50"))
    print (maxFromString("1q2b3"))
    print (maxFromString("5f4d3s2s1"))