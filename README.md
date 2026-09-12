# Useful Skills

This repository collects reusable Codex skills for research, writing, and project-to-paper workflows.

## Skills

### research-from-zero

`research-from-zero` is a full-process research manuscript coach. It is designed for situations where you already have an engineering or research project folder, including code, data, figures, notes, experiment logs, source-data files, and draft documents, and want to turn those materials into a structured manuscript.

It helps with:

- inspecting a project folder and reconstructing what the project did
- identifying the paper type, target journal, core claim, evidence, missing evidence, and boundaries
- mining defensible innovation candidates from project artifacts
- checking whether external literature-gap or novelty verification is still needed
- locating missing figure/table evidence and generating data-backed figure plans from existing data, logs, model outputs, or reproducible scripts
- cleaning internal project names, checkpoint names, dataset nicknames, solver-status jargon, and script-style terminology
- building a claim-evidence-figure map before drafting Results and Discussion
- splitting evidence between the main text and Supplementary Information
- running a final main-text/SI consistency pass for numbering, cross-references, terminology, and evidence support
- triaging advisor/reviewer feedback into prose edits, figure redraws, table updates, missing experiments, SI synchronization, release-repository updates, or discussion-only exploratory ideas
- preparing and auditing a GitHub/code-data release repository so a fresh clone can reproduce the manuscript-linked outputs
- assembling a final submission package with the current main text, SI, figures, source data, repository link, and required handoff notes
- designing the manuscript outline from project artifacts
- converting report-style writing into manuscript-style writing
- generating controlled prompts for GPT, DeepResearch, reviewer-style audit, or language polishing tools
- preparing Markdown-first manuscript drafts, with optional later conversion to Word or LaTeX

The skill is especially useful when a project has many scattered outputs and the main challenge is not simply polishing language, but deciding what paper can honestly be written from the available evidence.

## Current Contents

At the moment, this repository contains one skill:

| Skill | Purpose |
|---|---|
| `research-from-zero` | Turn an existing research or engineering project folder into a manuscript plan, innovation table, evidence map, figure/table plan, SI structure, draft paper, release repository audit, and final submission package checklist. |

## Included Resources

```text
research-from-zero/
  SKILL.md
  agents/
    openai.yaml
  references/
    project-intake.md
    innovation-mining.md
    evidence-chain.md
    figure-data-generation.md
    supplementary-information.md
    feedback-to-revision-workflow.md
    manuscript-si-consistency-audit.md
    terminology-cleanup.md
    section-playbooks.md
    report-to-paper-rewrites.md
    release-repository-management.md
    final-submission-package.md
    external-prompts.md
  scripts/
    inventory_project_evidence.py
    scan_manuscript_terms.py
```

## Helper Scripts

`inventory_project_evidence.py` lists candidate project evidence files such as CSV, TSV, JSON, logs, figures, text drafts, and analysis scripts. It is intentionally non-interpretive: it does not decide paper role, evidence strength, novelty, or confidence.

```bash
python scripts/inventory_project_evidence.py /path/to/project --limit 200
```

`scan_manuscript_terms.py` scans manuscript text for internal names, local paths, run stamps, solver-status jargon, and report-like phrasing.

```bash
python scripts/scan_manuscript_terms.py /path/to/manuscript-or-folder
```

## What This Version Adds

- Feedback items are handled through a register before editing, so exploratory ideas are not accidentally written into the paper as settled results.
- Main text, SI, captions, figures, source data, and repository files are checked as one evidence system before final handoff.
- GitHub release repositories are treated as part of the manuscript deliverable: public files should be clean, traceable, runnable after clone, and aligned with the reported figures/tables.
- Final package preparation now checks current-version files, figure/media availability, source-data coverage, code/data links, and missing declarations.

## Evidence Rules

- Do not invent results, mechanisms, references, baselines, or novelty.
- Generate figures and tables only from existing evidence or reproducible project computations.
- Run generated or revised figure/table scripts and verify source-data and output files before treating them as evidence.
- Mark missing evidence explicitly instead of writing around it.
- Preserve exact numeric values unless recomputing from documented source data.
- Treat Supplementary Information as part of the evidence system, not as a dumping ground for leftovers.
- Keep final claims, figures, source data, SI support, and release-repository contents aligned before declaring a manuscript package ready.

## Usage

Copy the skill folder into your Codex skills directory, then restart Codex so the skill is discovered.

Invoke it with:

```text
Use $research-from-zero to inspect this project, mine defensible innovation points, fill figure/table evidence gaps from existing data where possible, split main text versus SI support, audit manuscript/SI/source-data consistency, prepare the release repository, and build a manuscript plan and draft.
```

## Upload Notes

The repository should contain only source files:

```text
.gitignore
SKILL.md
agents/openai.yaml
references/*.md
scripts/*.py
```

Do not upload local caches, environment files, logs, compiled Python files, or private project handoff files.
