import sys
import os
import random

def Encode(word):
    
    count = 0
    current_letter = ""
    encoded = ""
    index = 0
    
    for character in word:
        
        if current_letter == "":
            #init current letter
            current_letter = character
            count += 1
        
        elif character == current_letter:
            count += 1
        
        else:
            #must be a different letter, let's reset things
            encoded += str(count) + current_letter
            current_letter = character
            count = 1   #count the current letter
            
        index += 1
        
        #check if it is the last letter in the word
        if index == len(word):
            #need to append the current letter and count
            encoded += str(count) + current_letter
            
    return encoded

def Decode(word):
    
    letter_count = ""
    decoded = ""
    
    for character in word:
        if character.isdigit():
            letter_count += character
        else:
            for i in range(int(letter_count)):
                decoded += character
            letter_count = ""
    return decoded

def main():
    word = "AAAABBBCCDAA"
    encoded = Encode(word)
    print (encoded)
    
    print (Decode(encoded))
    
if __name__=="__main__":main()