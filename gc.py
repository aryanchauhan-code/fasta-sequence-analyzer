def read_fasta(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        sequence = ""

        for line in lines:
            if not line.startswith(">"):
                sequence += line.strip().upper()

        # Keep only valid DNA bases
        sequence = "".join([base for base in sequence if base in "ATGC"])

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


def translate_dna(sequence):

    codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',

        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',

        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',

        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
        'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'
    }

    protein = ""

    for i in range(0, len(sequence)-2, 3):
        codon = sequence[i:i+3]
        protein += codon_table.get(codon, '?')

    return protein


def sequence_alignment(seq1, seq2):

    alignment = ""

    min_length = min(len(seq1), len(seq2))

    for i in range(min_length):

        if seq1[i] == seq2[i]:
            alignment += "|"

        else:
            alignment += " "

    print("\nSequence Alignment:\n")

    print(seq1)
    print(alignment)
    print(seq2)


def reverse_complement(sequence):

    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    reverse_seq = sequence[::-1]

    reverse_complement_seq = ""

    for base in reverse_seq:
        reverse_complement_seq += complement.get(base, base)

    return reverse_complement_seq


if __name__ == "__main__":

    fasta_file = "sequence.fasta"

    seq = read_fasta(fasta_file)

    print("Sequence Length:", len(seq))

    print("GC Content (%):", round(gc_content(seq), 2))

    print("Nucleotide Frequency:", nucleotide_frequency(seq))

    print("\nProtein Sequence:")

    print(translate_dna(seq))

    # Second sequence for alignment
    seq2 = "ATGCGTAGCTAGCTAGCTAGCGCGATATATCG"

    sequence_alignment(seq[:len(seq2)], seq2)

    print("\nReverse Complement:")

    print(reverse_complement(seq))