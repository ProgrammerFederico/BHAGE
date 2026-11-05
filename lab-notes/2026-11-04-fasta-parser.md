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

## What I Did
- Designed the parsing approach before implementation.
- Decided to represent completed FASTA records as a list of dictionaries, each with an identifier and sequence.
- Identified three pieces of parser state: `records`, `current_id`, and `sequence_lines`.
- Discussed detecting record boundaries from lines starting with `>`, saving the previous record at the next header, and saving the final record after the loop.
- Started drafting the function and line-reading loop.

## What Worked
- Recognized that a FASTA header marks the beginning of a new record.
- Reasoned that sequence lines should be collected temporarily and reset between records.
- Recognized the need to reject sequence data appearing before any header.
- Chose to preserve ambiguous nucleotides rather than remove them.

## What Didn't Work / Questions Encountered
- Initial draft used `lastLine = False`; this is unnecessary because the final record can be saved after the file-reading loop.
- Initial loop attempted `file.startsWith(">")` rather than checking the current line with Python's case-sensitive `.startswith()`.
- Initially used `continue` for headers, which would skip processing the identifier.
- Clarified why a list is useful for accumulating sequence lines and why `"".join(sequence_lines)` creates the final sequence string.
- **These are learning notes, not a claim that the parser is already implemented or tested.**

## Scientific / Engineering Decisions
1. **Multi-record FASTA:** Each `>` header begins a new record; multiline sequences belong to the current record until the next header or end of file.
2. **Separation of concerns:** The parser accepts a readable text stream. Opening files and handling Streamlit uploads belong outside the core parsing logic.
3. **Normalization:** Convert lowercase DNA symbols to uppercase.
4. **Valid symbols:** Accept standard IUPAC DNA symbols (`A C G T R Y S W K M B D H V N`). Preserve ambiguity codes, including `N`, and record relevant quality information.
5. **Invalid symbols:** Reject characters outside the accepted alphabet, such as `X`, with a clear error; validate while reading.
6. **Malformed input:** Reject sequence data before the first header.
7. **Error policy:** If any record in a single FASTA file is invalid, reject that entire file. A future batch analyzer can continue processing other files while reporting the failed file.
8. **Data integrity:** Do not silently remove ambiguous bases or merge distinct FASTA records.
9. **Modularity:** Keep parsing separate from genome statistics (M3.2) and Streamlit presentation (M3.4).

## Current Coding Progress
Initial attempt:

```python
def parse_fasta(file):
    record = []
    currentRecord = []
    lastLine = False
```

Initial loop attempt:

```python
for temp in file:
    if file.startsWith(">"):
        continue
```

Agreed state-variable design (not yet a completed parser):

```python
records = []
current_id = None
sequence_lines = []
```

## Next Steps
- [ ] Write the file-reading loop and correctly detect header lines.
- [ ] Extract the sequence identifier from each header.
- [ ] Collect, normalize, and validate sequence lines.
- [ ] Finalize records on a new header and at end of file.
- [ ] Handle malformed headers, empty sequences, and invalid characters with informative errors.
- [ ] Return structured records and relevant ambiguity/quality notes.
- [ ] Add automated tests under M3.3 once parser behavior is implemented.

## Research Reflection
Preserving original sequence positions, including ambiguous bases, protects genome-length accuracy and supports later statistics and ML work. Explicit validation failures are preferable to silently changing scientific input.

---
*Living lab note: update with actual code, tests, discoveries, and problems as implementation progresses.*
