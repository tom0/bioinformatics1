from __future__ import print_function


def hamming_distance(p, q):
    count = 0
    for idx, c in enumerate(p):
        if q[idx] != c:
            count += 1
    return count


if __name__ == '__main__':
    import sys

    p = sys.argv[1]
    q = sys.argv[2]
    print(hamming_distance(p, q))
