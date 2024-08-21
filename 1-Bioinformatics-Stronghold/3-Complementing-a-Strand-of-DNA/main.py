S = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G",
}
print("".join(S[x] for x in reversed(input())))
