import c1p1to3_CodeChalenges, c1p4_ClumpFinding, c1p4_TestCases_data, time
#start = datetime.datetime.now().time()
#print start

#a = "TCCGACGTTGACACTTCTAGCATAAGAGCAAGTTAGTTCTGGGACATCGTTATATATCATCGGGCGATTGTTCAACACCAGCTGTCAATTTGTAGGAAAGGGCCCTGCGATGCTCCAATAAGTGACAGC"

start = time.time()
print start
words = dict() 

words = c1p4_ClumpFinding.ClumpFinding (c1p4_TestCases_data.tdata_text, c1p4_TestCases_data.tdata_k, c1p4_TestCases_data.tdata_l, c1p4_TestCases_data.tdata_t)
#words = c1p4_ClumpFinding.ClumpFinding (a, 9, 574, 20)

print ' '.join(words)
print len(words)
end = time.time()
print end,    "diff = ", end - start 

