#!/usr/bin/env python

# Examine what happens when the global function `list` is called with a dictionary as an argument

d = {'a' : 97, 'b' : 98, 'c' : 99}

for i in list(d):
    print(i, d[i])
