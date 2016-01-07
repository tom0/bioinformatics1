from collections import defaultdict
from profile_most_probable.profile_most_probable import profile_most_probable


def get_profile_and_score(motifs):
    nucleotides = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    profile = []
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

        profile.append([c / float(height) for c in counts])
    return profile, score


def greedy_motif_search(dna_strings, k, t):
    best_score = None
    best_motifs = []
    for i in range(len(dna_strings[0]) - (k - 1)):
        kmer = dna_strings[0][i:i + k]
        motifs = [kmer]
        score = 0
        for i in range(1, t):
            profile, score = get_profile_and_score(motifs)
            most_probable_kmer = profile_most_probable(dna_strings[i], k, profile)
            motifs.append(most_probable_kmer)
        if best_score is None and score is not None:
            best_score = score
            best_motifs = motifs
        elif score is not None and score <= best_score:
            best_score = score
            best_motifs = motifs
    return best_motifs


if __name__ == '__main__':
    import sys

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        file_lines = f.readlines()

    k_t = file_lines[0].strip().split()
    k = int(k_t[0])
    t = int(k_t[1])
    dna_strings = [file_lines[i + 1].strip() for i in range(t)]

    res = greedy_motif_search(dna_strings, k, t)
    print("\n".join(res))
