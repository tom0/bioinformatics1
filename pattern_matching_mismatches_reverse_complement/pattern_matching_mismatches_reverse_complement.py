from __future__ import print_function
from collections import defaultdict
from neighbourhood.neighbourhood import neighbours
from reverse_complement.reverse_complement import reverse_complement


def pattern_matching_mismatches(text, k, d):
    counts = defaultdict(int)
    max_count = 0
    for i in range(len(text) - (k - 1)):
        kmer = text[i:i+k]
        for n in set.union(neighbours(kmer, d), neighbours(reverse_complement(kmer), d)):
            counts[n] += 1
            if counts[n] > max_count:
                max_count = counts[n]

    most_frequent = []
    for kmer, count in counts.items():
        if count == max_count:
            most_frequent.append(kmer)

    return most_frequent

if __name__ == '__main__':
    import sys
    (t, k, d) = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    print(' '.join(pattern_matching_mismatches(t, k, d)))
