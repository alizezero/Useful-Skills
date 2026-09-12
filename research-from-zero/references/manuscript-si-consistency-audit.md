# Manuscript and SI Consistency Audit

Use this for final checks, "is everything synchronized?", source-data alignment, figure/table renumbering, or after any major figure, table, experiment, or route change. The audit should find contradictions before a reviewer does.

## Audit Inputs

Identify the active files first:

- main manuscript;
- Supplementary Information;
- feedback notes still in scope;
- figure/media directory;
- source-data directory;
- plotting/table scripts;
- release repository or code/data package, if linked.

Do not audit stale drafts unless the user asks for a cross-version comparison.

## Core Checks

### 1. Storyline and Claim Consistency

- Abstract, introduction contributions, results section, discussion, and conclusion must describe the same main claim.
- Each results subsection should answer one question and name its evidence.
- Limitations should match what the results actually tested.
- Exploratory experiments should not appear as settled manuscript evidence unless approved.

### 2. Figure and Table Consistency

For every figure and table:

- file exists in the referenced media path;
- caption matches plotted panels, axes, sample set, metric, and route names;
- prose statements match the figure/table values;
- source-data file names in SI match actual files;
- figure/table numbering is continuous and cross-references point to the right item;
- legends do not mention removed visual elements;
- old representative samples, route names, or normalization schemes are not left in text.

### 3. Number Traceability

For every important number in the abstract, results, discussion, or conclusion:

| Number | Location | Meaning | Source file/script | Recomputed? | Status |
|---|---|---|---|---|---|

If a number cannot be traced, mark it as `source needed` instead of retaining it as a claim.

### 4. Main Text to SI Support

Check that each main-text claim has appropriate SI support:

- method details for nontrivial algorithms or solvers;
- dataset definitions and sample counts;
- variable definitions and units;
- hyperparameters and training/evaluation protocols;
- source-data cards for main figures;
- supplementary tables for extended metrics.

SI should follow the evidence order of the main text unless there is a strong reason not to.

### 5. Terminology and Old-Version Search

Build a short search list from the project history:

- old model names;
- old sample IDs;
- old figure/table numbers;
- old route counts;
- old inputs or removed variables;
- old metric definitions;
- internal run names and temporary filenames.

Search manually and judge each hit. Do not replace mechanically when a term is still valid in a provenance table or historical note.

### 6. Repository Alignment

If the manuscript references a code/data repository:

- public paths in SI exist in the repository;
- README commands match actual scripts;
- source-data files and generated figures are current;
- manifests or frozen metrics are updated after file changes;
- fresh clone validation has been run if the user requested release readiness.

## Output Format

Use a concise audit table:

| Area | Finding | Severity | File/location | Action |
|---|---|---:|---|---|

Severity guide:

- **High**: contradiction, wrong number, missing source data, broken figure/table reference, wrong method claim.
- **Medium**: unclear wording, missing SI support, stale but nonfatal terminology, incomplete provenance.
- **Low**: style, readability, redundant wording, optional cleanup.

End with:

- `Ready`: no high/medium issues remain;
- `Conditionally ready`: only listed minor items remain;
- `Not ready`: high/medium issues require action.

