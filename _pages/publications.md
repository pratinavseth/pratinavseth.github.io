---
layout: default
permalink: /publications/
title: "Publications — Pratinav Seth"
description: "46 papers (31 peer-reviewed, 210+ citations) spanning LLM post-training, safety alignment, mechanistic interpretability, and tabular foundation models. Venues include ICML, ACL, WWW, MIDL, and Nature Scientific Reports."
excerpt: "Full publication list: safety post-training & alignment, mechanistic interpretability & XAI, tabular foundation models, and open-source libraries."
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

# Publications <a href='https://scholar.google.com/citations?user=DwBn1fcAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>
{: #publications}

<p class="total-papers-note">Total Papers: 46*<br><small>* counted from the list below; additional work is in internal review and not yet listed here</small></p>

<div class="card--muted" markdown="1">
**Selected Publications**
- [CircuitKIT](https://arxiv.org/abs/2607.19317) — Pre-Print 2026 · Circuit discovery, evaluation, and application toolkit for mechanistic interpretability
- [C-ΔΘ: Circuit-Restricted Weight Arithmetic for Selective Refusal](https://arxiv.org/abs/2602.04521) — **Mechanistic Interpretability Workshop, ICML 2026** · Circuit-level weight edits that instil selective refusal — no inference-time steering, no runtime overhead
- [CuratorKIT](https://arxiv.org/abs/2606.21631) — Pre-Print 2026 · Provenance-grounded data-curation and synthetic-generation pipeline for LLM post-training
- [SafeTune](https://github.com/Lexsi-Labs/SafeTune) — Pre-Print 2026 · Unified library for auditing and repairing safety drift in fine-tuned LLMs
- [AlignTune](https://arxiv.org/abs/2602.09621) — Pre-Print 2026 · One interface for SFT, DPO, GRPO, and RLHF with modular reward framework and interchangeable backends
- [Forgetting That Sticks](https://arxiv.org/abs/2605.15138) — Pre-Print 2026 · Unlearning that survives quantization by identifying and zeroing the circuits that store the target knowledge
- [Interpretability as Alignment](https://arxiv.org/abs/2509.08592) — **EurIPS Workshop 2025 (Spotlight)** · Argues mechanistic interpretability should be a design principle in post-training, not a post-hoc audit
- [TabTune](https://arxiv.org/abs/2511.02802) — **WWW 2026 Demo** · Unified library for tabular foundation model inference, fine-tuning, and benchmarking across 7 architectures
- [Alberta Wells Dataset](https://arxiv.org/pdf/2410.09032) — **ICML 2025** · Satellite benchmark for detecting abandoned oil & gas wells; climate AI work with Mila / McGill
- [SELF-PERCEPT](https://aclanthology.org/2025.acl-short.52/) — **ACL 2025** · LLM introspection improves detection of multi-person mental manipulation in multi-turn conversations
</div>


#### Safety Post-Training & Alignment

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Pre-Print</div><img src='https://cdn.prod.website-files.com/690097e1da2dba144068cad2/699ab40523bab49830cce949_699ab3b9de2e66a74a06fd6a_4384885e.png' alt="AlignTune" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[AlignTune: Modular Toolkit for Post-Training Alignment of Large Language Models](https://arxiv.org/abs/2602.09621)

R E Zera Marveen Lyngkhoi, Chirag Chawla, **Pratinav Seth**, Utsav Avaiya, Soham Bhattacharjee, Mykola Khandoga, Rui Yuan, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Mech Interp Workshop, ICML 2026</div><img src='https://cdn.prod.website-files.com/690097e1da2dba144068cad2/698b87dd6f0ed0e2b76c8093_fig_1_cthetha.png' alt="C-ΔΘ" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[C-ΔΘ: Circuit-Restricted Weight Arithmetic for Selective Refusal](https://arxiv.org/abs/2602.04521)

Aditya Kasliwal, **Pratinav Seth**, Vinay Kumar Sankarapu

Accepted at the **Mechanistic Interpretability Workshop, ICML 2026** (in-person poster; <15% acceptance rate)

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AI for Good Workshop, ICML 2026</div><img src='/images/alignbeam-fig.png' alt="ALIGNBEAM" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ALIGNBEAM: Inference-Time Alignment Transfer via Cross-Vocabulary Logit Mixing](https://arxiv.org/abs/2606.12342)

Chirag Chawla, **Pratinav Seth**, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Pre-Print</div><img src='/images/forgetting-that-sticks-fig.png' alt="Forgetting That Sticks" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Forgetting That Sticks: Quantization-Permanent Unlearning via Circuit Attribution](https://arxiv.org/abs/2605.15138)

Saisab Sadhu, **Pratinav Seth**, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Pre-Print</div><img src='/images/behavioural-assurance-fig.png' alt="Position: Behavioural Assurance" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Position: Behavioural Assurance Cannot Verify the Safety Claims Governance Now Demands](https://arxiv.org/abs/2605.15164)

**Pratinav Seth**, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

- What Do Compliance Detectors Read? An Audit of Activation Probes and Guard Models, Saisab Sadhu, Aadit Sengupta, Vinay Kumar Sankarapu, **Pratinav Seth**, **Under Review**

- Drift Then Repair: A Controlled Cross-Paradigm Audit of Safety in Fine-Tuned LLMs, **Pratinav Seth**, Anshul Kaushal, Saisab Sadhu, Vinay Kumar Sankarapu, **Under Review**

- Self-Calibrating Weight-Arithmetic Safety-Drift Repair, **Pratinav Seth**, Vinay Kumar Sankarapu, **Under Review**

- The Off-Switch Failure: When Safety-Repair Evaluation Rewards Model Collapse, **Pratinav Seth**, **Under Review**

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Under Review</div><img src='/images/curatorkit-provenance-fig.png' alt="Provenance-Grounded Gating" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Provenance-Grounded Gating and Adaptive Recovery in Synthetic Post-Training Data Curation](https://arxiv.org/abs/2606.11127)

Soham Bhattacharjee, Karun Sharma, Vinay Kumar Sankarapu, **Pratinav Seth**

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

- Document-as-Function: Verifiable Generation of Long-Form Synthetic Documents, Karun Sharma, Soham Bhattacharjee, Vinay Kumar Sankarapu, **Pratinav Seth**, **Under Review**

#### Mechanistic Interpretability & XAI

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EurIPS Workshop 2025</div><img src='/images/interpawarealignmnet.png' alt="Interpretability as Alignment: making internal understanding a design principle, conceptual diagram" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Interpretability as Alignment: Making Internal Understanding a Design Principle](https://arxiv.org/abs/2509.08592)

Aadit Sengupta, **Pratinav Seth**, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">MICCAI Workshop 2025</div><img src='/images/interp-aware-pruning.png' alt="Interpretability-aware pruning pipeline for efficient medical image analysis" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Interpretability-aware pruning for efficient medical image analysis](https://arxiv.org/abs/2507.08330)

Nikita Malik, **Pratinav Seth**, Neeraj Kumar Singh, Chintan Chitroda, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EurIPS Workshop 2025</div><img src='/images/xaimetrics.jpg' alt="Bridging the gap in XAI: reliable metrics for explainability and compliance, diagram" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Bridging the gap in XAI-why reliable metrics matter for explainability and compliance](https://arxiv.org/abs/2502.04695)

**Pratinav Seth**, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IJCNN 2025</div><img src='/images/dlbacktrace.png' alt="DLBacktrace model-agnostic explainability architecture diagram" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[DLBacktrace: A Model Agnostic Explainability for any Deep Learning Models](https://arxiv.org/pdf/2411.12643)

Vinay Kumar Sankarapu, Chintan Chitroda, Yashwardhan Rathore, Neeraj Kumar Singh, **Pratinav Seth**

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:MXK_kJrjxJIC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:MXK_kJrjxJIC'></span></strong>
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Technical Report</div><img src='/images/xai-evals-fig.png' alt="xai_evals" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[xai_evals: A Framework for Evaluating Post-Hoc Local Explanation Methods](https://arxiv.org/pdf/2502.03014)

**Pratinav Seth**, Yashwardhan Rathore, Neeraj Kumar Singh, Chintan Chitroda, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Pre-Print</div><img src='/images/circuitkit-fig.png' alt="CircuitKIT" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[CircuitKIT: Circuit Discovery, Evaluation, and Application Toolkit for Mechanistic Interpretability](https://arxiv.org/abs/2607.19317)

**Pratinav Seth**, Hem Gosalia, Aditya Kasliwal, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Under Review</div><img src='/images/faithfulness-refusal-fig.png' alt="Faithfulness to Refusal" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Faithfulness to Refusal: A Causal Audit of Neuron Selectors in LLMs](https://arxiv.org/abs/2607.05355)

Ananth Eswar, **Pratinav Seth**, Utsav Avaiya, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

- Faithfulness Is Not Actionability: Component Heterogeneity in Discovered Circuits, **Pratinav Seth**, Hem Gosalia, Aditya Kasliwal, Vinay Kumar Sankarapu, **Under Review**

- [DLBacktrace v2: Extending Model-Agnostic Interpretability for LLMs and MoEs with CUDA Acceleration](https://github.com/Lexsi-Labs/DLBacktrace), Neeraj Kumar Singh, **Pratinav Seth**, Omkar Kakade, Chintan Chitroda, Vinay Kumar Sankarapu, **Pre-Print**

#### Tabular Foundation Models & Distillation

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Pre-Print</div><img src='/images/orionmsp.png' alt="Orion-MSP: multi-scale sparse attention for tabular in-context learning, architecture diagram" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Orion-MSP: Multi-Scale Sparse Attention for Tabular In-Context Learning](https://arxiv.org/abs/2511.02818)

Mohamed Bouadi, **Pratinav Seth**, Aditya Tanna, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">WWW 2026</div><img src='/images/orionbix.png' alt="Orion-BiX: bi-axial attention for tabular in-context learning, architecture diagram" width="100%"></div></div>
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

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">WWW 2026</div><img src='/images/tabtune.png' alt="TabTune unified library architecture for tabular foundation model inference and fine-tuning" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[TabTune: A Unified Library for Inference and Fine-Tuning Tabular Foundation Models (Demo)](https://arxiv.org/abs/2511.02802)

Aditya Tanna, **Pratinav Seth**, Mohamed Bouadi, Utsav Avaiya, Vinay Kumar Sankarapu

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">FMSD Workshop, ICML 2026</div><img src='/images/pocket-fm-distillation-fig.png' alt="Pocket Foundation Models distillation pipeline" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Pocket Foundation Models: Distilling TFMs into CPU-Ready Gradient-Boosted Trees](https://arxiv.org/abs/2605.18654)

Aditya Tanna, Nassim Bouarour, Mohamed Bouadi, Vinay Kumar Sankarapu, **Pratinav Seth**
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">FMSD Workshop, ICML 2026</div><img src='/images/ensembling-tfm-fig.png' alt="Ensembling Tabular Foundation Models Pareto frontier" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Ensembling Tabular Foundation Models: A Diversity Ceiling and a Calibration Trap](https://arxiv.org/abs/2605.18696)

Aditya Tanna, Yash Jignesh Desai, **Pratinav Seth**, Mohamed Bouadi, Nassim Bouarour, Vinay Kumar Sankarapu
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">SD4H Workshop, ICML 2026 — Spotlight</div><img src='/images/sd4h-distillation-fig.png' alt="Distilling Tabular Foundation Models for Structured Health Data pipeline" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Distilling Tabular Foundation Models for Structured Health Data](https://arxiv.org/abs/2605.18702)

Aditya Tanna, Nassim Bouarour, Mohamed Bouadi, Vinay Kumar Sankarapu, **Pratinav Seth**

**Best Paper Runner-Up (Spotlight)**
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">FinDS @ ACM SIGMOD 2026 — Oral</div><img src='/images/sigmod-credit-risk-fig.png' alt="Credit default prediction under severe class imbalance pipeline" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Data Presentation over Architecture: Resampling Strategies for Credit Risk Prediction with Tabular Foundation Models](https://arxiv.org/abs/2605.18635)

Aditya Tanna, Mitul Solanki, Mohamed Bouadi, Nassim Bouarour, **Pratinav Seth**, Vinay Kumar Sankarapu
</div>
</div>

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

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025 / CCAI ICLR 2025</div><img src='/images/AWD.png' alt="Alberta Wells Dataset pipeline for pinpointing oil and gas wells from satellite imagery" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Alberta Wells Dataset: Pinpointing Oil and Gas Wells from Satellite Imagery](https://arxiv.org/pdf/2410.09032)

**Pratinav Seth(#)**, Michelle Lin(#), Brefo Dwamena Yaw, Jade Boutot, Mary Kang, David Rolnick


[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:5nxA0vEk-isC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2022 Workshop</div><img src='/images/contrails-fig.png' alt="Predicted contrail segmentation mask" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Performance Evaluation of Deep Segmentation Models for Contrails Detection](https://arxiv.org/abs/2211.14851)

Akshat Bhandari, Sriya Rallabandi, Sanchit Singhal, Aditya Kasliwal, **Pratinav Seth**

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:2osOgNQ5qMEC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

- [Sailing Through Spectra: Unveiling the Potential of Multi-Spectral Information in Marine Debris Segmentation](https://openreview.net/pdf?id=tJPLJS97X4), Dyutit Mohanty, Aditya Kasliwal, Bharath Udapa, **Pratinav Seth**, **The Second Tiny Papers Track at ICLR 2024.** [**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:roLk4NBRz8UC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>

#### Medical Imaging

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">MIDL 2025</div><img src='/images/od_midl.png' alt="Obscure to Observe: lesion-aware MAE for glaucoma detection, model diagram" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Obscure to Observe: A Lesion-Aware MAE for Glaucoma Detection from Retinal Context](https://openreview.net/forum?id=gqLXT8Edf3)

Siddhant Bharadwaj, **Pratinav Seth**, Chandra Sekhar Seelamantula

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">WACV Workshop 2024</div><img src='/images/Diagram_FAIMI.jpg' alt="Pre-training techniques and skin tone bias in skin lesion classification, study diagram" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Does the Fairness of Your Pre-Training Hold Up? Examining the Influence of Pre-Training Techniques on Skin Tone Bias in Skin Lesion Classification](https://openaccess.thecvf.com/content/WACV2024W/Pretrain/papers/Seth_Does_the_Fairness_of_Your_Pre-Training_Hold_Up_Examining_the_WACVW_2024_paper.pdf)

**Pratinav Seth**, Abhilash K Pai

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:LkGwnXOMwfcC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">BrainLes @ MICCAI 2023</div><img src='/images/refuseg-fig.png' alt="Brain MRI slice used in ReFuSeg tumour segmentation" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ReFuSeg: Regularized Multi-Modal Fusion for Precise Brain Tumour Segmentation](https://arxiv.org/pdf/2308.13883)

Aditya Kasliwal, Sankarshanaa Sagaram, Laven Srivastava, **Pratinav Seth**, Adil Khan

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:Y0pCki6q_DkC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2022 Workshop</div><img src='/images/uatta-ens-fig.png' alt="Retinal fundus image used in UATTA-ENS diabetic retinopathy detection" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[UATTA-ENS: Uncertainty Aware Test Time Augmented Ensemble for PIRC Diabetic Retinopathy Detection](https://arxiv.org/pdf/2211.03148)

**Pratinav Seth**, Adil Khan, Ananya Gupta, Saurabh Kumar Mishra, Akshat Bhandhari

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:u-x6o8ySG0sC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

#### Uncertainty & Robustness

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Bayesian DL Workshop, NeurIPS 2021</div><img src='/images/eval-pred-uncertainty-fig.png' alt="F1 score vs retention fraction for single model vs ensemble" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Evaluating Predictive Uncertainty and Robustness to Distributional Shift Using Real World Data](https://arxiv.org/abs/2111.04665)

Kumud Lakara (†), Akshat Bhandari (†), **Pratinav Seth (†)**, Ujjwal Verma

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:u5HHmVD_uO8C) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

- [UATTA-EB: Uncertainty-Aware Test-Time Augmented Ensemble of BERTs for Classifying Common Mental Illnesses on Social Media Posts](https://arxiv.org/pdf/2304.04539), **Pratinav Seth  (†)**, Mihir Agarwal  (†), **1st Tiny Paper Track at ICLR 2023.** [**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:IjCSPb-OGe4C) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Pre-Print</div><img src='/images/fake-training-data-fig.png' alt="Sample low-fidelity synthetic training image" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Analyzing Effects of Fake Training Data on the Performance of Deep Learning Systems](https://arxiv.org/pdf/2303.01268)

**Pratinav Seth  (†)**, Akshat Bhandari (†), Kumud Lakara (†)

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:qjMakFHDy7sC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:qjMakFHDy7sC'></span></strong>
</div>
</div>

#### NLP & AI for Social Good

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2025 / NAACL SRW Workshop 2025</div><img src='/images/Manipulation_Techniques.png' alt="SELF-PERCEPT introspection pipeline for detecting multi-person mental manipulation" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SELF-PERCEPT: Introspection Improves Large Language Models' Detection of Multi-Person Mental Manipulation in Conversations](https://aclanthology.org/2025.acl-short.52/)

Danush Khanna, **Pratinav Seth**, Sidhaarth Sredharan Murali, Aditya Kumar Guru, Siddharth Shukla, Tanuj Tyagi, Sandeep Chaurasia, Kripabandhu Ghosh

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:kNdYIx-mwKoC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:kNdYIx-mwKoC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">3rd Workshop on NLP for Positive Impact @ EMNLP 2024</div><img src='/images/diag2.jpg' alt="AgriLLM transformer pipeline for farmer query handling" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[AgriLLM: Harnessing transformers for farmer queries.](https://arxiv.org/pdf/2407.04721)

 Krish Didwania (†), **Pratinav Seth (†)**, Aditya Kasliwal, Amit Agarwal

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:hqOjcs7Dif8C) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">SemEval-2023 @ ACL 2023</div><img src='/images/sss-semeval-fig.png' alt="Frequency distribution of sexism labels in the SemEval-2023 Task 10 dataset" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SSS at SemEval-2023 Task 10: Explainable Detection of Online Sexism using Majority Voted Fine-Tuned Transformers](https://aclanthology.org/2023.semeval-1.171/)

Sriya Rallabandi, Sanchit Singhal, **Pratinav Seth**

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:zYLM7Y9cAGgC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:zYLM7Y9cAGgC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">BLP 2023 @ EMNLP 2023</div><img src='/images/rsm-nlp-blp-fig.png' alt="Frequency distribution of sentiment labels in the BLP-2023 Task 2 dataset" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[RSM-NLP at BLP-2023 Task 2: Bangla Sentiment Analysis using Weighted and Majority Voted Fine-Tuned Transformers](https://aclanthology.org/2023.banglalp-1.40/)

**Pratinav Seth**, Rashi Goel, Komal Mathur, Swetha Vemulapalli

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:ufrVoPGSRksC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:ufrVoPGSRksC'></span></strong>
</div>
</div>

- [HGP-NLP at Shared Task: Leveraging LoRA for Lay Summarization of Biomedical Research Articles using Seq2Seq Transformers](https://aclanthology.org/2024.bionlp-1.78.pdf), Hemang Malik, Gaurav Pradeep, **Pratinav Seth**, **Accepted at BioNLP 2024 Workshop, ACL 2024.** [**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:0EnyYjriUFMC) <strong><span class='show_paper_citations' data='DwBn1fcAAAAJ:0EnyYjriUFMC'></span></strong>

#### Vision & Super-Resolution

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR Workshop 2023</div><img src='/images/unet-f.png' alt="CoReFusion contrastive regularized fusion architecture for thermal super-resolution" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[CoReFusion: Contrastive Regularized Fusion for Guided Thermal Super-Resolution](https://openaccess.thecvf.com/content/CVPR2023W/PBVS/html/Kasliwal_CoReFusion_Contrastive_Regularized_Fusion_for_Guided_Thermal_Super-Resolution_CVPRW_2023_paper.html)

Aditya Kasliwal, **Pratinav Seth**, Sriya Rallabandi, Sanchit Singhal

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:UeHWp8X0CEIC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI Student Abstract 2024</div><img src='/images/img3.jpg' alt="LaMAR Laplacian pyramid architecture for multimodal adaptive super resolution" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[LaMAR: Laplacian Pyramid for Multimodal Adaptive Super Resolution (Student Abstract)](https://ojs.aaai.org/index.php/AAAI/article/download/30463/32568)

Aditya Kasliwal, Aryan Kamani, Ishaan Gakhar, **Pratinav Seth**, Sriya Rallabandi

[**Citations**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DwBn1fcAAAAJ&citation_for_view=DwBn1fcAAAAJ:Se3iqnhoufwC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Scientific Reports (Nature)</div><img src='/images/LAPGSR.jpg' alt="Laplacian reconstructive network architecture for guided thermal super-resolution" width="100%"></div></div>
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


