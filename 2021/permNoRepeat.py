ITEM_NAME = 1
ITEM_QUANTITY = 0

def updateInventory(arr1, arr2):
    
    for item1 in arr2:
        found = False
        for item2 in arr1:
            if item1[ITEM_NAME] == item2[ITEM_NAME]:
                item2[ITEM_QUANTITY] += item1[ITEM_QUANTITY]
                found = True
        if not found:
            arr1.append(item1)
    return arr1
    
# Driver code
if __name__ == "__main__":
    
    curInv = [
        [21, "Bowling Ball"],
        [2, "Dirty Sock"],
        [1, "Hair Pin"],
        [5, "Microphone"]
    ]
    
    newInv = [
        [2, "Hair Pin"],
        [3, "Half-Eaten Apple"],
        [67, "Bowling Ball"],
        [7, "Toothpaste"]
    ]
    print(updateInventory(curInv, newInv))
    