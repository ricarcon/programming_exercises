def FindMissing(arr):
    
    for i in range(1, len(arr) + 1):
        if arr[i - 1] != i:
            return i

#print(FindMissing([1,2,3,4,5, 6, 7, 9, 10]))



def SumExists(arr, target):
    arr.sort()
    
    print(arr)
    
    #pointer for start
    #pointer for next
    p1 = 0
    p2 = 1
    
    while arr[p1] < target or p1 + 1 == len(arr):
        
        if arr[p1] + arr[p2] == target:
            return True
        elif p2 + 1 < len(arr):
            p2 += 1
        
        if arr[p2] >= target or p2 + 1 == len(arr):
            p1 += 1
            p2 = p1 + 1
            
    return False
    
#print (SumExists([1, 2, 4, 3, 6], 10))



def ReverseWords(arr):
    #arr.reverse()
    
    temp = []
    
    i = len(arr)
    while i > 0:
        i -= 1
        temp.append(arr[i])
    
    return temp
    
    
#print(ReverseWords(["i", "like", "this", "program", "very", "much"]))


def ReverseLinkedList(head):
    current = head
    previous = None
    
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
           
        
        
        
        
        
def funGenerator():
    import time
    
    for i in range(3):
        time.sleep(2)
        yield i

for item in funGenerator():
    print(item)
    