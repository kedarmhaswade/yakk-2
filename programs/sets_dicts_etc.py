#!/usr/bin/env python

# Goal: Combine dicts, sets, and loops.
# Task:
# You have a list of student names and their grades: (
#     students = [("Alice", 85), ("Bob", 92), ("Charlie", 85), ("Diana", 92), ("Eve", 78)]
#
# - Build a dictionary grades_dict where keys are grades and values are sets of student names.
# - Print the dictionary sorted by grades descending.
# - Ask the user for a grade and print the list of students who scored that grade.

students = [("Alice", 85), ("Bob", 92), ("Charlie", 85), ("Diana", 92), ("Eve", 78)]
grades_dict = {}
for name, grade in students:
    grades_dict.setdefault(grade, set())  # mutates the dictionary
    grades_dict[grade].add(name)

print(sorted(grades_dict.items(), key=lambda item: item[0], reverse=True))
grade = int(input("Enter a grade (an integer) for a set of students with that grade: "))
print(grades_dict.get(grade))
