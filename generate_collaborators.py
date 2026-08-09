"""
Regenerates the "Collaborators" list in _pages/service-skills.md from the
actual co-author lists in _pages/publications.md, instead of hand-maintained
counts. Also syncs the total paper count (front-matter descriptions, the
Total Papers note) to the actual number of papers listed, instead of a
hand-typed figure that can drift — it already had (the hand-typed "48" was
stale; the real count was 46). Run this after adding/removing papers from
Publications.

Usage:
    python3 generate_collaborators.py --write      # regenerate service-skills.md + sync paper count in place
    python3 generate_collaborators.py --markdown   # print the generated block only
    python3 generate_collaborators.py              # print raw counts (debugging)

Institution/relationship metadata (Manager / Mentor / which institution a
collaborator belongs to) is NOT derivable from co-authorship alone, so that
mapping stays in AFFILIATIONS below and must be updated by hand when a new
collaborator appears. The counts themselves are always derived fresh from
the paper list, so they can never drift out of sync with Publications.
"""
import re
import sys
from collections import Counter

PUBLICATIONS_MD = "_pages/publications.md"
SERVICE_SKILLS_MD = "_pages/education-service.md"

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
    with open(PUBLICATIONS_MD, encoding="utf-8") as f:
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


ROLE_TAG = {"mentee": "MENTEE"}  # roles that get an inline tag; "collaborator" gets none


GENERATED_MARKER = "<!-- GENERATED:COLLABORATORS -->"


def render_markdown(counts):
    """Single flat list, one line per person, sorted by co-authored-work
    count descending. Each line carries a ROLE tag (manager/mentor/mentee —
    collaborators get none, since that's the default) and an INSTITUTION
    tag, instead of nesting people under separate role/institution
    headings where the same person could end up listed more than once."""
    people = sorted(counts.items(), key=lambda x: -x[1])

    lines = [GENERATED_MARKER]
    for name, n in people:
        label, role = AFFILIATIONS[name]
        tags = []
        role_tag = ROLE_TAG.get(role, role.upper() if role in ("manager", "mentor") else None)
        if role_tag:
            tags.append(f"<span class='tag'>{role_tag}</span>")
        tags.append(f"<span class='tag'>{label.upper()}</span>")
        lines.append(f"- {name} ({n}) {' '.join(tags)}")

    return "\n".join(lines)


def write_service_skills(generated_markdown):
    """Splice the generated single-list block into _pages/education-service.md,
    replacing everything from the GENERATED_MARKER comment up to (not
    including) the closing '</details>'."""
    with open(SERVICE_SKILLS_MD, encoding="utf-8") as f:
        lines = f.readlines()

    start_idx = end_idx = None
    for i, l in enumerate(lines):
        if l.rstrip("\n") == GENERATED_MARKER or l.rstrip("\n") == "## Managers":
            start_idx = i
        if l.rstrip("\n") == "</details>":
            end_idx = i
            break

    if start_idx is None or end_idx is None:
        print(f"Could not find generated-block start / '</details>' markers in {SERVICE_SKILLS_MD}", file=sys.stderr)
        sys.exit(1)

    new_lines = lines[:start_idx] + [generated_markdown.rstrip("\n") + "\n", "\n"] + lines[end_idx:]
    with open(SERVICE_SKILLS_MD, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print(f"Wrote generated Collaborators block into {SERVICE_SKILLS_MD}", file=sys.stderr)


# Files (and the "48 papers" phrasing pattern within them) that mention the
# total paper count outside the list itself — front matter descriptions,
# excerpts, and the visible Total Papers note. Kept in sync with the actual
# count so it can't drift the way the hand-typed "48" already had (the real
# count was 46).
PAPER_COUNT_FILES = ["_pages/about.md", "_pages/publications.md", "_config.yml"]
PAPER_COUNT_PATTERN = re.compile(r"\b\d+ papers\b")
TOTAL_PAPERS_NOTE_PATTERN = re.compile(r"Total Papers: \d+\*")


def sync_total_papers(papers_seen):
    for path in PAPER_COUNT_FILES:
        with open(path, encoding="utf-8") as f:
            content = f.read()
        new_content = PAPER_COUNT_PATTERN.sub(f"{papers_seen} papers", content)
        new_content = TOTAL_PAPERS_NOTE_PATTERN.sub(f"Total Papers: {papers_seen}*", new_content)
        if new_content != content:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Synced paper count ({papers_seen}) into {path}", file=sys.stderr)


if __name__ == "__main__":
    counts, papers_seen = main()
    if "--write" in sys.argv:
        write_service_skills(render_markdown(counts))
        sync_total_papers(papers_seen)
    elif "--markdown" in sys.argv:
        print(render_markdown(counts))
    else:
        for name, n in counts.most_common():
            label, rel = AFFILIATIONS.get(name, ("UNKNOWN", "collaborator"))
            print(f"{name} ({n}) — {label} [{rel}]")
