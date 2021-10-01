class Node:

    
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def serialize(self):
        
        return Node._processNode(self)
     
    @staticmethod
    def _processNode(node):
    
        result = []
        
        
        #process current node
        result.append(node.val)
        
        #in order we process the left node next
        if node.left is not None:
            left = Node._processNode(node.left)
            result.append(left)
        
        #then we process the right node
        if node.right is not None:
            right = Node._processNode(node.right)
            result.append(right)
    
        return ";".join(result)
        
    def deserialize(self, string):
        return Node._processString(string)
        
    @staticmethod
    def _processString(string, node = None):
        
        parts = string.split(";")
        print (parts)
        
        
def main():
    
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    string = node.serialize()
    print(node.serialize())
    node.deserialize(string)

if __name__=="__main__":main()