"""
Regenerates the "Collaborators" list in _pages/about.md from the actual
co-author lists in the Publications section, instead of hand-maintained
counts. Run this after adding/removing papers from Publications.

Institution/relationship metadata (Manager / Mentor / which institution a
collaborator belongs to) is NOT derivable from co-authorship alone, so that
mapping stays in AFFILIATIONS below and must be updated by hand when a new
collaborator appears. The counts themselves are always derived fresh from
the paper list, so they can never drift out of sync with Publications.
"""
import re
import sys
from collections import Counter

ABOUT_MD = "_pages/about.md"

# Author -> (institution label, relationship: "manager" | "mentor" | "mentee" | "collaborator")
# Only used for grouping/labelling; counts are always computed from papers.
AFFILIATIONS = {
    "Vinay Kumar Sankarapu": ("Lexsi Labs / AryaXAI Alignment Labs", "manager"),
    "Chintan Chitroda": ("AryaXAI Alignment Labs", "manager"),
    "David Rolnick": ("Mila / McGill", "mentor"),
    "Abhilash K Pai": ("MIT MAHE", "mentor"),
    "Ujjwal Verma": ("MIT MAHE", "mentor"),

    "Aditya Kasliwal": ("Lexsi Labs", "mentee"),
    "Aditya Tanna": ("Lexsi Labs", "mentee"),
    "Utsav Avaiya": ("Lexsi Labs", "mentee"),
    "Saisab Sadhu": ("Lexsi Labs", "mentee"),
    "Chirag Chawla": ("Lexsi Labs", "mentee"),
    "Soham Bhattacharjee": ("Lexsi Labs", "mentee"),
    "Nikita Malik": ("Lexsi Labs", "mentee"),
    "Aadit Sengupta": ("Lexsi Labs", "mentee"),
    "R E Zera Marveen Lyngkhoi": ("Lexsi Labs", "mentee"),
    "Hem Gosalia": ("Lexsi Labs", "mentee"),
    "Ananth Eswar": ("Lexsi Labs", "mentee"),
    "Anshul Kaushal": ("Lexsi Labs", "mentee"),
    "Karun Sharma": ("Lexsi Labs", "mentee"),
    "Omkar Kakade": ("Lexsi Labs", "mentee"),
    "Mitul Solanki": ("Lexsi Labs", "mentee"),

    "Mohamed Bouadi": ("Lexsi Labs — Paris", "collaborator"),
    "Nassim Bouarour": ("Lexsi Labs — Paris", "collaborator"),
    "Mykola Khandoga": ("Lexsi Labs — Paris", "collaborator"),
    "Rui Yuan": ("Lexsi Labs — Paris", "collaborator"),
    "Yash Jignesh Desai": ("Lexsi Labs — Paris", "collaborator"),

    "Yashwardhan Rathore": ("AryaXAI Alignment Labs", "collaborator"),
    "Neeraj Kumar Singh": ("AryaXAI Alignment Labs", "collaborator"),

    "Akshat Bhandari": ("Mars Rover Manipal", "collaborator"),
    "Sriya Rallabandi": ("Mars Rover Manipal", "collaborator"),
    "Sanchit Singhal": ("Mars Rover Manipal", "collaborator"),
    "Kumud Lakara": ("Mars Rover Manipal", "collaborator"),
    "Aryan Kamani": ("Mars Rover Manipal", "collaborator"),
    "Ishaan Gakhar": ("Mars Rover Manipal", "collaborator"),
    "Adil Khan": ("Mars Rover Manipal", "collaborator"),
    "Ananya Gupta": ("Mars Rover Manipal", "collaborator"),
    "Saurabh Kumar Mishra": ("Mars Rover Manipal", "collaborator"),
    "Krish Didwania": ("Mars Rover Manipal", "collaborator"),
    "Laven Srivastava": ("Mars Rover Manipal", "collaborator"),
    "Sankarshanaa Sagaram": ("Mars Rover Manipal", "collaborator"),

    "Mihir Agarwal": ("Research Society Manipal", "collaborator"),
    "Dyutit Mohanty": ("Research Society Manipal", "collaborator"),
    "Bharath Udapa": ("Research Society Manipal", "collaborator"),
    "Rashi Goel": ("Research Society Manipal", "collaborator"),
    "Komal Mathur": ("Research Society Manipal", "collaborator"),
    "Swetha Vemulapalli": ("Research Society Manipal", "collaborator"),
    "Hemang Malik": ("Research Society Manipal", "collaborator"),
    "Gaurav Pradeep": ("Research Society Manipal", "collaborator"),

    "Siddhant Bharadwaj": ("MIT Manipal / IISc Bangalore", "collaborator"),
    "Chandra Sekhar Seelamantula": ("MIT Manipal / IISc Bangalore", "collaborator"),

    "Danush Khanna": ("Manipal University Jaipur", "collaborator"),
    "Aditya Kumar Guru": ("Manipal University Jaipur", "collaborator"),
    "Siddharth Shukla": ("Manipal University Jaipur", "collaborator"),
    "Tanuj Tyagi": ("Manipal University Jaipur", "collaborator"),
    "Sandeep Chaurasia": ("Manipal University Jaipur", "collaborator"),
    "Kripabandhu Ghosh": ("Manipal University Jaipur", "collaborator"),

    "Sidhaarth Sredharan Murali": ("NIT Surathkal", "collaborator"),

    "Jade Boutot": ("McGill University", "collaborator"),
    "Mary Kang": ("McGill University", "collaborator"),
    "Michelle Lin": ("McGill University", "collaborator"),
    "Brefo Dwamena Yaw": ("McGill University", "collaborator"),

    "Amit Agarwal": ("Wells Fargo AI COE", "collaborator"),
}

