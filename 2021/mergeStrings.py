def MergeStrings(str1, str2):
    str1_list = list(str1)
    str2_list = list(str2)
    result = ""
    alternate = True
    
    while len(str1_list) > 0 or len(str2_list) > 0:
        if len(str1_list) == 0 and len(str2_list) > 0:
            #just append results from list 2 to the result
            result += str2_list.pop(0)
        elif len(str1_list) > 0 and len(str2_list) == 0:
            #just append results from list1
            result += str1_list.pop(0)
        elif alternate:
            #pull from list 1
            result += str1_list.pop(0)
            alternate = False
        else:
            #pull from list 2
            result += str2_list.pop(0)
            alternate = True
    return result
        
# Driver code
if __name__ == "__main__":
    print(MergeStrings("abc12345678", "abcdefg"))