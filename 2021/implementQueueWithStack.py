class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.flag = True #when we move elements from one stack to the other, the new stack will now have the last element at the top vs the bottom, so we can just pop from the top if even
        
    def enQueue(self, val):
        self.s1.append(val)
        
    def deQueue(self):
        
        if self.flag:
            #in this case we'll pop everything until we have the last element and return the last element
            #s2 will then have the elements in order that we can just pop to dequeue
            while len(self.s1) > 0:
                #transfer everything from stack 1 to stack 2
                self.s2.append(self.s1.pop())
            self.flag = False
            
            #return the top of stack 2
            return self.s2.pop()
            
        else:
            element = None
            
            if len(self.s2) > 0:
                #reset the flag if we have no more elements in s2
                element = self.s2.pop()
                
                #if after popping the element we have nothing else, let's pull from the first stack by setting the flag accordingly
                if len(self.s2) == 0:
                    self.flag = True
            
            return element

# Driver code
if __name__ == "__main__":
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    
    print(q.deQueue())
    print(q.deQueue())
    
    q.enQueue(4)
    print(q.deQueue())
    print(q.deQueue())