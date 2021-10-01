'''
s = [1, 2, 3, 4, 5]

queue = []
done = False
alternate = True

while not done:
    if len(s) == 0 and len(queue) == 0:
        break
        
    if alternate:
        for i in range(len(s)):
            if len(s) == 1:
                print(s.pop(), end=' ')
                alternate = False
            else:
                queue.append(s.pop())
            
    else:
        for i in range(len(queue)):
            if i == 0:
                print (queue.pop(0), end=' ')
            else:
                s.insert(0,queue.pop(0))
        alternate = True
        
        
        
        '''
s = [1, 2, 3, 4, 5]

p1 = 0 
p2 = len(s)

alternate = True
while p1 != p2:
    #base case
    if p1 == 0:
        print (s[p1], end=' ')
        p1 += 1
        alternate = False
    elif alternate:
        print(s[p1], end=' ')
        p1 += 1
        alternate = False
    else:
        p2 -= 1
        print(s[p2], end=' ')
        alternate = True