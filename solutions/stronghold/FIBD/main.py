n, m = list(map(int, input().split()))
ages = [1] + [0 for _ in range(m - 1)]
for m in range(1, n):
    ages = [sum(ages[1:])] + ages[:-1]
print(sum(ages))
