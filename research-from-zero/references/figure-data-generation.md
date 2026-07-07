# Figure and Data Generation

Use this when an innovation candidate or Results claim needs missing figure/table support.

## Non-Negotiable Boundary

Generate figures from existing evidence only: source-data CSVs, raw data files, logs, JSON summaries, model outputs, checkpoints, or reproducible project scripts. Never fabricate data or invent numeric results.

## Workflow

1. **Name the claim**
   - Write the exact manuscript claim the figure/table should support.
   - State the dataset, metric, baseline, condition, and expected boundary.

2. **Locate evidence sources**
   - Search project folders for source data, logs, summaries, notebooks, plotting scripts, and generated figures.
   - Optionally run `scripts/inventory_project_evidence.py <project-folder>` to create a first-pass inventory.
   - Treat the inventory as non-interpretive. It finds candidate files; it does not decide paper role, evidence strength, novelty, or confidence.
   - Prefer source data over screenshots or final-only images.

3. **Decide whether the figure is possible**
   - Possible: source data or reproducible raw outputs exist.
   - Partly possible: some panels can be generated, but a baseline/condition is missing.
   - Not possible: no source data or computation path exists.

4. **Write a project-local script**
   - Put task-specific scripts near the manuscript or figure-output folder, not inside the skill.
   - Read structured data with pandas/csv/json/parquet APIs rather than manual string parsing when available.
   - Export source-data CSVs for plotted values.
   - Export publication-useful formats: SVG/PDF for vector plots and PNG/TIFF for previews or journal requests.

5. **Run and verify**
   - Run the generated or revised script.
   - Verify that every declared source-data CSV and figure/table file exists.
   - Open or inspect source-data dimensions, sample counts, key columns, and metric ranges.
   - For image outputs, verify file size is nonzero and the visual content is not blank, mislabeled, or based on the wrong dataset.
   - If verification fails, fix the data/script path or mark the item as `[Evidence needed: ...]`.

6. **Document the evidence**
   - Record input paths, output paths, metrics, filters, sample counts, and any exclusions.
   - Draft a caption that states comparison, dataset, metric, conclusion, and boundary.
   - Update the claim-evidence-figure map.

## Output Checklist

For every generated figure/table, provide:

- claim supported
- input data paths
- script path
- source-data CSV path
- figure/table output paths
- verification command and result
- metric definitions and sample counts
- caption draft
- boundary or overinterpretation warning

## When Data Are Missing

Do not produce a placeholder figure that looks evidential. Instead write:

```markdown
[Evidence needed: <specific missing data or computation>]
Required source:
Required metric:
Required comparison:
Suggested script or experiment:
Manuscript claim affected:
```

## Figure Planning Template

| Claim | Needed panel/table | Existing source data | Script action | Output | Status |
|---|---|---|---|---|---|
| bounded claim | panel A/B/table | path or missing | extract/recompute/plot | source CSV + figure | supported/partial/needed |

## Script Expectations

- Use clear CLI arguments or top-level path constants.
- Fail loudly when required input files are missing.
- Keep transformations traceable and avoid hidden manual edits.
- Preserve exact numeric values from sources unless recomputing with documented formulas.
- Avoid style work until the data logic is correct.
- Do not call a generated figure "supported" until the script has run and outputs have been checked.

## Common Figure Types

| Need | Useful Figure/Table |
|---|---|
| method beats baseline | matched bar/point plot with metric and uncertainty if available |
| constraint satisfaction | residual or violation distribution before/after projection |
| ablation | grouped bars or line plot across variants under same protocol |
| boundary/failure mode | success/failure counts, residual tails, or stratified metrics |
| workflow evidence | compact module-chain schematic plus quantitative panels |
| dataset basis | sample coverage, status counts, validity summary, provenance table |
