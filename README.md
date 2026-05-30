# 🧬 FASTA Sequence Analyzer

A Python-based bioinformatics toolkit for analyzing DNA sequences from FASTA files. This project performs sequence parsing, GC-content analysis, nucleotide frequency calculation, DNA translation, reverse complement generation, sequence alignment, and graphical visualization of sequence statistics.

---

## 🚀 Features

### Sequence Analysis

* FASTA file parsing
* Sequence length calculation
* GC-content calculation
* Nucleotide frequency analysis
* Reverse complement generation
* DNA → Protein translation
* Basic sequence alignment

### Data Visualization

* Nucleotide Frequency Bar Chart
* GC Content Distribution Pie Chart
* Automatic PNG export for reports and publications

### Bioinformatics Applications

* Genome sequence exploration
* Gene sequence analysis
* Comparative sequence studies
* Educational bioinformatics demonstrations
* NCBI FASTA sequence analysis

---

## 📂 Project Structure

```text
fasta-sequence-analyzer/
│
├── gc.py
├── sequence.fasta
├── nucleotide_frequency.png
├── gc_content_pie.png
├── requirements.txt
└── README.md
```

---

## 🛠 Technologies Used

* Python
* Matplotlib
* Bioinformatics Concepts
* File Handling
* Data Visualization

---

## 📊 Example Output

### Terminal Output

```text
Sequence Length: 326

GC Content (%): 40.18

Nucleotide Frequency:
A: 84
T: 111
G: 87
C: 44
```

### Nucleotide Frequency Analysis

![Nucleotide Frequency](nucleotide_frequency.png)

### GC Content Distribution

![GC Content](gc_content_pie.png)

---

## 🧬 Bioinformatics Concepts Implemented

### FASTA Parsing

Reads biological sequence data from FASTA formatted files.

### GC Content Analysis

Calculates the percentage of Guanine (G) and Cytosine (C) bases.

Formula:

GC Content (%) = ((G + C) / Total Bases) × 100

### DNA Translation

Translates nucleotide sequences into amino acid sequences using the standard genetic code.

### Reverse Complement

Generates the reverse complementary strand of DNA.

### Sequence Alignment

Performs a simple position-wise comparison between two sequences.

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/aryanchauhan-code/fasta-sequence-analyzer.git
cd fasta-sequence-analyzer
```

Install dependencies:

```bash
pip install matplotlib
```

---

## ▶️ Run the Program

```bash
python gc.py
```

---

## 📈 Generated Files

The program automatically creates:

```text
nucleotide_frequency.png
gc_content_pie.png
```

These images can be used in reports, presentations, and publications.

---

## 🔮 Future Enhancements

* ORF Finder
* Restriction Enzyme Site Analysis
* Motif Detection
* Biopython Integration
* CSV Report Export
* Streamlit Web Interface
* NCBI API Integration
* Multiple Sequence Alignment
* Codon Usage Analysis
* Phylogenetic Tree Construction

---

## 👨‍💻 Author

**Aryan Chauhan**

MSc Bioinformatics

GitHub: https://github.com/aryanchauhan-code

---

## ⭐ Support

If you found this project useful:

* Star the repository ⭐
* Fork the repository 🍴
* Share feedback 💡

---

Made with Python 🐍 and Bioinformatics 🧬

```
```