# Spelling variants of the same person across different papers (source data
# is inconsistent) -> canonical name used in AFFILIATIONS above.
ALIASES = {
    "Akshat Bhandhari": "Akshat Bhandari",
}

VENUE_KEYWORDS = re.compile(
    r"\b(Workshop|Conference|Track|Proceedings|Pre-?Print|Report|Under Review|"
    r"Accepted|Journal|Oral|Spotlight|Demo|arXiv|Best Paper|Runner-Up)\b",
    re.IGNORECASE,
)
HAS_DIGIT = re.compile(r"\d")
NAME_SUFFIX = re.compile(r"\s*(\(#\)|\(†\)|\(\*\*\)|\(\*\)|\*\*|\*|\(†\s*\))\s*$")


def clean_name(raw):
    name = raw.strip()
    name = name.strip("*")
    name = NAME_SUFFIX.sub("", name).strip()
    name = NAME_SUFFIX.sub("", name).strip()  # run twice for combos like " (†)**"
    name = name.strip("*").strip()
    name = ALIASES.get(name, name)
    return name


def is_venue_like(segment):
    s = segment.strip().strip("*").strip()
    if not s:
        return True
    if VENUE_KEYWORDS.search(s):
        return True
    if HAS_DIGIT.search(s):
        return True
    if s.startswith("[") or s.startswith("http"):
        return True
    return False


def extract_authors_from_line(line):
    text = line.strip()
    if not text:
        return None
    if not re.search(r"Pratinav Seth", text):
        return None
    if text.startswith("[**Citations**]") or text.startswith("<"):
        return None

    # Bullet lines: strip a leading "- " then a leading "[Title](url)," or "Title,"
    if text.startswith("- "):
        text = text[2:].strip()
        m = re.match(r"^\[[^\]]*\]\([^)]*\)\s*,\s*", text)
        if m:
            text = text[m.end():]
        else:
            m2 = re.match(r"^[^,]*,\s*", text)
            if m2:
                text = text[m2.end():]
            else:
                return None
    elif text.startswith("["):
        # a stray title line with no authors on it
        return None

    # Cut off anything from a Citations link onward
    text = text.split("[**Citations**]")[0]

    segments = [s for s in text.split(",")]
    authors = []
    for seg in segments:
        if is_venue_like(seg):
            break
        name = clean_name(seg)
        if name and re.search(r"[A-Za-z]", name):
            authors.append(name)
    return authors if authors else None


