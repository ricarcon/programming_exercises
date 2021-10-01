import sys
import os
import random
import math


def FindSequence(array, size, num):
    
    start = 0
    end = 0
    index = 0
    
    remainder = num
    
    while index < size:
    
        if remainder - array[index] == 0:
            #we've found a sequence of numbers that add up to the sum
            return (start, end)
        elif remainder - array[index] < 0:
            #add the start of the sequence we are tracking back onto the remainder
            remainder += array[start]
            #move the pointer over one
            start += 1
        else:
            remainder -= array[index]
            #move to the next element in the list
            index += 1
            
            end = index
        
    return (start, end)

def main():
    
    values = [1, 2, 3, 7, 5]
    
    start, end = FindSequence(values, len(values), 12)
    print("{}:{}".format(start + 1, end + 1))
    
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
    start, end = FindSequence(values, len(values), 15)
    print("{}:{}".format(start + 1, end + 1))
    
if __name__=="__main__":main()