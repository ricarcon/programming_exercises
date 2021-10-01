def find_k_sequence(array, k):
    result = []
    for i in range(len(array)):
        if i + k <= len(array):
            #continue
            result.append(max(array[i:i+k]))
        else:
            break #all done
    return result

def main():

    #array = [10, 5, 2, 7, 8, 7] and k = 3
    array = [10, 5, 2, 7, 8, 7]
    k = 3
    
    print(find_k_sequence(array, k))
    
if __name__=="__main__":main()