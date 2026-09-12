# Feedback to Revision Workflow

Use this when a draft already exists and the user provides advisor notes, reviewer comments, dated feedback files, margin comments, or informal revision instructions. The goal is to convert feedback into controlled manuscript changes without mixing discussion, experiments, and text edits.

## First Step: Build a Feedback Register

Do not edit immediately unless the feedback is trivial. Extract each actionable item into a register:

| ID | Source | Feedback item | Type | Affected files | Evidence needed | Decision | Status |
|---|---|---|---|---|---|---|---|
| F1 | file/comment | exact issue | text/figure/table/experiment/SI/repo/discuss | paths | data/script/user input | apply/defer/reject/ask | open/done |

Preserve the user's wording when possible. If feedback is ambiguous, write the two plausible interpretations and choose the one that best fits the manuscript evidence.

## Classification

Classify each item before acting:

- **Prose-only**: wording, logic order, claim strength, terminology, caption wording.
- **Figure redraw**: style, axes, legend, panel selection, sample choice, metric definition, source-data update.
- **Table update**: values, rows, columns, footnotes, route names, test set names.
- **Experiment or computation needed**: new run, rerun, ablation, metric recomputation, source-data extraction.
- **SI synchronization**: methods detail, source-data file list, supplementary table/figure, cross-reference.
- **Release repository update**: public code/data repo, GitHub, manifest, README, clone-run verification.
- **Discussion-only exploratory item**: useful scientific question not yet approved as manuscript evidence.

Do not treat exploratory experiments as manuscript content by default. Label them `exploratory` until the user decides whether they belong in main text, SI, or neither.

## Apply Changes Safely

For each accepted item:

1. Identify the newest manuscript/SI files before editing.
2. Locate all coupled locations: main text, SI, figure, caption, table, source data, scripts, repository docs.
3. If numbers or curves change, update the source table or script first, then the figure/table, then the prose.
4. If a figure changes, check the caption, results paragraph, SI source-data row, and release repository copy.
5. If a table changes, check every sentence that cites the table's numbers.
6. If a term changes, search for old terms and decide case-by-case rather than replacing blindly.

When feedback conflicts with existing evidence, say so explicitly and propose a bounded revision rather than hiding the conflict.

## Version Recovery for Long Projects

When feedback arrives after many revisions:

- Determine the latest main text and SI by filename, timestamp, open editor context, and user statement.
- Identify the active media/source-data directory and the release repository if one exists.
- Search for stale duplicates of the same manuscript and avoid editing old drafts unless the user asks.
- If two files are plausible latest versions, compare key recent changes before editing.

## Output

Report progress as:

```markdown
## Feedback Register
| ID | Type | Decision | Change made | Files touched | Verification |

## Deferred or Needs Input
| ID | Reason | Required input/evidence |
```

For substantial revisions, also produce a short "what changed in the manuscript logic" summary, not only a file list.