def main():
    with open(ABOUT_MD, encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    start = end = None
    for i, l in enumerate(lines):
        if re.match(r"^#\s*(📝\s*)?Publications\b", l):
            start = i
        elif start is not None and end is None and i > start and re.match(r"^#\s+[A-Z]", l) and "Publications" not in l:
            end = i
            break
    if start is None:
        print("Could not find Publications section header", file=sys.stderr)
        sys.exit(1)
    if end is None:
        end = len(lines)

    section = lines[start:end]

    # Exclude the "Selected Publications" curated card (duplicate of papers
    # counted below) and "Libraries & Toolkits" (no author lists) and
    # "Selected Blog Posts" (not papers) from counting.
    counted_lines = []
    skip = False
    for l in section:
        if re.match(r"^<div class=\"card--muted\"", l):
            skip = True
        if re.match(r"^</div>", l) and skip:
            skip = False
            continue
        if re.match(r"^####\s*(Libraries & Toolkits|Selected Blog Posts)", l):
            skip = "until-next-heading"
        elif re.match(r"^####\s", l) and skip == "until-next-heading":
            skip = False
        if skip:
            continue
        counted_lines.append(l)

    counts = Counter()
    papers_seen = 0
    for l in counted_lines:
        authors = extract_authors_from_line(l)
        if authors is None:
            continue
        papers_seen += 1
        for a in authors:
            if a == "Pratinav Seth":
                continue
            counts[a] += 1

    print(f"Parsed {papers_seen} paper author-lines.", file=sys.stderr)

    unmapped = sorted(set(counts) - set(AFFILIATIONS))
    if unmapped:
        print("WARNING: authors found with no AFFILIATIONS entry (add them to the script):", file=sys.stderr)
        for u in unmapped:
            print(f"  - {u} ({counts[u]})", file=sys.stderr)

    return counts, papers_seen


def render_group(names_counts, group_by_label=True):
    """names_counts: list of (name, count). Groups by institution label,
    preserving institution order of first appearance, sorted by count desc
    within each group."""
    out = []
    seen_labels = []
    by_label = {}
    for name, n in names_counts:
        label, _rel = AFFILIATIONS[name]
        by_label.setdefault(label, []).append((name, n))
        if label not in seen_labels:
            seen_labels.append(label)
    for label in seen_labels:
        entries = sorted(by_label[label], key=lambda x: -x[1])
        if group_by_label:
            out.append(f"\n**{label}**")
        for name, n in entries:
            suffix = f" ({n})"
            out.append(f"- {name}{suffix}")
    return "\n".join(out)


def render_markdown(counts):
    managers = [(n, c) for n, c in counts.items() if AFFILIATIONS[n][1] == "manager"]
    mentors = [(n, c) for n, c in counts.items() if AFFILIATIONS[n][1] == "mentor"]
    mentees = [(n, c) for n, c in counts.items() if AFFILIATIONS[n][1] == "mentee"]
    # "Collaborators" is the comprehensive by-institution index of everyone
    # except managers/mentors (who get their own sections above).
    collaborators = [(n, c) for n, c in counts.items() if AFFILIATIONS[n][1] in ("mentee", "collaborator")]

    managers.sort(key=lambda x: -x[1])
    mentors.sort(key=lambda x: -x[1])
    mentees.sort(key=lambda x: -x[1])
    collaborators.sort(key=lambda x: -x[1])

    parts = ["## Managers"]
    for name, n in managers:
        label, _ = AFFILIATIONS[name]
        suffix = f" ({n})"
        parts.append(f"- {name}{suffix} — {label}")

    parts.append("\n## Mentors")
    for name, n in mentors:
        label, _ = AFFILIATIONS[name]
        suffix = f" ({n})"
        parts.append(f"- {name}{suffix} — {label}")

    parts.append("\n## Mentees")
    parts.append(render_group(mentees))

    # Explicit id: this h2's auto-generated kramdown id would otherwise
    # collide with the page's "# Collaborators & Mentees {: #collaborators}"
    # h1 above it (duplicate IDs on the page).
    parts.append("\n\n## Collaborators\n{: #collaborators-list}")
    parts.append(render_group(collaborators))

    return "\n".join(parts)


if __name__ == "__main__":
    counts, papers_seen = main()
    if "--markdown" in sys.argv:
        print(render_markdown(counts))
    else:
        for name, n in counts.most_common():
            label, rel = AFFILIATIONS.get(name, ("UNKNOWN", "collaborator"))
            print(f"{name} ({n}) — {label} [{rel}]")
