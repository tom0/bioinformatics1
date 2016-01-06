from __future__ import print_function
from hamming_distance.hamming_distance import hamming_distance


def distance_between_pattern_and_strings(pattern, dna_list):
    k = len(pattern)
    distance = 0
    for dna in dna_list:
        min_hamming_distance = None
        for i in xrange(len(dna) - (k - 1)):
            kmer = dna[i:i + k]
            kmer_distance = hamming_distance(pattern, kmer)
            if min_hamming_distance is None or kmer_distance < min_hamming_distance:
                min_hamming_distance = kmer_distance
        distance += min_hamming_distance
    return distance

if __name__ == '__main__':
    result = distance_between_pattern_and_strings('GTCAGC', ['GCGGATGACTGTGGTCATAGCACAGAGCCTGGCATTAGCATAGGCTTAAGTAAGATAATATTTGCACGGCCTTTAGATTCAAATTCACCTTCCGATGGG', 'CAAGTAGCTCCGAGCTGGGTGATAGCAGTGTGATCGGAAACGCCGCACGTAAGGGCAAACTATACCACAAGACTAAAGCGTACCTCACGTTAAATCTCA', 'CCAACACCAGTTGAAGGGGCAACACGCGGCTCGGTAGTAGCCTCCGGCGCTTCTCATGTTTGTACACGACCCGATGAGGAGGAGGGGCGTGGAAACTCG', 'ACCCCTCGCCTAACTTGACGGTAAATGGACACCTTCCCCGTAGTCGCCAGTGACCCTCTTAGCCAACCATGCCTTTCCTTAGAAGGGGCAGTCGGCTAC', 'ACTGAATTTGTGGCGTTCTGTAGTGCCATCTTCTTTGGTGCACAACGAGTCCGGATATCAACATGGCTAAAATGTTAATCAAGCAGCGACAGATGGGAG', 'TCCCATAGTCATTGCCTGTTGAGGCTTTCTGCTCTCGTCTACCGCCAGTCTAGAAGTTATGAATTTACTCGTACTGGCGTACTAGATTCAAATTGTGGC', 'GTGTACGGAATGCTAATATCTTGCGTGTCTCCCCACACCACTAAATGTCCCGCCCCTAAAGTAAAACCGCTGATTTGTTGGTAAGGCAGCATTGATCTA', 'TTAACGCAACGGACCCAATTCCAGCTACTACCTTGCACCGCACGGATCAATAGCATATAATCGGTCTTTGCACCGCCTCTGGCCGAAAAAGAAACAGCT', 'GATTTATCCACACCGGTCCAGAATTTTCGGATATAGCGTATAAGTCTAGTGATGAGCCCCTCAAGCTTACTGCAACGGTGTTCTCCGCTCGCGATAAAA', 'ACGCGCTTAGTAAGGTACCGAGACTGCGGTGGCAGTCGCAGAAGCGAGCGTTTACCCCCCTTGGCGATGAGGATAGAGCTCCTCAGAGCCGTAGCATGA', 'CAGGTTCTGCGAGGCTCCCTAAGAAGTGTGAAATTTCCTGGAAGGACCACTGAGTACTCAGCGCAACCCGCCAAGATCGTTCAAGGTGTGCCCGTCTAT', 'TCCATCCTGTAAAGATCCAGGGTAATACGTCTTATAGCGACTTTTTTGGGACCACCGTAAGCTAATAAGTAGTTCCCGAAGACCGAGGCTACGCGAACC', 'CGGTGAACAATCACTAGAGGTAGCTGCAAAGTATTTAGTTACAAGAGCGGACCACTCTACGACGCATCCAGTTGTCACACCTGGCCCTAACGGGGAGAC', 'CCCTATAATTGTCCCGAAAACTCGCTCGTTCAATGCTCCTCATTATTTCTAAGTTATTCGATAAAATGAGAACTTCACTAGAGCGGCGTCTTCGAGGAT', 'TGAAGTGCTAAGGCTGCCAACCGGTCCGACTGTGGGCCAGCGGGGGCTTCGAGTTTCTGATTCGGGTGAGGCGTGACCAATTACTAAAGGTTAATCTTG', 'ACGTCATTTACTCTTAATTAGCAGGTCAGTTTTTCAGATCAGGATCCCGTGTGGAACATGAACTGATCACAGCACAAGGTTATATGGCAAGTGCTTAAG', 'GAGACAATAAATTCATTTTCGCTACTAAGTAACAATTGTGTCGTATGGGGCCACTTTACGTGGCTTTCGGGTGCGCTGTACGAACTGAGGCCAATCGGC', 'AAAGTTATGGAGTCCAAAGGTAGTACCTGCAAGAGTCTTTGCGCGGTGGGCAAATCCTGGATCCTAGCGCGACACTGATGATGTAATCCCAAATGTGGC', 'CAACGGGAAGGTGGGCCGGACACCTGTGGGCGTGTTACCCGGTGTAGGAATGATAGTAACCTAAAGGTTTGATGCACGGCGCCTGCCCACGGGGGTCAT', 'TCCAAAGGGTCGCATGACCTAATCGCGAGAAGCCTTATTTCAAGTAGTCTCAGCAACATCCCATGGATGCGTGGACACGTGTTCCCACCACTCCTACTA', 'CGCACGTGCCTATTCACTTCTTCGGTATTTCATGAGTGCAGAAGCTGTAGAGGCGTAACGCAGGCAATCCGCAGTCACATAACTCCCTCGGGTTAAATG', 'GAAGTAAATACAAGTCTAACGCTTGCGACATTGTTATAGCCAGGAGTGAGATACGGAGCTGTCCTTCCGCGACCACTACTCTTAGAGATGAAGTTCGTT', 'TACGGCTAGTTTACTTACTTGGTTTGCGTATCATCCCATCACGAACCTTAACCGGGTCCAATACCTGCACATCTGTCGCGTCCTAATCCCGCGAAGAGC', 'CGGTAACAGGTTGGGCGAGATTAGGACCGCGCCCGACTATGAGTATTTTCAATTTAAGCAATCCAGATAGTGCATTGGCTGAGTCGGTATATCGCCATA', 'GGTGATTCAAAATTCGCGAGTGTCCCTGTTCTCAGAATGATTTCGGTCCGACTGAGAGCTAGTGGCGCCCGGCTTTTCTCTGACTTCGATAAACCCTCA', 'ATTACCGTTTCCTTGCAGCGGCCAATCATCTTACATAGGAACTCATGCTAAGGGTGCTTCCGTAGAGACTTCACACCCTACGCGCTGAGGACCCCGCCT', 'CCCATAGCATTTTTCATGCAAGCCCTGTAATCTGCCCCAGTGAGTATCAACGTGACGCCAATTCGTGTGAGGTTCTCCGCACGTAAGAGACCCAACGAC', 'TTAGACAACCACGACTTGATGGAACGGCTATAGGGAGGAAGGCGTCCTTGCAGTTGAATATGGAATACTAACGGGCACGCCGCTATTTCGTAAAGGCGA', 'ATATTAGTTGACATGCCACAATAATGCGTGTGCGCTTCACACGCTCCAATATTTGGGGGACATAGGCTATGGCGAATTCACGTCATTGTTGAACTATAT', 'GAGAGAGCTTCGTCTGCCAAGCGTTCTGGTTTCCAAAGGTACTTGGGTAAAAAACAGATTGTGATGTTGGTATTGGCCTAGTGCGGGGACTGCGCTAGA', 'GCCACGACCTCAGTAGTGAGCTCCTGTATCGGTGGAAGTAGCCCCGAAAACGAAGCCCCCCGCTCTTTTTCACGAGCACTTAGCTCACGTGATACTGTT'])
    print(result)
