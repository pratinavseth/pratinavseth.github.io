---
permalink: /
title: "Pratinav Seth — LLM Post-Training, Safety & Mechanistic Interpretability"
description: "Lead Research Scientist at Lexsi Labs with 48 papers (31 peer-reviewed, 210+ citations) at ICML, ACL, WWW, MIDL, and Nature Scientific Reports. Research: post-training alignment for LLMs and circuit-level mechanistic interpretability."
excerpt: "Lead Research Scientist at Lexsi Labs. Post-training alignment and circuit-level mechanistic interpretability. 48 papers (31 peer-reviewed, 210+ citations) at ICML, ACL, WWW, MIDL, and Nature Scientific Reports."
keywords: "Pratinav Seth, LLM alignment, safety post-training, RLHF, DPO, SFT, mechanistic interpretability, AI safety, circuit analysis, weight arithmetic, safety fine-tuning, agentic systems, AI agents, evaluation, tabular foundation models, knowledge distillation, lead research scientist, machine learning, NLP"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
hero:
  eyebrow: "Lead Research Scientist · Lexsi Labs"
  name: "Pratinav Seth"
  tagline: "LLM post-training, safety alignment, and mechanistic interpretability — with a growing focus on AI agents and evaluation."
  stats:
    - number: "31"
      label: "Peer-Reviewed"
    - number: "210+"
      label: "Citations"
    - number: "8"
      label: "h-index"
---

<span class='anchor' id='about-me'></span>
## About

I started in computer vision and medical imaging — uncertainty quantification, model fairness, and segmentation with teams at IIT Kharagpur and Bosch Research. Moving into language models, I kept running into the same problem: a model that looked aligned on benchmarks would fail in ways that weren't visible from the outside. That gap — between what training instils and what survives deployment — became the question I keep returning to.

