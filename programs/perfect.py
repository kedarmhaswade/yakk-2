# Implements a rather straightforward (slow) algorithm to print the perfect numbers less than or equal to N.
# Time is quadratic in N and space is linear in N. Perhaps this program can be exploited to solve the problem using
# number theory. Euclid had already proved something remarkable 2300+ years ago: If (2^p)-1 is prime, then 2^(p-1) times
# that prime, i.e. 2^(p-1)x(2^p)-1 is perfect!

N = 100_000_000 # adjust depending on your patience
d = [0, 0]
for i in range(2, N + 1):
    d.append(1)
for i in range(2, N + 1):
    m = 2
    index = m * i
    while index <= N:
        d[index] += i
        m += 1
        index = m * i
for i in range(2, N + 1):
    if d[i] == i:
        print(i)
