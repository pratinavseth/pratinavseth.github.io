---
layout: default
permalink: /experience/
title: "Professional Experience — Pratinav Seth"
description: "Research career from Lead Research Scientist at Lexsi Labs back through Mila Quebec AI Institute, Bosch Research India, and IIT Kharagpur — post-training alignment, mechanistic interpretability, and tabular foundation models."
excerpt: "Research positions, collaborations, leadership roles, and early career experience."
---

# Professional Experience
{: #professional-experience}

## Research Positions

<div class="role-list" markdown="1">
- <span class="role-list__date">2026.04 – Present</span>**Lead Research Scientist** at [Lexsi Labs, Lexsi.ai](https://lexsi.ai/) (Aurionpro Solutions Group), Remote
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

- <span class="role-list__date">2025.07 – 2026.03</span>**Research Scientist** at [Lexsi Labs, Lexsi.ai](https://lexsi.ai/) (Aurionpro Solutions Group) *[Previously: AryaXAI, Arya.ai]*, Remote
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

- <span class="role-list__date">2024.07 – 2025.06</span>**Research Scientist** at [AryaXAI Alignment Labs](https://www.aryaxai.com/) *(rebranded to Lexsi Labs in 2025)*, Remote / Mumbai, India
  - **Research Focus**: Working at the intersection of Explainable AI (XAI), AI alignment, and AI safety in high-stakes domains—interpreting black-box models, assessing XAI reliability, and developing foundation models for tabular data in fraud detection and mission-critical applications
  - **Explainability**: Enhanced the DL-Backtrace method by generalizing its mechanics for model-agnostic use; co-developed a benchmarking framework for the systematic evaluation of XAI techniques
  - **XAI-Guided Optimization & Alignment**: Investigating model-agnostic post-hoc optimization and alignment strategies across various model architectures—leveraging interpretability for safer, more reliable model behavior
  - **Leadership & Mentorship**: Mentored two research interns; led recruitment of interns and full-time scientists (Paris and India); authored technical and research documentation for stakeholders; initiated proof-of-concept (POC) projects to advance internal algorithmic capabilities
  - **Representation**: Served as R&D representative in client-facing engagements and presented AryaXAI solutions at industry forums, including the 5th MLOps Conference
  - **Publications**:
    - DL-Backtrace: A Model-Agnostic Explainability Method for Deep Learning Models. Accepted at IJCNN 2025.
    - XAI Evals: A Framework for Evaluating Post-Hoc Local Explanation Methods. Technical Report, 2025.
    - Bridging the Gap in XAI: Why Reliable Metrics Matter for Explainability and Compliance. Accepted at EurIPS Workshop on Private AI Governance, 2025.

- <span class="role-list__date">2024.01 – 2024.06</span>Research Intern at [Rolnick Lab, Mila Quebec AI Institute](https://davidrolnick.com/lab/), Remote
  - **Project**: Computer vision and deep learning for geospatial applications targeting climate change
  - **Focus**: Detecting abandoned oil and gas wells from satellite imagery; created new geospatial dataset and benchmarked deep learning models
  - **Mentor**: Dr. David Rolnick (McGill University, Université de Montréal, Mila)
  - **Outcome**: Led to ICML 2025 publication on Alberta Wells Dataset

- <span class="role-list__date">2023.06 – 2023.10</span>Computer Vision Research Intern at [Robert Bosch Research and Technology Center India](https://www.linkedin.com/in/pratinav-seth/), Bangalore
  - **Project**: Vision-based generative AI for autonomous driving using Latent Diffusion Models
  - **Focus**: Generating additional data for difficult or misclassified samples to improve downstream task network optimization
  - **Mentors**: Mr. Koustav Mullick (CR/RDT-2), Dr. Amit Kale
  
- <span class="role-list__date">2021.03 – 2024.01</span>Research Progression at [Mars Rover Manipal](https://www.marsrovermanipal.com/research)
  - Advanced from Trainee to Senior Researcher and Mentor
  - Led AI research initiatives leading to multiple publications at NeurIPS, ACL, AAAI, CVPR, etc. with projects in Generative AI, Medical Image Analysis, and Climate Change.
  - Built a team of 10+ members and mentored them in their research.


- <span class="role-list__date">2023.04 – 2023.12</span>Research Assistant under [Dr. Abhilash K. Pai](https://sites.google.com/site/abhilashkpai), Dept. of DSCA, MIT MAHE
  - Focused on medical image analysis and fairness in AI. 
  - Worked on a study on effects of pretraining techniques on skin tone bias in skin lesion classification with support from MAHE Undergraduate Research Grant leading to a publication at Pre-Train Workshop at WACV 2024.
</div>

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


