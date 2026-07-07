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

## SI Evidence Pack Workflow

Use this workflow when the main manuscript claims and main figures are mostly fixed, but Supplementary Notes, Supplementary Tables, Supplementary Figures, source data, and provenance are scattered.

1. **Build the main-text to SI support map**
   - For each main-text section, figure, table, and numerical claim, assign the SI Note/Table/Figure or source-data file that supports it.
   - If no support exists, mark `[SI evidence needed: ...]` instead of smoothing over the gap.

2. **Create the SI inventory before rewriting SI prose**
   - List all planned Supplementary Notes, Tables, Figures, Algorithms, and Source Data files.
   - Give each item one job: method detail, dataset definition, metric definition, ablation, boundary check, source data, or provenance.
   - Do not draft narrative SI paragraphs until this inventory exists.

3. **Create source-data cards for every main figure**
   - Each main figure must have a source-data card, even when the plotted CSV is not yet assembled.
   - The card records the main-text claim, panel list, sample set, metric definitions, input files, scripts, output figure path, source-data CSV path, and verification status.

4. **Trace every manuscript number**
   - Any number in the main text or abstract that supports a claim must map to a source table, CSV, log, or reproducible script.
   - Use a number traceability table with columns: `manuscript number`, `location`, `meaning`, `source data`, `script/calculation`, `verification status`.

5. **Separate publication terminology from raw provenance**
   - Main text and ordinary SI prose use canonical manuscript terms only.
   - Raw filenames, checkpoints, run names, internal dataset nicknames, solver-status codes, and directory paths appear only in reproducibility/provenance tables or file inventories.
   - If an internal name must appear, pair it with its publication term.

6. **Draft SI Notes in evidence order**
   - Order SI by the main-text evidence chain, not by experiment chronology or file chronology.
   - A reader should be able to move from a main-text claim to the SI item that verifies it without knowing the project history.

7. **Run the final SI audit**
   - Check cross-references, numbering, terminology, source-data existence, and whether each SI item has a clear main-text anchor or reproducibility purpose.

## Standard SI Note Template

Use this structure for each Supplementary Note unless the note is purely a table caption or short derivation:

```markdown
### Supplementary Note Sx. <Title>

**Purpose.** What this note supports and why it is in SI rather than main text.

**Main-text link.** Section/Figure/Table/claim supported.

**Data, model, or protocol.** Datasets, variables, algorithms, solver settings, training settings, or evaluation protocol.

**Metrics and acceptance criteria.** Metric definitions, units, thresholds, filters, sample counts, and exclusion rules.

**Boundary.** What this note does not imply, especially for local projections, diagnostics, supporting benchmarks, or non-main claims.

**Files and reproducibility.** Source data, scripts, model versions, logs, and output files. Use raw paths here, not in ordinary narrative prose.
```

## Source-Data Card Template

Use one card per main figure or claim-critical SI figure/table.

| Field | Required content |
|---|---|
| Main figure/table | e.g., Fig. 4 |
| Main-text claim supported | Exact bounded claim |
| Panels/metrics | Panel IDs, metrics, units |
| Sample set/problem set | Dataset name, sample count, filters |
| Source data | CSV/JSON/log/model output path or `[SI evidence needed: ...]` |
| Script/calculation | Script path, command, or calculation rule |
| Output files | Figure/table path and source-data CSV path |
| Verification | Exists/checked/recomputed; date if relevant |
| Boundary | What the figure/table must not be used to claim |

## Manuscript Number Traceability Template

Use this for every claim-carrying number in the abstract, Results, and key figure captions.

| Manuscript number | Location | Meaning | Source data/table | Script/calculation | Verification status |
|---|---|---|---|---|---|
| `50/50` | Section 4.3 | product-input closed-loop accepted cases | path/Table Sx | script or rule | checked/needed |

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
