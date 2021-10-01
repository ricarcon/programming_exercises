import sys
import os
import random

def GenerateSpaces(n):
    spaces = ""
    for i in range (n):
        spaces += " "
    return spaces
    
def Justify(array, k):
    
    sentences = []
    current_sentence_length = 0
    current_sentence = []
    
    for j in range(len(array)):
        
        if len(array[j]) + current_sentence_length + len(current_sentence) - 1 > k or j == len(array) - 1:
            
            if j == len(array)- 1:
                current_sentence.append(array[j])
                current_sentence_length += len(array[j])
                
            #the next word puts us over the top, let's add extra spaces between words and find out how many we have available and how many words we have
            num_spaces_left = k - current_sentence_length
            total_number_of_spaces_needed = len(current_sentence) - 1
            
            if len(current_sentence) == 1:
                spaces = GenerateSpaces(num_spaces_left)
                sentences.append(current_sentence[0] + spaces)
                
            else:
                num_spaces_per = int(num_spaces_left/total_number_of_spaces_needed)
                num_uneven = num_spaces_left - (total_number_of_spaces_needed * num_spaces_per)
                
                spaces = GenerateSpaces(num_spaces_per)
                sentence = ""
                
                #form the sentence
                for i in range(len(current_sentence)):
                    if num_uneven > 0:
                        sentence += current_sentence[i] + spaces + " "  #add an extra space to distribute the last uneven space
                        num_uneven = num_uneven - 1
                    elif i < len(current_sentence) - 1:
                        sentence += current_sentence[i] + spaces
                    else:
                        sentence += current_sentence[i]
                    
                sentences.append(sentence)
            
            #reset values for space length and sentence
            current_sentence_length = 0
            current_sentence = []
        
        #length of current word + the current sentence length + need to factor in number of spaces (minimum of one between words)
        if len(array[j]) + current_sentence_length + len(current_sentence) - 1 <= k:
            current_sentence.append(array[j])
            current_sentence_length += len(array[j])
            
    return sentences
    
def main():
    words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    k = 16
    #print(Justify(words, k))
    
    words = ["thethethethe", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    k = 16
    
    for sentence in Justify(words, k):
        print ("'{}'".format(sentence))
    
    
if __name__=="__main__":main()