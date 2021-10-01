class Node():
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None

def treeToDoublyLinked(root):
    if root is None:
        return None
        
    left = treeToDoublyLinked(root.left)
    right = treeToDoublyLinked(root.right)
    
    root.left = root.right = root
    
    return concatLinkedList(concatLinkedList(left, root), right)
    
def DisplayList(root):
    itr = root
    first = 1
    
    while (root != itr or first):
        print(itr.val, end = " ")
        itr = itr.right
        first = 0
    
def concatLinkedList(leftList, rightList):
    
    if (leftList == None):
        return rightList 
    if (rightList == None): 
        return leftList 
  
    # Store the last Node of left List 
    leftLast = leftList.left 
  
    # Store the last Node of right List 
    rightLast = rightList.left 
  
    # Connect the last node of Left List 
    # with the first Node of the right List 
    leftLast.right = rightList 
    rightList.left = leftLast 
  
    # Left of first node points to 
    # the last node in the list 
    leftList.left = rightLast 
  
    # Right of last node refers to 
    # the first node of the List 
    rightLast.right = leftList 
  
    return leftList
    
'''
tbd
'''

# Driver code
if __name__ == "__main__":
 
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)
    
    DisplayList(treeToDoublyLinked(root))