import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('_pages/about.md', 'r', encoding='utf-8') as f:
    content = f.read()

# ── 1. Update description metadata ──────────────────────────────────────────
old_desc = 'description: "Lead Research Scientist at Lexsi Labs. 30+ publications at ICML, ACL, NeurIPS, CVPR, WWW, AAAI. Expertise: LLM post-training (RLHF, DPO, SFT), AI alignment & safety, mechanistic interpretability, agentic systems, coding agents, knowledge distillation."'
new_desc = 'description: "Lead Research Scientist at Lexsi Labs. 30+ publications at ICML, ACL, NeurIPS, CVPR, WWW, AAAI. Works on LLM post-training, safety alignment, mechanistic interpretability, and tabular foundation models."'
if old_desc in content:
    content = content.replace(old_desc, new_desc, 1)
    print("Updated description")
else:
    print("WARNING: old description not found")

# ── 2. Replace Other Work section with sub-categorized content ──────────────
other_work_marker = '#### Other Work\n'
academic_service_marker = '# \U0001f393 Academic Service\n'

ow_start = content.index(other_work_marker)
as_first = content.index(academic_service_marker)

new_other_work = r"""#### Climate Change & Earth Observation

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

"""

# Replace Other Work section
content = content[:ow_start] + new_other_work + '\n' + content[as_first:]
print("Replaced Other Work section")

# ── 3. Remove the duplicate (second Academic Service onwards) ────────────────
first_as_new = content.index(academic_service_marker)
try:
    second_as_new = content.index(academic_service_marker, first_as_new + 1)
    content = content[:second_as_new].rstrip('\n') + '\n'
    print("Removed duplicate section")
except ValueError:
    print("No duplicate found")

# ── 4. Fix Forgetting That Sticks venue in Professional Experience ───────────
old_venue = 'Forgetting That Sticks: Quantization-Permanent Unlearning via Circuit Attribution. 2026. Mechanistic Interpretability Workshop, ICML 2026.'
new_venue = 'Forgetting That Sticks: Quantization-Permanent Unlearning via Circuit Attribution. 2026. Pre-Print.'
if old_venue in content:
    content = content.replace(old_venue, new_venue)
    print("Fixed Forgetting That Sticks venue")
else:
    print("NOTE: Forgetting That Sticks old venue not found (may already be fixed)")

# ── 5. Add Conferences Attended to Events section ───────────────────────────
events_marker = '# \U0001f310 Events & Conferences\n\n'
if events_marker in content:
    conferences_addition = '# \U0001f310 Events & Conferences\n\n## Academic Conferences Attended\n- **EurIPS Workshop on Private AI Governance**, Copenhagen, Denmark (December 2025)\n- **ICML 2025**, Vancouver, Canada\n- **ICLR 2025**\n- **AAAI 2023**, Washington D.C., USA\n\n## Industry Events\n\n'
    content = content.replace(events_marker, conferences_addition, 1)
    print("Added Conferences Attended section")
else:
    print("WARNING: Events marker not found")

with open('_pages/about.md', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nDone! New file length: {len(content.splitlines())} lines")
