def minimum_skew(dna):
    minimum = None
    counts = [0]
    for idx, char in enumerate(dna):
        new_count = counts[idx]
        if char == 'C':
            new_count -= 1
        elif char == 'G':
            new_count += 1

        if minimum is None or new_count < minimum:
            minimum = new_count

        counts.append(new_count)

    res = []
    for idx, val in enumerate(counts):
        if val == minimum:
            res.append(idx)

    return res


if __name__ == '__main__':
    import sys

    dna = sys.argv[1]
    print(" ".join([str(i) for i in minimum_skew(dna)]))
