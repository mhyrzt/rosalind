import math
k, n = list(map(int, input().split()))

p = 1.0
for x in range(n):
    k2 = 2 ** k
    p -= math.comb(k2, x) * (0.25 ** x) * (0.75 ** (k2 - x))
print(round(p, 3))
