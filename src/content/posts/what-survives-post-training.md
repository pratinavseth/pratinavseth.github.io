---
title: What survives post-training?
description: The question that connects my work on circuit-level refusal, safety drift, unlearning under quantization and interpretability-first governance.
date: 2026-10-19
draft: true
tags: [post-training, safety, mechanistic interpretability]
---

<!-- DRAFT for Pratinav to edit. Every claim below is taken from the linked papers; check the framing is yours before setting draft: false. -->

Most safety work evaluates a model at one moment: full precision, right after training, on a benchmark. Almost no deployed model stays in that state. It gets fine-tuned on a customer's domain, quantized to fit the hardware, wrapped in a serving stack, and updated again a few months later. The question I keep coming back to is simple to state and hard to answer: **which properties of a model survive all of that, and how would we know?**

## Behaviour drifts when you aren't looking

Domain fine-tuning quietly erodes safety. A model tuned on legal or financial text will often comply with harmful requests as long as they are phrased in that domain's language. We built [SafeTune](/publications/safetune/) to audit and repair that drift, and [Drift, Then Repair](/publications/drift-then-repair/) to measure it across fine-tuning paradigms. When you can't touch the weights at all, [ALIGNBEAM](/publications/alignbeam/) transfers safety at inference time from an aligned anchor model, even across model families with different vocabularies.

Compression has the same problem in a sharper form. In [Forgetting That Sticks](/publications/forgetting-that-sticks/) we found that most unlearning methods either forget the target knowledge and then lose that forgetting once the model is quantized to 4 bits, or survive quantization because they barely changed the model. The cause is mundane: the per-parameter updates are tens to hundreds of times smaller than a quantization bin, so they round away. The fix was to concentrate the update on the circuit that actually stores the knowledge, so each change is big enough to persist.

## Edit the mechanism, not the output

That result points at the general approach I trust most: find the mechanism responsible for a behaviour, then change it directly. [C-ΔΘ](/publications/c-delta-theta/) does this for refusal. It localises the circuit behind category-specific refusal and computes a weight update restricted to that circuit, usually under 5% of parameters. The result is an ordinary checkpoint with no inference-time hooks, so the safety behaviour costs nothing at serving time. [CircuitKIT](/publications/circuitkit/) packages the discovery, evaluation and editing steps so the team can do this routinely rather than as one-off research code.

The same audit, correct, re-verify loop is what we applied to [Gemma 4 31B](/publications/gemma-4-safety-repair/) for multilingual and cybersecurity safety failures.

## Are we editing the right thing?

Editing mechanisms only works if the mechanism you found is real. A lot of my recent work is about checking that:

- [Faithfulness to Refusal](/publications/faithfulness-to-refusal/) tests whether attribution methods pick out causally important neurons. Some of the most stable selectors turned out to be among the least causally valid, and refusal lives in a redundant subspace that different methods reach through largely different neurons.
- [Faithfulness Is Not Actionability](/publications/faithfulness-is-not-actionability/) asks whether a circuit that scores well on faithfulness is actually useful when you prune with it.
- [Every Ablation Is a Dose](/publications/every-ablation-is-a-dose/) argues that "self-repair" after ablation follows a simple law once you treat an ablation as one point on a continuous intervention axis.
- [The Off-Switch Failure](/publications/the-off-switch-failure/) shows how safety-repair evaluations can reward a model that has simply collapsed.

## Why this matters beyond the lab

Governance frameworks increasingly ask for evidence about properties like hidden objectives or bounded capabilities. Behavioural evaluations and red-teaming only see outputs, so they cannot verify those claims. That is the argument of our [position paper on behavioural assurance](/publications/position/), and the reason I think of interpretability as infrastructure rather than a post-hoc explanation tool ([Interpretability as Alignment](/publications/interpretability-as-alignment/)).

## What's next

I'm extending this to agents, where the gap between what a model was trained on and how it's deployed is even wider, and to evaluation tooling that keeps an auditable record of every intervention. If you're working on any of these questions, especially verifying safety properties after fine-tuning or compression, [I'd like to hear from you](/#contact).
