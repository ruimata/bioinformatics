from scripts import ReverseComplementDNA as RevComp
from Textbook_01G import MismatchList

#with open('filename.txt') as input_data:
#        dna, [k, d] = [line.strip() if index == 0 else map(int, line.strip().split()) for index, line in enumerate(input_data.readlines())]

dna = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1

# Use a dictionary to count the occurence of each k-mer and its reverse complement with up to d mismatches on each.
mismatch_dict = {}
for i in xrange(len(dna)-k+1):
        for kmer in MismatchList(dna[i:i+k], d)+MismatchList(RevComp(dna[i:i+k]), d):
                if kmer in mismatch_dict:
                        mismatch_dict[kmer] += 1
                else:
                        mismatch_dict[kmer] = 1

# Computing the maximum value is somewhat time consuming to repeat, so only do it once!
max_val = max(mismatch_dict.values())
kmers = [item[0] for item in mismatch_dict.items() if item[1] == max_val]

print ' '.join(kmers)
with open('output/textbook/Textbook_01H.txt', 'w') as output_data:
        output_data.write(' '.join(kmers))