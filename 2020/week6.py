import sys
import os
import random
import math

def Padding(number, n):
    i = 0
    while i < n:
        number = "0" + number
        i +=1
        
    return number

def FindMaxNumber(array):
    
    answer = []
    
    if len(array) > 0:
        i = 0
        current_max = str(array[0])
        current_max_index = 0
        
        #we'll pop elements from array into answer
        while len(array) > 0:
        
            temp = str(array[i])

            if temp > current_max:
                current_max = temp
                current_max_index = i
            
            i += 1
            
            if i == len(array):
                #add our current largest number to the answer
                answer.append(current_max)
                
                #remove the element from the list, reset i, current max and index
                array.pop(current_max_index)
                
                if len(array) > 0:
                    i = 0
                    current_max = str(array[i])
                    current_max_index = 0
            
    
    return "".join(answer)

def main():
    array = [50, 2, 1, 9]
    print (FindMaxNumber(array))
    
    array = [5, 50, 56]
    print (FindMaxNumber(array))
    
if __name__=="__main__":main()