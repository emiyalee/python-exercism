MAP = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
}


def to_rna(dna_strand):
    return "".join([MAP[c] for c in dna_strand])
