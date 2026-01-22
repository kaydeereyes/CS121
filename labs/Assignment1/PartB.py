import sys
import PartA as tokenizer

def findIntersection(freqA: dict, freqB: dict) -> dict:
    """
    Returns the intersection of two token frequency dictionaries.
    Runtime: O(k), k = number of unique tokens in both files.
    Explanation: For each token present in both freqA and freqB, we compute min(freqA[k], freqB[k]).
    """
    return {k: min(freqA[k], freqB[k]) for k in freqA.keys() & freqB.keys()}

def commonTokenCount(intersection: dict) -> int:
    """
    Computes total number of tokens in the intersection.
    Runtime: O(k), k = number of unique tokens in intersection.
    """
    return sum(intersection.values())

if __name__ == '__main__':
    # Require exactly 2 command-line arguments: file1 and file2
    if len(sys.argv) != 3:
        print("Usage: python PartB.py <file1> <file2>")
        sys.exit(1)

    fileA = sys.argv[1]
    fileB = sys.argv[2]

    # Compute token frequencies using PartA
    freqA = tokenizer.getFileFrequencies(fileA)
    freqB = tokenizer.getFileFrequencies(fileB)

    # Compute intersection
    intersection = findIntersection(freqA, freqB)

    # Print intersection tokens and total
    print("Intersection tokens:")
    for token, count in intersection.items():
        print(token.value(), count)

    print("Total common tokens:", commonTokenCount(intersection))
