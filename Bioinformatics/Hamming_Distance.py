#compute Hamming Distance
a='CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG'
b='ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT'
dist = 0

for i in range (len(a)):
    if a[i] == b[i]:
        dist += 1

print(dist)