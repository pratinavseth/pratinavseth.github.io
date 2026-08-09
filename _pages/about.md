---
permalink: /
title: "Pratinav Seth — LLM Post-Training, Safety & Mechanistic Interpretability"
description: "AI researcher with 46 papers (31 peer-reviewed, 210+ citations) and 7 open-source research libraries. Research: post-training safety and circuit-level mechanistic interpretability for language models."
excerpt: "AI researcher working on post-training safety and mechanistic interpretability for language models. 46 papers (31 peer-reviewed, 210+ citations), 7 open-source research libraries."
keywords: "Pratinav Seth, LLM alignment, safety post-training, RLHF, DPO, SFT, mechanistic interpretability, AI safety, circuit analysis, weight arithmetic, safety fine-tuning, agentic systems, AI agents, evaluation, tabular foundation models, knowledge distillation, lead research scientist, machine learning, NLP"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
hero:
  eyebrow: "AI Researcher"
  name: "Pratinav Seth"
  tagline: "Post-training safety and mechanistic interpretability for language models."
  stats:
    - number: "31"
      label: "Peer-Reviewed"
    - number: "7"
      label: "OSS Libraries"
    - number: "210+"
      label: "Citations"
  h_index: "8"
  cta:
    - label: "View Publications"
      url: "/publications/"
      primary: true
    - label: "CV"
      url: "/files/pratinav-seth-cv-full.pdf"
    - label: "Resume"
      url: "/files/pratinav-seth-cv.pdf"
---

<span class='anchor' id='about-me'></span>
## About

