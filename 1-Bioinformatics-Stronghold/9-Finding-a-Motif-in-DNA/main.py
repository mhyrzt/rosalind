# n, m = list(map(int, input().split()))
n, m = 6, 3
rabbits = [1, 1] + [0 for _ in range(n - 2)]
for i in range(2, n):
    rabbits[i] = rabbits[i - 1] + rabbits[i - 2]
    if i > m:
        rabbits[i] -= rabbits[i - m - 1]
print(list(range(n)))
print(rabbits)
print(rabbits[-1])
