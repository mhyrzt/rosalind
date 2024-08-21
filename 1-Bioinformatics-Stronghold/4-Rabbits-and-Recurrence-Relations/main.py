n, k = list(map(int, input().split()))
rabbits = [1, 1]
for i in range(len(rabbits), n):
    n_1 = rabbits[i - 1]
    n_2 = rabbits[i - 2]
    rabbits.append(n_1 + k * n_2)
print(rabbits[-1])
