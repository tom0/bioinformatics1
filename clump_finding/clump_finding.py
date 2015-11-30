def find_clumps(genome, k, l, t):
    from collections import defaultdict
    kmers = defaultdict(list)
    for i in range(len(genome) - k - 1):
        kmers[genome[i:i + k]].append(i)

    max_diff = (l - k)  # -k so that the right-hand pattern fits in the window completely
    clumps = []
    tmin1 = t - 1
    for k, pos_list in kmers.items():
        pos_list_len = len(pos_list)
        if pos_list_len < t:
            continue

        for i in range(pos_list_len - tmin1):
            if pos_list[i + tmin1] - pos_list[i] <= max_diff:
                clumps.append(k)
                break

    return clumps


if __name__ == '__main__':
    import sys

    filename, k, l, t = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    with open(filename, 'r') as f:
        print(" ".join([str(i) for i in find_clumps(f.read(), k, l, t)]))
