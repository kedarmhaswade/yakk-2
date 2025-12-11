#!/usr/bin/env python

# Goal: Integrate lists, dicts, mutability, and user interaction.
#
# Task:
# - Create an empty shopping cart (list).
# - Allow the user to add items with name and price.
# - Store items as a tuple (name, price) inside the cart list.
# - Let the user remove items by name.
#
# At checkout, compute:
# Total price
# Most expensive item
# Average price
# Print a summary dict:
#
# {
#     "total_items": ...,
#     "total_price": ...,
#     "most_expensive": ...,
#     "average_price": ...
# }
#
#
# Hints:
#
# Use loops, list comprehension, max() with key function.
#
# Tuples inside list demonstrate immutability vs. mutability.


def shop():
    cart = []
    total = 0
    maxp = 0
    most_exp = ""
    while True:
        name = input(f"\tAdd item name: (Enter to check out) ")
        if name == "":
            if len(cart) > 0:
                print(f"\t\ttotal_items {len(cart)}: {cart}")
                print(f"\t\ttotal_price: {total}")
                print(f"\t\tmost_expensive: {most_exp}: {maxp}")
                print(f"\t\taverage_price: {total / len(cart)}")
            break
        price = float(input("\tAdd item price: "))
        cart.append((name, price))
        if price > maxp:
            maxp = price
            most_exp = name
        total += price


while True:
    n = input("Welcome! Enter 1, anything else to exit: ")
    if n == "":
        print("Good Bye!")
        break
    if int(n) == 1:
        shop()


from collections import namedtuple