
array = ["GeeksforGeeeks", "I", "from", "am"]
array2 = ["You", "are", "beautiful", "looking"]


def SortWords(array):
    ordered_array = []
    for word in array:
        
        if len(ordered_array) > 0:
            index = 0
            for ordered_word in ordered_array:
                if len(word) <= len(ordered_word):
                    if len(word) == len(ordered_word):
                        ordered_array.insert(index + 1, word)
                    else:
                        ordered_array.insert(index, word)
                    break
                index += 1
        else:
            #init ordered array
            ordered_array.append(word)
            
    return ordered_array
    
print (SortWords(array))
print (SortWords(array2))
