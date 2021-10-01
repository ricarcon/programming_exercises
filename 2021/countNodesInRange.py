class Node():
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None

START_RANGE = 0
END_RANGE = 1

def countNodesInRange(root, range):
    if root == None:
        return 0
        
    if root.val > range[START_RANGE] and root.val < range[END_RANGE]:
        return root.val + countNodesInRange(root.left, range) + countNodesInRange(root.right, range)
    elif root.val < range[START_RANGE]:
        return countNodesInRange(root.right, range)
    else:
        return countNodesInRange(root.left, range)
'''
start = 0
end = 5
a a

start = 1
end = 4
b e
'''

# Driver code
if __name__ == "__main__":
 
    root = Node(10)
    root.left = Node(5)
    root.right = Node(50)
    root.left.left = Node(1)
    root.right.left = Node(40)
    root.right.right = Node(100)
    
    range = [5, 45]
    print(countNodesInRange(root, range))