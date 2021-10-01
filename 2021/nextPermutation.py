import math

def nextPermutation(string):
    
    if string is not None:
        letters = list(string)
        previous = letters[0]
        smallest = previous
        previous_index = 0
        i=1
        
        while i < len(letters):
            if letters[i] < previous:
                char_to_swap_with, index_of_char = findSmallest(letters[i:len(letters)-1])
                
                temp = letters[previous_index]
                letters[previous_index] = char_to_swap_with
                letters[i] = temp
                break #don't need to process further
                
            previous = letters[i]
            previous_index = i
            i += 1
        #now we need to sort from i to end of string in desc order to get the next permutation
        return sortDescAtIndex(letters, i)
        
        
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return (smallest, smallest_index)
    
def sortDescAtIndex(arr, index):
    sub_arr = arr[index:]
    sub_arr.sort()
    final_arr = arr[:index]
    final_arr.extend(sub_arr)
    return final_arr
    
print(nextPermutation("abedc"))

