import sys
import random
import re

class Token:
    def __init__(self, value):
        self.value = value
        self.count = 0

    def increment_count(self): # Do I Need This if i just use the count method?
        self.count += 1

    def set_count(self, n):
        self.count = n

    def get_count(self):
        return self.count

#Should I create a method that just runs all 3? Tokenize, Count, and Print?

def open_file(path) -> list:
    with open(path, 'r') as f:
        content = f.read(100) #Reads the first 100 chars in case of large files
        contentLower = content.lower()
        preprocessedWords = contentLower.split()
        filteredWords = [word for word in preprocessedWords if len(word) >= 3]
    return filteredWords

def tokenize(TextFilePath) -> list:
    tokenList = list()

    filteredWords = open_file(TextFilePath)
    
    tokenSet = set(filteredWords)
	
    for word in tokenSet:
        tokenList.append(Token(word))
        
    return tokenList

# def tokenCount(tokenList<Token>): 
#     for token in set(tokenList): # Can I do this?
        

    
        
    
    

    


    


