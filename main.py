# DNA Sequence Analyzer

# Read FASTA file safely
with open("sample.fasta", "r") as file:
    lines = file.readlines()

# Extract sequence
sequence = lines[1].strip()

# Basic calculations
length = len(sequence)

g_count = sequence.count("G")
c_count = sequence.count("C")
gc_count = g_count + c_count
gc_percentage = (gc_count / length) * 100

at_count = length - gc_count
at_percentage = (at_count / length) * 100

# Professional Output
print("===== DNA Sequence Analysis =====")
print("Sequence:", sequence)
print("Length:", length)
print("GC Count:", gc_count)
print("GC %:", round(gc_percentage, 2))
print("AT Count:", at_count)
print("AT %:", round(at_percentage, 2))