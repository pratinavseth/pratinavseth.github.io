---
title: "How I got into AI safety research"
description: "From a college research club to leading a safety and alignment team: the path, the detours, and the one question that connected them."
date: 2026-11-24
draft: true
tags: [journey, AI safety, career]
---

<!-- DRAFT for Pratinav to write in his own voice. Every date, role and number below comes from the site's own pages (Experience, Education, Talks). The comments marked YOUR VOICE are where only you can add the why; please fill or delete them before setting draft: false. -->

What I care about most is being able to see why a model does what it does, so that safety claims come from how a model actually works, not how it looks from the outside. That question took me a while to find, and it did not start as an AI safety question. This is the path.

<!-- YOUR VOICE: one or two sentences on the moment you first cared about safety specifically, if there was one. -->

## A research club, from trainee to lead (2020 to 2023)

I started a B.Tech in Data Science & Engineering at Manipal Institute of Technology in October 2020, and joined the AI Research Wing at Mars Rover Manipal as a trainee a month later. I became a researcher in August 2021 and, from August 2022 to August 2023, a senior researcher leading the wing. Along the way I mentored more than ten undergraduates, and we published workshop papers at NeurIPS, CVPR, ICLR and MICCAI, an AAAI student abstract and a paper in Nature Scientific Reports.

Outside the wing I co-led the Research Society MIT Manipal, an undergraduate research organisation of more than 90 members, and co-founded The Data Alchemists, an AI/ML club that grew to more than 30 members.

<!-- YOUR VOICE: what running a club taught you about research, mentoring, or choosing problems. -->

## Trying many things (2022 to 2023)

Looking back, my projects in these years look scattered, and I would not have planned them that way:

- Placing 5th of 134 teams in a malware classification competition.
- Building generative models for synthetic tabular data at Eedge.ai, and studying how that data changes the interpretability of fine-tuned models.
- Building NLP pipelines for a healthcare chatbot at CUREYA.
- Developing a graph convolutional network for chest X-ray screening at the KLIV Research Group, IIT Kharagpur, where I also investigated sanity checks for class activation maps, a question about whether an explanation can be trusted.
- Working on metric learning with researchers at NEC Labs and IIT Roorkee.

In February 2023 I was one of 11 undergraduates selected as an AAAI Undergraduate Consortium Scholar, with a $2,000 travel grant to present at AAAI-23 in Washington D.C. In 2026 I came back to the same programme as a mentor.

<!-- YOUR VOICE: which of these projects changed how you thought, and why. -->

## Industry and a research lab (2023 to 2024)

In 2023 I was a computer vision research intern at Bosch Research in Bangalore, working on generative data augmentation for autonomous driving. In 2024 I spent six months in David Rolnick's lab at Mila, where my bachelor's thesis became the Alberta Wells Dataset: a benchmark of more than 213,000 oil and gas wells in Alberta, for finding abandoned wells from satellite imagery. It became a first-author paper at ICML 2025.

## From explaining models to fixing them (2024 to now)

I graduated in July 2024 and joined AryaXAI Alignment Labs, now Lexsi Labs, working on explainability: generalising DLBacktrace so it works on any model architecture, building xai_evals to benchmark explanation methods, and measuring how reliable those methods are for high-stakes uses such as fraud detection.

The question I moved to next was what you can do once you can see inside a model. In 2025 that work included AlignTune, a post-training toolkit, and an EurIPS workshop paper, [Interpretability as Alignment](/publications/interpretability-as-alignment/), which I presented as a spotlight talk in Copenhagen. In 2026 I became Lead Research Scientist, heading the Model Science group, and founded the AI Safety & Alignment team. The questions I work on now are: repairing a model's safety in its weights ([SafeTune](/publications/safetune/), [C-ΔΘ](/publications/c-delta-theta/)), checking that the repair held, and extending the same discipline to agents.

<!-- YOUR VOICE: the hardest call or the biggest mistake of this stretch, and what you changed afterwards. -->

## What connects it

Every step above was a version of the same question: can we trust what a model tells us about itself, and if not, how would we know? A saliency map, a refusal, an agent's explanation of its own tool call: each is a claim that needs evidence from inside the system.

<!-- YOUR VOICE: advice for a student deciding where to start, in two or three sentences. -->

If you are an early-career researcher thinking about this path, [write to me](/#contact) with who you are and the one question you want help with.
