#!/usr/bin/env python
"""
Word Frequency Counter
Goal: Read a sentence, and count how many times each word appears and print a frequency table sorted by most frequent words first.
Task:
- Convert all words to lowercase (so 'The' and 'the' are treated the same).
- Remove punctuation (optional, but makes it cleaner).
- Count occurrences of each word using a dictionary.
- Print words sorted by frequency descending, then alphabetically for ties.
"""
def count_word_frequencies(s):
    d = {}
    for w in s.split():
        w = w.lower()
        if w.startswith("'"):
            w = w[1:]
        if w.endswith("'"):
            w = w[:len(w)-1]
        if w.startswith('"'):
            w = w[1:]
        if w.endswith('"'):
            w = w[:len(w)-1]
        d[w] = d.get(w, 0) + 1

    return d


histo = count_word_frequencies(input("Enter a sentence: "))

ss = sorted(histo.items(), key=lambda t2: (-t2[1], t2[0]))
for p in ss:
    print(f"{p[0]}: {p[1]}")

# ChatGPT's suggestion.
#import string

# def count_word_frequencies(s):
#     s = s.lower().translate(str.maketrans('', '', string.punctuation))
# (or)         w = w.strip("'\"")   # remove leading/trailing quotes -- beginner
#     d = {}
#     for w in s.split():
#         d[w] = d.get(w, 0) + 1
#     return d

# histo = count_word_frequencies(input("Enter a sentence: "))
# ss = sorted(histo.items(), key=lambda t: (-t[1], t[0]))
# for word, count in ss:
#     print(f"{word}: {count}")

# ChatGPT recommendation:
# Stick to readable code for now.
# Once you hit Martelli’s chapter on str objects in detail, then revisit translate.
#
# Your current level of cleanliness and correctness is exactly right.

# lesson learned: Know/study standard libraries.
