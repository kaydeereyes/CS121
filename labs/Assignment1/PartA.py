import typing
import sys

class Token:
    """
    Represents a token derived from a text.
    """

    def __init__(self, word):
        self.word = word

    def __eq__(self, other):
        return isinstance(other, Token) and self.word == other.word

    def __hash__(self):
        return hash(self.word)
        
    def value(self):
        return self.word

def open_file(path):
    """
    Reads given file line by line. Yields tokens.
    Runtime: O(n). Each character is visited exactly once. 
    n = number of characters in the file.
    Exception: handled through encoding utf-8 and errors='ignore'
    """
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                for word in line.lower().split():
                    subwords = word.split('-')  # Splits hyphenated words
                    for sub in subwords:
                        wordAlpha = ''.join(c for c in sub if c.isalnum())
                        if wordAlpha:
                            yield wordAlpha
    except FileNotFoundError:
        print(f"Error: File not found: {path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file {path}: {e}")
        sys.exit(1)
            
def tokenize(TextFilePath: str) -> list[Token]:
    """
    Tokenizes file into a list of Tokens.
    Runtime = O(m), where m is the number of tokens generated.
    """
    return [Token(word) for word in open_file(TextFilePath)]

def computeWordFrequencies(tokenList: list[Token]) -> dict[Token, int]:
    """
    Computes frequencies of each Token.
    Runtime = O(m), where m = number of tokens.
    Explanation: Each token is visited exactly once. Dictionary lookup and insertion is O(1).
    """
    tokenCount = dict()
    for token in tokenList:
        tokenCount[token] = tokenCount.get(token, 0) + 1

    sortedCount = dict(sorted(tokenCount.items(), key=lambda item: item[1], reverse=True))
    return sortedCount

def printTokens(tokens: dict[Token, int]) -> None:
    """
    Prints tokens and their given frequencies.
    Runtime: O(k), where k = number of unique tokens.
    """
    for token, count in tokens.items():
        print(f'{token.value()} {count}\n')

def getFileFrequencies(path: str):
    """
    Convenience Method to assist Part B and reduce duplicated code. 
    Runtime: O(n), where n = number of characters in the file.
    """
    tokens = tokenize(path)
    return computeWordFrequencies(tokens)

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: python PartA.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]  # Get file name from command-line
    tokenCount = getFileFrequencies(input_file)
    printTokens(tokenCount)