I lead the Model Science group at **[Lexsi Labs](https://lexsi.ai/)**, directing research across post-training, alignment, mechanistic interpretability, and tabular foundation models. The team has grown to 20+ researchers and interns across India and Paris; I've worked on hiring, roadmap, grants, and research-to-product integration alongside the research itself.

Most of that research asks what survives post-training: how fine-tuning, quantization, and deployment change a model's behavior, and how to find the specific mechanisms responsible. I use mechanistic interpretability to answer this, then audit, repair, or steer those mechanisms directly: circuit-level refusal ([C-ΔΘ](https://arxiv.org/abs/2602.04521)), circuit discovery and attribution ([CircuitKIT](https://arxiv.org/abs/2607.19317)), and safety-drift auditing and repair ([SafeTune](https://github.com/Lexsi-Labs/SafeTune)). Alongside this, I build the post-training infrastructure that ships it: [AlignTune](https://arxiv.org/abs/2602.09621) for training, [CuratorKIT](https://arxiv.org/abs/2606.21631) for data curation, and [ALIGNBEAM](https://arxiv.org/abs/2606.12342) for inference-time alignment transfer. I'm increasingly extending this work to agentic systems and evaluation.

<div class="tag-row">
  <span class="tag tag--interp">Post-Training &amp; Alignment</span>
  <span class="tag tag--interp">LLM Safety</span>
  <span class="tag tag--training">Mechanistic Interpretability</span>
  <span class="tag tag--alignment">Research Systems</span>
  <span class="tag tag--tabular">Foundation Models</span>
</div>

Published at **ICML, ACL, WWW, MIDL, AAAI, IJCNN**, and **Nature Scientific Reports**, plus workshops and shared tasks at **NeurIPS, ICLR, CVPR, MICCAI, EurIPS, EMNLP, WACV**, and **ACM SIGMOD**.

In parallel, I used to work on the [Orion](https://arxiv.org/abs/2511.02818) tabular foundation model series and [TabTune](https://arxiv.org/abs/2511.02802), an inference and fine-tuning library for tabular foundation models, with follow-on work in distillation, ensembling, and applications in structured health data and credit risk.

<div class="journey-strip">
  <div class="journey-step">
    <span class="journey-step__date">2022 – 23</span>
    <span class="journey-step__label">IIT Kharagpur</span>
    <span class="journey-step__desc">Medical image analysis and explainable AI for chest radiographs, KLIV Lab</span>
  </div>
  <div class="journey-step">
    <span class="journey-step__date">2023</span>
    <span class="journey-step__label">Bosch Corporate Research</span>
    <span class="journey-step__desc">Generative data augmentation for safety-critical autonomous-driving perception</span>
  </div>
  <div class="journey-step">
    <span class="journey-step__date">2024</span>
    <span class="journey-step__label">Mila &mdash; Rolnick Lab</span>
    <span class="journey-step__desc">Geospatial climate AI; built the Alberta Wells Dataset (first-author, ICML 2025)</span>
  </div>
  <div class="journey-step">
    <span class="journey-step__date">2024 &ndash; Present</span>
    <span class="journey-step__label">Lexsi Labs</span>
    <span class="journey-step__desc">Research Scientist &rarr; Lead Research Scientist, Model Science</span>
  </div>
</div>

I completed my B.Tech in Data Science from MIT Manipal in 2024, and I'm an **[AAAI Undergraduate Consortium Scholar](https://aaai-uc.github.io/2023_scholars.html)** (2023 → Mentor, 2026). **[Full experience →](/experience/)**

## Selected Work

<div class="work-grid">
  <a class="work-card" href="https://arxiv.org/abs/2607.19317">
    <span class="work-card__tag">LIBRARY</span>
    <h3 class="work-card__title">CircuitKIT</h3>
    <p class="work-card__desc">Circuit discovery, evaluation, and application toolkit for mechanistic interpretability.</p>
  </a>
  <a class="work-card" href="https://github.com/Lexsi-Labs/SafeTune">
    <span class="work-card__tag">LIBRARY</span>
    <h3 class="work-card__title">SafeTune</h3>
    <p class="work-card__desc">Audits and repairs safety drift in fine-tuned language models.</p>
  </a>
  <a class="work-card" href="https://arxiv.org/abs/2602.09621">
    <span class="work-card__tag">LIBRARY</span>
    <h3 class="work-card__title">AlignTune</h3>
    <p class="work-card__desc">Modular post-training toolkit spanning SFT, DPO, GRPO, and RLHF.</p>
  </a>
  <a class="work-card" href="https://arxiv.org/abs/2606.21631">
    <span class="work-card__tag">LIBRARY</span>
    <h3 class="work-card__title">CuratorKIT</h3>
    <p class="work-card__desc">Provenance-grounded data curation and synthetic generation for LLM post-training.</p>
  </a>
  <a class="work-card" href="https://arxiv.org/abs/2602.04521">
    <span class="work-card__tag">PAPER</span>
    <h3 class="work-card__title">C-ΔΘ</h3>
    <p class="work-card__desc">Circuit-restricted weight arithmetic for selectively modifying refusal behavior.</p>
  </a>
</div>

**[View all research → Publications](/publications/)**

# News
{: #news}

## Recent Publications & Acceptances

<div class="timeline-list" markdown="1">
- <span class="timeline-list__date">2026.07</span>Released **CircuitKIT**, a toolkit for circuit discovery, evaluation, and application in mechanistic interpretability
- <span class="timeline-list__date">2026.07</span>New pre-print: **Faithfulness to Refusal**, a causal audit of neuron selectors used for LLM refusal behavior
- <span class="timeline-list__date">2026.06</span>Released **CuratorKIT**, provenance-grounded data curation and synthetic generation for LLM post-training
- <span class="timeline-list__date">2026.06</span>**ALIGNBEAM** accepted at the AI for Good Workshop, ICML 2026: inference-time alignment transfer via cross-vocabulary logit mixing
- <span class="timeline-list__date">2026.06</span>Released **SafeTune**, a library for auditing and repairing safety drift in fine-tuned LLMs
- <span class="timeline-list__date">2026.05</span>**Distilling Tabular Foundation Models for Structured Health Data** wins Best Paper Runner-Up (Spotlight), SD4H Workshop @ ICML 2026
</div>

<details markdown="1">
<summary>Earlier publications & acceptances</summary>
<div class="timeline-list" markdown="1">
- <span class="timeline-list__date">2026.05</span>**Data Presentation over Architecture: Resampling Strategies for Credit Risk Prediction with Tabular Foundation Models** accepted as an **Oral at FinDS Workshop @ ACM SIGMOD 2026**
- <span class="timeline-list__date">2026.05</span>New Pre-Print: **Position: Behavioural Assurance Cannot Verify the Safety Claims Governance Now Demands**
- <span class="timeline-list__date">2026.05</span>**Pocket Foundation Models: Distilling TFMs into CPU-Ready Gradient-Boosted Trees** accepted at **FMSD Workshop @ ICML 2026**
- <span class="timeline-list__date">2026.05</span>**Ensembling Tabular Foundation Models: A Diversity Ceiling and a Calibration Trap** accepted at **FMSD Workshop @ ICML 2026**
- <span class="timeline-list__date">2026.02</span>New Pre-Print: **AlignTune: Modular Toolkit for Post-Training Alignment of Large Language Models**
- <span class="timeline-list__date">2026.02</span>**C-ΔΘ: Circuit-Restricted Weight Arithmetic for Selective Refusal** accepted at the **Mechanistic Interpretability Workshop @ ICML 2026** — in-person poster, &lt;15% acceptance rate
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

## Academic Service
{: #academic-service-summary}

**Academic service:** AAAI 2027 Program Committee; reviewer for NeurIPS, CVPR, ECCV, ACM AIES, WACV, IJCNN, and workshops across ICML, EMNLP, and COLM.

**[Full service record →](/education-service/#academic-service)**

## Contact

<div class="notice--warning" markdown="1">
**Lexsi Labs — Internships & Full-Time Roles:** For internship and FTE applications at Lexsi Labs, please **apply directly** via [lexsi.ai](https://lexsi.ai) rather than reaching out for referrals.
</div>
<div class="notice--success" markdown="1">
**Mentoring:** I'm occasionally able to advise early-stage researchers. Include a short introduction, your current work, and the specific question you'd like to discuss, and [email me](mailto:seth.pratinav@gmail.com).
</div>
