from __future__ import print_function

_symbols = ['A', 'C', 'G', 'T']


def pattern_to_number(pattern):
    while pattern and pattern[0] == 'A':
        pattern = pattern[1:]

    total = 0
    for i, c in enumerate(reversed(pattern)):
        val = _symbols.index(c)
        total += (val * 4 ** i)

    return total


def number_to_pattern(number, k=None):
    (num, rem) = divmod(number, 4)
    rems = [rem]
    while num > 0:
        (num, rem) = divmod(num, 4)
        rems.append(rem)

    pattern = ''
    for r in reversed(rems):
        pattern += _symbols[r]

    if k is not None:
        padding_len = k - len(pattern)
        if padding_len > 0:
            pattern = ('A' * padding_len) + pattern
    return pattern


if __name__ == '__main__':
    assert(number_to_pattern(912, 6) == 'ATGCAA')
    assert(pattern_to_number('AAAAAATGCAA') == 912)
