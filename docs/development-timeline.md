# BHAGE — Development Timeline

**Planning baseline:** November 9, 2026

These are proposed target dates, not confirmed completion dates. Milestones must satisfy scientific and engineering acceptance criteria before being marked complete.

| Milestone | Target period | Target completion | Status |
| --- | --- | --- | --- |
| M1 — Repository Foundation | October 2026 | Completed | Complete |
| M2 — Streamlit Dashboard | October–November 2026 | Completed | Complete |
| M3 — Genome Analysis | November 9–30, 2026 | November 30, 2026 | In progress |
| M4 — Host Prediction v0.1 | December 1–31, 2026 | December 31, 2026 | Planned |
| M5 — Advanced ML Features | January 1–15, 2027 | **January 15, 2027** | Planned |
| M6 — Scientific Research Engine | February–March 2027 | March 31, 2027 | Provisional |
| M7 — AI Research Assistant v0.1 | April–May 2027 | May 31, 2027 | Provisional |
| M8 — Expanded Phage Research | June–July 2027 | July 31, 2027 | Provisional |
| M9 — Integrated Research & Discovery | August 2027 | August 31, 2027 | Provisional |

## M3.1 — FASTA Parsing & Validation

**Progress as of November 11, 2026:** In progress — 2 of 5 planned work sessions completed. Target: November 14, 2026.

| Session | Scope | Status |
| --- | --- | --- |
| Day 1 | Multi-record parsing: save previous record, reset sequence collection, save final record, guard against saving a missing identifier | Complete |
| Day 2 | Strip surrounding whitespace, uppercase DNA, join sequence lines, return structured records | Complete |
| Day 3 | Header and nucleotide validation, including malformed records | Pending |
| Day 4 | Error handling and empty-input/empty-sequence behavior | Pending |
| Day 5 | Automated tests, edge cases, and refinement | Pending |

**Verification:** On November 11, the parser successfully returned all three expected normalized genome records from `tests/fixtures/test_normalization.fasta`. This manual test covers multi-record separation, case normalization, sequence joining, and final-record saving. Full validation and edge-case testing remain outstanding.

**Next:** Complete M3.1 validation before starting M3.2 — Nucleotide Counting & GC Content.

## Milestone outcomes

- **M3:** FASTA parsing, genome statistics, tests, and Streamlit integration.
- **M4:** First supervised host-genus prediction baseline, with evaluation and limitations documented.
- **M5:** Expanded genomic features, k-mers, and comparison of ML approaches, potentially including PyTorch.
- **M6:** Reusable scientific research tools, provenance, and experiment tracking.
- **M7:** Researcher-supervised conversational AI prototype connected to scientific tools.
- **M8:** Add and evaluate another phage research capability.
- **M9:** Integrate capabilities for evidence synthesis and testable research hypotheses.

**Schedule risk:** The January 15 M5 target is ambitious, especially if M4 dataset curation and validation take longer than planned. Reassess dates when the evidence warrants it.
