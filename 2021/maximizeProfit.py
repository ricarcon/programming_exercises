def maximizeProfit(arr):
    if len(arr) < 2:
        return 
    i = 0
    while i < (len(arr) - 1):
        while i < len(arr) - 1 and arr[i + 1] <= arr[i]:
            i += 1
            
        if i == len(arr) - 1:
            break
        
        buy = i
        i += 1
        
        while i < len(arr) and arr[i] >= arr[i - 1]:
            i += 1
            
        sell = i - 1
            
        print (buy)
        print (sell)
    
'''
tbd
'''

# Driver code
if __name__ == "__main__":
    arr = [100, 180, 260, 310, 40, 535, 695]
    print(maximizeProfit(arr))