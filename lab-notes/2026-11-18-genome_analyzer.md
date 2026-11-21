# M3.2 — Genome Analyzer: Lab Notes

**Initialization Date:** 2026-11-19
**Updated Date:** 2026-11-20
**Project:** BHAGE
**Milestone:** M3 — Genome Analysis
**Task:** M3.2 — Nucleotide Counting and Genome Statistics (#12)
**Status:** Complete

## Program / Task
`bhage/genome_analyzer.py` — `analyze_genome(parsed_record)` 

## Goal
Build a reusable genome analyzer uses validated DNA sequences, including genome length, nucleotide composition, GC content, and ambiguous nucleotide counts to calculate essential statistics. Return said structured analysis results independently of Streamlit to support downstream analysis and machine learning.


## 30 Second Session Observation 

- Different ways to structure a dictionary.
- Function Modularity vs Multi-Feature Function
- Saving dictionary / nested dictionary values using the key and index number.


## What Worked

- Seperating the functions into specific tasks.
- Using previously learned knowledge about looping through a string to successfully count nucleotides.
- Calculating genome length using len().
- Calculating nucleotide count using a for in loop containing with an if statement.
- Calculating GC content using nucleotide count, taking its sum, then dividing guanine / cytosine sum by total nucleotide count. Note: I chose to use a variable instead of .sum() and .values() for capturing the 4 main nucleotide bases, as if any other bases are added the GC content calculation will be impacted.
- Calculating ambiguity by first grabbing known genome length, and nucleotide count. Then, using sum() and .values() method to add up the nucleotide counts. Then subtracting said counts from the genome length. sum(nucleotide_count.values()) works because the dictionary currently contains only confirmed A, T, G, and C nucleotides. Adding ambiguous nucleotide categories would require revising this calculation.
- Setting up analyze_genome function as a "coordinator" to create the analysis_result record for each parsed_record.


## What Didn't Work

- Error occurs when total number of confirmed nucleotides were zero, thus causing the division to be by zero. 
- Incorrect f string syntax when trying to apply the "%" sign to the rounded percentage.


## What I Learned

- Using sum() in combination with .values() dictionary method to calculate known counts.
- Neater syntax for dictionaries.
- Importance of distinguishing a GC percentage of 0% from an undefined GC percentage caused by zero confirmed nucleotides.


## Scientific Decisions
- Seperate responsibilities of functions rather than having a multi-purpose function that handles all.
- Future ML pipeline most likely should not use a completely ambiguous genome for host prediction, as it has no confirmed nucleotide-composition information.
- Return None when GC percentage is undefined because no confirmed nucleotides are present, instead of incorrect reporting 0%.
- Store percentages as numeric values without formatting, which occurs downstream.
- Return structured analysis results, including genome identifiers and ambiguity statistics.


## Testing Results

| Test | Result |
| Normal sequence of DNA | Passed|
| Pure ambigious nucleotide sequence | Passed |


**Final result:** 2/2 manual tests passed.

## Next Steps

- [x] Calculate total genome length.
- [x] Implement nucleotide counting.
- [x] Calculate GC content using a documented denominator.
- [x] Handle ambiguous nucleotides consistently.
- [x] Return structured analysis results, including genome identifiers and quality notes.
- [x] Verify normal and ambiguous DNA sequences.
- [x] Document numerical edge cases.
- [ ] M3.3 - Write automated tests for Genome Analysis.