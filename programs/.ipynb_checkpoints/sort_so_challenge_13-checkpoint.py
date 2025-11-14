# https://stackoverflow.com/beta/challenges/79811869/challenge-13-integer-sorting-in-a-grid/

# This script implements a solution to this challenge. The problem was first solved using pencil and
# (a lot of) paper and was coded to the best of my abilities with readability, correctness, and efficiency in mind.

# Pledge: No AI assistance is sought in writing this code. I used the standard, non-AI code-completion
# assistance in the PyCharm editor.

def init_matrix(n):
    d2 = []
    for i in range(n):
        d2.append([])
        for j in range(n):
            d2[i].append(0)
    return d2


def populate_matrix_diagonally(d1, rows):
    """
    Rearranges the given list of integers according to the rules of the challenge and returns a matrix.
    :param d1:
    :param rows:
    :return:
    Implementation notes: The given list must contain only integers. It is first reverse-sorted in place (rev_sorted).
    The returned matrix is filled from bottom left to top right by the numbers from rev_sorted. The number of non-principal
    diagonals, num_diag is clearly 2 * rows - 1 and each diagonal has first increasing and then decreasing number
    of numbers (len_diag) in it: 1, 2, 3, ..., rows, rows - 1, rows - 2, ..., 1.
    """
    # assumption: rows * rows = len(d1)
    d1.sort(reverse=True)
    rev_sorted = d1
    matrix = init_matrix(rows)
    i = 0  # index in the reverse-sorted 1-d list
    sri = sci = 0  # sri and sci are the starting (row, col) indices where a non-principal diagonal starts
    ri = sri
    ci = sci  # ri and ci are the (row, col) indices where a number is put in a diagonal
    num_diag = 2 * rows - 1  # number of diagonals of the matrix
    len_diag = 1  # number of numbers in each diagonal
    di = ei = 0  # di: index of a diagonal, ei: index of the element in that diagonal
    while di < num_diag:
        while ei < len_diag:
            num = rev_sorted[i]
            if ri > 0 and matrix[ri - 1][ci] == num:
                raise ValueError(f"Impossible! Repeated number {num} in the column at ({ri}, {ci})")
            if ci > 0 and matrix[ri][ci - 1] == num:
                raise ValueError(f"Impossible! Repeated number {num} in the row at ({ri}, {ci})")
            matrix[ri][ci] = num
            i += 1
            ei += 1
            ri -= 1
            ci += 1
        di += 1
        ei = 0
        if di <= rows - 1:
            len_diag += 1
            sri += 1
        else:
            len_diag -= 1
            sci += 1
        ri = sri
        ci = sci
    assert i == len(d1), f"The list must have been exhausted, but not! i: expected [{len(d1)}], found [{i}]"
    return matrix

# s = "[27, 63, 51, 6, 3, 10, 7, 36, 80, 51, 93, 71, 73, 25, 3, 77, 35, 56, 36, 36, 77, 97, 14, 1, 78, 83, 5, 51, 99, 5, 93, 90, 1, 36, 83, 4]"
# s = "[54, 95, 98, 26, 3, 39, 77, 30, 83, 62, 20, 92, 61, 59, 26, 63, 92, 49, 38, 51, 99, 64, 65, 52, 98, 18, 90, 97, 96, 13, 74, 3, 88, 88, 67, 10]"
# s = "[95, 84, 44, 16, 42, 73, 0, 53, 14, 63, 81, 91, 42, 14, 13, 59, 91, 24, 99, 71, 73, 34, 60, 65, 82, 55, 16, 75, 7, 18, 68, 6, 61, 6, 80, 41]"
# s = "[2, 2, 2, 4]"
# s = "[9, 8, 8, 7, 7, 7, 6, 6, 5]"
# s = "[9, 2, 10, 57, 79, 65, 65, 0, 19, 64, 3, 18, 20, 93, 10, 30, 9, 0, 40, 51, 87, 34, 52, 71, 28, 23, 73, 61, 77, 60, 66, 91, 57, 58, 2, 9]"
# d1 = ([int(x) for x in s[1:-1].split(",")])
# d1.sort(reverse=True)
# print(d1)
# d2 = populate_matrix_diagonally(d1, int(len(d1)**0.5))
# for row in d2:
#     print(row)
# Does not work ?
# def preprocess(d1, rows):
#     d1.sort(reverse=True)
#     freq = {}
#     for num in d1:
#         freq[num] = freq.get(num, 0) + 1
#     unique_nos = len(freq)
#     min_unique_nos = 2 * rows - 1
#     if unique_nos < min_unique_nos:
#         raise ValueError(f"Not enough unique numbers; required >= {min_unique_nos}, found: {unique_nos}")

# not needed!
# def preprocess(xs):
#     """
#         Returns the rank of each number in xs as a dictionary
#         :param xs: list of integers
#         :return: {x : its rank (int)}; 1 is the highest rank
#     """
#     xs.sort(reverse=True) # highest number first
#     ranks = {}
#     high = xs[0]
#     ranks[xs[0]] = cur_rank = 1
#     for i in range(1, len(xs)):
#         if xs[i] < high:
#             high = xs[i]
#             cur_rank += 1
#         ranks[xs[i]] = cur_rank
#     return ranks
