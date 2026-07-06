# Supplementary Information

Use this when a project-to-paper task includes detailed methods, variable tables, datasets, ablations, diagnostics, extra figures, source-data notes, or provenance that should support but not overload the main text.

## Core Rule

Supplementary Information is evidence architecture. It should make the main claims more verifiable, not hide weak logic or collect unused project artifacts.

## Main-Text/SI Split

| Content | Main Text | Supplementary Information |
|---|---|---|
| Core innovation claim | concise statement and key evidence | detailed derivation, extra diagnostics |
| Essential method | workflow, assumptions, module roles | implementation details, variable tables, solver settings |
| Main comparison | decisive metric and matched baseline | extended metrics, sensitivity, robustness |
| Ablation | claim-critical ablation | exhaustive variants or secondary ablations |
| Failure mode | boundary that changes interpretation | detailed cases, extra examples, provenance |
| Dataset | sample design and evaluation protocol | full variable list, filters, source-data provenance |
| Figure | claim-carrying visual | sanity checks, repeated panels, debug-style evidence |

## SI Architecture

Build SI as a support document with section jobs:

1. **Supplementary Methods**
   - define variables, equations, algorithms, solver/projection settings, training details, and reproducibility notes.
2. **Supplementary Data and Evaluation Sets**
   - document datasets, sample counts, filters, accepted/excluded cases, and source-data locations.
3. **Supplementary Figures**
   - include diagnostics, ablations, boundary checks, and extended visual evidence.
4. **Supplementary Tables**
   - include variable definitions, hyperparameters, metrics, per-case summaries, and provenance.
5. **Supplementary Notes**
   - explain limitations, numerical details, or implementation caveats too detailed for the main text.

Use only sections that are needed. Do not create empty SI sections.

## Cross-Reference Consistency

Run a provisional check during the initial main-text/SI split, then repeat a final check after terminology cleanup, claim-evidence mapping, and section architecture. Before final drafting, check:

- every main-text "Supplementary Fig./Table/Note" reference has a matching SI item
- every SI item is referenced from the main text or clearly supports reproducibility
- numbering is sequential within each SI type
- captions define dataset, metric, comparison, conclusion, and boundary
- terminology matches the main manuscript ledger
- SI does not introduce stronger claims than the main text

## SI Rewrite Rules

- Rewrite work-log details into reproducibility prose.
- Keep internal paths, run names, and checkpoints only when needed for traceability; otherwise convert them to role-based terms.
- Preserve exact numeric values and sample counts.
- Put local provenance in tables or notes, not in narrative paragraphs.
- Do not use SI to bury failed baselines that affect the main claim. If a baseline changes interpretation, mention it in the main text.

## Output Templates

### Main-Text/SI Split Table

| Claim or evidence item | Main-text role | SI support | Source artifact | Status |
|---|---|---|---|---|
| bounded claim | paragraph/Fig/Table | Fig. Sx/Table Sx/Note Sx | path | supported/needs work |

### SI Item Plan

| SI item | Purpose | Source data/script | Main-text anchor | Risk |
|---|---|---|---|---|
| Fig. Sx | diagnostic/ablation/provenance | path | Section/Fig/Table | overinterpretation or missing data |

## When SI Data Are Missing

Use explicit labels:

- `[SI evidence needed: complete variable table]`
- `[SI evidence needed: source data for Fig. Sx]`
- `[SI evidence needed: matched ablation details]`
- `[Boundary: SI diagnostic only, not main evidence]`

## Final SI Audit

Return a short audit before finalizing:

- main-text claims with SI backup
- SI items without clear purpose
- cross-reference mismatches
- terminology mismatches
- evidence that should move from SI to main text
- evidence that should move from main text to SI
- SI figures/tables whose scripts or source-data outputs have not been verified
