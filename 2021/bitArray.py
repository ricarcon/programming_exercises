class BitArray(object):
    
    def __init__(self, value):
        #self.array = []
        self.arr = [0] * ((value >> 5) + 1)
        #for i in range(value):
            #init to 0 - default value
            #self.array.append(0)
    
    def set (self, i, val):
        try:
            self.array[i] = val
        except:
            pass
        
    def get(self, i):
        try:
            return self.array[i]
        except IndexError:
            return "Index out of range: array size is {}".format(len(self.array))
            
    def size(self):
        return len(self.arr)

ba = BitArray(128)
print (ba.size())
print (ba.arr)
'''
ba.set(6, 1)
ba.set(3, 1)
ba.set(0, 1)
print (ba.array)
print (ba.get(3))
print (ba.get(1))
'''