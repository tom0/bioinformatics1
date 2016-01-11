from collections import defaultdict
from random import randint
from greedy_motif_search.greedy_motif_search_pseudocounts import get_profile_and_score
from operator import itemgetter
from profile_most_probable.profile_most_probable import profile_most_probable_motifs


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


def randomized_motif_search(dna_strings, k, t):
    motifs = [_get_random_kmer(dna, k) for dna in dna_strings]
    best_motifs = motifs
    while True:
        profile, best_motifs_score = get_profile_and_score(motifs, t)
        motifs = profile_most_probable_motifs(dna_strings, k, profile)
        new_score = _get_score(motifs)
        if new_score < best_motifs_score:
            best_motifs = motifs
        else:
            return best_motifs, best_motifs_score


def randomized_motif_search_score_bound(dna_strings, k, t, max_score):
    motifs, score = randomized_motif_search(dna_strings, k, t)
    while score > max_score:
        motifs, score = randomized_motif_search(dna_strings, k, t)
    return motifs


def randomized_motif_search_n_times(dna_strings, k, t, n):
    counts = defaultdict(int)
    for i in range(n):
        motifs, score = randomized_motif_search(dna_strings, k, t)
        key = " ".join(motifs)
        counts[key] += 1
    sorted_counts = sorted(counts.items(), key=itemgetter(1), reverse=True)
    return sorted_counts[0][0].split()


if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        file_lines = f.readlines()

    k_t = file_lines[0].strip().split()
    k = int(k_t[0])
    t = int(k_t[1])
    dna_strings = [file_lines[i+1].strip() for i in range(t)]

    print('\n'.join([str(x) for x in randomized_motif_search_score_bound(dna_strings, k, t, 70)]))
