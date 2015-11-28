from __future__ import print_function


def pattern_count(text, pattern):
    count = 0
    pattern_len = len(pattern)
    for i in range(0, len(text) - pattern_len):
        if text[i:i + pattern_len] == pattern:
            count += 1
    return count


if __name__ == '__main__':
    import sys

    t, p = sys.argv[1], sys.argv[2]
    print(pattern_count(t, p))
