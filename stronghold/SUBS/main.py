s, t = input(), input()
for i in range(len(s) - len(t)):
    if s[i : i + len(t)] == t:
        print(i + 1, end=" ")
