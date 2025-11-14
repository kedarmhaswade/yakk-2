import os
from unittest import TestCase

from programs.sort_so_challenge_13 import populate_matrix_diagonally


class TestChallenge13(TestCase):
    def test_populate_matrix_diagonally(self):
        filename = os.path.join(os.path.dirname(__file__), "RandomNumbers.txt")
        try:
            with open(filename, 'r') as file:
                impossible_count = 0
                for line in file:
                    try:
                        line.strip()  # .strip() removes leading/trailing whitespace, including '\n'
                        d1 = ([int(x) for x in line[1:-2].split(",")])
                        d1.sort(reverse=True)
                        print(d1)
                        d2 = populate_matrix_diagonally(d1, int(len(d1) ** 0.5))
                        for row in d2:
                            print(row)
                    except ValueError as v:
                        impossible_count += 1
                        print(v)
                print(f"total number of impossible cases {impossible_count}")
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
