from __future__ import print_function
from distance_between_pattern_and_strings.distance_between_pattern_and_strings import \
    distance_between_pattern_and_strings
from utils.base4 import number_to_pattern


def median_string(dna_list, k):
    median = None
    distance = None
    for i in xrange((4 ** k) - 1):
        pattern = number_to_pattern(i, k)
        dist = distance_between_pattern_and_strings(pattern, dna_list)
        if distance is None or dist < distance:
            distance = dist
            median = pattern
    return median

if __name__ == '__main__':
    res = median_string(['TTCTGTCCCGAGAAACAAGCTCCTTGCTCCCAGCTTTGTCAT', 'CTTGTTTGGTTATCGCCGGTGTTTCTCTGTTCCGAGCGGGGA', 'CTGCGCCACACTCTTGGCGGCGGGCGTCACATCTGTGTTAAC', 'CTCTGTATAGAAGTCCGTTAATGCTTAATTTTTCTGGTCCCC', 'ATCTGTTATGGGCGGTGTATGACTGATGGCAATGCTGAAGGG', 'ATGGGAGGTAAGTCTGACATCTCGGTCTGTCTTTAAGATCTC', 'CTGATCCTCTGTAAGTCGCTTAGGCCATTCTTCGCGGAAGCC', 'TAGCACTAACAGTTCTGTTAGATTAACGTTCAACTAGTTGAG', 'AAACGGTACGACCAATTGCTATTCGTCTGTAACCGTTCTGAA', 'GGCACGTAGTACAGCGCTCACTACGCCGTCCGCTGTCTCTGT'], 6)
    print(res)

