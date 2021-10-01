'''
Consider the following examples:

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2
d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2

'''


class KeyValueAtTime:
    def __init__(self):
        self.map = {}
        
    def set(self, key, value, time):
        
        if key not in self.map:
            self.map[key] = []
        
        if len(self.map[key]) <= time:
        
            #fill the array to indicated time with None and then set the time at the given value
            for i in range(len(self.map[key]),time + 1):
                self.map[key].append(None)
        
        self.map[key][time] = value
            
    def get(self, key, time):
        
        if time >= len(self.map[key]):
            return self.map[key][-1]
            
        elif self.map[key][time] == None:
            i = time - 1
            while i >= 0:
                if self.map[key][i] != None:
                    return self.map[key][i]
                i -= 1
                
        return self.map[key][time]
        
    def __str__(self):
        return str(self.map)
        

d = KeyValueAtTime()
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
print(d.get(1, 1)) # get key 1 at time 1 should be 1
print(d.get(1, 3)) # get key 1 at time 3 should be 2
print(d)
print("==========================")

d = KeyValueAtTime()
d.set(1, 1, 5) # set key 1 to value 1 at time 5
print(d.get(1, 0)) # get key 1 at time 0 should be null
print(d.get(1, 10)) # get key 1 at time 10 should be 1
print(d)
print("==========================")

d = KeyValueAtTime()
d.set(1, 1, 0) # set key 1 to value 1 at time 0
print(d)
d.set(1, 2, 0) # set key 1 to value 2 at time 0
print(d.get(1, 0)) # get key 1 at time 0 should be 2
print(d)
print("==========================")
