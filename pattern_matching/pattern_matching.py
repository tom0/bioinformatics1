def pattern_matching(genome, pattern):
    pattern_len = len(pattern)
    return [i for i in range(0, len(genome)-pattern_len) if genome[i:i+pattern_len] == pattern]

if __name__ == '__main__':
    import sys

    p, filename = sys.argv[1], sys.argv[2]
    with open(filename, 'r') as f:
        print(" ".join([str(i) for i in pattern_matching(f.read(), p)]))
