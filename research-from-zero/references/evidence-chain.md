# Claim-Evidence-Figure Map

Use this before writing Results/Discussion or deciding which figures belong in the main text.

## Core Principle

Do not ask "what figures do we have?" first. Ask "what claims must the paper prove?" Then assign evidence and figures.

## Evidence Ladder

For method/system papers:

1. Problem setup and data basis.
2. Main workflow result.
3. Baseline comparison under matched conditions.
4. Ablation or mechanism isolation.
5. Boundary, failure mode, or cost analysis.
6. Case-level interpretation or practical implication.

## Map Template

| Section | Claim | Evidence | Main figure/table | SI support | Status |
|---|---|---|---|---|---|
| 4.1 | data basis is physically valid | residual acceptance, sampling design | Fig. 2/Table 1 | SI data provenance | supported/needs work |
| 4.2 | module improves closure | comparison/ablation | Fig. 3 | SI logs | supported/needs work |

## Figure Decision Rules

Main-text figures should:

- support a claim a reader must believe
- be interpretable without reading code provenance
- avoid duplicating another main figure
- compare methods only under a clear common protocol
- include enough labels to understand axes, metrics, and sample sets

Move to SI when:

- the figure is provenance, sanity check, or exhaustive detail
- it repeats a main-text conclusion
- it is only useful for debugging
- it shows an implementation detail that distracts from the argument

## Caption Requirements

Every caption should state:

- what is compared
- on which dataset/problem set
- what metric is shown
- what visual marks mean
- what conclusion the figure supports
- what the figure does not imply, if overinterpretation is likely

## Missing Evidence Labels

Use explicit labels instead of writing around gaps:

- `[Evidence needed: baseline under same projection cost]`
- `[Evidence needed: source data for Fig. X]`
- `[Evidence needed: stress test outside interpolation range]`
- `[Boundary: local projection only, no global optimality claim]`
