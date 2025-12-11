#!/usr/bin/env python

"""
Goal: Practice lists, tuples, strings, and basic operations.

Task:
- Ask the user to input a sentence.
- Count and print:
  - Total number of words
  - Number of unique words
  - Length of the longest word
- Return a tuple containing: (total_words, unique_words, longest_word_length)
- Print all words in reverse order (use slicing).
"""

sentence = input("Enter a sentence: ")


def analyze(sentence):
    unique_words = set()
    num_words = 0
    num_unique_words = 0
    longest_word_length = 0
    word_list = []
    for w in sentence.split():
        num_words += 1
        word_list.append(w)
        if not w in unique_words:
            unique_words.add(w)
            num_unique_words += 1
            word_length = len(w)
            longest_word_length = max(word_length, longest_word_length)
    assert num_unique_words == len(unique_words)
    for i in range(num_words):
        print(word_list[num_words - 1 - i])
    return num_words, num_unique_words, longest_word_length


print(analyze(sentence))

# ChatGPT suggests
# def analyze(sentence):
#     words = sentence.split() # You don’t need word_list since sentence.split() already gives a list
#     unique_words = set(words)
#     longest_word_length = max(len(w) for w in words) # Uses a generator expression
#
#     for w in reversed(words): # this gives a reverse Iterator, not a new list. More readable.
#         print(w)
#
#     return len(words), len(unique_words), longest_word_length

# lesson learned: Use basic data structures, iterators better. Think declaratively. Readability counts.
# However, doesn't longest_word_length = max(len(w) for w in words) result in comparing lengths again? I guess
# that's okay. My preference is to maintain a "running max-len", like, for example, a running average in a streaming case.
# Is a Generator solution better? It depends. For now, readability is your guide. For fun, code a generator-based solution.
