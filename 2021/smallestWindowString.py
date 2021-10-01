import math
no_of_chars = 256

def findSubString(string, pat):
    
    len1 = len(string)
    len2 = len(pat)
    
    ans = math.inf
    start = 0
    count = 0
    
    m = [0] * no_of_chars
    
    for i in range(len2):
        if m[pat[i]] == 0:
            count += 1
        m[pat[i]] += 1
        
    i = 0
    j = 0
    
    while (j < len1):
        m[string[j]] -= 1
        if m[string[j]] == 0:
            count -= 1
        
        if count == 0:
            while count == 0:
                if ans > j - i + 1:
                    ans = min(ans, j - i + 1)
                    start = i
                
                m[string[i]] += 1
                if m[string[i]] > 0:
                    count += 1
                    
                i += 1
        j += 1
    
    if ans != math.inf:
        return string[start:ans]
        
    return "Not possible"
    
# Driver code
if __name__ == "__main__":
 
    string = "this is a test string"
    pat = "tist"
 
    print("Smallest window is : ")
    print(findSubString(string, pat))