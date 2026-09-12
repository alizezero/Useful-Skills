# Release Repository Management

Use this when a paper-writing task reaches code/data release, GitHub upload, reproducibility packaging, SI source-data linking, or repository cleanup. The goal is a repository that a reader can clone, hydrate, and run without knowing the author's workstation history.

## Scope and Boundaries

- Treat the repository as part of the manuscript evidence system, not as a raw backup folder.
- Do not create a new remote repository, change visibility, add deploy keys, rewrite history, force-push, delete remote branches, or publish private data unless the user explicitly asks for that operation.
- Do not include credentials, tokens, `.env` files, private server paths, unreleased third-party data, or proprietary raw outputs unless the user confirms they are allowed to be shared.
- If the task is only to plan a release, do not mutate the repository. If the user asks to upload/update, perform the Git workflow and verify the remote state.

## Public Repository Shape

A manuscript-linked repository should make the active evidence easy to find and the historical clutter hard to confuse with the release:

```text
README.md        one-command reproduction and scope
configs/         machine-readable dataset/model/experiment/training definitions
data/            canonical public datasets or pointers to external deposits
results/         source-data tables for manuscript figures/tables
manuscript/      frozen manuscript/SI snapshots and referenced media, if appropriate
models/          released checkpoints, with Git LFS when needed
workflows/       active training, plotting, optimization, and analysis code
scripts/         stable entry points such as setup/check/reproduce/build_manifest
expected/        frozen metrics or checksums used by validation
docs/            provenance, model card, results map, limitations, troubleshooting
outputs/         generated locally; normally ignored
```

Adapt names to the project, but preserve the separation between active public artifacts and obsolete development history. If an archive is retained, make it short, optional, and clearly excluded from public entry points.

## Cleanup Rules

- Keep only artifacts needed for the manuscript, SI, source-data verification, reproducibility, or defensible provenance.
- Remove or relocate old experiment folders, duplicate figures, failed trial outputs, long server logs, and obsolete route names that no longer support the current manuscript.
- Avoid Windows-hostile paths. Check tracked paths for excessive length, nonportable characters, and deeply nested archives. If a fresh Windows clone fails, shorten paths or remove nonessential historical directories.
- Replace hard-coded absolute paths with repository-relative paths. Search for drive roots, `/home/`, `/data`, server usernames, and temporary directories.
- Put large binary files under Git LFS deliberately. Verify that clones can hydrate them with `git lfs pull`.
- Preserve source-data CSVs for plotted values. Do not leave only final PNGs when a figure supports a manuscript claim.
- Keep publication terminology in public docs. Internal names may appear in provenance tables, but should not define the public model or dataset names.

## Manuscript and SI Alignment

Before publishing or updating GitHub, build a release alignment table:

| Manuscript item | Public artifact | Script or command | Verification |
|---|---|---|---|
| Figure/Table/number | `results/...` or `data/...` | script path or formula | checked/pending |

Check that:

- every claim-carrying main figure has source data and, when possible, a plotting script;
- every important manuscript number maps to a CSV, JSON, log, or reproducible calculation;
- SI source-data file names match repository files exactly;
- figure captions describe what is actually plotted after the latest redraw;
- old sample IDs, route names, observation variables, or figure legends are not left in text after the experimental story changes.

## Reproduction Entry Points

Prefer a small number of stable public commands:

```bash
python scripts/report_environment.py
python scripts/reproduce.py --mode check
python scripts/reproduce.py --mode frozen
```

Common modes:

- `check`: file presence, shapes, hashes, LFS hydration, portable paths, config consistency.
- `frozen`: recompute released metrics and regenerate released figures from source-data tables.
- `figures`: regenerate figures only.
- `retrain-smoke`: tiny integration test when full retraining is expensive.
- `retrain`: full workflow, documented as compute-intensive and platform-dependent.

Document which modes require IPOPT, GPU, large memory, external simulators, or private software. The default public mode should not unexpectedly launch a costly training run.

## Program Format Management

For code quality in a release repository:

- Use repository-relative paths and CLI arguments or config files for data locations.
- Prefer structured readers (`csv`, `json`, `pandas`, `yaml`) over ad hoc parsing.
- Keep active workflows importable or executable from the repository root.
- Validate JSON/YAML configs.
- Compile or syntax-check Python scripts after edits.
- Keep generated outputs out of version control unless they are release artifacts.
- Put repeated checks in scripts rather than relying on manual inspection.
- Update manifests, metric references, and result maps in the same commit as source-data or figure changes.

## GitHub Update Workflow

When the user asks to upload or update GitHub:

1. Identify the intended local repository and remote URL.
2. Inspect `git status --short`, current branch, latest commit, and remote.
3. Run the repository's release checks locally.
4. Stage only intended changes. Do not revert unrelated user changes.
5. Commit with a plain message describing the release-level change.
6. Push to the requested remote/branch using the user's configured authentication.
7. Verify the remote branch points to the pushed commit with `git ls-remote` or equivalent.
8. Make a fresh clone into a temporary directory, run `git lfs pull`, and execute the public `check` and `frozen` commands.
9. Report the commit hash, remote branch, commands run, and any residual limitations.

If authentication fails, report the failure and likely cause. Do not add SSH keys, deploy keys, credentials, or new remotes without explicit user approval.

## Fresh-Clone Acceptance Criteria

The release is not complete until a fresh clone passes:

- checkout succeeds on the target operating systems;
- `git lfs pull` hydrates required large files;
- public setup instructions are sufficient;
- `check` passes without missing files, bad shapes, stale manifests, or broken paths;
- `frozen` reproduces the released metrics and figures;
- README and docs do not point to removed directories or obsolete experiments;
- no old archive path is required for public reproduction unless intentionally documented.

If fresh clone fails, fix the package rather than explaining around it.

## Final Report Template

Report concisely:

```text
Remote:
Branch:
Commit:
Main changes:
Validation:
Fresh clone:
Known limitations:
```

Mention if a full retraining workflow was not run because it requires special hardware or solver dependencies. Do not claim more reproducibility than the executed checks support.
