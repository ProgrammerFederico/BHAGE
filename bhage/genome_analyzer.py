def calculate_genome_length(sequence):
    genome_length = len(sequence)

    return(genome_length)

def count_nucleotides(sequence):
    nucleotide_counts = {
        "A": 0, 
        "G": 0, 
        "T": 0, 
        "C": 0
        }

    for nucleotide in sequence:
        if nucleotide in nucleotide_counts: nucleotide_counts[nucleotide] += 1

    return nucleotide_counts

def calculate_gc_content(nucleotide_counts):
    count_total = (nucleotide_counts["A"] + nucleotide_counts["G"] + nucleotide_counts["T"] + nucleotide_counts["C"])
    if count_total == 0: return None
    gc_content = ((nucleotide_counts["G"] + nucleotide_counts["C"]) / count_total) * 100

    return gc_content

def calculate_ambiguity(genome_length, nucleotide_count):
    known_count = sum(nucleotide_count.values())
    ambigious_count = genome_length - known_count
    ambiguity = {
        "count": ambigious_count, 
        "percentage": (ambigious_count * 100) / genome_length
        }
    return ambiguity
    
def analyze_genome(parsed_record):
    sequence = parsed_record["genetic_payload"]
    genome_length = calculate_genome_length(sequence)
    nucleotide_count = count_nucleotides(sequence)
    gc_content = calculate_gc_content(nucleotide_count)
    ambiguity = calculate_ambiguity(genome_length, nucleotide_count)

    analysis_result = {
        "id": parsed_record["id"], 
        "genome_length": genome_length,
        "nucleotide_count": nucleotide_count,
        "gc_content": gc_content,
        "ambiguity": ambiguity
        }
    
    return analysis_result

test_record = {
    "id": "Phage_B",
    "genetic_payload": "NNNN"
}

print(analyze_genome(test_record))