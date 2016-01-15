from random import random, randint
from profile_most_probable.profile_most_probable import profile_most_probable_motifs, calc_kmer_prob


def _get_profile(motifs, succession):
    nucleotides = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    profile = []
    for i in range(len(motifs[0])):
        counts = [0] * 4
        height = len(motifs)
        for j in range(height):
            nuc = motifs[j][i]
            count_idx = nucleotides[nuc]
            counts[count_idx] += 1

        profile.append([c + 1 / float(height + succession) for c in counts])
    return profile


def _get_random_kmer(dna, k):
    start = randint(0, len(dna) - k)
    return dna[start:start + k]


def _get_score(motifs):
    nucleotides = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    score = None
    for i in range(len(motifs[0])):
        counts = [0] * 4
        height = len(motifs)
        most_frequent_count = 0
        most_frequent_nuc = None
        for j in range(height):
            nuc = motifs[j][i]
            count_idx = nucleotides[nuc]
            counts[count_idx] += 1
            if counts[count_idx] > most_frequent_count:
                most_frequent_count = counts[count_idx]
                most_frequent_nuc = nuc

        for key, val in nucleotides.items():
            count = counts[val]
            if key != most_frequent_nuc and count != 0:
                if score is None:
                    score = count
                else:
                    score += count
    return score


def get_random_number(probs):
    s = sum(probs)
    if s != 1:
        probs = [p / s for p in probs]

    p = random()
    prev = 0
    for idx, prob in enumerate(probs):
        prob = prob + prev
        if p <= prob:
            return idx
        prev = prob


def _get_kmer_probs(text, profile, k):
    probs = []
    for i in range(len(text) - (k - 1)):
        probs.append(calc_kmer_prob(text[i:i + k], profile))
    return probs


def gibbs_sampler(dna_strings, k, t, n):
    motifs = [_get_random_kmer(dna, k) for dna in dna_strings]
    best_motifs = motifs
    best_score = _get_score(motifs)
    for _ in range(n):
        i = randint(0, t - 1)
        motifs.pop(i)
        profile = _get_profile(motifs, t)
        probs = _get_kmer_probs(dna_strings[i], profile, k)
        rand = get_random_number(probs)
        rand_kmer = dna_strings[i][rand:rand + k]
        motifs.insert(i, rand_kmer)
        new_score = _get_score(motifs)
        if new_score < best_score:
            best_motifs = motifs
            best_score = _get_score(best_motifs)
    return best_motifs


def gibbs_sampler_with_score_threshold(dna_strings, k, t, max_score):
    motifs = [_get_random_kmer(dna, k) for dna in dna_strings]
    best_motifs = motifs
    best_score = _get_score(motifs)
    while best_score > max_score:
        i = randint(0, t - 1)
        motifs.pop(i)
        profile = _get_profile(motifs, t)
        probs = _get_kmer_probs(dna_strings[i], profile, k)
        rand = get_random_number(probs)
        rand_kmer = dna_strings[i][rand:rand + k]
        motifs.insert(i, rand_kmer)
        new_score = _get_score(motifs)
        if new_score < best_score:
            best_motifs = motifs
            best_score = _get_score(best_motifs)
            print(best_score)
    return best_motifs


if __name__ == '__main__':
    import sys

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        file_lines = f.readlines()

    k_t_n = file_lines[0].strip().split()
    k = int(k_t_n[0])
    t = int(k_t_n[1])
    n = int(k_t_n[2])
    dna_strings = [file_lines[i + 1].strip() for i in range(t)]
    print("\n".join(gibbs_sampler_with_score_threshold(dna_strings, k, t, 70)))
