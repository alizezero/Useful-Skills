# Final Submission Package

Use this when the user asks for a final manuscript package, submission-ready files, final export, or pre-submission cleanup. This is different from ordinary writing: the deliverable must be complete, current, and internally consistent.

## Define the Package

Ask only when necessary. Otherwise infer and list the package components:

- main manuscript;
- Supplementary Information;
- figures and tables;
- source-data files;
- cover letter or response letter, if relevant;
- graphical abstract or highlights, if required;
- code/data repository link and release commit, if applicable;
- journal-specific files such as declarations, data availability, ethics, author contributions, or competing interests.

## Final File Rules

- Identify the newest active files and do not package stale drafts.
- Use clean filenames that do not expose temporary internal states unless the user wants versioned working files.
- Keep original editable sources where useful, but do not mix draft backups into the final delivery folder.
- Make sure every figure referenced in the manuscript exists in the package or in the release repository as expected.
- If the target journal requires separate figure files, preserve panel quality and do not rely only on embedded images.

## Submission-Readiness Checks

Run these checks before declaring the package ready:

1. **Main/SI consistency**
   - Run the audit logic in `manuscript-si-consistency-audit.md`.

2. **Figure/table package**
   - Check file existence, numbering, captions, source-data mapping, and image non-blankness.
   - Confirm final figure versions match the prose after recent redraws.

3. **Reference and citation state**
   - Check citation numbering or author-year consistency.
   - Flag missing references, placeholder citations, or uncited bibliography entries.

4. **Data and code availability**
   - Confirm data availability and code availability statements match the actual repository/deposit status.
   - If a GitHub repository is part of the submission, record remote URL, branch/tag/commit, and validation status.

5. **Formatting hazards**
   - Search for comments, tracked-change remnants, TODOs, placeholders, broken links, local paths, mojibake, and duplicated captions.
   - Check units, notation, abbreviation definitions, and figure/table cross-references.

6. **Journal-specific requirements**
   - Apply only requirements known for the target journal or supplied by the user. Do not invent a journal checklist.

## Final Package Report

Return a compact status report:

```markdown
## Final Package
| Component | Path | Status |

## Checks Run
| Check | Result |

## Remaining Issues
| Issue | Required action |

## Release Repository
Remote:
Commit/tag:
Validation:
```

Do not say the package is submission-ready if source data, figures, code links, or required declarations are missing. Say what is missing and where it blocks submission.
