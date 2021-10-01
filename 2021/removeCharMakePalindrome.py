def isPalindrome(string):
    start = 0 
    end = len(string) - 1
    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            return False
            
    return True

def removeCharMakePalindromeNaive(string):
    
    for i in range(len(string)):
        temp = ""
        for j in range(len(string)):
            if j != i:
                temp += string[j]
        if isPalindrome(temp):
            return True
    return False
    
def removeCharMakePalindrome(string):
    start = 0
    end = len(string) - 1
    
    while start < end:
        
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            
            if isPalindrome(string[start+1:end+1]):
                return True
            if isPalindrome(string[start:end]):
                return True
                
            return False
            
    return True
    
'''
start = 0
end = 5
a a

start = 1
end = 4
b e
'''

# Driver code
if __name__ == "__main__":
 
    string = "abcbea"
    
    print(removeCharMakePalindromeNaive(string))
    print(removeCharMakePalindrome(string))