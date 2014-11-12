def Hamming_Distace (input1, input2):
    """ Compute the hamming distance between two k-mers of equal dimension

    Taken two input strings representing two equal sized k-mers, compute the number of differences, 
    between same relative positions in the strings.
    """
    #confirm that input strings are the same size
    if len(input1) <> len(input2):
        print "Error. Input strings of different sizes"
        return -1
    
    count = 0
    for x in range(0, len(input1)):
        if input1[x] <> input2[x]:
            count += 1
    return count

def Approximate_Pattern_Matching(pattern, text, d):
    """ Find all approximate occurrences of a pattern in a string.

    Find all approximate occurences of a pattern in a given string where the "humming difference" does not 
    exeed an identified max (d)
    """
    count = 0
    output = ""
    for x in range(0, len(text)-len(pattern)+1):
        if Hamming_Distace(pattern, text[x:x+len(pattern)]) <= d:
            count += 1
            output += str(x) + " "
    return output

def FrequentWords1 (text, pattern, d):
    """ count frequent occurences of a pattern in text with max x mismatches
    
    Given strings Text and Pattern as well as an integer d, count total number of occurrences of Pattern in Text
    with at most d mismatches.
    """
    count = 0
    for x in range(0, len(text) - len(pattern) + 1):
        if Hamming_Distace(pattern, text[x:x+len(pattern)]) <= d :
            count += 1
    return count

def Frequent_Words_With_Mismatches (text, k, d):
    """ Find the most frequent k-mers with mismatches in a string.

    Taking a string, a numeric length for k-mers and a max Humming distance, identify all the most frequent words
    with k length and max humming distance <= d.
    """

    for x in range(0, len(text) - k+1):
        null #to be completed...