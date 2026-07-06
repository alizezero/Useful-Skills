# Project Intake

Use this when the user provides a project folder, mixed notes, code outputs, or existing drafts.

## Folder Inspection Order

1. List top-level folders and recent files.
2. Read README, task state, project notes, manuscript drafts, figure plans, and review comments first.
3. Inspect code/output folders only enough to identify:
   - what was computed or built
   - which datasets and checkpoints exist
   - which figures/tables already exist
   - which outputs are final versus exploratory
4. Build an artifact inventory before proposing a paper.

## Artifact Inventory Template

| Artifact | Location | What it contains | Paper role | Confidence |
|---|---|---|---|---|
| manuscript draft | path | current text | base draft | high/medium/low |
| figure output | path | result figure | main/SI/candidate | high/medium/low |
| source data | path | plotted values | evidence verification | high/medium/low |
| code/script | path | model/test generation | method/provenance | high/medium/low |

## Paper-Readiness Diagnosis

Return this after intake:

- **What the project did:** 2-5 sentences.
- **Likely paper object:** method, system, dataset, experiment, case study, review, or hybrid.
- **Core claim candidate:** one sentence, bounded by evidence.
- **Evidence already present:** figures, tables, datasets, comparisons, logs.
- **Evidence missing:** baselines, ablations, stress tests, failure modes, literature, source data.
- **Risks:** overclaiming, internal naming, unclear target journal, weak figure logic.
- **Next action:** outline, evidence map, terminology cleanup, or section rewrite.

## Questions to Ask Only If Needed

Ask at most one at a time:

- Target journal or journal family?
- Article type: research article, methods paper, application/case study, communication?
- Is the paper meant to be Chinese draft first, English submission draft, or both?
- Which results are already trusted and which are still exploratory?
