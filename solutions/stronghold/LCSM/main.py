def read_fasta() -> dict:
    key = None
    seq = ""
    data = {}
    try:
        for line in iter(input, ""):
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if key:
                    data[key] = seq
                key = line[1:]
                seq = ""
            else:
                seq += line
    except EOFError:
        pass

    if key:
        data[key] = seq
    return data


def generate_substrings(s: str):
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            yield s[i:j]


def find_longest(lst: list[str]) -> str:
    max_len = 0
    max_str = None
    for sub in generate_substrings(lst[0]):
        in_all = True
        for s in lst:
            in_all = in_all and (sub in s)
            if not in_all:
                break
        if not in_all:
            continue
        if len(sub) <= max_len:
            continue
        max_str = sub
        max_len = len(sub)
    return max_str


if __name__ == "__main__":
    fasta = read_fasta()
    values = list(fasta.values())
    print(find_longest(values))