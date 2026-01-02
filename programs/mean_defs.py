def mean1(a, b, *more, weights=None):
    print(more)
    return (a + b + sum(more)) / (2 + len(more))


def mean2(a, b, *, weights=None):
    return (a + b) / 2

m = (3, 5)
(a, b) = (3, 4)

print(a)
print(b)

print(mean1(2, 7, 3, 4))
print(mean1(2, 7, *m))