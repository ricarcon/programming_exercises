class Node():
    def __init__(self, value):
        self.val = value
        self.next = None
        self.arb = None

def deepCopy(list):
    
    current = list  #pointer to the first element in the list (init list pointer)
    
    while current is not None:
        new = Node(current.val)
        new.next = current.next
        current.next = new
        current = current.next.next
        
    current = list
    while current is not None:
        current.next.arb = current.arb.next
        current = current.next.next
        
    current = list
    copy = list.next
    while current.next is not None:
        temp = current.next
        current.next = current.next.next
        current = temp
        
    return copy
        
    
def PrintList(root):
    
    current = root
    while current is not None:
        print(current.val, end = " ")
        current = current.next
    
# Driver code
if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    
    a.next = b
    b.next = c
    c.next = d 
    d.next = e 
    
    a.arb = c 
    b.arb = a 
    c.arb = e
    d.arb = c 
    e.arb = b
    
    
    PrintList(deepCopy(a))