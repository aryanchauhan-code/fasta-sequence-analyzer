def read_fasta(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        sequence = ""

        for line in lines:
            if not line.startswith(">"):
                sequence += line.strip()

        return sequence


def gc_content(sequence):
    g = sequence.count("G")
    c = sequence.count("C")

    return ((g + c) / len(sequence)) * 100


def nucleotide_frequency(sequence):
    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }


if __name__ == "__main__":
    fasta_file = "sequence.fasta"

    seq = read_fasta(fasta_file)

    print("Sequence Length:", len(seq))
    print("GC Content (%):", round(gc_content(seq), 2))
    print("Nucleotide Frequency:", nucleotide_frequency(seq))
    