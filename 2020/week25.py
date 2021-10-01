'''
Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
'''

def find_subset(test_string, test_set):
    
    start = 0
    end = 0
    index = 0
    characters_found = 0
    substring = None
    
    while index < len(test_string):
        if test_string[index] in test_set and characters_found < len(test_set):
            if start == 0:
                start = index
                
            else:
                end = index
            
            characters_found += 1
        elif characters_found == len(test_set):
            substring = test_string[start:end+1]
        index += 1
    
    return substring
    
    

def main():
    test_string = "figehaeci"
    string_set = ["a", "e", "i"]

    print(find_subset(test_string, string_set))

if __name__=="__main__":
    main()