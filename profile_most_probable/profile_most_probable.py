def calc_kmer_prob(kmer, profile):
    nucleotides = ['A', 'C', 'G', 'T']
    result = 1
    for i, c in enumerate(kmer):
        result *= profile[i][nucleotides.index(c)]
    return result


def profile_most_probable_motifs(dna_strings, k, profile):
    return [profile_most_probable(dna, k, profile) for dna in dna_strings]


def profile_most_probable(text, k, profile):
    max_prob = None
    max_prob_kmer = None
    for i in xrange(len(text) - (k - 1)):
        kmer = text[i:i + k]
        prob = calc_kmer_prob(kmer, profile)
        if max_prob is None or prob > max_prob:
            max_prob = prob
            max_prob_kmer = kmer
    return max_prob_kmer


def _parse_profile(profile_lines):
    line_len = len(profile_lines[0].split())
    profile = [[] for i in range(line_len)]

    for line in profile_lines:
        for j, freq in enumerate(line.split()):
            profile[j].append(float(freq))

    return profile


if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        file_lines = f.readlines()

    kmer = file_lines[0].strip()
    k = int(file_lines[1])
    profile_lines = [file_lines[i+2].strip() for i in range(4)]

    profile = _parse_profile(profile_lines)
    result = profile_most_probable(kmer, k, profile)

    print(result)
