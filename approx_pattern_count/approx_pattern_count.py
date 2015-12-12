from __future__ import print_function
from hamming_distance.hamming_distance import hamming_distance

def approx_pattern_count(text, pattern, d):
    count = 0
    pattern_len = len(pattern)
    for i in range(len(text) - (pattern_len-1)):
        substr = text[i:i+pattern_len]
        if hamming_distance(pattern, substr) <= d:
            count += 1
    return count

if __name__ == '__main__':
    p = 'TACAG'
    t = 'GAATCCGCCAAGTACCAAGATGTAAGTGAGGAGCGCTTAGGTCTGTACTGCGCATAAGCCTTAACGCGAAGTATGGATATGCTCCCCGGATACAGGTTTGGGATTTGGCGGTTACCTAAGCTAACGGTGAGACCGATATGACGAGGTTCCTATCTTAATCATATTCACATACTGAACGAGGCGCCCAGTTTCTTCTCACCAATATGTCAGGAAGCTACAGTGCAGCATTATCCACACCATTCCACTTATCCTTGAACGGAAGTCTTATGCGAAGATTATTCTGAGAAGCCCTTGTGCCCTGCATCACGATTTGCAGACTGACAGGGAATCTTAAGGCCACTCAAA'
    d = 2
    print(approx_pattern_count(t, p, d))