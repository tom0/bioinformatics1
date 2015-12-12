from __future__ import print_function
from hamming_distance.hamming_distance import hamming_distance


def neighbours(pattern, d):
    nucleotides = ['A', 'C', 'G', 'T']
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return set(nucleotides)
    neighbourhood = set()
    suffix_pattern = pattern[1:]
    suffix_neighbours = neighbours(suffix_pattern, d)
    for t in suffix_neighbours:
        if hamming_distance(suffix_pattern, t) < d:
            for n in nucleotides:
                neighbourhood.add(n + t)
        else:
            neighbourhood.add(pattern[0] + t)

    return neighbourhood

if __name__ == '__main__':
    print('\n'.join(neighbours('GATCTACTA', 3)))