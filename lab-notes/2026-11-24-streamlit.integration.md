# M3.4 — Streamlit Integration: Lab Notes

**Initialization Date:** 2026-11-24  
**Updated Date:** 2026-11-27  
**Project:** BHAGE  
**Milestone:** M3 — Genome Analysis  
**Task:** M3.4 Streamlit Integration  
**Status:** Implementation complete — pending deployment

## Program / Task

`bhage/app.py`  — Integration of the FASTA parser and genome analyzer into the BHAGE research dashboard.

## Goal

Connect the existing bioinformatics scripts to the Streamlit application, setup FASTA file upload functionality, analyze multiple phage genomes, and ability to interactively visualize their genomic characteristics.

## Data Transformation & Parser Compatibility

- Extracted raw bytes from uploaded FASTA file object then decoded them into a single string.
- Split decoded strings into lists of individual lines compatible with the FASTA parser.
- Iterated through parsed records and passed each record into the genome analyzer.
- Stored analyzed records in a list of dictionaries.
- Transformed nucleotide count dictionaries into Pandas DataFrames for visualization with Altair.

## What Worked

- Successful integration of the FASTA parser and genome analyzer.
- Dynamic presentation of GC content, genome length, and sequence ambiguity.
- Interactive nucleotide distribution charts.
- Selection and analysis of individual genomes within multi-record FASTA files.
- Exception handling for malformed and invalid FASTA files.
- Independent selection of records containing duplicate phage identifiers.

## What Didn't Work

- Initially encountered compatibility issues when processing uploaded FASTA data, requiring conversion from bytes into strings.
- Encountered difficulties transforming nucleotide dictionaries into chart-compatible data.
- Name-based record selection could not distinguish duplicate phage identifiers because `.index()` retrieves only the first matching element.
- Initial error message formatting produced a `TypeError` due to incorrect positional arguments.
- Final regression testing initially failed due to a missing empty FASTA fixture. Recreating the fixture resolved the failure.

## What I Learned

- Refreshed my understanding of for-loop iteration and nested data structures.
- Learned how to decode bytes and transform strings into lists.
- Developed a stronger understanding of Pandas DataFrames and data visualization using Altair.
- Learned how to use nested functions, keyword arguments, and exception handling (definitely could use some more practice on this).
- Learned the distinction between referencing and calling a function.
- Gained introductory experience with callback functions through Streamlit's `format_func` parameter.
- Developed a better understanding of separating underlying data values from their visual representation.

## Architectural Decisions

- Maintained separation between the FASTA parser, genome analyzer, and presentation layer.
- Preserved original phage identifiers rather than rejecting duplicate names.
- Replaced name-based record retrieval with index-based selection to prevent incorrect genome retrieval.
- Used a formatting callback to generate distinguishable record labels without modifying original research data.
- Handled parsing errors within the dashboard to prevent invalid inputs from reaching the analysis stage.
- Reserved sequence-level deduplication for future machine learning dataset curation.

## Testing Results

| Test | Result |
|---|---|
| Multiple records and normalization | Passed |
| Balanced nucleotide distribution | Passed |
| Unbalanced nucleotide distribution | Passed |
| Fully ambiguous genome | Passed |
| Malformed FASTA handling | Passed |
| Invalid nucleotide handling | Passed |
| Empty FASTA handling | Passed |
| Invalid header handling | Passed |
| Duplicate identifier display | Passed |
| Duplicate record #2 retrieval | Passed |
| Full automated regression suite | 16/16 passed |

**Final result:** All 16 automated tests passed. Dashboard integration and visualization were manually tested.

## Next Steps

- [x] Complete final dashboard verification.
- [x] Update research index.
- [x] Commit and push M3 changes.
- [x] Verify live deployment.
- [x] Revisit callback functions to reinforce understanding.
- [x] Begin M4 — Phage Host Prediction v0.1.