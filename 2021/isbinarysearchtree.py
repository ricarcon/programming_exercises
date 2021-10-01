class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
        


def is_binary_search_tree(root,
                          lower_bound=-float('inf'),
                          upper_bound=float('inf')):
    if not root:
        return True

    if (root.value >= upper_bound or root.value <= lower_bound):
        return False

    return (is_binary_search_tree(root.left, lower_bound, root.value)
            and is_binary_search_tree(root.right, root.value, upper_bound))
            
            
            
a = BinaryTreeNode(5)
a.insert_left(4)
a.insert_right(3)

print (is_binary_search_tree(a))