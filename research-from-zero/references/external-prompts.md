# External Prompts

Use this when asking GPT, DeepResearch, or another external tool to help with literature, language, or style. Prompts must preserve evidence and boundaries.

## Literature / DeepResearch Prompt

```text
I am writing a research manuscript on [topic]. Please find and categorize peer-reviewed literature for the following argument, not a generic bibliography.

Paper context:
- Field:
- Method or system:
- Application case:
- Core claim:
- Boundaries:

Please organize sources into:
1. prior work on the application/problem
2. prior work on the method family
3. baselines or competing approaches
4. known limitations/failure modes
5. sources that should not be overused or are only tangential

For each source, provide DOI, venue, year, exact claim it supports, and whether it is primary evidence or background.
Do not invent citations. Mark uncertain bibliographic details clearly.
```

## Language Polish Prompt

```text
Please polish the following manuscript section into journal-style academic prose.

Hard constraints:
1. Do not add new results, references, mechanisms, or claims.
2. Preserve all numeric values and dataset conditions.
3. Preserve the terminology ledger below.
4. Keep boundaries and limitations explicit.
5. Convert report-like phrasing into claim-first manuscript prose.
6. Keep figure references, but do not make every sentence start with "Figure X shows".

Terminology ledger:
[paste ledger]

Section purpose:
[state section job]

Text:
[paste text]
```

## Results Rewrite Prompt

```text
Rewrite this Results/Discussion section so that each paragraph starts with the scientific or technical claim, followed by evidence.

Requirements:
- Results sentences should report what was observed.
- Discussion sentences may interpret, but must remain bounded.
- Every performance claim must specify dataset, metric, baseline and condition.
- Keep stronger baselines and failure modes visible.
- Remove internal version names, script names and checkpoint names.
```

## Figure Planning Prompt

```text
Given the manuscript outline and claims below, propose main-text figures and SI figures.

For each figure, specify:
- claim supported
- panel layout
- data needed
- metric and axis definitions
- main-text or SI placement
- risk of misinterpretation
- one-sentence caption conclusion

Do not propose decorative figures. Every figure must support a manuscript claim.
```

## Reviewer-Style Audit Prompt

```text
Read the manuscript section below as a skeptical reviewer.

Audit:
1. What claim is being made?
2. What evidence supports it?
3. What evidence is missing?
4. Which terms sound like internal project names?
5. Which sentences sound like a work report rather than a paper?
6. Which claims are overextended?
7. What should move to SI?

Return concise, actionable findings with line-level references if possible.
```
