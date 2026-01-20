import sys
import random
import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.frequency = 0

    def increment_count(self):
        self.frequency += 1

    def get_frequency(self):
        return self.frequency

def tokenize(TextFilePath) -> list<Token>:
    tokenList = list()

    with open(TextFilePath, 'r') as file:
        content = f.read() 
    


