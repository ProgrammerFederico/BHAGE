# M3.1 — FASTA Parser: Lab Notes

**Date:** 2026-11-04
**Project:** BHAGE
**Milestone:** M3 — Genome Analysis
**Task:** M3.1 — FASTA Parsing and Validation (#11)
**Status:** In progress

## Program / Task
`bhage/fasta_parser.py` — `parse_fasta(file)`

## Goal

Build a reusable FASTA parser that reads a text stream, supports multiple FASTA records in one file, normalizes and validates DNA sequences, and returns structured records independently of Streamlit.

## 30 Second Session Observation 

- Struggled with tracking multiple variables simunltaneously.
- Understood individual Python concepts but struggled when combining them.
- Encountered difficulty following execution order and indentation.
- Made significant progress after breaking the parser down into smaller pieces.

## What Worked

- Successfully implemented multi-record FASTA parsing.
- Cleaned raw DNA sequences using .strip() and upper.()
- Combined multiline DNA sequences into continuous strings.
- Saved final FASTA record after loop finishes.
- Validated nucleotides against IUPAC alphabet.
- Breaking down complex logic into individual steps.
- Implemented validation for malformed headers, invalid nucleotides, empty genomes, and empty fasta files.
- Using visual representations such as flow charts to understand variables and their changing values.
- Developed nine automated tests using pytest.
- Strengthed said exception tests by verifying exact expected error messages.


## What Didn't Work
- Accounting for final FASTA record when no header was present.
- Reviewing entire parser at once made execution order difficult to follow.
- Incorrect indentation which led to FASTA headers being processsed as nucleotide sequences.
- Premature empty-genome validation caused valid reecords to be rejected.
- Initially confused testing successful outputs with testing exceptions. 



## What I Learned

- Empty python strings are seen as false.
- Nested conditionals/loops, indentation, and execution order.
- Raise to print an error statement triggered by a conditional.
- String slicing and concatenation using join().
- Importance of handling final record seperately outside the loop.
- How to represent multiple genomes using a list of dictionaries.
- File handling and iteration.
- The difference between accessing a file, iterating through its lines, and iterating through individual characters. (File - > Lines - > Characters)
- The difference between manual and automated testing.
- Using with open() to automatically manage the opening and closing of files.
- Using assert to verify expected results.
- Using pytest.raise() to verify expected exceptions.
- Using match to verify exception messages and prevent false-positive tests.
- Utilizing variables to hold function return values without repeatedly executing the function.
- Regression testing to properly ensure future changes do not break currently existing functionality.


## Scientific Decisions
- Represent each phage genome as an individual record.
- Convert DNA sequences to uppercase.
- Reject malformed FASTA input instead of accepting invalid data.
- Support ambiguous nucleotides through the IUPAC DNA alphabet.
- Reject genome genomes as well as invalid FASTA headers to prevent invalid data from entering downstream analysis.
- Seperate FASTA parsing and validation from downstream gnome analysis to maintain modularity.

## Testing Results

| Test | Result |
|---|---|
| Multiple records and normalization | Passed |
| Valid IUPAC nucleotides | Passed |
| Invalid nucleotides | Passed |
| Invalid header | Passed |
| Malformed FASTA | Passed |
| Empty genome | Passed |
| Empty final genome | Passed |
| Blank genome | Passed |
| Empty FASTA file | Passed |

**Final result:** 9/9 automated tests passed.

## Next Steps

- [x] Implement multi-record FASTA parsing.
- [x] Implement sequence normalization.
- [x] Manually test multi-record parsing and normalization.
- [X] Complete header and malformed FASTA validation.
- [X] Implement IUPAC nucleotide validation.
- [X] Handle empty sequences and empty FASTA files.
- [X] Develop automated parser tests.
- [X] Verify parser reliability before progressing to M3.2 — Genome Feature Extraction.


