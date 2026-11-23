import pytest

import bhage.genome_analyzer as ga

# Test Genome Length
def test_genome_length():
    result = ga.calculate_genome_length(sequence="ATGC")
    assert result == 4


# Test Nucleotide Counter
def test_nucleotide_count():
    result = ga.count_nucleotides(sequence="AATGC")
    assert sum(result.values()) == 5
    assert result["A"] == 2
    assert result["G"] == 1


#Test Guanine Cytosine Content Calculator 
def test_gc_content_calculator():
    result = ga.calculate_gc_content({"A": 2, "T": 2, "G": 2, "C": 2})
    assert result == 50.0

#Test Ambiguity Calculator 
def test_ambiguity_calculator():
    result = ga.calculate_ambiguity(4, {"A": 1, "T": 1, "G": 1, "C": 0})
    assert result["count"] == 1
    assert result["percentage"] == 25.0

# Test Analyze Genome function with valid genome.
def test_analyze_valid_genome():
    result = ga.analyze_genome({"id": "Phage_A", "genetic_payload": "ATGC"})
    assert result["id"] == "Phage_A"
    assert result["genome_length"] == 4
    assert result["nucleotide_count"] == {"A": 1, "T": 1, "G": 1, "C": 1}
    assert result["gc_content"] == 50.0
    assert result["ambiguity"] == {"count": 0, "percentage": 0}

# Test Analyze Genome function with ambiguous genome.
def test_analyze_ambiguous__genome():
    result = ga.analyze_genome({"id": "Phage_A", "genetic_payload": "ATNGC"})
    assert result["id"] == "Phage_A"
    assert result["genome_length"] == 5
    assert result["nucleotide_count"] == {"A": 1, "T": 1, "G": 1, "C": 1}
    assert result["gc_content"] == 50.0
    assert result["ambiguity"] == {"count": 1, "percentage": 20.0}

# Test Analyze Genome function with all ambiguous genome.
def test_analyze_all_ambiguous__genome():
    result = ga.analyze_genome({"id": "Phage_A", "genetic_payload": "NNNN"})
    assert result["id"] == "Phage_A"
    assert result["genome_length"] == 4
    assert result["nucleotide_count"] == {"A": 0, "T": 0, "G": 0, "C": 0}
    assert result["gc_content"] is None
    assert result["ambiguity"] == {"count": 4, "percentage": 100.0}
