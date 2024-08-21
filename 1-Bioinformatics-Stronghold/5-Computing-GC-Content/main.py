def process_input(data: str) -> dict:
    data = data.split(">")
    keys = map(lambda x: x.split("\n")[0], data)
    vals = map(lambda x: "".join(x.split("\n")[1:]), data)
    data = dict(zip(keys, vals))
    del data[""]
    return data


def calc_gc_content(dna: str) -> float:
    return 100 * (dna.count("G") + dna.count("C")) / len(dna)


data = open("rosalind_sample.txt", "r").read()
vals = sorted(
    [(k, calc_gc_content(v)) for k, v in process_input(data).items()],
    key=lambda x: x[-1],
    reverse=True,
)
print(*vals[0], sep="\n")
