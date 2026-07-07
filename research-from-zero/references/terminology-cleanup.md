# Terminology Cleanup

Use this before final drafting or whenever the text reads like an engineering report.

## Problem

Project folders contain names that are useful during iteration but inappropriate in a paper: checkpoint names, date stamps, script names, status codes, dataset nicknames, local paths, and temporary figure labels. These names make the manuscript look like a work log.

## Mandatory Cleanup Steps

1. Scan manuscript and figure captions for internal names.
2. Classify each term as:
   - keep as formal term
   - replace with publication term
   - move to SI/provenance
   - delete
3. Build a terminology ledger.
4. Apply replacements consistently across title, abstract, main text, captions, tables, and conclusion.

## Common Internal Terms

| Internal pattern | Publication treatment |
|---|---|
| date/version names such as `model_v3`, `run_0421`, `20240115` | replace with model/data role; keep date only in provenance/SI |
| checkpoint/model nicknames such as `forward_checkpoint`, `inverse_candidate_v2` | replace with formal module role |
| status codes such as `accepted_status`, `status_code_0` | replace with acceptance definition or solver status |
| dataset nicknames such as `test_set_v2`, `all_samples_500`, `outer_range_10_20` | replace with sample size and sampling condition |
| script/function names | move to SI/code availability unless central method |
| local file paths | remove from manuscript text; keep in internal evidence package |
| figure generation folder names | do not expose in captions |

## Ledger Template

| Internal term | Formal manuscript term | First definition | Keep in main text? | Notes |
|---|---|---|---|---|
| `model_v3` | final model for the stated task | define by role | no internal name | use model role |
| `accepted_status` | accepted solver/projection case | define threshold | no internal code | report count |

## Replacement Rules

- Prefer role-based names over implementation names.
- Use symbols for modules once defined, e.g. \(G_{\phi}\), \(R_{\psi}\), \(F_{\theta}\), \(S_{\omega}\), \(\mathcal{H}\).
- Do not rename a method to sound more novel than it is.
- Keep exact dataset sizes and conditions, but write them as prose: "50 held-out samples", "500 interpolation samples", "500 extrapolation samples".
- If a term is needed for reproducibility but not understanding, move it to SI.

## Red Flags

- A reader cannot tell whether a term is a model, dataset, script, or checkpoint.
- A figure caption contains local folder names or version stamps.
- The abstract contains training-run names.
- The same module appears under several names.
