import sys
import random
import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.count = 0

    def increment_count(self): # Do I Need This if i just use the count method?
        self.count += 1

    def set_count(self, n):
        self.count = n

    def get_count(self):
        return self.count

def open_file(path) -> list:
    with open(path, 'r') as file:
        content = f.read(100) #Reads the first 100 chars in case of large files
        contentLower = content.lower()
        preprocessedWords = contentLower.split()
        filteredWords = [word for word in preprocessedWords if len(word) >= 3]
    return filteredWords

def tokenize(TextFilePath) -> list<Token>:
    tokenList = list()

    filteredWords = open_file(TextFilePath)
    
    tokenSet = set(filteredWords)
	
	for word in tokenSet:
        aToken = Token(tokenSet)
        aToken.set_count = filteredWords.count(word)
        tokenList.append(aToken)
        
    return tokenList

    
        
    
    

    


    


