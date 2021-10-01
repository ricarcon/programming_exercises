import sys
import os
import random
import math

def GetFibValues(n):
    
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        
        fib = [0, 1]    #init fib sequence to 0 and 1
        i = 2           #since we've handled the case where n = 0, 1 & 2, we'll start at 3 here
        
        while i < n:
            
            fib.append(fib[i-1] + fib[i-2])
            i += 1
        
        return fib
        
    #default
    return []

def main():
    
    n = 100
    print (GetFibValues(n))
    
if __name__=="__main__":main()