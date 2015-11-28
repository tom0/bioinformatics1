def reverse_complement(str_pattern):
    complements = {
        'G': 'C',
        'A': 'T',
        'C': 'G',
        'T': 'A'
    }
    result = ""
    for c in str_pattern:
        result = complements[c] + result
    return result

if __name__ == '__main__':
    import sys

    t = sys.argv[1]
    print(reverse_complement(t))
