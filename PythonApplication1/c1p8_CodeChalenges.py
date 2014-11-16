import c1p1to3_CodeChalenges

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

def Neighbours (text, d, neighbors_dict, index, start_text):
    """Implement Neighbors to find the d-neighborhood of a string.

    Generate a dictionary with all neighbors of a given word with a max Hamming distance of (d)
    """
    variation_dict = {"A":"A", "C":"C", "G":"G", "T":"T"}
    #neighbors_dict = dict()
    for z in range (0, len(text)):
        for variation in variation_dict:
            #if variation <> text[z]:
            aux = start_text + text[0:z]+variation+text[z+1:]
            if aux in neighbors_dict:
                if index not in neighbors_dict[aux][1]:
                    neighbors_dict[aux][0] += 1
                    neighbors_dict[aux][1].append(index)
            else:
                neighbors_dict[aux] = [1, [index]]
            if d > 1:
                neighbors_dict = Neighbours(text[z+1: ], d - 1, neighbors_dict, index, start_text + text[0:z] + variation)
    return neighbors_dict

def Build_Frequent_Words_With_Mismatches(text, k, d, reverse):
    """ Build frequency tree, based on number of occurrences of a pattern (and all patterns at a d distance)
    """
    words = dict()
    # Dictionary of every word of k length and mapping of all of its occurences (including mismatches with max d distance)
    for x in range(0, len(text) - k+1):
        pattern = text[x : x + k]
        #Generation of all pattern neighbors with max Hamming distance (d)
        words = Neighbours(pattern, d, words, x, '')
        if reverse:
            words = Neighbours(c1p1to3_CodeChalenges.ReverseComplement(pattern), d, words, x, '')
    return words


def Frequent_Words_With_Mismatches (text, k, d, reverse):
    """ Find the most frequent k-mers with mismatches in a string.

    Taking a string, a numeric length for k-mers and a max Humming distance, identify all the most frequent words
    with k length and max humming distance <= d.
    """
    
    # Generate frequency dictionary of pattern occurrences
    words1 = Build_Frequent_Words_With_Mismatches(text, k, d, reverse)
    #words2 = Build_Frequent_Words_With_Mismatches(c1p1to3_CodeChalenges.ReverseComplement(text), k, d, reverse)
    words = dict()
    #for each in words1:
    #    words[each] = words1[each][0] + words2[c1p1to3_CodeChalenges.ReverseComplement(each)][0]
    for each in words1:
        words[each] = words1[each][0]
    #for each in words2:
    #    words[c1p1to3_CodeChalenges.ReverseComplement(each)] += words2[each][0]

    # identify maximum number of occurences in list
    maxx = max(words.values())
    #keys = [item[0] for item in words.items() if item[1] == maxx]
    keys = [x for x,y in words.items() if y ==maxx]
    #keys = [x for x,y in words.items() if y[0] ==maxx[0]]
    #keys = [item[0] for item in words.items() if item[1][0] == maxx[0]]
    return keys

def Frequent_Words_With_Mismatches_and_ReverseComplements (text, k, d):
    """ Find the most frequent k-mers with mismatches and reverse complements in a string.

    Taking a string, a numeric length for k-mers and a max Humming distance, identify all the most frequent words
    with k length and max humming distance <= d that maximize the sum Countd(Text, Pattern)+ Countd(Text, Pattern)
    """

    # Generate frequency dictionary of pattern occurrences
    words = Build_Frequent_Words_With_Mismatches(text, k, d, True)
    #words = Build_Frequent_Words_With_Mismatches(c1p1to3_CodeChalenges.ReverseComplement(text), k, d)

    # Build a paired (pattern + reverse complement)
    #pairs = dict()
    #for pattern in words:
    #    pairs[pattern+c1p1to3_CodeChalenges.ReverseComplement(pattern)] = [1, []]

    return words

