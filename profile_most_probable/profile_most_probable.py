def _calc_kmer_prob(kmer, profile):
    nucleotides = ['A', 'C', 'G', 'T']
    result = 1
    for i, c in enumerate(kmer):
        result *= profile[i][nucleotides.index(c)]
    return result


def _profile_most_probable(text, k, profile):
    max_prob = 0
    max_prob_kmer = None
    for i in xrange(len(text) - (k - 1)):
        kmer = text[i:i + k]
        prob = _calc_kmer_prob(kmer, profile)
        if prob > max_prob:
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


def profile_most_probable(text, k, profile_lines):
    profile = _parse_profile(profile_lines)
    return _profile_most_probable(text, k, profile)


if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        file_lines = f.readlines()

    kmer = file_lines[0].strip()
    k = int(file_lines[1])
    profile_lines = [file_lines[i+2].strip() for i in range(4)]

    profile = profile_most_probable(kmer, k, profile_lines)

    print(profile)
