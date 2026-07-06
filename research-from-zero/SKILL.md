---
name: research-from-zero
description: Full-process research manuscript coach for turning an existing engineering or research project folder into a paper. Use when the user gives a project directory, code/data/results/figures/notes, or says to write a paper/manuscript/journal article from project materials; also use for innovation mining, novelty planning, manuscript diagnosis, missing-evidence detection, data-backed figure/table generation, main-text/SI planning, supplementary information rewriting, terminology cleanup, claim-evidence-figure mapping, report-to-paper rewriting, section drafting, and controlled GPT/DeepResearch prompts.
---

# Research From Zero

Turn an existing project folder into a manuscript. This skill is not a copy editor first; it is a project-to-paper workflow. Start by understanding what the project did, then decide what paper can honestly be written from it, mine publishable innovation candidates, locate missing evidence, generate data-backed figure/table support when possible, and only then build the outline, evidence chain, terminology, figures, and sections.

## Operating Principles

- Inspect the project before writing. If the user provides a folder, read its structure, README, notes, scripts, outputs, figures, tables, and manuscript drafts before proposing the paper.
- Do not invent results, mechanisms, references, baselines, or novelty. Mark missing evidence explicitly.
- Mine innovation from evidence, not from preferred storylines. A candidate novelty claim must name its supporting artifacts and its missing evidence.
- Generate new figures/tables only from existing data, logs, source data, model outputs, or reproducible scripts. Never fabricate data to make an innovation point work.
- Treat internal engineering names as draft artifacts, not paper terminology. Always build a terminology ledger before final rewriting.
- Treat figures as evidence, not decoration. Every main-text figure must support a claim.
- Treat Supplementary Information as part of the evidence system, not as a dumping ground for leftovers.
- Default output is Markdown. Convert to Word or LaTeX only when the user requests or the target journal workflow requires it.
- Use a coach-plus-executor style: diagnose and propose a structure first; once the user approves, edit files, draft sections, generate figure plans, or write prompts.

## Default Workflow

1. **Project Intake**
   - Inspect the provided folder and summarize what was built, what artifacts exist, and what evidence is already available.
   - Read `references/project-intake.md` when the user gives a folder or a scattered project.

2. **Manuscript Diagnosis**
   - Identify the paper type, target journal, audience, core claim, available evidence, missing evidence, and boundaries.
   - If the target journal is unknown, ask for it or state assumptions.

3. **Innovation Mining**
   - Mandatory before outline locking. Infer candidate innovation points from the project artifacts, not from generic claims.
   - Read `references/innovation-mining.md`.
   - Produce an innovation table with candidate claim, supporting evidence, missing evidence, publishability strength, overclaiming risk, and recommended manuscript location.

4. **Evidence and Figure/Table Gap Planning**
   - Mandatory after innovation mining and before Results drafting.
   - Read `references/evidence-chain.md` and `references/figure-data-generation.md`.
   - If a claim needs a figure/table, first locate existing source data. Optionally run `scripts/inventory_project_evidence.py <project-folder>` to find candidate CSV, JSON, log, figure, and manuscript artifacts.
   - If data exist, write or revise project-local scripts to extract metrics, create source-data CSVs, and export publication-ready figures/tables.
   - If data do not exist, mark `[Evidence needed: ...]` and propose the missing experiment or computation instead of fabricating support.

5. **Initial Main-Text/SI Split**
   - Mandatory before final section architecture when the project has many methods, variables, datasets, ablations, diagnostics, or provenance artifacts.
   - Read `references/supplementary-information.md`.
   - Decide the provisional main-text versus Supplementary Information role for each evidence item. Re-check this split after terminology cleanup and the final claim-evidence map.

6. **Terminology Cleanup**
   - Mandatory before final drafting. Detect internal version names, script names, checkpoint names, dataset nicknames, solver-status jargon, and temporary figure names.
   - Read `references/terminology-cleanup.md`.
   - Optionally run `scripts/scan_manuscript_terms.py <path>` on manuscript files or project notes.

