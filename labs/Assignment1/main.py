import tokenizer

def main():
    path = input('Please input file path: ')
    tokenList = tokenizer.tokenize(path)

if __name__ == '__main__':
    main()