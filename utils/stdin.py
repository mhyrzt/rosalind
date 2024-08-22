def read_fasta() -> dict:
    key = None
    seq = ""
    data = {}

    for line in iter(input, ""):
        line = line.strip()
        if not line:
            break
        if line.startswith(">"):
            if key:
                data[key] = seq
            key = line[1:]
            seq = ""
        else:
            seq += line

    if key:
        data[key] = seq

    return data
