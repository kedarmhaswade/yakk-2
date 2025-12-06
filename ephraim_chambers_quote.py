#!/usr/bin/env python

"""
Knuth writes in the preface of his TAoCP book, Volume 4A: Combinatorial Algorithms, Part 1:

It’s true that combinatorial problems are often associated with humongously large numbers.
Johnson’s dictionary entry also included a quote from Ephraim Chambers, who had stated that
the total number of words of length 24 or less, in a 24-letter alphabet, is
1,391,724,288,887,252,999,425,128,493,402,200.

The corresponding number when we replace 24 by 10 in Chambers’s statement is 11,111,111,110;
and it’s only 3905 when we reduce the parameter to 5. Thus, a “combinatorial explosion” certainly
does occur as the size of the problem grows from 5 to 10 to 24 and beyond.

I decided to write a program for this. Fortunately, a closed-form formula exists!
"""

def num_max_words(asize=5):
    """
    Returns the maximum number of words of that can be formed by a given alphabet. The minimum word length
    is 1 and maximum asize. Repetition of letters is allowed. This is a problem of arrangements.
    :param asize: the size of the alphabet
    """
    return ((asize ** (asize + 1)) - asize) // (asize - 1)

print(num_max_words())
print(num_max_words(10))
print(num_max_words(24)) # 1391724288887252999425128493402200, yay!


