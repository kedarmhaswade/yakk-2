from sympy import factorint, nextprime


def is_semiprime(n):
    fs = factorint(n)
    values = list(fs.values())
    if (len(values) == 2 and values[0] == 1 and values[1] == 1) or (len(values) == 1 and values[0] == 2):
        # print(fs)
        return fs.keys()
    # print(f"Not a semiprime, {n}, factors: {fs}")
    return None


def next_semiprime(sp):
    factors = is_semiprime(sp)
    if not factors:
        raise Exception(f"not a semiprime: {sp}")
    sf = sorted(factors)
    f1, f2 = sf[0], sf[1 if len(sf) == 2 else 0]
    lim = min(nextprime(f1) * f2, f1 * nextprime(f2))
    i = sp + 1
    while i < lim:
        if is_semiprime(i):
            return i
        i += 1
    return lim

# sp = 2026
# nsp = next_semiprime(sp)
# print(f"semiprime successor of {sp}: {nsp}, factors: {factorint(nsp)}")

n = 4
print(n)
while n < 1_000_000:
    n = next_semiprime(n)
    print(n)
