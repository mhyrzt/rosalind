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