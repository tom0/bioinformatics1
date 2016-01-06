from __future__ import print_function
from neighbourhood.neighbourhood import neighbours
from hamming_distance.hamming_distance import hamming_distance


def hamming_in_all(dna_strings, kmer, d):
    for dna in dna_strings:
        k = len(kmer)
        found_match = False
        for j in xrange(len(dna) - k + 1):
            kmer2 = dna[j:j + k]
            if hamming_distance(kmer, kmer2) <= d:
                found_match = True
                break
        if not found_match:
            return False
    return True


def motif_enumeration(dna_strings, k, d):
    # Epic runtime!
    patterns = set()
    for dna in dna_strings:
        for i in xrange(len(dna) - k + 1):
            ns = neighbours(dna[i:i + k], d)
            for n in ns:
                if hamming_in_all([x for x in dna_strings if x != dna], n, d):
                    patterns.add(n)
    return patterns

if __name__ == '__main__':
    import sys
    k, d = int(sys.argv[1]), int(sys.argv[2])
    dna = sys.argv[3:]
    # k = 3
    # d = 1
    # dna = [ 'ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT' ]
    print(" ".join(motif_enumeration(dna, k, d)))

