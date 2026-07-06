# Report-to-Paper Rewrites

Use this when a draft sounds like a work report, lab note, code log, or meeting summary.

## Diagnosis

Report-like prose often:

- uses figure numbers as the subject
- lists operations in chronological order
- exposes internal names and paths
- says "we tested" before saying why the test matters
- mixes setup, result, interpretation, and boundary in one paragraph
- gives many numbers without a claim

## Rewrite Pattern

Report style:

> Figure X compares A, B and C. We used dataset D. The result is ...

Paper style:

> Method A improved [claim] under [condition]. On dataset D, A achieved [metric], compared with B and C. This isolates [interpretation/boundary].

## Sentence Moves

| Report move | Paper move |
|---|---|
| "Figure X shows..." | "This comparison shows..." |
| "We then tested..." | "To determine whether..." |
| "Here we use..." | "The evaluation used..." |
| "This figure is used to..." | delete or move to caption |
| "The data came from..." | "The evidence was evaluated on..." |
| "It can be seen that..." | state the observation directly |

## Paragraph Jobs

One paragraph should usually do one job:

- setup
- result
- comparison
- mechanism/interpretation
- limitation

If a paragraph explains experimental setup and interprets meaning, split it.

## Results vs Discussion

Results:

- "achieved"
- "decreased"
- "increased"
- "remained"
- "was lower/higher than"

Discussion:

- "suggests"
- "may reflect"
- "is consistent with"
- "does not imply"
- "is limited by"

## Before/After Mini Example

Before:

> Figure 4 compares fixed initialization and NN initialization. The fixed initialization has 376/500 status-code-0 cases, and NN has 500/500 accepted cases.

After:

> Learned initial states expanded the local convergence basin of hard projection. In 500 interpolation samples, fixed initialization produced 376 strictly converged projections, whereas learned initialization produced 500 accepted projections.

## Keep Boundaries Visible

Do not turn a bounded result into a universal claim. If a baseline is stronger under a condition, say so. If a projection is local, do not imply global optimality.
