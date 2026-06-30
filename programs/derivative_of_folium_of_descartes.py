#!/usr/bin/env python

# How do we plot the derivative of the folium of Descartes on a graphing calculator such as Desmos?

# One way is to use copy-paste!
# This program outputs the values of the derivative (x^2-y/x-y^2) for some values of x, which can then be c+p ed on Desmos.
# A cubic must be solved to get the value of y for each x, according to the folium's implicit equation: x^3+y^3=3xy

import numpy as np


# Function: folium of descartes.
# Returns the values of y for a given value of x.
def fod(x):
    coeffs = [1, 0, -3 * x, x ** 3]
    roots = np.roots(coeffs)
    real_roots = [float(r.real) for r in roots if abs(r.imag) < 1e-10]
    return real_roots


# Function: derivative of folium of Descartes at a given x = x**2-y/x-y**2
def d_fod(x):
    ys = fod(x)
    print(f"x: {x}, ys: {ys}")
    if len(ys) == 0:
        raise Exception(f"Weird! No value for the the folium at x = {x}")
    y = ys[0]  # consider the first real value
    d = x - (y * y)
    if d == 0:
        raise Exception(f"Weird! Derivative of the folium at x = {x}, y = {y} does not exist!")
    n = x * x - y
    return n / d


# Function to plot the derivative of the folium.
# Returns an array of 2-tuples (x, y), where y=f'(x), f' is the derivative
def d_fod_table(low=-10, high=10, step=0.1):
    table = []
    x = low
    while x <= high:
        try:
            d = d_fod(x)  # may raise
            table.append((x, d))
        except Exception as e:
            print("Got an exception ({e}). Ignoring {x}")
        finally:
            x = x + step
    return table

for p in d_fod_table():
    print(f"{p[0]},{p[1]}")
