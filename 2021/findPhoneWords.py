hashTable = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

def printWordsUtil(number, curr, output):
    if(curr == len(number)):
        print(output)
        return
        
    for i in range(len(hashTable[number[curr]])):
        output.append(hashTable[number[curr]][i])
        printWordsUtil(number, curr + 1, output)
        output.pop()
        if(number[curr] == 0 or number[curr] == 1):
            return

def printWords(number):
    printWordsUtil(number, 0, [])

# Driver function
if __name__ == '__main__':
    number = [2, 3, 4]
    printWords(number)