def PatternCount (Text, Pattern):
    #print "Pattern lenght = ", len(Pattern)
    #print "Text input= ", Text
    #print "Pattern to search for= ", Pattern
    matches = 0
    for i in range(0,len(Text)):
        #print "Seleccionando: ", Text[i:i+len(Pattern)]
        if Text[i:i+len(Pattern)] == Pattern :
            matches += 1
    #print "Number of matches= ", matches
    return matches

def PatternMatch (Pattern, Genome):
    matches = ""
    for i in range(0,len(Genome)-len(Pattern)):
        if Genome[i:i+len(Pattern)] == Pattern :
            matches += str(i) + " "
    return matches

def FrequentWords (Text, k):
    FrequentPatterns = []
    Count = []
    for i in range(0, len(Text) - k):
        Pattern = Text[i:i+k]
        # print Pattern
        Count.append(PatternCount (Text, Pattern))
    maxCount = max(Count)  
    # print Count
    for i in range(0, len(Text) - k):
        if Count[i] == maxCount:
            aux = Text[i:i+k]
            # check if item exists already before inserting in array
            if FrequentPatterns.count(aux) == 0:
                FrequentPatterns.insert(0,Text[i:i+k])
    return FrequentPatterns

def ReverseComplement (Pattern):
    Reverse = ""
    for j in Pattern:
        i = ""
        if   j == "A": i = "T"
        elif j == "T": i = "A"
        elif j == "C": i = "G"
        elif j == "G": i = "C"
        Reverse = i + Reverse
    return Reverse
