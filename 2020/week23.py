'''
For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

def permutations(array):
    
    permutations = []
    
    for i in range(len(array)):
        
        permutation = []
        permutation.append(array[i])
        
        for j in range(len(array)):
            if j != i:
                permutation.append(array[j])
        
        permutations.append(permutation)
        
    return permutations


array = [1,2,3]

print(permutations(array))