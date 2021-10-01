dictionary = ["eat", "rain", "in", "rat"]
hash = {}

def isWord(str):
    for word in dictionary:
        if str == word:
            return True
    return False

def FindWordsUtil(matrix, visited, str, i, j, m, n):
    
    visited[i][j] = True
    str = str + matrix[i][j]
    
    if isWord(str):
        if str not in hash:
            hash[str] = True
    
    for k in range(i - 1, i + 2):
        for l in range (j - 1, j + 2):
            if k < m and l < n and k >= 0 and l >= 0 and not visited[k][l]:
                FindWordsUtil(matrix, visited, str, k, l, m, n)
        
    str = "".join(list(str)[:-1])
    visited[i][j] = False


def FindWords(matrix, m, n):
    visited = [[],[],[]]
    for i in range(m):
        for j in range(n):
            visited[i].append(False)
            
    str = ""
    
    for i in range(m):
        for j in range(n):
            FindWordsUtil(matrix, visited, str, i, j, m, n)
        
# Driver code
if __name__ == "__main__":
    matrix = [
        ['e', 'a', 'n'],
        ['t', 't', 'i'],
        ['a', 'r', 'a']
    ]
    FindWords(matrix, 3, 3)
    
    for key in hash:
        print(key)