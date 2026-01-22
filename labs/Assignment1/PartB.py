import PartA as tokenizer

def findIntersection(freqA: dict, freqB: dict) -> dict:
    intersection = {k: abs(freqA[k] - freqB[k])
                    for k in freqA.keys() & freqB.keys()
                    if freqA[k] != freqB[k]}

    return intersection

def commonTokenCount(intersection: dict) -> int:
    return sum(intersection.values())

if __name__ == '__main__':
    freqA = tokenizer.getFileFrequencies()
    freqB = tokenizer.getFileFrequencies()

    intersection = findIntersection(freqA, freqB)

    print(commonTokenCount(intersection))