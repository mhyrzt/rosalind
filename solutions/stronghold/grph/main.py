from utils import read_fasta


def get_edges(fasta: dict, name: str, k: int) -> tuple:
    edges = []
    lst_k = fasta[name][-k:]
    for key, dna in fasta.items():
        if key == name or dna[:k] != lst_k:
            continue
        edges.append(key)
    return set(edges)


def create_graph(fasta: dict, k: int = 3) -> dict:
    return {x: get_edges(fasta, x, k) for x in fasta}


def print_graph(graph: dict) -> None:
    for n1 in graph:
        for n2 in graph[n1]:
            print(n1, n2)


if __name__ == "__main__":
    print_graph(create_graph(read_fasta()))
