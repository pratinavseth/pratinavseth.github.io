// Site-wide identity and links. Edit here; every page reads from this file.
export const site = {
  name: 'Pratinav Seth',
  url: 'https://pratinavseth.github.io',
  role: 'Lead Research Scientist',
  org: 'Lexsi Labs',
  orgUrl: 'https://lexsi.ai/',
  location: 'India & Paris (remote)',
  // One sentence that answers "what do you work on?" — shown large in the hero.
  thesis: 'I study what survives post-training: how fine-tuning, quantization and deployment change a model’s behaviour, and how to find and repair the circuits responsible.',
  tagline: 'Post-training safety and mechanistic interpretability for language models.',
  description:
    'Pratinav Seth leads the Model Science group at Lexsi Labs, working on post-training safety, alignment and mechanistic interpretability for language models.',
  email: 'seth.pratinav@gmail.com',
  avatar: '/images/profile-summit.jpg',
  cv: '/files/pratinav-seth-cv-full.pdf',
  resume: '/files/pratinav-seth-cv.pdf',
  scholarUser: 'DwBn1fcAAAAJ',
  links: {
    linkedin: 'https://www.linkedin.com/in/pratinav-seth/',
    scholar: 'https://scholar.google.com/citations?user=DwBn1fcAAAAJ',
    github: 'https://github.com/pratinavseth',
    twitter: 'https://twitter.com/pratinavseth',
    orcid: 'https://orcid.org/0009-0001-4525-4464',
    dblp: 'https://dblp.org/pid/305/7312',
    researchgate: 'https://www.researchgate.net/profile/Pratinav_Seth',
  },
  // What people can openly reach out about (shown in the hero and contact block).
  openTo: ['Research collaborations', 'Talks & panels'],
  // GoatCounter site code (the "xxx" in xxx.goatcounter.com). Empty = analytics off.
  goatcounter: '',
  // Google Scholar stats branch written by the citation crawler workflow.
  scholarDataUrl: 'https://raw.githubusercontent.com/pratinavseth/pratinavseth.github.io/google-scholar-stats/gs_data.json',
  keywords: [
    'Pratinav Seth', 'LLM alignment', 'post-training safety', 'mechanistic interpretability', 'AI safety',
    'circuit analysis', 'weight arithmetic', 'RLHF', 'DPO', 'tabular foundation models', 'Lexsi Labs',
  ],
} as const;

export const nav = [
  { href: '/', label: 'About' },
  { href: '/publications/', label: 'Publications' },
  { href: '/experience/', label: 'Experience' },
  { href: '/talks-events/', label: 'Talks' },
  { href: '/writing/', label: 'Writing' },
  { href: '/education-service/', label: 'Education & Service' },
] as const;
