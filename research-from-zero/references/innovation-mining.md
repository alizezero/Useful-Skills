# Innovation Mining

Use this after project intake and before locking the manuscript outline.

## Core Rule

Mine novelty from evidence. Do not decide the story first and then search for convenient support.

## Inspection Targets

Look for innovation candidates in:

- project goals and unresolved pain points
- methods, constraints, data pipelines, solvers, and model interfaces
- baseline comparisons, ablations, stress tests, and failure analyses
- figures, source-data CSVs, logs, checkpoints, and evaluation scripts
- manuscript drafts, meeting notes, task-state files, and reviewer notes

## Innovation Candidate Types

| Type | What to Look For | Example Wording |
|---|---|---|
| Problem framing | difficult or under-served task made actionable | "target-directed regulation from product specifications" |
| Method composition | modules combined into a reproducible workflow | "learning plus hard projection rather than raw neural output" |
| Constraint handling | physical, numerical, or domain constraints made enforceable | "hard feasibility layer with scaled nonlinear projection" |
| Data/evidence basis | new benchmark, curated dataset, or projection-completed corpus | "physically accepted training/evaluation basis" |
| Ablation/mechanism | isolated reason a component matters | "warm-start residual reduction improves projection entry" |
| Boundary insight | honest failure mode or operating regime | "projection success is not determined only by initial residual magnitude" |
| Application proof | demanding case where workflow closes the loop | "steady-state LLDPE product recovery proof-of-case" |

## Output Table

Produce this before writing the outline:

| Candidate innovation | Evidence found | Literature-gap status | Evidence missing | Strength | Overclaiming risk | Manuscript role |
|---|---|---|---|---|---|---|
| one bounded claim | files, figures, metrics, logs | verified/plausible/unverified/not a gap | needed baseline/figure/data | high/medium/low | risk and mitigation | title/abstract/intro/results/SI |

## Strength Labels

- **High**: supported by matched comparison, quantitative result, source data, and clear boundary.
- **Medium**: supported by quantitative evidence but missing a baseline, ablation, or stress test.
- **Low**: plausible from project design or partial result, but not yet enough for a main claim.

## Decision Rules

- Promote high-strength candidates to main-paper claims.
- Use medium-strength candidates as bounded secondary claims or SI-supported evidence.
- Keep low-strength candidates as missing-evidence items, future work, or experiments to run.
- If a candidate needs a figure/table and source data exist, route to `figure-data-generation.md`.
- If no source data exist, mark `[Evidence needed: ...]` and propose the computation or experiment.
- If claiming external novelty or literature gap, run the novelty-verification hook before calling it novel.

## Literature-Gap / Novelty-Verification Hook

Use this when the candidate contribution depends on being new relative to prior work, not only new inside the project.

1. State the exact novelty claim in one sentence.
2. Identify method family, application domain, baseline family, and nearest-neighbor prior-work terms.
3. Search directly or generate a controlled literature prompt using `external-prompts.md`.
4. Classify support as:
   - **verified gap**: matched prior work checked and the gap remains.
   - **plausible gap**: preliminary search supports the gap, but citation audit is incomplete.
   - **unverified gap**: no literature check yet; do not state as novelty.
   - **not a gap**: prior work already does it; reframe as application, integration, benchmark, or evidence contribution.
5. Record citations or search notes in the innovation table.

## Anti-Patterns

- Calling a workflow "novel" because it has many modules.
- Treating an internal engineering name as a contribution.
- Claiming global optimality, generality, or mechanism from local or case-specific evidence.
- Hiding a stronger baseline or a failed extrapolation.
- Creating figures that decorate the story but do not test the innovation claim.

## Minimal Diagnosis Template

```markdown
## Innovation Diagnosis

Recommended main contribution:
- ...

Secondary contributions:
- ...

Claims not yet safe:
- [Evidence needed: ...]

Most important figure/table gap:
- ...
```
