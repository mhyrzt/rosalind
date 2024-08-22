def get_input():
    data = ""
    while True:
        try:
            line = input().strip()
            if line[0] == ">" or len(line) == 0:
                if data != "":
                    yield data
                data = ""
            else:
                data += line
            if len(line) == 0:
                break
        except:
            yield data
            break


def count(dna_list: list[str], symbol: str, col: int):
    return sum(int(dna[col] == symbol) for dna in dna_list)


def get_profile(dna_list: list[str]) -> list[list[int]]:
    n = len(dna_list[0])
    return [[count(dna_list, s, c) for c in range(n)] for s in "ACGT"]


def get_max(profile: list[list[int]], col: int) -> str:
    val, sym = -1, None
    for i, p in enumerate(profile):
        if p[col] > val:
            sym = i
            val = p[col]
    return "ACGT"[sym]


def get_consensus(profile: list[list[int]]) -> str:
    ans = ""
    for col in range(len(profile[0])):
        ans += get_max(profile, col)
    return ans


def print_profile(profile):
    for i, p in enumerate(profile):
        print(f'{"ACGT"[i]}:', *p)


if __name__ == "__main__":
    dna_lst = list(get_input())
    profile = get_profile(dna_lst)
    print(get_consensus(profile))
    print_profile(profile)
