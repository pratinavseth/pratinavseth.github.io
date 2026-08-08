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
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>
# Hi, I'm Pratinav Seth! 👋  

I am a **Lead Research Scientist** at **[Lexsi Labs](https://lexsi.ai/)**, leading the Model Science group (16 interns and 8 full-time researchers) across India and Paris. I work on LLM post-training — safety alignment, mechanistic interpretability, and foundation models for structured data — with a growing focus on AI agents and evaluation. I have **48 papers overall (31 peer-reviewed, 210+ citations, h-index 8)** at ICML, ACL, WWW, MIDL, and Nature Scientific Reports. I completed my B.Tech in Data Science from MIT Manipal in 2024. Before Lexsi Labs, I worked at **[Mila Quebec AI Institute](https://mila.quebec/en)** (with Prof. David Rolnick), **[Bosch Research India](https://www.bosch.in/our-company/bosch-in-india/bangalore/)**, and **[IIT Kharagpur](https://iitkliv.github.io/)**. I am an **[AAAI Undergraduate Consortium Scholar](https://aaai-uc.github.io/2023_scholars.html)** (2023 → Mentor, 2026).

Recent work: [AlignTune](https://arxiv.org/abs/2602.09621) · [CircuitKIT](https://arxiv.org/abs/2607.19317) · [C-ΔΘ](https://arxiv.org/abs/2602.04521) · [CuratorKIT](https://arxiv.org/abs/2606.21631) · [SafeTune](https://github.com/Lexsi-Labs/SafeTune) · [Forgetting That Sticks](https://arxiv.org/abs/2605.15138) · [TabTune](https://arxiv.org/abs/2511.02802) · [Orion-MSP](https://arxiv.org/abs/2511.02818)

Feel free to reach out or see my **[Resume](https://linktr.ee/pratinavseth)**.

---

I started in computer vision and medical imaging — uncertainty quantification, model fairness, and segmentation with teams at IIT Kharagpur and Bosch Research. Moving into language models, I kept running into the same problem: a model that looked aligned on benchmarks would fail in ways that weren't visible from the outside. That gap — between what training instils and what survives deployment — became the question I keep returning to. On the safety side, I study how fine-tuning and quantization silently erode alignment, and how to find and repair the specific weights responsible using mechanistic interpretability: circuit-level refusal ([C-ΔΘ](https://arxiv.org/abs/2602.04521)), quantization-permanent unlearning ([Forgetting That Sticks](https://arxiv.org/abs/2605.15138)), and safety drift auditing. On the structured data side, I work on tabular foundation models — how to train, fine-tune, and distil them down to something deployable ([TabTune](https://arxiv.org/abs/2511.02802), [Orion-MSP](https://arxiv.org/abs/2511.02818), [Orion-BiX](https://huggingface.co/Lexsi/Orion-BiX)). Most of this ships as open-source tools. The next problems I care most about are safety in reasoning models and interpretability for agentic systems.

<div style="margin: 1em 0 1.5em 0;">
  <span style="display:inline-block;background:#e8f5e9;color:#2e7d32;border-radius:12px;padding:3px 12px;margin:3px 4px 3px 0;font-size:0.85em;font-weight:600;">AI Alignment &amp; Safety</span>
  <span style="display:inline-block;background:#e8f5e9;color:#2e7d32;border-radius:12px;padding:3px 12px;margin:3px 4px 3px 0;font-size:0.85em;font-weight:600;">Mechanistic Interpretability</span>
  <span style="display:inline-block;background:#e3f2fd;color:#1565c0;border-radius:12px;padding:3px 12px;margin:3px 4px 3px 0;font-size:0.85em;font-weight:600;">LLM Post-Training</span>
  <span style="display:inline-block;background:#e3f2fd;color:#1565c0;border-radius:12px;padding:3px 12px;margin:3px 4px 3px 0;font-size:0.85em;font-weight:600;">RLHF &amp; DPO</span>
  <span style="display:inline-block;background:#f3e5f5;color:#4a148c;border-radius:12px;padding:3px 12px;margin:3px 4px 3px 0;font-size:0.85em;font-weight:600;">Safety Fine-Tuning</span>
  <span style="display:inline-block;background:#fce4ec;color:#880e4f;border-radius:12px;padding:3px 12px;margin:3px 4px 3px 0;font-size:0.85em;font-weight:600;">Agentic Systems</span>
  <span style="display:inline-block;background:#fff3e0;color:#e65100;border-radius:12px;padding:3px 12px;margin:3px 4px 3px 0;font-size:0.85em;font-weight:600;">Tabular Foundation Models</span>
  <span style="display:inline-block;background:#fff3e0;color:#e65100;border-radius:12px;padding:3px 12px;margin:3px 4px 3px 0;font-size:0.85em;font-weight:600;">Knowledge Distillation</span>
  <span style="display:inline-block;background:#fce4ec;color:#880e4f;border-radius:12px;padding:3px 12px;margin:3px 4px 3px 0;font-size:0.85em;font-weight:600;">XAI</span>
</div>

## 🚀 Key Highlights
- 📚 **48 Papers Overall — 31 Peer-Reviewed** (210+ citations, h-index 8) at **ICML, ACL, WWW, MIDL, IJCNN, AAAI, Nature Scientific Reports**, plus workshops and shared tasks at CVPR, NeurIPS, ICLR, MICCAI, EurIPS, ACL, and SIGMOD.
- 🔬 **Research Focus**: LLM safety post-training — circuit-level mechanistic interpretability, safety weight arithmetic, unlearning, post-training alignment, and a growing focus on AI agents & evaluation.
- 🧰 **7 Open-Source Libraries Released**: TabTune (116⭐, WWW 2026), AlignTune (37⭐), DLBacktrace v2 (26⭐), CuratorKIT (24⭐), xai_evals (15⭐), CircuitKIT (14⭐), SafeTune (7⭐).
- 🏆 **AAAI Undergraduate Consortium Scholar** & Mentor (2023 → 2026).
- 🎤 **Spotlight Talk** at EurIPS Workshop on Private AI Governance, Copenhagen (December 2025).

<div style="background:#fff8e1;border-left:4px solid #f9a825;padding:10px 16px;border-radius:4px;margin-bottom:0.6em;font-size:0.9em;">
  <strong>📢 Lexsi Labs — Internships & Full-Time Roles:</strong> For internship and FTE applications at Lexsi Labs, please <strong>apply directly</strong> via <a href="https://lexsi.ai">lexsi.ai</a> rather than reaching out for referrals.
</div>
<div style="background:#e8f5e9;border-left:4px solid #43a047;padding:10px 16px;border-radius:4px;margin-bottom:1.2em;font-size:0.9em;">
  <strong>🎓 Mentoring:</strong> I am open to mentoring early-stage and young researchers. If you'd like to connect, feel free to <a href="mailto:seth.pratinav@gmail.com">reach out via email</a> — please be respectful of my time and include a brief note about your background and what you're working on.
</div>


# 🔥 News

## Recent Publications & Acceptances
- *2026.07*: &nbsp;🎉 New Pre-Print: **CircuitKIT: Circuit Discovery, Evaluation, and Application Toolkit for Mechanistic Interpretability**!
- *2026.07*: &nbsp;🎉 New Pre-Print: **Faithfulness to Refusal: A Causal Audit of Neuron Selectors in LLMs**!
- *2026.06*: &nbsp;🎉 New Pre-Print: **CuratorKIT: Data Curation and Synthetic Data Generation for LLM Post-Training**!
- *2026.06*: &nbsp;🎉 New Pre-Print: **ALIGNBEAM: Inference-Time Alignment Transfer via Cross-Vocabulary Logit Mixing**, accepted at **AI for Good Workshop @ ICML 2026**!
- *2026.06*: &nbsp;🎉 New library release: **SafeTune** — a unified library for auditing and repairing safety drift in fine-tuned LLMs!
- *2026.05*: &nbsp;🎉 **Data Presentation over Architecture: Resampling Strategies for Credit Risk Prediction with Tabular Foundation Models** accepted as an **Oral at FinDS Workshop @ ACM SIGMOD 2026**!
- *2026.05*: &nbsp;🎉 **Distilling Tabular Foundation Models for Structured Health Data** wins **Best Paper Runner-Up (Spotlight)** at **SD4H Workshop @ ICML 2026**!
- *2026.05*: &nbsp;🎉 New Pre-Print: **Position: Behavioural Assurance Cannot Verify the Safety Claims Governance Now Demands**!
- *2026.05*: &nbsp;🎉 **Pocket Foundation Models: Distilling TFMs into CPU-Ready Gradient-Boosted Trees** accepted at **FMSD Workshop @ ICML 2026**!
- *2026.05*: &nbsp;🎉 **Ensembling Tabular Foundation Models: A Diversity Ceiling and a Calibration Trap** accepted at **FMSD Workshop @ ICML 2026**!
- *2026.02*: &nbsp;🎉 New Pre-Print: **AlignTune: Modular Toolkit for Post-Training Alignment of Large Language Models**!
- *2026.02*: &nbsp;🎉 New Pre-Print: **C-ΔΘ: Circuit-Restricted Weight Arithmetic for Selective Refusal**!
- *2026.01*: &nbsp;🎉 **Orion-Bix: Bi-Axial Attention for Tabular In-Context Learning** accepted at **WWW 2026**!
- *2026.01*: &nbsp;🎉 **Exploring Fine-Tuning for Tabular Foundation Models** accepted at **WWW 2026**!
- *2026.01*: &nbsp;🎉 **TabTune: A Unified Library for Inference and Fine-Tuning Tabular Foundation Models (Demo)** accepted at **WWW 2026**!
- *2026.01*: &nbsp;🎉 **Laplacian reconstructive network for guided thermal super-resolution** accepted at **Scientific Reports (Nature)**!
- *2025.11*: &nbsp;🎉 **Interpretability as Alignment: Making Internal Understanding a Design Principle** accepted at **EurIPS Workshop on Private AI Governance**!
- *2025.11*: &nbsp;🎉 **Bridging the gap in XAI-why reliable metrics matter for explainability and compliance** accepted at **EurIPS Workshop on Private AI Governance**!
- *2025.11*: &nbsp;🎉 **EurIPS Workshop on Private AI Governance 2025 Spotlight Talk**!
- *2025.09*: &nbsp;🎉 **Interpretability-aware pruning for efficient medical image analysis** accepted at **MICCAI Workshop 2025**!
- *2025.05*: &nbsp;🎉 **SELF-PERCEPT: Mental Manipulation Detection** accepted at **ACL 2025**!
- *2025.05*: &nbsp;🎉 **Alberta Wells Dataset** accepted at **ICML 2025**! (Really Grateful to the Team for their efforts and Prof. David Rolnick)!

## Academic Service & Reviewing
- *2026.07*: &nbsp;📝 **Reviewer** for **Actionable Interpretability Workshop @ COLM 2026**
- *2026.07*: &nbsp;📝 **Program Committee** for **AAAI 2027**
- *2026.06*: &nbsp;📝 **Reviewer** for **ACM AIES 2026**
- *2026.06*: &nbsp;📝 **Reviewer** for **System Demonstrations Track @ EMNLP 2026**
- *2026.06*: &nbsp;📝 **Reviewer** for **NLP4PI Workshop @ EMNLP 2026**
- *2026.06*: &nbsp;📝 **Reviewer** for **BlackboxNLP Workshop @ EMNLP 2026**
- *2026.05*: &nbsp;📝 **Reviewer** for **AI for Good Workshop @ ICML 2026**
- *2026.05*: &nbsp;📝 **Reviewer** for **Mechanistic Interpretability Workshop @ ICML 2026**
- *2026.05*: &nbsp;📝 **Reviewer** for **TAIGR Workshop @ ICML 2026**
- *2026.05*: &nbsp;📝 **Reviewer** for **FMSD Workshop @ ICML 2026**
- *2026.05*: &nbsp;📝 **Reviewer** for **FAIMI-BRIDGE-EPIMI Workshop @ MICCAI 2026**
- *2026.05*: &nbsp;📝 **Reviewer** for **WACV 2027**
- *2026.04*: &nbsp;📝 **Reviewer** for **NeurIPS 2026**
- *2026.04*: &nbsp;📝 **Reviewer** for **BMVC 2026**
- *2026.03*: &nbsp;📝 **Reviewer** for **ECCV 2026**
- *2026.03*: &nbsp;📝 **Reviewer** for **FinDS Workshop @ ACM SIGMOD 2026**
- *2026.02*: &nbsp;📝 **Reviewer** for **Advances in Financial AI Workshop (ICLR 2026)**
- *2026.01*: &nbsp;📝 **Reviewer** for **CVPR 2026**
- *2025.12*: &nbsp;📝 **Mentor** at **AAAI Undergraduate Consortium 2026**

# 📝 Publications <a href='https://scholar.google.com/citations?user=DwBn1fcAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>

<div style="background:#f8f9fa;border:1px solid #dee2e6;border-radius:6px;padding:14px 18px;margin-bottom:1.5em;">
  <strong>Selected Publications</strong>
  <ul style="margin:0.5em 0 0 0;padding-left:1.2em;">
    <li><a href="https://arxiv.org/abs/2607.19317">CircuitKIT</a> — Pre-Print 2026 · Circuit discovery, evaluation, and application toolkit for mechanistic interpretability (14+ GitHub stars)</li>
    <li><a href="https://arxiv.org/abs/2602.04521">C-ΔΘ: Circuit-Restricted Weight Arithmetic for Selective Refusal</a> — <strong>Mechanistic Interpretability Workshop, ICML 2026</strong> · Circuit-level weight edits that instil selective refusal — no inference-time steering, no runtime overhead</li>
    <li><a href="https://arxiv.org/abs/2606.21631">CuratorKIT</a> — Pre-Print 2026 · Provenance-grounded data-curation and synthetic-generation pipeline for LLM post-training (24+ GitHub stars)</li>
    <li><a href="https://github.com/Lexsi-Labs/SafeTune">SafeTune</a> — Pre-Print 2026 · Unified library for auditing and repairing safety drift in fine-tuned LLMs (7+ GitHub stars)</li>
    <li><a href="https://arxiv.org/abs/2602.09621">AlignTune</a> — Pre-Print 2026 · One interface for SFT, DPO, GRPO, and RLHF with modular reward framework and interchangeable backends (37+ GitHub stars)</li>
    <li><a href="https://arxiv.org/abs/2605.15138">Forgetting That Sticks</a> — Pre-Print 2026 · Unlearning that survives quantization by identifying and zeroing the circuits that store the target knowledge</li>
    <li><a href="https://arxiv.org/abs/2509.08592">Interpretability as Alignment</a> — <strong>EurIPS Workshop 2025 (Spotlight)</strong> · Argues mechanistic interpretability should be a design principle in post-training, not a post-hoc audit</li>
    <li><a href="https://arxiv.org/abs/2511.02802">TabTune</a> — <strong>WWW 2026 Demo</strong> · Unified library for tabular foundation model inference, fine-tuning, and benchmarking across 7 architectures (116+ GitHub stars)</li>
    <li><a href="https://arxiv.org/pdf/2410.09032">Alberta Wells Dataset</a> — <strong>ICML 2025</strong> · Satellite benchmark for detecting abandoned oil & gas wells; climate AI work with Mila / McGill</li>
    <li><a href="https://aclanthology.org/2025.acl-short.52/">SELF-PERCEPT</a> — <strong>ACL 2025</strong> · LLM introspection improves detection of multi-person mental manipulation in multi-turn conversations</li>
  </ul>
</div>


#### Safety Post-Training & Alignment

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Pre-Print</div><img src='https://cdn.prod.website-files.com/690097e1da2dba144068cad2/699ab40523bab49830cce949_699ab3b9de2e66a74a06fd6a_4384885e.png' alt="AlignTune" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[AlignTune: Modular Toolkit for Post-Training Alignment of Large Language Models](https://arxiv.org/abs/2602.09621)

R E Zera Marveen Lyngkhoi, Chirag Chawla, **Pratinav Seth**, Utsav Avaiya, Soham Bhattacharjee, Mykola Khandoga, Rui Yuan, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Pre-Print</div><img src='https://cdn.prod.website-files.com/690097e1da2dba144068cad2/698b87dd6f0ed0e2b76c8093_fig_1_cthetha.png' alt="C-ΔΘ" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[C-ΔΘ: Circuit-Restricted Weight Arithmetic for Selective Refusal](https://arxiv.org/abs/2602.04521)

Aditya Kasliwal, **Pratinav Seth**, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>


- [ALIGNBEAM: Inference-Time Alignment Transfer via Cross-Vocabulary Logit Mixing](https://arxiv.org/abs/2606.12342), Chirag Chawla, **Pratinav Seth**, Vinay Kumar Sankarapu, **AI for Good Workshop, ICML 2026**

- [Forgetting That Sticks: Quantization-Permanent Unlearning via Circuit Attribution](https://arxiv.org/abs/2605.15138), Saisab Sadhu, **Pratinav Seth**, Vinay Kumar Sankarapu, **Pre-Print**

- [Position: Behavioural Assurance Cannot Verify the Safety Claims Governance Now Demands](https://arxiv.org/abs/2605.15164), **Pratinav Seth**, Vinay Kumar Sankarapu, **Pre-Print**

- What Do Compliance Detectors Read? An Audit of Activation Probes and Guard Models, Saisab Sadhu, Aadit Sengupta, Vinay Kumar Sankarapu, **Pratinav Seth**, **Under Review**

- Drift Then Repair: A Controlled Cross-Paradigm Audit of Safety in Fine-Tuned LLMs, **Pratinav Seth**, Anshul Kaushal, Saisab Sadhu, Vinay Kumar Sankarapu, **Under Review**

- Self-Calibrating Weight-Arithmetic Safety-Drift Repair, **Pratinav Seth**, Vinay Kumar Sankarapu, **Under Review**

- The Off-Switch Failure: When Safety-Repair Evaluation Rewards Model Collapse, **Pratinav Seth**, **Under Review**

- [Provenance-Grounded Gating and Adaptive Recovery in Synthetic Post-Training Data Curation](https://arxiv.org/abs/2606.11127), Soham Bhattacharjee, Karun Sharma, Vinay Kumar Sankarapu, **Pratinav Seth**, **Under Review**

- Document-as-Function: Verifiable Generation of Long-Form Synthetic Documents, Karun Sharma, Soham Bhattacharjee, Vinay Kumar Sankarapu, **Pratinav Seth**, **Under Review**

#### Mechanistic Interpretability & XAI

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EurIPS Workshop 2025</div><img src='images/interpawarealignmnet.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Interpretability as Alignment: Making Internal Understanding a Design Principle](https://arxiv.org/abs/2509.08592)

Aadit Sengupta, **Pratinav Seth**, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">MICCAI Workshop 2025</div><img src='images/interp-aware-pruning.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Interpretability-aware pruning for efficient medical image analysis](https://arxiv.org/abs/2507.08330)

Nikita Malik, **Pratinav Seth**, Neeraj Kumar Singh, Chintan Chitroda, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EurIPS Workshop 2025</div><img src='images/xaimetrics.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Bridging the gap in XAI-why reliable metrics matter for explainability and compliance](https://arxiv.org/abs/2502.04695)

**Pratinav Seth**, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IJCNN 2025</div><img src='images/dlbacktrace.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[DLBacktrace: A Model Agnostic Explainability for any Deep Learning Models](https://arxiv.org/pdf/2411.12643)

Vinay Kumar Sankarapu, Chintan Chitroda, Yashwardhan Rathore, Neeraj Kumar Singh, **Pratinav Seth**

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:MXK_kJrjxJIC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:MXK_kJrjxJIC'></span></strong>
</div>
</div>


- [xai_evals: A Framework for Evaluating Post-Hoc Local Explanation Methods](https://arxiv.org/pdf/2502.03014),**Pratinav Seth**, Yashwardhan Rathore, Neeraj Kumar Singh, Chintan Chitroda, Vinay Kumar Sankarapu, **Technical Report** [**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>

- [CircuitKIT: Circuit Discovery, Evaluation, and Application Toolkit for Mechanistic Interpretability](https://arxiv.org/abs/2607.19317), **Pratinav Seth**, Hem Gosalia, Aditya Kasliwal, Vinay Kumar Sankarapu, **Pre-Print**

- [Faithfulness to Refusal: A Causal Audit of Neuron Selectors in LLMs](https://arxiv.org/abs/2607.05355), Ananth Eswar, **Pratinav Seth**, Utsav Avaiya, Vinay Kumar Sankarapu, **Under Review**

- Faithfulness Is Not Actionability: Component Heterogeneity in Discovered Circuits, **Pratinav Seth**, Hem Gosalia, Aditya Kasliwal, Vinay Kumar Sankarapu, **Under Review**

- DLBacktrace v2: Extending Model-Agnostic Interpretability for LLMs and MoEs with CUDA Acceleration, Neeraj Kumar Singh, **Pratinav Seth**, Omkar Kakade, Chintan Chitroda, Vinay Kumar Sankarapu, **Pre-Print**

#### Tabular Foundation Models & Distillation

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Pre-Print</div><img src='images/orionmsp.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Orion-MSP: Multi-Scale Sparse Attention for Tabular In-Context Learning](https://arxiv.org/abs/2511.02818)

Mohamed Bouadi, **Pratinav Seth**, Aditya Tanna, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">WWW 2026</div><img src='images/orionbix.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Orion-BiX: Bi-Axial Attention for Tabular In-Context Learning](https://huggingface.co/Lexsi/Orion-BiX)

Mohamed Bouadi, **Pratinav Seth**, Aditya Tanna, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">WWW 2026</div><img src='https://cdn.prod.website-files.com/690097e1da2dba144068cad2/690b5c2945fcabe3b15d04df_2.jpeg' alt="Exploring Fine-Tuning" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Exploring Fine-Tuning for Tabular Foundation Models](https://arxiv.org/abs/2601.09654)

Aditya Tanna, **Pratinav Seth**, Mohamed Bouadi, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">WWW 2026</div><img src='images/tabtune.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[TabTune: A Unified Library for Inference and Fine-Tuning Tabular Foundation Models (Demo)](https://arxiv.org/abs/2511.02802)

Aditya Tanna, **Pratinav Seth**, Mohamed Bouadi, Utsav Avaiya, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>


- [Pocket Foundation Models: Distilling TFMs into CPU-Ready Gradient-Boosted Trees](https://arxiv.org/abs/2605.18654), Aditya Tanna, Nassim Bouarour, Mohamed Bouadi, Vinay Kumar Sankarapu, **Pratinav Seth**, **Foundation Models for Structured Data (FMSD) Workshop, ICML 2026**

- [Ensembling Tabular Foundation Models: A Diversity Ceiling and a Calibration Trap](https://arxiv.org/abs/2605.18696), Aditya Tanna, Yash Jignesh Desai, **Pratinav Seth**, Mohamed Bouadi, Nassim Bouarour, Vinay Kumar Sankarapu, **Foundation Models for Structured Data (FMSD) Workshop, ICML 2026**

- [Distilling Tabular Foundation Models for Structured Health Data](https://arxiv.org/abs/2605.18702), Aditya Tanna, Nassim Bouarour, Mohamed Bouadi, Vinay Kumar Sankarapu, **Pratinav Seth**, **Structured Data for Health (SD4H) Workshop, ICML 2026 — Best Paper Runner-Up, Spotlight**

- [Data Presentation over Architecture: Resampling Strategies for Credit Risk Prediction with Tabular Foundation Models](https://arxiv.org/abs/2605.18635), Aditya Tanna, Mitul Solanki, Mohamed Bouadi, Nassim Bouarour, **Pratinav Seth**, Vinay Kumar Sankarapu, **FinDS Workshop @ ACM SIGMOD 2026 (Oral)**

<!-- Position: Institutional Tabular Foundation Models: Rethinking AI for Enterprise Decision-Making — Aditya Tanna, Nassim Bouarour, Mohamed Bouadi, Pratinav Seth, Vinay Kumar Sankarapu — Pre-Print (link pending) -->

#### Libraries & Toolkits

*Designed and built the initial release of each library below.*

- [TabTune](https://arxiv.org/abs/2511.02802) — Unified inference and fine-tuning library for tabular foundation models across 7 architectures. **WWW 2026 Demo** (116⭐).
- [AlignTune](https://arxiv.org/abs/2602.09621) — Modular post-training toolkit: SFT, DPO, GRPO, and RLHF with interchangeable backends. **Pre-Print 2026** (37⭐).
- [DLBacktrace v2](https://github.com/AryaXAI/DLBacktrace) — `torch.export`-based, model-agnostic explainability for LLMs and MoEs with CUDA acceleration. **Pre-Print 2026** (26⭐).
- [CuratorKIT](https://arxiv.org/abs/2606.21631) — Provenance-grounded data-curation and synthetic-generation pipeline for LLM post-training. **Pre-Print 2026** (24⭐).
- [xai_evals](https://arxiv.org/pdf/2502.03014) — Framework for evaluating post-hoc local explanation methods. **Technical Report 2025** (15⭐).
- [CircuitKIT](https://arxiv.org/abs/2607.19317) — Circuit discovery, evaluation, and application toolkit for mechanistic interpretability. **Pre-Print 2026** (14⭐).
- [SafeTune](https://github.com/Lexsi-Labs/SafeTune) — Unified library for auditing and repairing safety drift in fine-tuned LLMs. **Pre-Print 2026** (7⭐).
- [DLBacktrace (v1)](https://arxiv.org/pdf/2411.12643) — Model-agnostic explainability for deep learning models. **IJCNN 2025.**

*In development: multiple additional tools across interpretability, post-training alignment, and LLM safety.*

#### Climate Change & Earth Observation

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025 / CCAI ICLR 2025</div><img src='images/AWD.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Alberta Wells Dataset: Pinpointing Oil and Gas Wells from Satellite Imagery](https://arxiv.org/pdf/2410.09032)

**Pratinav Seth(#)**, Michelle Lin(#), Brefo Dwamena Yaw, Jade Boutot, Mary Kang, David Rolnick


[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:5nxA0vEk-isC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

- [Performance Evaluation of Deep Segmentation Models for Contrails Detection](https://arxiv.org/abs/2111.04665), Akshat Bhandari, Sriya Rallabandi, Sanchit Singhal, Aditya Kasliwal, **Pratinav Seth**, **Tackling Climate Change with Machine Learning Workshop at NeurIPS 2022.** [**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:2osOgNQ5qMEC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>

- [Sailing Through Spectra: Unveiling the Potential of Multi-Spectral Information in Marine Debris Segmentation](https://openreview.net/pdf?id=tJPLJS97X4), Dyutit Mohanty, Aditya Kasliwal, Bharath Udapa, **Pratinav Seth**, **The Second Tiny Papers Track at ICLR 2024.** [**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:roLk4NBRz8UC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>

#### Medical Imaging

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">MIDL 2025</div><img src='images/od_midl.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Obscure to Observe: A Lesion-Aware MAE for Glaucoma Detection from Retinal Context](https://openreview.net/forum?id=gqLXT8Edf3)

Siddhant Bharadwaj, **Pratinav Seth**, Chandra Sekhar Seelamantula

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">WACV Workshop 2024</div><img src='images/Diagram_FAIMI.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Does the Fairness of Your Pre-Training Hold Up? Examining the Influence of Pre-Training Techniques on Skin Tone Bias in Skin Lesion Classification](https://openaccess.thecvf.com/content/WACV2024W/Pretrain/papers/Seth_Does_the_Fairness_of_Your_Pre-Training_Hold_Up_Examining_the_WACVW_2024_paper.pdf)

**Pratinav Seth**, Abhilash K Pai

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:LkGwnXOMwfcC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

- [ReFuSeg: Regularized Multi-Modal Fusion for Precise Brain Tumour Segmentation](https://arxiv.org/pdf/2308.13883), Aditya Kasliwal, Sankarshanaa Sagaram, Laven Srivastava, **Pratinav Seth**, Adil Khan, **9th Edition of the Brain Lesion (BrainLes) workshop, MICCAI 2023.** [**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:Y0pCki6q_DkC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>

- [UATTA-ENS: Uncertainty Aware Test Time Augmented Ensemble for PIRC Diabetic Retinopathy Detection](https://arxiv.org/pdf/2211.03148), **Pratinav Seth**, Adil Khan, Ananya Gupta, Saurabh Kumar Mishra, Akshat Bhandhari, **Medical Imaging meets NeurIPS Workshop, NeurIPS 2022.** [**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:u-x6o8ySG0sC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>

#### Uncertainty & Robustness

- [Evaluating Predictive Uncertainty and Robustness to Distributional Shift Using Real World Data](https://arxiv.org/abs/2111.04665), Kumud Lakara (†), Akshat Bhandari (†), **Pratinav Seth (†)**, Ujjwal Verma, **Bayesian Deep Learning Workshop, NeurIPS 2021.** [**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:u5HHmVD_uO8C) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>

- [UATTA-EB: Uncertainty-Aware Test-Time Augmented Ensemble of BERTs for Classifying Common Mental Illnesses on Social Media Posts](https://arxiv.org/pdf/2304.04539), **Pratinav Seth  (†)**, Mihir Agarwal  (†), **1st Tiny Paper Track at ICLR 2023.** [**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:IjCSPb-OGe4C) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>

- [Analyzing Effects of Fake Training Data on the Performance of Deep Learning Systems](https://arxiv.org/pdf/2303.01268), **Pratinav Seth  (†)**, Akshat Bhandari (†), Kumud Lakara (†), **Pre-Print** [**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:qjMakFHDy7sC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:qjMakFHDy7sC'></span></strong>

#### NLP & AI for Social Good

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2025 / NAACL SRW Workshop 2025</div><img src='images/Manipulation_Techniques.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SELF-PERCEPT: Introspection Improves Large Language Models' Detection of Multi-Person Mental Manipulation in Conversations](https://aclanthology.org/2025.acl-short.52/)

Danush Khanna, **Pratinav Seth**, Sidhaarth Sredharan Murali, Aditya Kumar Guru, Siddharth Shukla, Tanuj Tyagi, Sandeep Chaurasia, Kripabandhu Ghosh

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">3rd Workshop on NLP for Positive Impact @ EMNLP 2024</div><img src='images/diag2.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[AgriLLM: Harnessing transformers for farmer queries.](https://arxiv.org/pdf/2407.04721)

 Krish Didwania (†), **Pratinav Seth (†)**, Aditya Kasliwal, Amit Agarwal

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:hqOjcs7Dif8C) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

- [SSS at SemEval-2023 Task 10: Explainable Detection of Online Sexism using Majority Voted Fine-Tuned Transformers](https://aclanthology.org/2023.semeval-1.171/), Sriya Rallabandi, Sanchit Singhal, **Pratinav Seth**, **Proceedings of the 17th International Workshop on Semantic Evaluation (SemEval-2023), ACL 2023** [**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:zYLM7Y9cAGgC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:zYLM7Y9cAGgC'></span></strong>

- [RSM-NLP at BLP-2023 Task 2: Bangla Sentiment Analysis using Weighted and Majority Voted Fine-Tuned Transformers](https://aclanthology.org/2023.banglalp-1.40/), **Pratinav Seth**, Rashi Goel, Komal Mathur, Swetha Vemulapalli, **Proceedings of the 1st Workshop on Bangla Language Processing (BLP 2023), EMNLP 2023** [**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:ufrVoPGSRksC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:ufrVoPGSRksC'></span></strong>

- [HGP-NLP at Shared Task: Leveraging LoRA for Lay Summarization of Biomedical Research Articles using Seq2Seq Transformers](https://aclanthology.org/2024.bionlp-1.78.pdf), Hemang Malik, Gaurav Pradeep, **Pratinav Seth**, **Accepted at BioNLP 2024 Workshop, ACL 2024.** [**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:0EnyYjriUFMC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:0EnyYjriUFMC'></span></strong>

#### Vision & Super-Resolution

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR Workshop 2023</div><img src='images/unet-f.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[CoReFusion: Contrastive Regularized Fusion for Guided Thermal Super-Resolution](https://openaccess.thecvf.com/content/CVPR2023W/PBVS/html/Kasliwal_CoReFusion_Contrastive_Regularized_Fusion_for_Guided_Thermal_Super-Resolution_CVPRW_2023_paper.html)

Aditya Kasliwal, **Pratinav Seth**, Sriya Rallabandi, Sanchit Singhal

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:UeHWp8X0CEIC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI Student Abstract 2024</div><img src='images/img3.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[LaMAR: Laplacian Pyramid for Multimodal Adaptive Super Resolution (Student Abstract)](https://ojs.aaai.org/index.php/AAAI/article/download/30463/32568)

Aditya Kasliwal, Aryan Kamani, Ishaan Gakhar, **Pratinav Seth**, Sriya Rallabandi

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:Se3iqnhoufwC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Scientific Reports (Nature)</div><img src='images/LAPGSR.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Laplacian reconstructive network for guided thermal super-resolution](https://doi.org/10.1038/s41598-026-36027-x)

Aditya Kasliwal, Ishaan Gakhar, Aryan Kamani, **Pratinav Seth**, Ujjwal Verma

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:8k81kl-MbHgC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

#### Selected Blog Posts

- [Retail Banking Case Study: Why Specialists Beat Generalists on Template-Strict Workflows](https://lexsi.ai/resources/articles/retail-banking-case-study-why-specialists-beat-generalists-on-template-strict-workflows-wpx7b), Chirag Chawla, Zera Lyngkhoi, **Pratinav Seth**, Utsav Avaiya, Soham Bhattacharjee, Mykola Khandoga, Rui Yuan, Vinay Kumar Sankarapu, **Lexsi Labs, 2026**
- [The Specialization Dividend: Aligning a 4B Model for Wealth Management Using AlignTune](https://lexsi.ai/resources/articles/the-specialization-dividend-aligning-a-4b-model-for-wealth-management-using-aligntune), Chirag Chawla, Zera Lyngkhoi, **Pratinav Seth**, Utsav Avaiya, Soham Bhattacharjee, Mykola Khandoga, Rui Yuan, Vinay Kumar Sankarapu, **Lexsi Labs, 2026**
- [Now Shipping: TabTune Regression for Tabular Foundation Models](https://lexsi.ai/resources/articles/now-shipping-tabtune-regression-for-tabular-foundational-models), Aditya Tanna, **Pratinav Seth**, Mohamed Bouadi, Utsav Avaiya, Vinay Kumar Sankarapu, **Lexsi Labs, 2026**


# 🎓 Academic Service
- **Mentor**: AAAI Undergraduate Consortium 2026 (Scholar 2023 → Mentor 2026)

## Conference Reviewing & Program Committee
- **Main Conference Reviewer**: AAAI 2027 (Program Committee), NeurIPS 2026, ACM AIES 2026, CVPR (2025-26), ECCV (2024-26), ICCV (2025), WACV (2026-27), BMVC 2026, IJCNN (2025)
- **Workshop & Track Reviewer (2026)**:
  - Mechanistic Interpretability Workshop (ICML 2026)
  - AI for Good Workshop (ICML 2026)
  - TAIGR Workshop (ICML 2026)
  - Foundation Models for Structured Data (FMSD) Workshop (ICML 2026)
  - FinDS Workshop @ ACM SIGMOD 2026
  - Advances in Financial AI Workshop (ICLR 2026)
  - BlackboxNLP Workshop (EMNLP 2026)
  - NLP4PI Workshop (EMNLP 2026)
  - System Demonstrations Track (EMNLP 2026)
  - Actionable Interpretability Workshop (COLM 2026)
  - FAIMI-BRIDGE-EPIMI Workshop (MICCAI 2026)
- **Workshop Reviewer (2021–25)**:
  - Actionable Interpretability Workshop (ICML 2025)
  - RegML Workshop (NeurIPS 2025)
  - NLP for Positive Impact Workshop (EMNLP 2024)
  - Bayesian Decision-making and Uncertainty Workshop (NeurIPS 2024)
  - Frontiers in Probabilistic Inference (ICLR 2025)
  - SyntheticData4ML Workshop (NeurIPS 2022-23)
  - FAIMI Workshop (MICCAI 2024)
  - Domain Adaptation and Representation Transfer Workshop (MICCAI 2023)
  - Topological, Algebraic, and Geometric P.R.A. Workshop (CVPR 2023)

# 💻 Professional Experience

## Research Positions
- *2026.04 - Present*, **Lead Research Scientist** at [Lexsi Labs, Lexsi.ai](https://lexsi.ai/) (Aurionpro Solutions Group), Remote
  - **Post-Training & Alignment**: Lead the lab's post-training and alignment research, directing workstreams across interpretability, safety, model optimization, and agents; scaled **AlignTune** (37⭐) into a production-grade multi-backend ecosystem spanning multiple SFT/RL algorithms, model merging, and domain-specific alignment auditing for BFSI, legal, and healthcare; shared applied results in case studies on template-strict domain specialization and wealth-management alignment with AlignTune
  - **Post-Training & Data Curation**: Building **CuratorKIT** (24⭐), a provenance-grounded data-curation and synthetic-generation pipeline; verifiable long-form synthetic document generation, with further work under review
  - **Post-Hoc Interpretability**: Built unified post-hoc explainability tooling (LRP, Integrated Gradients, DL-Backtrace), including LRP- and DLB-based analysis of model refusal behavior
  - **Mechanistic Interpretability**: Lead circuit-level interpretability: built **CircuitKIT** (14⭐), a circuit discovery, evaluation, and application toolkit; co-led **C-ΔΘ**, a circuit-restricted weight-arithmetic method for selective refusal (ICML 2026 Workshop); advised machine unlearning via circuit attribution, with further work on circuit faithfulness under review
  - **Safety & Steering**: Improve safety alignment across the model lifecycle — during training, post-training recovery and fixing, and at inference time. Co-built **SafeTune** (7⭐), a unified library for auditing and repairing safety drift in fine-tuned LLMs; built an inference-time alignment-transfer method (**ALIGNBEAM**, ICML 2026 Workshop); a position paper on the limits of behavioral safety assurance for governance; audited compliance detectors and guard models; further work on safety-drift repair and safety-repair evaluation, under review
  - **Model Optimization**: Lead structured-pruning and quantization work for efficient model deployment
  - **AI & Coding Agents**: Explore agent and coding-agent architectures; early exploration of a self-improving post-training agent and autonomous-research (auto-research) agents
  - **Evaluation**: Built an internal LLM evaluation library
  - **Research-to-Product Integration**: Translate research into production — integrate interpretability, alignment, and safety tooling into the product stack
  - **Team & Delivery**: Lead the Model Science group (16 interns and 8 full-time researchers across India and Paris), covering grants, hiring, roadmap, and overall planning. Team output spans ICML 2026 workshop papers and submissions under review at A* venues (NeurIPS, ACL, and more)
  - **Publications**:
    - AlignTune: Modular Toolkit for Post-Training Alignment of Large Language Models. 2026. Pre-print.
    - CuratorKIT: Data Curation and Synthetic Data Generation for LLM Post-Training. 2026. Pre-print.
    - CircuitKIT: Circuit Discovery, Evaluation, and Application Toolkit for Mechanistic Interpretability. 2026. Pre-print.
    - SafeTune: A Unified Faithful Library for Auditing and Repairing Safety Drift in Fine-Tuned LLMs. 2026. Pre-print.
    - C-ΔΘ: Circuit-Restricted Weight Arithmetic for Selective Refusal. 2026. Mechanistic Interpretability Workshop, ICML 2026.
    - ALIGNBEAM: Inference-Time Alignment Transfer via Cross-Vocabulary Logit Mixing. 2026. AI for Good Workshop, ICML 2026.
    - Forgetting That Sticks: Quantization-Permanent Unlearning via Circuit Attribution. 2026. Pre-Print.
    - Position: Behavioural Assurance Cannot Verify the Safety Claims Governance Now Demands. 2026. Pre-print.

- *2025.07 - 2026.03*, **Research Scientist** at [Lexsi Labs, Lexsi.ai](https://lexsi.ai/) (Aurionpro Solutions Group) *[Previously: AryaXAI, Arya.ai]*, Remote
  - **Model Science Group**: Led and scaled the lab's Model Science group across post-training alignment, safety, and interpretability into a core research team driving the lab's alignment and safety agenda
  - **AlignTune**: Built AlignTune, a modular toolkit for post-training alignment of LLMs spanning SFT, preference optimization, and safety methods (37⭐); formalized the **Interpretability as Alignment** framework (EurIPS 2025 Workshop) as a guiding design principle for the team's alignment work
  - **Interpretability**: Led the lab's interpretability tooling: rearchitected **DLBacktrace v2** on a `torch.export`-based graph-capture design to keep it model-agnostic across architectures, with CUDA acceleration for LLMs and MoEs (26⭐); drove actionable interpretability into model optimization through interpretability-aware pruning for medical imaging (MICCAI Workshop 2025)
  - **Tabular Foundation Models**: Led problem framing, early model design, and benchmarking for the ORION tabular foundation-model series — Orion-BiX (WWW 2026) and Orion-MSP (AITD Workshop @ EurIPS 2025) — and drove its extension to regression
  - **TabTune**: Architected TabTune, an open-source toolkit for inference, fine-tuning, and regression with tabular foundation models (116⭐, WWW 2026 Demo), shipped with an accompanying fine-tuning study; later advised distillation, ensembling (ICML 2026 Workshops), and credit-risk prediction (FinDS @ ACM SIGMOD 2026, Oral) for health and enterprise deployment
  - **Model Compression**: Built an internal pruning and model-compression toolkit, bringing interpretability-guided compression into the production deployment pipeline
  - **Team & Mentorship**: Led the Model Science group (14 interns and 5 full-time researchers during this period across India and Paris) spanning tabular, alignment, and interpretability; worked on grants, hiring, and overall planning
  - **Talks & Posters**: Spotlight talk at EurIPS 2025 Workshop; poster at MICCAI Workshop 2025
  - **Publications**:
    - Interpretability-Aware Pruning for Efficient Medical Image Analysis. 2025. MICCAI Workshop 2025 (LNCS).
    - Interpretability as Alignment: Making Internal Understanding a Design Principle. 2025. Position Paper (Accepted at EurIPS Workshop on Private AI Governance).
    - TabTune: A Unified Library for Inference and Fine-Tuning Tabular Foundation Models. 2026. Accepted at WWW 2026 (Demo).
    - Orion-MSP: Multi-Scale Sparse Attention for Tabular In-Context Learning. 2025. AITD Workshop @ EurIPS 2025.
    - Orion-BiX: Bi-Axial Attention for Tabular In-Context Learning. 2026. Accepted at WWW 2026.
    - Exploring Fine-Tuning for Tabular Foundation Models. 2026. Accepted at WWW 2026.

- *2024.07 - 2025.06*, **Research Scientist** at [AryaXAI Alignment Labs](https://www.aryaxai.com/) *(rebranded to Lexsi Labs in 2025)*, Remote / Mumbai, India
  - **Research Focus**: Working at the intersection of Explainable AI (XAI), AI alignment, and AI safety in high-stakes domains—interpreting black-box models, assessing XAI reliability, and developing foundation models for tabular data in fraud detection and mission-critical applications
  - **Explainability**: Enhanced the DL-Backtrace method by generalizing its mechanics for model-agnostic use; co-developed a benchmarking framework for the systematic evaluation of XAI techniques
  - **XAI-Guided Optimization & Alignment**: Investigating model-agnostic post-hoc optimization and alignment strategies across various model architectures—leveraging interpretability for safer, more reliable model behavior
  - **Leadership & Mentorship**: Mentored two research interns; led recruitment of interns and full-time scientists (Paris and India); authored technical and research documentation for stakeholders; initiated proof-of-concept (POC) projects to advance internal algorithmic capabilities
  - **Representation**: Served as R&D representative in client-facing engagements and presented AryaXAI solutions at industry forums, including the 5th MLOps Conference
  - **Publications**:
    - DL-Backtrace: A Model-Agnostic Explainability Method for Deep Learning Models. Accepted at IJCNN 2025.
    - XAI Evals: A Framework for Evaluating Post-Hoc Local Explanation Methods. Technical Report, 2025.
    - Bridging the Gap in XAI: Why Reliable Metrics Matter for Explainability and Compliance. Accepted at EurIPS Workshop on Private AI Governance, 2025.

- *2024.01 - 2024.06*, Research Intern at [Rolnick Lab, Mila Quebec AI Institute](https://davidrolnick.com/lab/), Remote
  - **Project**: Computer vision and deep learning for geospatial applications targeting climate change
  - **Focus**: Detecting abandoned oil and gas wells from satellite imagery; created new geospatial dataset and benchmarked deep learning models
  - **Mentor**: Dr. David Rolnick (McGill University, Université de Montréal, Mila)
  - **Outcome**: Led to ICML 2025 publication on Alberta Wells Dataset

- *2023.06 - 2023.10*, Computer Vision Research Intern at [Robert Bosch Research and Technology Center India](https://www.linkedin.com/in/pratinav-seth/), Bangalore
  - **Project**: Vision-based generative AI for autonomous driving using Latent Diffusion Models
  - **Focus**: Generating additional data for difficult or misclassified samples to improve downstream task network optimization
  - **Mentors**: Mr. Koustav Mullick (CR/RDT-2), Dr. Amit Kale
  
- *2021.03 - 2024.01*, Research Progression at [Mars Rover Manipal](https://www.marsrovermanipal.com/research)
  - Advanced from Trainee to Senior Researcher and Mentor
  - Led AI research initiatives leading to multiple publications at NeurIPS, ACL, AAAI, CVPR, etc. with projects in Generative AI, Medical Image Analysis, and Climate Change.
  - Built a team of 10+ members and mentored them in their research.


- *2023.04 - 2023.12*, Research Assistant under [Dr. Abhilash K. Pai](https://sites.google.com/site/abhilashkpai), Dept. of DSCA, MIT MAHE
  - Focused on medical image analysis and fairness in AI. 
  - Worked on a study on effects of pretraining techniques on skin tone bias in skin lesion classification with support from MAHE Undergraduate Research Grant leading to a publication at Pre-Train Workshop at WACV 2024.

## Research Collaborations
- *2023.12 - 2024.01*, Research Collaboration with [Dr. Amit Agarwal, Wells Fargo AI COE](https://arxiv.org/abs/2407.04721)
- *2022.05 - 2023.12*, Research Intern at [KLIV Lab, IIT Kharagpur](https://www.linkedin.com/in/pratinav-seth/) under Dr. Debdoot Sheet and mentored by Mr. Rakshith Satish. Worked on integrating domain knowledge in medical image analysis using Graph Convolutional Networks and Explainable AI for chest radiographs.
- *2022.10 - 2023.03*, Research Collaboration with [IIT Roorkee](https://www.linkedin.com/in/pratinav-seth/).

## Leadership Roles
- *2022.09 - 2023.09*, Co-President & AI Research Mentor, [Research Society MIT Manipal](https://www.instagram.com/researchsoc/?hl=en)
- *2022.11 - 2023.08*, Co-founder & Head of AI, [The Data Alchemists](https://www.linkedin.com/company/the-data-alchemists/)

## Early Career Experience
- *2022.06 - 2022.09*, Research Assistant, Dept. of DSCA, MIT MAHE under Dr. Vidya Rao & Dr. Poornima P.K. working on International Cyber Security Data Mining Competition leading to a position of 5th out of 134+ teams.
- *2022.03 - 2022.05*, Machine Learning Intern, [Eedge.ai](https://www.linkedin.com/in/pratinav-seth/)
- *2022.01 - 2022.02*, Data Science (NLP) Intern, [CUREYA](https://www.linkedin.com/in/pratinav-seth/)


# 🎖 Honors and Awards
- *2023.02* One of the 11 Undergraduates Selected as an [AAAI Undergraduate Consortium Scholar 2023](https://aaai-uc.github.io/2023_scholars.html). Included a Travel Grant of $2000 to present at AAAI-23 at Washington DC, USA.
- *2023.01* Received MAHE Undergraduate Research Grant Worth 10K INR for Project : Explainable & Trustworthy Skin Lesion Classification under Dr. Abhilash K. Pai, Dept. of DSCA, Manipal Institute of Technology, MAHE.
- *2022.06* **Top 10 Team** out of 1000+ submissions in **Bajaj Finserv HackRx3.0 Hackathon**.

# 📖 Education
- *2020.10 - 2024.07*, Bachelors of Technology in Data Science & Engineering (B.Tech), Manipal Academy of Higher Education, Manipal, Karnataka, India.
  - **CGPA**: 8.31/10

# 🛠️ Technical Skills

### 🔬 Interpretability
Mechanistic interpretability, circuit analysis & attribution; TransformerLens, Captum, SHAP, LIME, Integrated Gradients, LRP, DL-Backtrace

### 🎯 Post-Training & Alignment
RLHF, DPO, Constitutional AI; PEFT (LoRA, QLoRA, DoRA), TRL (SFTTrainer, DPOTrainer), Axolotl, Unsloth, LlamaFactory, HF Accelerate

### ⚡ LLM Systems & Efficiency
Flash Attention 2, MoE architectures, quantization (bitsandbytes, AutoGPTQ), pruning, ONNX, TensorRT, lm-evaluation-harness

### 🖥️ Deep Learning Systems
CUDA programming, Triton kernels, distributed training (DeepSpeed, FSDP), mixed precision; GPUs: H200, H100, RTX 6000 Pro (multi-GPU)

### 📊 Tabular & Classical ML
XGBoost, LightGBM, CatBoost, TabPFN, Optuna, Ray Tune

### 🤖 AI & Coding Agents
LangChain, LangGraph, Claude Code, Codex, Cursor, Windsurf

### ⚙️ MLOps, Serving & Infra
Weights & Biases, MLflow, Ray, Docker, Slurm, Git, Linux, HPC, HF Hub/Datasets, FAISS, AWS/GCP; vLLM, FastAPI, Flask, Gradio, Streamlit, Ollama

### 💻 Languages & Core Libraries
Python, C++, SQL, Java, C, LaTeX; PyTorch, TensorFlow, Keras, Scikit-Learn, NumPy, Pandas, Seaborn, Matplotlib, OpenCV, PIL, Geopandas, Shapely, NLTK, SpaCy

### 🏅 Certifications
- **Deep Learning Specialization** - DeepLearning.ai
- **6th Summer School on AI** - CVIT IIITH

# 🤝 Collaborators

## Managers
- Vinay Kumar Sankarapu (11) — Lexsi Labs / AryaXAI Alignment Labs
- Chintan Chitroda (3) — AryaXAI Alignment Labs
- Koustav Mullick — Robert Bosch Research India
- Amit Kale — Robert Bosch Research India

## Mentors
- David Rolnick (1) — Mila / McGill
- Abhilash K Pai (1) — MIT MAHE
- Ujjwal Verma (2) — MIT MAHE

## Mentees

**Lexsi Labs**
- Aditya Kasliwal (9)
- Aditya Tanna (7)
- Utsav Avaiya (3)
- Saisab Sadhu (2)
- Chirag Chawla (2)
- Soham Bhattacharjee (2)
- Nikita Malik (1)
- Aadit Sengupta (1)
- R E Zera Marveen Lyngkhoi (1)
- Hem Gosalia (1)
- Ananth Eswar (1)
- Anshul Kaushal (1)
- Karun Sharma (1)

**Manipal University Jaipur**
- Danush Khanna (1)

**Mars Rover Manipal**
- Sriya Rallabandi (4)
- Sanchit Singhal (3)
- Aryan Kamani (2)
- Ishaan Gakhar (2)
- Adil Khan (2)
- Ananya Gupta (1)
- Saurabh Kumar Mishra (1)
- Krish Didwania (1)
- Laven Srivastava (1)

**Research Society Manipal**
- Dyutit Mohanty (1)
- Bharath Udupa (1)
- Rashi Goel (1)
- Komal Mathur (1)
- Swetha Vemulapalli (1)
- Hemang Malik (1)
- Gaurav Pradeep (1)

**AAAI Undergraduate Consortium**
- Hai Le — Singapore

## Collaborators

**Lexsi Labs — India**
- Aditya Kasliwal (9)
- Aditya Tanna (7)
- Neeraj Kumar Singh (3)
- Utsav Avaiya (3)
- Saisab Sadhu (2)
- Chirag Chawla (2)
- Soham Bhattacharjee (2)
- Nikita Malik (1)
- Aadit Sengupta (1)
- R E Zera Marveen Lyngkhoi (1)
- Hem Gosalia (1)
- Ananth Eswar (1)
- Anshul Kaushal (1)
- Karun Sharma (1)

**Lexsi Labs — Paris**
- Mohamed Bouadi (7)
- Nassim Bouarour (3)
- Mykola Khandoga (1)
- Rui Yuan (1)
- Yash Jignesh Desai (1)

**AryaXAI Alignment Labs**
- Yashwardhan Rathore (2)
- Neeraj Kumar Singh (3)

**Mars Rover Manipal**
- Aditya Kasliwal (8)
- Akshat Bhandari (4)
- Sriya Rallabandi (4)
- Sanchit Singhal (3)
- Kumud Lakara (2)
- Aryan Kamani (2)
- Ishaan Gakhar (2)
- Adil Khan (2)
- Ananya Gupta (1)
- Saurabh Kumar Mishra (1)
- Krish Didwania (1)
- Laven Srivastava (1)

**Research Society Manipal**
- Mihir Agarwal (1)
- Dyutit Mohanty (1)
- Bharath Udupa (1)
- Rashi Goel (1)
- Komal Mathur (1)
- Swetha Vemulapalli (1)
- Hemang Malik (1)
- Gaurav Pradeep (1)

**MIT Manipal / IISc Bangalore**
- Siddhant Bharadwaj (1)

**Manipal University Jaipur**
- Danush Khanna (1)
- Aditya Kumar Guru (1)
- Siddharth Shukla (1)
- Tanuj Tyagi (1)

**NIT Surathkal**
- Sidhaarth Sredharan Murali (1)

**McGill University**
- Jade Boutot (1)
- Mary Kang (1)

**Wells Fargo AI COE**
- Amit Agarwal (1)

# 🌐 Events & Conferences

## Academic Conferences Attended
- **ICML 2026**, Seoul, South Korea
- **The Web Conference (WWW) 2026**, Dubai, UAE *(attended remotely)*
- **EurIPS Workshop on Private AI Governance**, Copenhagen, Denmark (December 2025)
- **MICCAI 2025 Workshop**, Daejeon, South Korea
- **ICML 2025**, Vancouver, Canada
- **ICLR 2025**, Singapore
- **AAAI 2023**, Washington D.C., USA

## Industry Events

- *2026.02*, **India AI Impact Summit 2026**, Bharat Mandapam, New Delhi *(representing Lexsi Labs)*
  - Attended **AI Safety Connect Day** hosted by the International Association for Safe and Ethical Artificial Intelligence — discussions on interpretability, transparency, and safety in real-world AI deployment
  - Participated in **closed-door roundtable** by The Dialogue: *"Powering the AI Frontier: Building India's Compute, Infrastructure, and Trust Backbone for Inclusive AI Growth"*
  - Shared Lexsi Labs' work on alignment & RL, interpretability-driven safety, and open-source toolkits; co-organised a post-summit gathering
- *2026.02*, **PyTorch Day Bangalore 2026**, Bangalore
- *2025.12*, **AurionAI Launch Event**, India *(representing Lexsi Labs)*

# 💬 Invited Talks & Presentations

## 2025
- *2025.12*, **EurIPS Spotlight Talk**: *"Interpretability as Alignment: Making Internal Understanding a Design Principle"* at the EurIPS Workshop on Private AI Governance, Copenhagen, Denmark — with Aadit Sengupta
- **AryaXAI Alignment Lab Webinars**:
  - "Inside the Black Box: Interpreting LLMs with DL-Backtrace (DLB)"
  - "Beyond Explainability – Evaluating XAI Methods with Confidence Using xai evals"
  - "Interpretability Aware Pruning in Medical Imagery" (Paper Podcast)

## 2024
- *2024.03*, **Introduction to Research**, at ACM-W Manipal Chapter.
- *2024.02*, Data Dialogue invited by The Data Alchemists, The Official Data Science Club of MIT Manipal.  \| [\[link\]](https://www.instagram.com/p/C2B-pv7v82l/?igsh=OXd3d2J6YTh6aXVt)

## 2023
- *2023.03*, Research as Undergrad, at ACM-W Manipal Chapter.
