import sys
import os
import random
import math

def MergeArrays(array1, array2):
    
    merged_array = []
    i = 0
    while i < len(array1) + len(array2):
        
        if i % 2 == 0:
            merged_array.append(array1[i/2])
        else:
            merged_array.append(array2[i/2])
        
        i += 1
        
    return merged_array

def main():
    array1 = [1, 5, 3, 2]
    array2 = ['a', 'b', 'c', 'd']
    
    print ( MergeArrays(array1, array2) )
    
if __name__=="__main__":main()