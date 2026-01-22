import typing

class Token:
    def __init__(self, word):
        self.word = word

    def __eq__(self, other):
        return isinstance(other, Token) and self.word == other.word

    def __hash__(self):
        return hash(self.word)
        
    def value(self):
        return self.word

def open_file(path) -> list:
    if not path:
        path = input(f'Input File Path: ').strip()
    
    with open(path, 'r') as f:
        for line in f:
            for word in line.lower().split():
                wordAlpha = ''.join(c for c in word if c.isalnum()) #checks if its alphanumeric
                if len(wordAlpha) > 3:
                    yield wordAlpha
            
def tokenize(TextFilePath=None) -> list[Token]:
    return [Token(word) for word in open_file(TextFilePath)]

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

if __name__ == '__main__':
    Testing = True

    if Testing:
        tokenList = tokenize("texts/test01.txt")
        tokenCount = computeWordFrequencies(tokenList)
        printTokens(tokenCount)

    runTokenizer()


    
        
    
    

    


    


