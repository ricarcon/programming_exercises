import re

def SaveIronman(str):
    
    i = 0
    j = len(str) - 1
    list_str = list(str)
    
    while i <= j:
        if list_str[i].lower() == list_str[j].lower():
            i += 1
            j -= 1
        elif not re.match("[a-zA-Z]", list_str[i]):
            i += 1
        elif not re.match("[a-zA-Z]", list_str[j]):
            j -= 1
        else:
            return False
    return True
    
        
# Driver code
if __name__ == "__main__":
    
    print(SaveIronman("I am :IronnorI Ma, i"))
    print(SaveIronman("Ab?/Ba"))
    print(SaveIronman("abcde"))