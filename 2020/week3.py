import sys
import os
import random
import math

def SumWhile(array):
    
    index = 0
    sum = 0
    while index < len(array):
        sum += array[index]
        index+= 1
        
    return sum

def SumFor(array):
    sum = 0
    for num in array:
        sum += num
    return sum
    
def SumRecursion(array):
    
    if len(array) > 1:
        temp = array[1:]
        return array[0] + SumRecursion(temp)
        
    else:
        return array[0]
    
def main():
    array = [1, 5, 3, 2]
    print(SumWhile(array))
    print(SumFor(array))
    print(SumRecursion(array))
    
if __name__=="__main__":main()