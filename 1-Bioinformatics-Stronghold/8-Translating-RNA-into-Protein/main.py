import os


def get_current_dir() -> str:
    return os.path.dirname(os.path.abspath(__file__))


def read_table(dir: str = None, filename: str = "codon_table.csv") -> dict:
    with open(os.path.join(dir or get_current_dir(), filename), "r") as f:
        return dict(map(lambda x: x.split(), f.readlines()))


rna = input()
table = read_table()
protein = ""
for i in range(0, len(rna), 3):
    a = table[rna[i : i + 3]]
    protein += a if a != "Stop" else ""
print(protein)
