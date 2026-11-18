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


def test_invalid_nucleotide():
    with open("tests/fixtures/test_invalid_iupac.fasta") as file:
        with pytest.raises(ValueError, match="Invalid Nucleotide detected"):
            parse_fasta(file)

def test_valid_iupac():
    with open("tests/fixtures/test_valid_iupac.fasta") as file:
        result = parse_fasta(file)
        assert result[0]["genetic_payload"] == "ATGCNRYS"
        assert result[1]["genetic_payload"] == "ACGTWKMBDHV"

def test_invalid_header():
    with open("tests/fixtures/test_invalid_header.fasta") as file:
        with pytest.raises(ValueError, match="FASTA header is missing a phage identifier."):
            parse_fasta(file)


def test_malformed_fasta():
    with open("tests/fixtures/test_malformed_fasta.fasta") as file:
        with pytest.raises(ValueError, match="Malformed FASTA file detected."):
            parse_fasta(file)

def test_empty_genome():
    with open("tests/fixtures/test_empty_genome.fasta") as file:
        with pytest.raises(ValueError, match="Empty genome detected."):
            parse_fasta(file)

def test_empty_final_genome():
    with open("tests/fixtures/test_empty_final_genome.fasta") as file:
        with pytest.raises(ValueError, match="Empty genome detected."):
            parse_fasta(file)

def test_blank_genome():
    with open("tests/fixtures/test_blank_genome.fasta") as file:
        with pytest.raises(ValueError, match="Empty genome detected."):
            parse_fasta(file)

def test_empty_fasta():
    with open("tests/fixtures/test_empty_fasta.fasta") as file:
        with pytest.raises(ValueError, match="Empty FASTA file detected."):
            parse_fasta(file)