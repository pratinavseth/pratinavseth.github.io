---
title: "Do compliance checkers read the rule?"
description: "Three audits of LLM compliance systems point to the same finding: the verdict often does not depend on the rule it is supposed to enforce."
date: 2026-11-24
draft: true
tags: [compliance, evaluation, research notes]
---

<!-- DRAFT for Pratinav to edit. Every claim and number below comes from the abstracts of the three papers linked in the text. Add your own framing where marked YOUR VOICE, then set draft: false. -->

A compliance checker is meant to answer one question: does this output follow this written rule? That is only a meaningful answer if the verdict depends on the rule. Three papers from our group tested that directly, and found that it often does not.

<!-- YOUR VOICE: why you started looking at this, and where you have seen these systems used. -->

## The test: change the rule, hold the case fixed

All three audits use the same idea. Keep the case the same and change the governing rule: delete it, permute it, swap it for an unrelated or a permissive one, or negate it. If a system really reads the rule, its verdict should move.

## Detectors that ignore the rule

[*What Do Compliance Detectors Read?*](/publications/what-do-compliance-detectors-read/) audits activation probes and guard models, checking outputs against rules spanning data protection, healthcare, financial regulation and platform policy. For every guard and probe tested, deleting, permuting or substituting the rule left detection accuracy unchanged. That includes a policy-conditioned guard that correctly cites the governing clause yet barely changes its verdict when the clause is swapped for its permissive counterpart. We call this *rule blindness*, and built a benchmark that crosses two rules with two scenarios so that neither alone predicts the label.

## Verdicts that do not move

[*Verdict Without the Rule*](/publications/verdict-without-the-rule/) runs the same kind of test across five models and 20 regulatory and platform-policy domains. Models' verdicts are often invariant to substantial changes to the supplied rule. The guard model was the least rule-sensitive and the least accurate of the five, at 51%, barely above chance, against 90 to 92% for the general-purpose models.

The paper is careful about what this means. It reflects easy cases more than blanket neglect: on cases where deleting the rule changes a previously correct model prediction, models do track the rule closely.

## Citing the law is not the same as using it

[*Cited but Not Consulted*](/publications/cited-but-not-consulted/) asks the question for legal reasoning. Models often justify a decision by naming the statute or precedent behind it. Holding the case facts fixed and substituting an unrelated authority, we decoded the model's evolving verdict from its hidden states. Across seven open-weight models (8B to 70B) and four benchmarks, models named the correct authority in 66.7% to 100% of generations, while the verdict changed when the authority changed only 0.0% to 21.7% of the time on CaseHOLD, 30.0% to 76.7% on ECHR and SCOTUS, and 43.3% to 50.0% on ContractNLI. Neither scale nor a purpose-built legal-reasoning model closed the gap.

## What to take from it

If you deploy or buy a compliance system, the cheapest useful test is the one these papers use: hold the case fixed, change the rule, and see whether the verdict moves. A system that cites the right clause is not evidence that it used the clause.

<!-- YOUR VOICE: one or two sentences on what you would want a regulator, auditor or product team to do differently. -->

The three papers are [What Do Compliance Detectors Read?](/publications/what-do-compliance-detectors-read/) (TAE Workshop, NeurIPS 2026), [Verdict Without the Rule](/publications/verdict-without-the-rule/) (NLLP Workshop, EMNLP 2026) and [Cited but Not Consulted](/publications/cited-but-not-consulted/) (NLLP Workshop, EMNLP 2026 and TAE Workshop, NeurIPS 2026). A fourth, [Evaluating Rule Adherence in Language Model Compliance Detection](/publications/evaluating-rule-adherence/), is under review.
