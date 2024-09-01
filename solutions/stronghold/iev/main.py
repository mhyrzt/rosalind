
offsprings = [1.0, 1.0, 1.0, 0.75, 0.5]
couples = list(map(int, input().split()))
dominants = [2 * o * c for o, c in zip(offsprings, couples)]
print(sum(dominants))
