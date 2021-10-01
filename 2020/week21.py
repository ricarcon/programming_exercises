class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    
def ValidateBinaryTree(node):
    
    
    if node is not None:
    
        if node.left is not None and node.right is not None:
            if node.value < node.left.value or node.value > node.right.value:
                return False
        elif node.left is not None and node.right is None:
            if node.value < node.left.value:
                return False
        elif node.left is None and node.right is not None:
            if node.value > node.right.value:
                return False
        
        #process left and right branches recursively
        left = ValidateBinaryTree(node.left)
        right = ValidateBinaryTree(node.right)
        
        if left and right:
            return True
        
    #none node is true
    return True

# Driver program to test above function 
if __name__=='__main__': 
    
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    
    root.left.left = Node(1)
    root.left.right = Node(6)
    
    root.right.left = Node(12)
    root.right.right = Node(17)
    
    result = ValidateBinaryTree(root)
    
    print(result)
    
    root = Node(10)
    root.left = Node(11)
    root.right = Node(15)
    
    root.left.left = Node(1)
    root.left.right = Node(6)
    
    root.right.left = Node(12)
    root.right.right = Node(17)
    
    result = ValidateBinaryTree(root)
    
    print(result)
    
    
    root = Node(10)
    root.left = Node(11)
    root.right = Node(15)
    
    root.left.left = Node(1)
    root.left.right = Node(6)
    
    root.right.left = Node(12)
    root.right.right = Node(9)
    
    result = ValidateBinaryTree(root)
    
    print(result)
    
    root = Node(10)
    root.left = Node(10)
    root.right = Node(15)
    
    root.left.left = Node(1)
    root.left.right = Node(6)
    
    root.right.left = Node(12)
    root.right.right = Node(19)
    
    result = ValidateBinaryTree(root)
    
    print(result)