On the safety side, I study how fine-tuning and quantization silently erode alignment, and how to find and repair the specific weights responsible using mechanistic interpretability: circuit-level refusal ([C-ΔΘ](https://arxiv.org/abs/2602.04521)), quantization-permanent unlearning ([Forgetting That Sticks](https://arxiv.org/abs/2605.15138)), and safety drift auditing. On the structured data side, I work on tabular foundation models — how to train, fine-tune, and distil them down to something deployable ([TabTune](https://arxiv.org/abs/2511.02802), [Orion-MSP](https://arxiv.org/abs/2511.02818), [Orion-BiX](https://huggingface.co/Lexsi/Orion-BiX)). Most of this ships as open-source tools. The next problems I care most about are safety in reasoning models and interpretability for agentic systems.

<div class="tag-row">
  <span class="tag tag--interp">AI Alignment &amp; Safety</span>
  <span class="tag tag--interp">Mechanistic Interpretability</span>
  <span class="tag tag--training">LLM Post-Training</span>
  <span class="tag tag--training">RLHF &amp; DPO</span>
  <span class="tag tag--alignment">Safety Fine-Tuning</span>
  <span class="tag tag--agentic">Agentic Systems</span>
  <span class="tag tag--tabular">Tabular Foundation Models</span>
  <span class="tag tag--tabular">Knowledge Distillation</span>
  <span class="tag tag--agentic">XAI</span>
</div>

---

I lead the Model Science group at **[Lexsi Labs](https://lexsi.ai/)** across India and Paris. I completed my B.Tech in Data Science from MIT Manipal in 2024, and before that worked at **[Mila Quebec AI Institute](https://mila.quebec/en)** (with Prof. David Rolnick), **[Bosch Research India](https://www.bosch.in/our-company/bosch-in-india/bangalore/)**, and **[IIT Kharagpur](https://iitkliv.github.io/)**. I'm an **[AAAI Undergraduate Consortium Scholar](https://aaai-uc.github.io/2023_scholars.html)** (2023 → Mentor, 2026).

Recent work: [AlignTune](https://arxiv.org/abs/2602.09621) · [CircuitKIT](https://arxiv.org/abs/2607.19317) · [C-ΔΘ](https://arxiv.org/abs/2602.04521) · [CuratorKIT](https://arxiv.org/abs/2606.21631) · [SafeTune](https://github.com/Lexsi-Labs/SafeTune) · [Forgetting That Sticks](https://arxiv.org/abs/2605.15138) · [TabTune](https://arxiv.org/abs/2511.02802) · [Orion-MSP](https://arxiv.org/abs/2511.02818)

Feel free to reach out or see my **[Resume](https://linktr.ee/pratinavseth)**.

## Key Highlights

Published at ICML, ACL, WWW, MIDL, IJCNN, AAAI, and Nature Scientific Reports, plus workshops and shared tasks at CVPR, NeurIPS, ICLR, MICCAI, EurIPS, ACL, and SIGMOD.

- **Research Focus**: LLM safety post-training — circuit-level mechanistic interpretability, safety weight arithmetic, unlearning, post-training alignment, and a growing focus on AI agents & evaluation.
- **7 open-source libraries released** — see [Libraries & Toolkits](/publications/#libraries--toolkits).
- **AAAI Undergraduate Consortium Scholar** & Mentor (2023 → 2026); **Spotlight Talk** at EurIPS Workshop on Private AI Governance, Copenhagen (December 2025).

<div class="notice--warning" markdown="1">
**Lexsi Labs — Internships & Full-Time Roles:** For internship and FTE applications at Lexsi Labs, please **apply directly** via [lexsi.ai](https://lexsi.ai) rather than reaching out for referrals.
</div>
<div class="notice--success" markdown="1">
**Mentoring:** I am open to mentoring early-stage and young researchers. If you'd like to connect, feel free to [reach out via email](mailto:seth.pratinav@gmail.com) — please be respectful of my time and include a brief note about your background and what you're working on.
</div>


# News
{: #news}

## Recent Publications & Acceptances

<div class="timeline-list" markdown="1">
- <span class="timeline-list__date">2026.07</span>New Pre-Print: **CircuitKIT: Circuit Discovery, Evaluation, and Application Toolkit for Mechanistic Interpretability**
- <span class="timeline-list__date">2026.07</span>New Pre-Print: **Faithfulness to Refusal: A Causal Audit of Neuron Selectors in LLMs**
- <span class="timeline-list__date">2026.06</span>New Pre-Print: **CuratorKIT: Data Curation and Synthetic Data Generation for LLM Post-Training**
- <span class="timeline-list__date">2026.06</span>New Pre-Print: **ALIGNBEAM: Inference-Time Alignment Transfer via Cross-Vocabulary Logit Mixing**, accepted at **AI for Good Workshop @ ICML 2026**
- <span class="timeline-list__date">2026.06</span>New library release: **SafeTune** — a unified library for auditing and repairing safety drift in fine-tuned LLMs
- <span class="timeline-list__date">2026.05</span>**Distilling Tabular Foundation Models for Structured Health Data** wins **Best Paper Runner-Up (Spotlight)** at **SD4H Workshop @ ICML 2026**
</div>

<details markdown="1">
<summary>Earlier publications & acceptances</summary>
<div class="timeline-list" markdown="1">
- <span class="timeline-list__date">2026.05</span>**Data Presentation over Architecture: Resampling Strategies for Credit Risk Prediction with Tabular Foundation Models** accepted as an **Oral at FinDS Workshop @ ACM SIGMOD 2026**
- <span class="timeline-list__date">2026.05</span>New Pre-Print: **Position: Behavioural Assurance Cannot Verify the Safety Claims Governance Now Demands**
- <span class="timeline-list__date">2026.05</span>**Pocket Foundation Models: Distilling TFMs into CPU-Ready Gradient-Boosted Trees** accepted at **FMSD Workshop @ ICML 2026**
- <span class="timeline-list__date">2026.05</span>**Ensembling Tabular Foundation Models: A Diversity Ceiling and a Calibration Trap** accepted at **FMSD Workshop @ ICML 2026**
- <span class="timeline-list__date">2026.02</span>New Pre-Print: **AlignTune: Modular Toolkit for Post-Training Alignment of Large Language Models**
- <span class="timeline-list__date">2026.02</span>New Pre-Print: **C-ΔΘ: Circuit-Restricted Weight Arithmetic for Selective Refusal**
- <span class="timeline-list__date">2026.01</span>**Orion-Bix: Bi-Axial Attention for Tabular In-Context Learning** accepted at **WWW 2026**
- <span class="timeline-list__date">2026.01</span>**Exploring Fine-Tuning for Tabular Foundation Models** accepted at **WWW 2026**
- <span class="timeline-list__date">2026.01</span>**TabTune: A Unified Library for Inference and Fine-Tuning Tabular Foundation Models (Demo)** accepted at **WWW 2026**
- <span class="timeline-list__date">2026.01</span>**Laplacian reconstructive network for guided thermal super-resolution** accepted at **Scientific Reports (Nature)**
- <span class="timeline-list__date">2025.11</span>**Interpretability as Alignment: Making Internal Understanding a Design Principle** accepted at **EurIPS Workshop on Private AI Governance**
- <span class="timeline-list__date">2025.11</span>**Bridging the gap in XAI-why reliable metrics matter for explainability and compliance** accepted at **EurIPS Workshop on Private AI Governance**
- <span class="timeline-list__date">2025.11</span>**EurIPS Workshop on Private AI Governance 2025 Spotlight Talk**
- <span class="timeline-list__date">2025.09</span>**Interpretability-aware pruning for efficient medical image analysis** accepted at **MICCAI Workshop 2025**
- <span class="timeline-list__date">2025.05</span>**SELF-PERCEPT: Mental Manipulation Detection** accepted at **ACL 2025**
- <span class="timeline-list__date">2025.05</span>**Alberta Wells Dataset** accepted at **ICML 2025** (grateful to the team for their efforts, and to Prof. David Rolnick)
</div>
</details>

## Academic Service & Reviewing

<div class="timeline-list" markdown="1">
- <span class="timeline-list__date">2026.07</span>**Reviewer** for **Actionable Interpretability Workshop @ COLM 2026**
- <span class="timeline-list__date">2026.07</span>**Program Committee** for **AAAI 2027**
- <span class="timeline-list__date">2026.06</span>**Reviewer** for **ACM AIES 2026**
- <span class="timeline-list__date">2026.06</span>**Reviewer** for **System Demonstrations Track @ EMNLP 2026**
- <span class="timeline-list__date">2026.06</span>**Reviewer** for **NLP4PI Workshop @ EMNLP 2026**
- <span class="timeline-list__date">2026.06</span>**Reviewer** for **BlackboxNLP Workshop @ EMNLP 2026**
</div>

<details markdown="1">
<summary>Earlier service & reviewing</summary>
<div class="timeline-list" markdown="1">
- <span class="timeline-list__date">2026.05</span>**Reviewer** for **AI for Good Workshop @ ICML 2026**
- <span class="timeline-list__date">2026.05</span>**Reviewer** for **Mechanistic Interpretability Workshop @ ICML 2026**
- <span class="timeline-list__date">2026.05</span>**Reviewer** for **TAIGR Workshop @ ICML 2026**
- <span class="timeline-list__date">2026.05</span>**Reviewer** for **FMSD Workshop @ ICML 2026**
- <span class="timeline-list__date">2026.05</span>**Reviewer** for **FAIMI-BRIDGE-EPIMI Workshop @ MICCAI 2026**
- <span class="timeline-list__date">2026.05</span>**Reviewer** for **WACV 2027**
- <span class="timeline-list__date">2026.04</span>**Reviewer** for **NeurIPS 2026**
- <span class="timeline-list__date">2026.04</span>**Reviewer** for **BMVC 2026**
- <span class="timeline-list__date">2026.03</span>**Reviewer** for **ECCV 2026**
- <span class="timeline-list__date">2026.03</span>**Reviewer** for **FinDS Workshop @ ACM SIGMOD 2026**
- <span class="timeline-list__date">2026.02</span>**Reviewer** for **Advances in Financial AI Workshop (ICLR 2026)**
- <span class="timeline-list__date">2026.01</span>**Reviewer** for **CVPR 2026**
- <span class="timeline-list__date">2025.12</span>**Mentor** at **AAAI Undergraduate Consortium 2026**
</div>
</details>

