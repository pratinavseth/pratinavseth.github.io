---
title: "What we learned about tabular foundation models"
description: "Fine-tuning, ensembling, distillation and context building, studied across hundreds of datasets: where the gains are, and where they are not."
date: 2026-11-24
draft: true
tags: [tabular foundation models, research notes]
---

<!-- DRAFT for Pratinav to edit. Every number below comes from the abstracts of the papers linked in the text. Add your own framing where marked YOUR VOICE, then set draft: false. Advice is limited to what the papers' own findings support. -->

Tabular foundation models (TFMs) match or beat tuned gradient-boosted trees on a growing share of tabular tasks, without task-specific training. Over the last year our group studied what to do with them. The short version: the obvious levers help less than people expect, and a few unglamorous ones help more.

<!-- YOUR VOICE: how you came to this line of work, and which result surprised you most. -->

## The models and the library

We built two models and a library for working with them. [Orion-MSP](/publications/orion-msp/) is a tabular in-context learning architecture designed to fix three limits of earlier models: single-scale feature processing, dense attention that grows quadratically with table width, and strictly sequential components. [Orion-BiX](/publications/orion-bix/) alternates standard, grouped, hierarchical and relational attention and is meta-trained on synthetic tables with causal priors. [TabTune](/publications/tabtune/) puts seven models behind one interface for zero-shot use, meta-learning, supervised fine-tuning and parameter-efficient tuning, and evaluates calibration and fairness as well as accuracy.

## Fine-tuning is not a free win

In [Exploring Fine-Tuning for Tabular Foundation Models](/publications/exploring-fine-tuning-for-tabular-foundation-models/), the first comprehensive study of the question, zero-shot TFMs were already strong, and the benefit of fine-tuning depended heavily on the model and the data. Meta-learning and parameter-efficient tuning gave moderate gains under specific conditions, while full supervised fine-tuning often reduced accuracy or calibration.

## Ensembling barely helps

The natural fix when no single model wins everywhere is to ensemble. In [Ensembling Tabular Foundation Models](/publications/ensembling-tabular-foundation-models/), six modern TFMs turned out to be nearly redundant, with a mean pairwise Q-statistic of 0.961. Across 153 OpenML classification tasks, the best ensemble gained 0.18% accuracy over the strongest single model, at 253 times the compute. Stacking with a logistic-regression meta-learner kept competitive accuracy and ROC-AUC but had the worst log-loss rank among the ensembles.

## Distil it for production

A fraud scorer may need an answer in under 2 ms; the best TFMs take 151 to 1,275 ms on GPU. [Pocket Foundation Models](/publications/pocket-foundation-models/) distils a TFM into an XGBoost or CatBoost student that runs on CPU. The obstacle specific to in-context models is that they leak labels when scoring their own training set, which collapses the soft targets; stratified out-of-fold labeling prevents it. Across 153 datasets, distilling TabICLv2 into XGBoost reached 0.882 macro-mean AUC, 96.5% of the teacher's, at 1.9 ms on CPU.

For health data, [Distilling Tabular Foundation Models for Structured Health Data](/publications/distilling-tfms-structured-health-data/) found across 19 datasets that students kept at least 90% of the teacher's AUC while running at least 26 times faster on CPU, preserving the calibration and fairness health applications need. Averaging several teachers did not consistently beat the best single teacher.

## How you build the context matters more than the model

In credit-default prediction, a TFM's predictions depend on how its context window is built. [Data Presentation over Architecture](/publications/data-presentation-over-architecture/) benchmarked four classical models and five TFMs on Home Credit and Lending Club. The context strategy explained more variance in AUC-ROC than the choice of TFM family: balanced and hybrid sampling added 3 to 4 AUC points over uniform sampling, more than the gap between models. With a balanced context of 5K to 10K examples, the strongest TFMs reached the AUC of classical baselines trained on the full data.

## What it adds up to

On these benchmarks, the order of effort that paid off was: check zero-shot first, spend effort on how the context is built, distil for deployment, and be sceptical of ensembles and full fine-tuning.

<!-- YOUR VOICE: where you disagree, what these studies did not cover, and what you would test next. -->

Venues: the ensembling and Pocket Foundation Models papers appeared at the Foundation Models for Structured Data workshop at ICML 2026; the health-data paper was a spotlight at the SD4H workshop at ICML 2026, where it received a Best Paper Runner-Up; the credit-risk paper was an oral at the FinDS workshop at ACM SIGMOD 2026; Orion-BiX, the fine-tuning study and TabTune appeared at WWW 2026.
