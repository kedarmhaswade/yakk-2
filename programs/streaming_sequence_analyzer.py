#!/usr/bin/env python

# See the discussion at the end of sequence_analyzer.py. This script contains a generator-based solution.
# Is this more readable than the "declarative solution" presented by ChatGPT in that script?

import string


def gen_words(chars):
    """
    This generator function yields words from a sentence. A word contains no whitespace characters and
    does not start or end with a punctuation mark.
    :param chars: a string
    :return: a generator function
    """
    index = 0
    word_start = 0  # inclusive, index of the starting character in a word
    word_end = 0
    while index < len(chars):
        while index < len(chars) and chars[index] in string.whitespace:
            index += 1
        while index < len(chars) and chars[index] in string.punctuation:
            index += 1
        word_start = index
        while index < len(chars) and chars[index] not in string.whitespace:
            index += 1
        # found a sequence that may have ended with punctuation mark(s)
        word_end = index - 1
        while word_end >= 0 and chars[word_end] in string.punctuation:
            word_end -= 1
        if word_end >= word_start:
            yield chars[word_start:word_end + 1]


def analyze(chars):
    """
    Analyzes characters in the given parameter and returns a 3-tuple.
    :param chars: [str]
    :return: (number of words, number of unique words, length of longest word)
    """
    gen = gen_words(chars)
    unique_words = {} # dictionary is preferred to set; we count frequency of every word
    max_word_len = 0
    num_words = 0
    for word in gen:
        num_words += 1
        unique_words[word] = unique_words.get(word, 0) + 1
        if len(word) > max_word_len:
            max_word_len = len(word)
    print(unique_words)
    return num_words, len(unique_words), max_word_len

sentence = input("Enter a sentence: ")
t3 = analyze(sentence)
print(t3)
