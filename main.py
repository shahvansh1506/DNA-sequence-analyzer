import sys

# Check if user provided a file
if len(sys.argv) < 2:
    print("Usage: python main.py <fasta_file>")
    sys.exit()

filename = sys.argv[1]

# Read FASTA file
with open(filename, "r") as file:
    lines = file.readlines()

sequence = lines[1].strip()

length = len(sequence)

g_count = sequence.count("G")
c_count = sequence.count("C")
gc_count = g_count + c_count
gc_percentage = (gc_count / length) * 100

at_count = length - gc_count
at_percentage = (at_count / length) * 100

print("===== DNA Sequence Analysis =====")
print("Sequence:", sequence)
print("Length:", length)
print("GC Count:", gc_count)
print("GC %:", round(gc_percentage, 2))
print("AT Count:", at_count)
print("AT %:", round(at_percentage, 2))