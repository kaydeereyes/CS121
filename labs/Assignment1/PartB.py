import PartA as tokenizer

def findIntersection(freqA: dict, freqB: dict) -> dict:
    intersection = {k: abs(freqA[k] - freqB[k])
                    for k in freqA.keys() & freqB.keys()
                    if freqA[k] != freqB[k]}
    return intersection

def commonTokenCount(intersection: dict) -> int:
    return sum(intersection)

if __name__ == '__main__':
    tokensA = tokenizer.tokenize()
    tokensB = tokenizer.tokenize()

    freqA = tokenizer.computeWordFrequencies(tokensA)
    freqB = tokenizer.computeWordFrequencies(tokensB)

    intersection = findIntersection(freqA, freqB)

    print(commonTokenCount(intersection))