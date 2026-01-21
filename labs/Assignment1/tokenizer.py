
import typing

class Token:
    def __init__(self, word):
        self.word = word
        self.count = 0

    def __eq__(self, other):
        return isinstance(other, Token) and self.word == other.word

    def __hash__(self):
        return hash(self.word)

    def increment_count(self): # Do I Need This if i just use the count method?
        self.count += 1

    def set_count(self, n):
        self.count = n

    def get_count(self):
        return self.count

    def value(self):
        return self.word

#Should I create a method that just runs all 3? Tokenize, Count, and Print?

def open_file(path) -> list:
    with open(path, 'r') as f:
        content = f.read(100) #Reads the first 100 chars in case of large files
        contentLower = content.lower()
        preprocessedWords = contentLower.split()
        filteredWords = [word for word in preprocessedWords if len(word) > 3]
    return filteredWords

def tokenize(TextFilePath) -> list[Token]:
    tokenList = list()

    filteredWords = open_file(TextFilePath)
    	
    for word in filteredWords:
        tokenList.append(Token(word))
        
    return tokenList

def computeWordFrequencies(tokenList: list[Token]) -> dict[Token, int]:
    tokenCount = dict()

    for token in tokenList:
        tokenCount[token] = tokenCount.get(token, 0) + 1

    sortedCount = dict(sorted(tokenCount.items(), 
                              key=lambda item: item[1], reverse = True))

    return sortedCount

def printTokens(tokens: dict[Token, int]) -> None:
    for token, count in tokens.items():
        print(f'{token.value()} {count}\n')

def runTokenizer(TextFilePath) -> None:
    tokenList = tokenize(TextFilePath)
    tokenCount = computeWordFrequencies(tokenList)
    printTokens(tokenCount)
        


    
        
    
    

    


    


