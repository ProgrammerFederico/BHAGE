import pytest

from bhage.fasta_parser import parse_fasta

def test_multiple_records():
    with open("tests/fixtures/test_normalization.fasta") as file:
        result = parse_fasta(file)
    
    assert len(result) == 3 
    assert result[0]["genetic_payload"] == "ATGCGGTA"
    assert result[1]["genetic_payload"] == "CCATTTAA"
    assert result[2]["genetic_payload"] == "GGCCAATT"

    assert result[0]["id"] == "Phage_A"
    assert result[1]["id"] == "Phage_B"
    assert result[2]["id"] == "Phage_C"


def test_invaid_nucleotide():
    with open("tests/fixtures/test_invalid_iupac.fasta") as file:
        with pytest.raises(ValueError):
            parse_fasta(file)
