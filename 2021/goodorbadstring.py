vowels = ['a', 'e', 'i', 'o', 'u']

def GoodBad(str):
    consonants_count = 0
    vowels_count = 0
    
    for char in list(str):
        if char in vowels:
            vowels_count += 1
            consonants_count = 0
        else:
            consonants_count += 1
            vowels_count = 0
            
        if char == '?':
            if consonants_count > 3:
                consonants_count -= 2 #have to subtract 2 since we added 1 above in the else block
            elif vowels_count > 5:
                vowels_count -= 1
            
        if vowels_count > 5:
            return False
            
        if consonants_count > 3:
            return False
            
    #if here, it means it's good
    return True
        
# Driver code
if __name__ == "__main__":
    
    print (GoodBad("aeioup??"))
    print (GoodBad("aeio?pq?r"))
    print (GoodBad("aei?ouae?iou?p"))