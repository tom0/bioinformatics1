from __future__ import print_function
from collections import defaultdict
from neighbourhood.neighbourhood import neighbours
from approx_pattern_count.approx_pattern_count import approx_pattern_count
from utils.base4 import pattern_to_number, number_to_pattern


def pattern_matching_mismatches_copy_pseudocode(text, k, d):
    frequent_patterns = set()
    close = []
    frequency_array = []
    for i in range(4**k):
        close.append(False)
        frequency_array.append(0)

    for i in range(len(text) - (k)):
        neighbourhood = neighbours(text[i:i+k], d)
        for pattern in neighbourhood:
            index = pattern_to_number(pattern)
            close[index] = True

    for i in range(4**k):
        if close[i]:
            pattern = number_to_pattern(i, k)
            frequency_array[i] = approx_pattern_count(text, pattern, d)

    max_count = max(frequency_array)
    for i in range(4**k):
        if frequency_array[i] == max_count:
            pattern = number_to_pattern(i, k)
            frequent_patterns.add(pattern)

    return frequent_patterns


def pattern_matching_mismatches(text, k, d):
    counts = defaultdict(int)
    max_count = 0
    for i in range(len(text) - (k - 1)):
        kmer = text[i:i+k]
        ns = neighbours(kmer, d)
        for n in ns:
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

