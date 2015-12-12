def hamming_distance(p, q):
    count = 0
    for idx, c in enumerate(p):
        if q[idx] != c:
            count += 1
    return count