7. **Claim-Evidence-Figure Map**
   - Mandatory before Results/Discussion drafting. Map each subsection claim to datasets, metrics, figures, tables, baselines, ablations, and SI support.
   - Read `references/evidence-chain.md`.

8. **Section Architecture**
   - Convert the project into a paper outline. Decide what each section is responsible for before writing prose.
   - Read `references/section-playbooks.md`.

9. **Final Main/SI and Evidence Consistency Pass**
   - Revisit `references/supplementary-information.md` after terminology cleanup, claim-evidence mapping, and section architecture.
   - Verify main-text/SI cross-references, numbering, terminology, SI backup for main claims, and whether any evidence should move between main text and SI.

10. **Draft or Rewrite Sections**
   - Draft from claim and evidence outward. Do not begin with a list of experiments.
   - For report-like text, read `references/report-to-paper-rewrites.md`.

11. **External Prompt Generation**
   - When literature search, English polishing, DeepResearch, or external GPT rewriting is useful, generate controlled prompts that preserve claims, numbers, boundaries, and terminology.
   - Read `references/external-prompts.md`.

12. **Output Packing**
   - Keep source documents, figure paths, evidence tables, and rewrite notes traceable.
   - Default deliverables: manuscript Markdown, innovation table, main-text/SI split plan, final main/SI consistency audit, SI outline or rewrite notes, terminology ledger, claim-evidence-figure map, figure/table source-data paths, figure-generation notes, missing-evidence list, and external prompts.

## First Response Pattern

When the user says "write this project into a paper" and gives a folder:

1. State that you will first inspect the project rather than draft immediately.
2. Ask only for target journal/article type if not discoverable.
3. Inspect files with fast search/listing tools.
4. Return a compact project-to-paper diagnosis:
   - what the project appears to have done
   - likely paper claim and innovation candidates
   - available evidence
   - missing evidence and whether it can be generated from existing data
   - main-text/SI split opportunities
   - likely paper structure
   - next action

## Rewriting Rules

- Replace "we did X test / Figure X shows" with "This result demonstrates/limits/isolates X" when evidence supports it.
- Keep figure and table references, but do not make them the grammatical subject unless the sentence is a caption or navigation sentence.
- Separate Results from Discussion: Results report what was observed; Discussion interprets meaning and limits.
- Preserve exact numeric values unless the user asks to update them from source data.
- If a result is stronger than the evidence supports, soften the claim rather than hiding the limitation.

## Figure/Data Generation Rules

- Generate support figures only after naming the claim they support.
- Prefer project-local, reproducible scripts over ad hoc spreadsheet editing.
- Save source-data CSVs beside generated figures whenever practical.
- Run generated or revised figure/table scripts and verify that source-data and figure/table outputs exist before treating them as evidence.
- Captions must state dataset, metric, comparison, conclusion, and boundary.
- If source data are absent, produce a missing-evidence item or experiment plan instead of a figure.
- Treat `scripts/inventory_project_evidence.py` as a non-interpretive file finder. It does not assign paper role, evidence strength, novelty, or confidence.

## Resource Guide

- `references/project-intake.md`: how to inspect project folders and reconstruct what was done.
- `references/innovation-mining.md`: how to mine defensible innovation candidates from existing project evidence.
- `references/figure-data-generation.md`: how to turn claim gaps into data-backed figures/tables without fabricating evidence.
- `references/supplementary-information.md`: how to plan and rewrite SI as traceable support for the main text.
- `references/terminology-cleanup.md`: how to turn engineering names into publication terms.
- `references/evidence-chain.md`: claim-evidence-figure mapping and figure/SI decisions.
- `references/section-playbooks.md`: section jobs from title to conclusion.
- `references/report-to-paper-rewrites.md`: templates for converting report prose into manuscript prose.
- `references/external-prompts.md`: controlled prompts for GPT/DeepResearch/language polish.
- `scripts/scan_manuscript_terms.py`: flags likely internal names and report-like phrases in manuscripts.
- `scripts/inventory_project_evidence.py`: inventories candidate evidence files and lightweight metadata for figure/table planning.
