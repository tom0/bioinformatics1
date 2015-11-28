def frequent_words(text, k):
    kmers = {}
    max = 0
    for i in range(0, len(text) - k):
        kmer = text[i:i+k]
        if not kmer in kmers:
            kmers[kmer] = 0
        kmers[kmer] += 1
        if kmers[kmer] > max:
            max = kmers[kmer]

    return [kmer[0] for kmer in kmers.items() if kmer[1] == max]

if __name__ == '__main__':
    import sys

    t, k = sys.argv[1], int(sys.argv[2])
    print(" ".join(frequent_words(t, k)))
