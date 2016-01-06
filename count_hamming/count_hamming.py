from __future__ import print_function
from hamming_distance.hamming_distance import hamming_distance


def count_hamming(pattern, text, d):
    count = 0
    pattern_len = len(pattern)
    for i in range(len(text) - (pattern_len - 1)):
        sub_text = text[i:i+pattern_len]
        if hamming_distance(sub_text, pattern) <= d:
            count += 1
    return count

if __name__ == '__main__':
    import sys

    p, t, d = sys.argv[1], sys.argv[2], int(sys.argv[3])
    print(count_hamming(p, t, d))

