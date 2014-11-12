import c1p1to3_CodeChalenges, time

def MapWords (Text, k, words):
    for j in range(0, len(Text) - k + 1):
        if Text[j:j+k] in words :
            words[Text[j:j+k]][0] += 1
            words[Text[j:j+k]][1].append(j)
        else:
            words[Text[j:j+k]] = [1, [j]]
    return words


def FindClumps ( words, k, l, t):
    FrequentClumps = []
    for item in words.items():
        on = True
        if item[1][0] >= t:
            for index in range(0, item[1][0] - t + 1):
                a = item[1][1][index] + l - k + 1
                b = item[1][1][index + t - 1]
                c = a - b
                if item[1][1][index] + l - k + 1 >= item[1][1][index + t - 1] and on:
                    FrequentClumps.append(item[0])
                    on = False
    return FrequentClumps

def ClumpFinding ( genome, k, l, t):
    Clumps = []
    aux = dict()
    i = 0

    a = time.time()
    print "a mapear... ", a
    aux = MapWords(genome, k, aux)
    b = time.time()
    print "            ", b
    print "             diff = ", b-a

    a = time.time()
    print "a escolher... ", a
    aux1 = FindClumps(aux, k, l, t)
    b = time.time()
    print "            ", b
    print "             diff = ", b-a
    return aux1


#def ClumpFinding ( genome, k, l, t):
#    Clumps = []
#    for i in range (0, len(genome) - l):
#        aux = FindClumps ( genome[i: i+l], k, t)
#        for j in aux:
#            if Clumps.count (j) == 0:
#                Clumps.append (j)
#    return Clumps

#def ClumpFinding ( genome, k, l, t):

#    Clumps = []
#    i = 0
#    while (i < len (genome) - k + 1):
#        if i + l - k + 1 <= len (genome):
#            end = i+l-k+1
#        else :
#            end = len (genome) - i
#        aux = FindClumps ( genome[i: end], k, t)
#        i += l - k + 1

#        for j in aux:
#            if Clumps.count (j) == 0:
#                Clumps.append (j)
#    return Clumps



#def FindClumps ( Text, k, t):
#    """given a text string, identifies every clump of k-mer dimension appearing at least t times"""

#    FrequentClumps = []
#    Count = []
#    for i in range(0, len(Text) - k):
#        Pattern = Text[i:i+k]
#        # print Pattern
#        Count.append(c1p1to3_CodeChalenges.PatternCount (Text, Pattern))
#    # print Count
#    for i in range(0, len(Text) - k):
#        if Count[i] >= t:
#            aux = Text[i:i+k]
#            # check if item exists already before inserting in array
#            if FrequentClumps.count(aux) == 0:
#                FrequentClumps.append (Text[i:i+k])
#    return FrequentClumps