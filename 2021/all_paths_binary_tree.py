class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
      self.visited = False
      
    def printPaths(self):
        # list to store path
        path = []
        printPathsRec(self, path, 0)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)



