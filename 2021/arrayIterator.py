class ArrayIterator(object):
    def __init__(self):
        self.matrix = []    #contains list of arrays (2D array)
        self.__x = 0        #x coordinate on 2D array for "next" column
        self.__y = 0        #y coordinate on 2D array for "next" row
        
    def push(self, array):
        self.matrix.append(array)
        
    def next(self):
    
        #move to the next row until we have something or encounter an exception
        while len(self.matrix[self.__y]) == 0:
            self.__y += 1
        
        val = self.matrix[self.__y][self.__x]
        
        if self.__x + 1 < len(self.matrix[self.__y]):
            self.__x += 1
        else:
            #we need to move to the next row - that means reset X and increment Y
            self.__x = 0
            self.__y += 1
            
        return val
        
    def has_next(self):
        try:
            val = self.matrix[self.__y][self.__x]
            return True
        except:
            return False
            
    def __str__(self):
        val = ""
        for array in self.matrix:
            for element in array:
                val += str(element) + ";"
        return val
        
a = [1, 2]
b = [3]
c = []
d = [4, 5, 6]

matrix = ArrayIterator()
matrix.push(a)
matrix.push(b)
matrix.push(c)
matrix.push(d)

print(matrix.next())
print(matrix.has_next())


print(matrix.next())
print(matrix.has_next())


print(matrix.next())
print(matrix.has_next())


print(matrix.next())
print(matrix.has_next())


print(matrix.next())
print(matrix.has_next())


print(matrix.next())
print(matrix.has_next())

print(matrix.next())