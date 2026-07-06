# Section Playbooks

Use this to convert a project into a manuscript outline and assign jobs to sections.

## Title

The title should name the object, action, and consequence. Avoid internal method names unless they are the formal contribution.

Pattern:

`target/problem + method/workflow + application/boundary`

## Abstract

Use:

`context/problem -> gap -> approach -> strongest quantitative result -> comparison/boundary -> implication`

Avoid listing every module and every number.

## Introduction

Jobs:

1. Establish why the problem matters.
2. Organize literature by method gap, not by paper list.
3. State the missing capability.
4. State the contribution and evidence plan.

Do not start with case-specific details unless the case is the main field contribution.

## Methods / Framework

Jobs:

1. Define notation and assumptions.
2. Explain the workflow before module details.
3. Define each module by role, input, output, and boundary.
4. Separate general framework from case implementation.

Avoid reporting performance in Methods unless needed to define a procedure.

## Case / Problem Definition

Jobs:

1. Explain why this case is a meaningful test.
2. Define variables, states, constraints, outputs, and available measurements.
3. Explain dataset construction and evaluation sets.
4. Keep detailed variable tables in SI unless central to the argument.

## Results

Jobs:

1. State each result as a claim.
2. Provide dataset, metric, baseline, and number.
3. Use figures as evidence, not as the subject of every paragraph.
4. Include ablations and fair comparisons.
5. Report failure modes and boundaries.

## Discussion

Jobs:

1. Interpret what the evidence means.
2. Explain why some results are weaker or stronger.
3. Compare with prior approaches without overclaiming.
4. Name boundaries revealed by the experiments.

## Conclusion

Jobs:

1. Restate the demonstrated advance.
2. Summarize the strongest evidence.
3. State the method's operating boundary.
4. Identify realistic next steps without marketing language.
