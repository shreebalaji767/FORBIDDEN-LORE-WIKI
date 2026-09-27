from pathlib import Path
import json
import random
import html
import textwrap


# ============================================================
# FORBIDDEN LORE WIKI
# Python -> single static HTML5 file
# ============================================================

OUTPUT_DIR = Path("output")
OUTPUT_FILE = OUTPUT_DIR / "index.html"

random.seed(742913)


# ============================================================
# ORIGINAL WORLDS
# ============================================================

WORLDS = [
    {
        "id": "vael-taryn",
        "name": "Vael Taryn",
        "type": "Original World",
        "era": "Ashen Imperial Period",
        "description": (
            "A fictional northern imperial civilization whose surviving "
            "records disagree about the circumstances of its collapse."
        ),
        "regions": [
            "Northern Elarian Basin",
            "Kareth Marches",
            "Seven Provincial Territories",
            "Taryn River Valley",
        ],
        "capital": "Taryn",
        "founded": "842 A.E.",
        "ended": "1454 A.E.",
        "government": "Imperial monarchy",
        "language": "Old Tarynic",
        "currency": "Taryn silver",
    },
    {
        "id": "elaria",
        "name": "Elaria",
        "type": "Original World",
        "era": "Recorded Age",
        "description": (
            "A continent-spanning fictional setting containing competing "
            "kingdoms, forgotten civilizations, maritime republics and "
            "unresolved supernatural traditions."
        ),
        "regions": [
            "Northern Elarian Basin",
            "Ash Coast",
            "Western Marches",
            "Sable Archipelago",
            "Eastern Crownlands",
        ],
        "capital": "No single capital",
        "founded": "Pre-recorded history",
        "ended": "Ongoing",
        "government": "Multiple political systems",
        "language": "Multiple languages",
        "currency": "Regional currencies",
    },
    {
        "id": "ashen-realms",
        "name": "The Ashen Realms",
        "type": "Original World",
        "era": "Post-Cataclysmic Age",
        "description": (
            "A fictional multiregional world reconstructed from fragmented "
            "chronicles following a civilization-ending event."
        ),
        "regions": [
            "The Glass Plains",
            "Ashen Coast",
            "The Hollow North",
            "Crownless Territories",
        ],
        "capital": "Unknown",
        "founded": "After the First Cataclysm",
        "ended": "Ongoing",
        "government": "Fragmented states",
        "language": "Old Common",
        "currency": "Regional",
    },
    {
        "id": "seven-stars",
        "name": "The Seven-Star Continuum",
        "type": "Original World",
        "era": "Astral Historical Period",
        "description": (
            "A fictional cosmic setting in which several civilizations "
            "recorded the same celestial event using incompatible calendars."
        ),
        "regions": [
            "First Sphere",
            "Outer March",
            "The Seven Stations",
            "The Silent Belt",
        ],
        "capital": "Station Seven",
        "founded": "Unknown",
        "ended": "Unknown",
        "government": "Interstellar treaty system",
        "language": "Common Astral",
        "currency": "Station credits",
    },
]


# ============================================================
# ORIGINAL CHARACTERS
# ============================================================

CHARACTERS = [
    {
        "name": "Arven III",
        "world": "Vael Taryn",
        "role": "Emperor",
        "period": "418–447 A.E.",
        "description": (
            "The third ruler to use the title Arven. His reign is associated "
            "with the consolidation of the northern provinces."
        ),
    },
    {
        "name": "Ilyan Voss",
        "world": "Vael Taryn",
        "role": "Military commander",
        "period": "5th century A.E.",
        "description": (
            "A fictional commander whose surviving correspondence suggests "
            "that he opposed the imperial expansion into the Kareth Marches."
        ),
    },
    {
        "name": "Merovan Edras",
        "world": "Elaria",
        "role": "Chronicler",
        "period": "3rd century A.E.",
        "description": (
            "A fictional historian whose chronicle is one of the principal "
            "sources for the early Tarynic period."
        ),
    },
    {
        "name": "Sera Valen",
        "world": "Elaria",
        "role": "Historian",
        "period": "Modern archival period",
        "description": (
            "A fictional academic associated with the revisionist school "
            "of Elarian history."
        ),
    },
    {
        "name": "Cael IV",
        "world": "Vael Taryn",
        "role": "Emperor",
        "period": "Late Imperial Period",
        "description": (
            "A fictional ruler whose reported death is disputed by three "
            "major historical traditions."
        ),
    },
    {
        "name": "Nera Kesh",
        "world": "Ashen Realms",
        "role": "Cartographer",
        "period": "Post-Cataclysmic Age",
        "description": (
            "A fictional mapmaker whose surviving charts contain coastlines "
            "not found on any contemporary map."
        ),
]


# ============================================================
# ORIGINAL EVENTS
# ============================================================

EVENTS = [
    {
        "name": "The First War of Broken Stars",
        "year": "Unknown",
        "world": "Seven-Star Continuum",
        "type": "Cosmic conflict",
        "description": (
            "A disputed fictional event described by several civilizations "
            "as the moment when the seven known celestial domains ceased "
            "to share a common calendar."
        ),
    },
    {
        "name": "The Black Census",
        "year": "611 A.E.",
        "world": "Vael Taryn",
        "type": "Administrative event",
        "description": (
            "A fictional imperial census in which surviving copies list "
            "identical population totals but completely different names."
        ),
    },
    {
        "name": "The Silent Eclipse",
        "year": "1454 A.E.",
        "world": "Vael Taryn",
        "type": "Collapse",
        "description": (
            "The conventional name for the fictional collapse of the "
            "Tarynic imperial capital."
        ),
    },
    {
        "name": "The Battle of Kareth",
        "year": "527 A.E.",
        "world": "Vael Taryn",
        "type": "Battle",
        "description": (
            "A fictional military engagement remembered differently by "
            "imperial and provincial records."
        ),
    },
    {
        "name": "The Glass Rain",
        "year": "Unknown",
        "world": "Ashen Realms",
        "type": "Cataclysm",
        "description": (
            "A fictional environmental disaster described in several "
            "independent regional traditions."
        ),
    },
    {
        "name": "The Seven-Day Silence",
        "year": "Uncertain",
        "world": "Elaria",
        "type": "Historical anomaly",
        "description": (
            "A fictional period during which several independent archives "
            "contain no surviving dated records."
        ),
]


# ============================================================
# ORIGINAL FACTIONS
# ============================================================

FACTIONS = [
    {
        "name": "The Seven Provincial Houses",
        "world": "Vael Taryn",
        "type": "Political alliance",
        "description": (
            "A fictional collection of hereditary provincial families "
            "whose autonomy expanded during the later imperial period."
        ),
    },
    {
        "name": "Order of the Hollow Sun",
        "world": "Elaria",
        "type": "Religious order",
        "description": (
            "A fictional religious institution associated with manuscripts "
            "that describe the sun as an artificial celestial object."
        ),
    },
    {
        "name": "The Unnamed Observers",
        "world": "Seven-Star Continuum",
        "type": "Unknown organization",
        "description": (
            "A fictional organization appearing only in fragments of "
            "astronomical records."
        ),
    },
    {
        "name": "Kareth League",
        "world": "Vael Taryn",
        "type": "Merchant alliance",
        "description": (
            "A fictional commercial coalition controlling several northern "
            "river crossings."
        ),
]


# ============================================================
# ORIGINAL ARTIFACTS
# ============================================================

ARTIFACTS = [
    {
        "name": "The Ninth Imperial Seal",
        "world": "Vael Taryn",
        "classification": "Royal artifact",
        "description": (
            "A fictional seal supposedly belonging to the final imperial "
            "administration. Its authenticity remains disputed."
        ),
    },
    {
        "name": "Kareth Tablet IV",
        "world": "Vael Taryn",
        "classification": "Inscribed tablet",
        "description": (
            "A fictional archaeological fragment containing an incomplete "
            "list of provincial governors."
        ),
    },
    {
        "name": "The Seven-Point Astrolabe",
        "world": "Seven-Star Continuum",
        "classification": "Astronomical instrument",
        "description": (
            "A fictional instrument whose calibration markings do not "
            "correspond to the surviving celestial calendar."
        ),
    },
    {
        "name": "The Black Ledger",
        "world": "Ashen Realms",
        "classification": "Manuscript",
        "description": (
            "A fictional ledger containing hundreds of names with no "
            "corresponding settlements."
        ),
    },
]


# ============================================================
# ORIGINAL DOCUMENTS
# ============================================================

DOCUMENTS = [
    {
        "title": "The Chronicle of Edras",
        "world": "Elaria",
        "date": "3rd century A.E.",
        "type": "Chronicle",
        "status": "Partially preserved",
        "excerpt": (
            "The northern gates were closed before the bells were sounded. "
            "No official proclamation survives explaining why."
        ),
    },
    {
        "title": "The Ninth Imperial Census",
        "world": "Vael Taryn",
        "date": "611 A.E.",
        "type": "Administrative record",
        "status": "Disputed",
        "excerpt": (
            "The population shall be recorded by household, occupation and "
            "province. The surviving copy contains no provincial totals."
        ),
    },
    {
        "title": "Report from the Kareth Excavation",
        "world": "Vael Taryn",
        "date": "Modern archival period",
        "type": "Archaeological report",
        "status": "Restricted",
        "excerpt": (
            "The lower chamber was sealed from the inside. No secondary "
            "entrance has yet been identified."
        ),
    },
    {
        "title": "Station Seven Astronomical Register",
        "world": "Seven-Star Continuum",
        "date": "Unknown",
        "type": "Astronomical record",
        "status": "Incomplete",
        "excerpt": (
            "At the seventh observation the northern light appeared below "
            "the horizon. The observation was repeated three times."
        ),
    },
]


# ============================================================
# CANON REFERENCE CATEGORIES
#
# These are deliberately kept as references/categories rather
# than fabricated "official" canon material.
# ============================================================

CANON_GROUPS = [
    {
        "name": "Anime",
        "items": [
            "Naruto",
            "One Piece",
            "Dragon Ball",
            "Attack on Titan",
            "Fullmetal Alchemist",
            "Death Note",
            "Demon Slayer",
            "Jujutsu Kaisen",
        ],
    },
    {
        "name": "Manhwa",
        "items": [
            "Solo Leveling",
            "Tower of God",
            "Omniscient Reader",
            "The Beginning After the End",
            "The God of High School",
        ],
    },
    {
        "name": "Manhua",
        "items": [
            "Soul Land",
            "The King's Avatar",
            "Battle Through the Heavens",
            "Martial Peak",
        ],
    },
    {
        "name": "Donghua",
        "items": [
            "Chinese animated fantasy",
            "Cultivation animation",
            "Xianxia animation",
            "Wuxia animation",
        ],
    },
    {
        "name": "Light Novels",
        "items": [
            "Re:Zero",
            "Overlord",
            "Mushoku Tensei",
            "That Time I Got Reincarnated as a Slime",
            "Sword Art Online",
        ],
    },
    {
        "name": "Comics",
        "items": [
            "Image Comics",
            "Dark Horse Comics",
            "IDW Publishing",
            "Independent comics",
        ],
    },
    {
        "name": "DC",
        "items": [
            "DC Universe",
            "Batman",
            "Superman",
            "Wonder Woman",
            "Justice League",
            "Green Lantern",
            "The Flash",
        ],
    },
    {
        "name": "Marvel",
        "items": [
            "Marvel Universe",
            "Spider-Man",
            "Avengers",
            "X-Men",
            "Fantastic Four",
            "Guardians of the Galaxy",
        ],
    },
]


# ============================================================
# LEARNING QUESTIONS
# ============================================================

QUESTIONS = [
    "Who created it?",
    "When did it appear?",
    "Where did it originate?",
    "Why did it become important?",
    "How did it change over time?",
    "Who opposed it?",
    "What evidence survives?",
    "What remains uncertain?",
    "Which sources disagree?",
    "What happened afterward?",
    "How does it connect to other events?",
    "Which interpretations are disputed?",
]


# ============================================================
# ARTICLE TYPES
# ============================================================

ARTICLE_TYPES = [
    "Civilization",
    "Character",
    "Historical Event",
    "Faction",
    "Artifact",
    "Document",
    "Battle",
    "Political System",
    "Religion",
    "Technology",
    "Location",
    "Historical Mystery",
    "Cosmic Event",
    "Language",
    "Dynasty",
]


# ============================================================
# UI THEMES
# ============================================================

THEMES = [
    {
        "name": "Midnight Archive",
        "bg": "#090b0f",
        "panel": "#11151b",
        "panel2": "#171c23",
        "text": "#e7e2d5",
        "muted": "#92999f",
        "accent": "#c5a86a",
        "accent2": "#6d849b",
        "line": "#2b3138",
        "paper": "#d9d0bc",
    },
    {
        "name": "Obsidian Library",
        "bg": "#0b0b0b",
        "panel": "#151515",
        "panel2": "#1d1d1d",
        "text": "#eeeeea",
        "muted": "#999991",
        "accent": "#b9b9a9",
        "accent2": "#747d86",
        "line": "#303030",
        "paper": "#ddd9ce",
    },
    {
        "name": "Archive Green",
        "bg": "#07100c",
        "panel": "#0c1912",
        "panel2": "#112319",
        "text": "#d9e4d9",
        "muted": "#829285",
        "accent": "#aabf8e",
        "accent2": "#64877b",
        "line": "#24372b",
        "paper": "#d5dccb",
    },
    {
        "name": "Old Observatory",
        "bg": "#090b14",
        "panel": "#111425",
        "panel2": "#181c31",
        "text": "#e4e5ef",
        "muted": "#9297ad",
        "accent": "#aeb3d6",
        "accent2": "#6c789f",
        "line": "#292e48",
        "paper": "#d9d8ca",
    },
    {
        "name": "Crimson Archive",
        "bg": "#10090b",
        "panel": "#1a1013",
        "panel2": "#251519",
        "text": "#eee1df",
        "muted": "#a38d8d",
        "accent": "#c08a82",
        "accent2": "#80666c",
        "line": "#3b252a",
        "paper": "#ddd0c6",
    },
]


# ============================================================
# LAYOUT PERSONALITIES
# ============================================================

LAYOUTS = [
    "classic",
    "terminal",
    "manuscript",
    "research",
    "museum",
    "minimal",
    "casefile",
]


# ============================================================
# HELPERS
# ============================================================

def esc(value):
    return html.escape(str(value))


def slug(value):
    result = []
    for ch in value.lower():
        if ch.isalnum():
            result.append(ch)
        else:
            result.append("-")
    return "".join(result).strip("-")


def random_item(items):
    return random.choice(items)


def all_lore_names():
    names = []

    names.extend(item["name"] for item in WORLDS)
    names.extend(item["name"] for item in CHARACTERS)
    names.extend(item["name"] for item in EVENTS)
    names.extend(item["name"] for item in FACTIONS)
    names.extend(item["name"] for item in ARTIFACTS)
    names.extend(item["title"] for item in DOCUMENTS)

    return names


def random_lore_reference(exclude=None):
    values = all_lore_names()

    if exclude and len(values) > 1:
        values = [x for x in values if x != exclude]

    return random.choice(values)


def random_year():
    return random.choice([
        "17 A.E.",
        "91 A.E.",
        "238 A.E.",
        "417 A.E.",
        "527 A.E.",
        "611 A.E.",
        "842 A.E.",
        "1021 A.E.",
        "1187 A.E.",
        "1454 A.E.",
        "Unknown",
        "Uncertain",
        "Before recorded history",
    ])


def generated_fake_scholar():
    first = random.choice([
        "Ilyan",
        "Sera",
        "Merovan",
        "Tavian",
        "Neris",
        "Alden",
        "Varo",
        "Edrin",
        "Mira",
        "Calen",
    ])

    last = random.choice([
        "Varek",
        "Valen",
        "Edras",
        "Kesh",
        "Orin",
        "Taryn",
        "Meral",
        "Dovren",
        "Salen",
        "Voss",
    ])

    return f"{first} {last}"


def generated_source_title():
    titles = [
        "Administrative Records of the Northern Provinces",
        "Notes on Early Elarian Chronology",
        "The Northern Annals",
        "Archaeological Survey of the Kareth Basin",
        "Political Institutions of Early Taryn",
        "The Seven Calendars",
        "Studies in Imperial Succession",
        "Fragments of the Old Chronicle",
        "The Ashen Historical Register",
        "Catalogue of Unresolved Inscriptions",
    ]
    return random.choice(titles)


# ============================================================
# DYNAMIC ORIGINAL ARTICLE
# ============================================================

def build_dynamic_article():
    world = random.choice(WORLDS)
    article_type = random.choice(ARTICLE_TYPES)
    year = random_year()
    scholar = generated_fake_scholar()
    related_1 = random_lore_reference()
    related_2 = random_lore_reference(exclude=related_1)
    related_3 = random_lore_reference(exclude=related_1)

    subject_names = [
        f"The {random.choice(['Northern', 'Second', 'Lost', 'Silent', 'Sevenfold', 'Final'])} "
        f"{random.choice(['Dynasty', 'Expedition', 'Census', 'War', 'Treaty', 'Chronicle'])}",
        random.choice(CHARACTERS)["name"],
        random.choice(ARTIFACTS)["name"],
        random.choice(EVENTS)["name"],
        random.choice(FACTIONS)["name"],
    ]

    subject = random.choice(subject_names)

    opening_templates = [
        (
            f"{subject} is generally associated with the {world['name']} "
            f"historical record. Surviving material indicates that it played "
            f"a significant role during the {world['era'].lower()}, although "
            f"the surviving chronology is incomplete."
        ),
        (
            f"Records concerning {subject} are unusually inconsistent. "
            f"The earliest surviving references appear to place it in "
            f"{world['name']} around {year}, but later sources assign it "
            f"a different date."
        ),
        (
            f"Modern researchers use the designation {subject} for a body "
            f"of evidence associated with {world['name']}. The designation "
            f"does not necessarily reflect how the original participants "
            f"understood the subject."
        ),
    ]

    opening = random.choice(opening_templates)

    return {
        "title": subject,
        "subtitle": f"{article_type} · {world['name']}",
        "type": article_type,
        "world": world["name"],
        "year": year,
        "author": scholar,
        "opening": opening,
        "sections": [
            (
                "Historical context",
                f"The available record places the subject within a period of "
                f"political and cultural change. Contemporary accounts are "
                f"limited, and later historians frequently reconstructed the "
                f"sequence of events from incomplete material."
            ),
            (
                "Development",
                f"During the following period, references to {subject} become "
                f"more frequent. Several records suggest that its importance "
                f"was connected to trade, administration, military organization "
                f"or religious practice, although no single interpretation has "
                f"achieved universal acceptance within the fictional historical "
                f"record."
            ),
            (
                "Evidence",
                f"The principal evidence consists of manuscripts, inscriptions, "
                f"administrative fragments and later commentary. Some sources "
                f"appear to have been copied centuries after the events they "
                f"describe, making precise dating difficult."
            ),
            (
                "Competing interpretations",
                f"{scholar} argues that the conventional interpretation places "
                f"too much weight on later chronicles. Other fictional scholars "
                f"maintain that the surviving administrative records provide "
                f"a more reliable chronology."
            ),
            (
                "Unresolved questions",
                f"It remains uncertain whether the surviving records represent "
                f"a complete account. Several references suggest the existence "
                f"of additional documents that have not been recovered."
            ),
        ],
        "questions": random.sample(QUESTIONS, 6),
        "related": [related_1, related_2, related_3],
        "source": generated_source_title(),
        "source_status": random.choice([
            "Disputed",
            "Partially preserved",
            "Reconstructed",
            "Incomplete",
            "Apocryphal",
            "Uncertain",
        ]),
    }


# ============================================================
# STATIC DATA EMBEDDED INTO GENERATED JS
# ============================================================

DATA = {
    "worlds": WORLDS,
    "characters": CHARACTERS,
    "events": EVENTS,
    "factions": FACTIONS,
    "artifacts": ARTIFACTS,
    "documents": DOCUMENTS,
    "canonGroups": CANON_GROUPS,
}


# ============================================================
# HTML GENERATOR
# ============================================================

def build_html():

    theme = random.choice(THEMES)
    layout = random.choice(LAYOUTS)

    dynamic_article = build_dynamic_article()

    data_json = json.dumps(DATA, ensure_ascii=False)

    article_json = json.dumps(dynamic_article, ensure_ascii=False)

    css = f"""
:root {{
    --bg: {theme["bg"]};
    --panel: {theme["panel"]};
    --panel2: {theme["panel2"]};
    --text: {theme["text"]};
    --muted: {theme["muted"]};
    --accent: {theme["accent"]};
    --accent2: {theme["accent2"]};
    --line: {theme["line"]};
    --paper: {theme["paper"]};

    --radius: 14px;
    --shadow: 0 18px 60px rgba(0,0,0,.25);
    --max: 1500px;
}}

* {{
    box-sizing: border-box;
}}

html {{
    scroll-behavior: smooth;
}}

body {{
    margin: 0;
    min-height: 100vh;
    background:
        radial-gradient(
            circle at 15% 10%,
            color-mix(in srgb, var(--accent) 7%, transparent),
            transparent 30%
        ),
        radial-gradient(
            circle at 85% 80%,
            color-mix(in srgb, var(--accent2) 7%, transparent),
            transparent 32%
        ),
        var(--bg);
    color: var(--text);
    font-family:
        Inter,
        ui-sans-serif,
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
    line-height: 1.7;
}}

button,
input,
select {{
    font: inherit;
}}

button {{
    cursor: pointer;
}}

a {{
    color: inherit;
}}

::selection {{
    background: var(--accent);
    color: var(--bg);
}}

.no-script {{
    padding: 16px;
    background: #300;
    color: white;
    text-align: center;
}}

.site {{
    width: min(100%, var(--max));
    margin: auto;
    padding: 18px;
}}

.topbar {{
    position: sticky;
    top: 0;
    z-index: 100;
    backdrop-filter: blur(18px);
    background: color-mix(in srgb, var(--bg) 88%, transparent);
    border-bottom: 1px solid var(--line);
}}

.topbar-inner {{
    width: min(100%, var(--max));
    margin: auto;
    padding: 13px 18px;
    display: flex;
    gap: 18px;
    align-items: center;
}}

.brand {{
    min-width: max-content;
    text-decoration: none;
}}

.brand-title {{
    font-family: Georgia, serif;
    font-size: 1.1rem;
    letter-spacing: .12em;
}}

.brand-sub {{
    color: var(--muted);
    font-size: .67rem;
    letter-spacing: .16em;
    text-transform: uppercase;
}}

.search {{
    flex: 1;
    position: relative;
}}

.search input {{
    width: 100%;
    border: 1px solid var(--line);
    background: var(--panel);
    color: var(--text);
    border-radius: 999px;
    padding: 11px 16px;
    outline: none;
}}

.search input:focus {{
    border-color: var(--accent);
    box-shadow: 0 0 0 3px color-mix(in srgb, var(--accent) 12%, transparent);
}}

.top-actions {{
    display: flex;
    gap: 8px;
}}

.icon-btn,
.action-btn {{
    border: 1px solid var(--line);
    background: var(--panel);
    color: var(--text);
    border-radius: 10px;
    padding: 9px 12px;
}}

.icon-btn:hover,
.action-btn:hover {{
    border-color: var(--accent);
    color: var(--accent);
}}

.app {{
    display: grid;
    grid-template-columns: 245px minmax(0, 1fr);
    gap: 22px;
    margin-top: 22px;
}}

.sidebar {{
    position: sticky;
    top: 83px;
    height: calc(100vh - 105px);
    overflow: auto;
    padding-right: 6px;
}}

.sidebar-section {{
    margin-bottom: 22px;
}}

.sidebar-label {{
    color: var(--muted);
    text-transform: uppercase;
    font-size: .68rem;
    letter-spacing: .16em;
    margin: 0 0 8px;
}}

.nav-item {{
    display: block;
    width: 100%;
    text-align: left;
    border: 0;
    background: transparent;
    color: var(--text);
    padding: 9px 10px;
    border-radius: 9px;
}}

.nav-item:hover {{
    background: var(--panel);
    color: var(--accent);
}}

.main {{
    min-width: 0;
}}

.hero {{
    border: 1px solid var(--line);
    background:
        linear-gradient(
            135deg,
            color-mix(in srgb, var(--accent) 8%, var(--panel)),
            var(--panel)
        );
    border-radius: var(--radius);
    padding: clamp(24px, 5vw, 55px);
    box-shadow: var(--shadow);
    overflow: hidden;
    position: relative;
}}

.hero::after {{
    content: "";
    position: absolute;
    width: 260px;
    height: 260px;
    right: -100px;
    top: -100px;
    border-radius: 50%;
    border: 1px solid color-mix(in srgb, var(--accent) 18%, transparent);
}}

.eyebrow {{
    color: var(--accent);
    text-transform: uppercase;
    letter-spacing: .18em;
    font-size: .7rem;
    font-weight: 700;
}}

.hero h1 {{
    font-family: Georgia, "Times New Roman", serif;
    font-weight: 500;
    font-size: clamp(2rem, 5vw, 4.5rem);
    line-height: 1.03;
    max-width: 900px;
    margin: 12px 0;
}}

.hero p {{
    max-width: 850px;
    color: var(--muted);
    font-size: clamp(.98rem, 1.6vw, 1.16rem);
}}

.hero-meta {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 20px;
}}

.tag {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 5px 9px;
    border: 1px solid var(--line);
    border-radius: 999px;
    color: var(--muted);
    font-size: .74rem;
    background: color-mix(in srgb, var(--panel2) 80%, transparent);
}}

.content-grid {{
    display: grid;
    grid-template-columns: minmax(0, 1fr) 285px;
    gap: 22px;
    margin-top: 22px;
}}

.article {{
    min-width: 0;
}}

.article-card,
.infobox,
.panel,
.timeline,
.related,
.document {{
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: var(--radius);
}}

.article-card {{
    padding: clamp(20px, 4vw, 38px);
}}

.article-header {{
    padding-bottom: 20px;
    margin-bottom: 24px;
    border-bottom: 1px solid var(--line);
}}

.article-header h2 {{
    margin: 5px 0;
    font-family: Georgia, serif;
    font-size: clamp(1.8rem, 4vw, 3rem);
    font-weight: 500;
    line-height: 1.15;
}}

.article-header p {{
    color: var(--muted);
    margin-bottom: 0;
}}

.article-section {{
    margin: 30px 0;
}}

.article-section h3 {{
    font-family: Georgia, serif;
    font-weight: 500;
    font-size: 1.35rem;
    margin-bottom: 8px;
}}

.article-section p {{
    color: color-mix(in srgb, var(--text) 88%, var(--muted));
}}

.callout {{
    margin: 25px 0;
    padding: 17px 19px;
    border-left: 3px solid var(--accent);
    background: color-mix(in srgb, var(--accent) 5%, var(--panel));
}}

.infobox {{
    height: max-content;
    overflow: hidden;
}}

.infobox-title {{
    padding: 16px;
    font-family: Georgia, serif;
    font-size: 1.25rem;
    background: var(--panel2);
    border-bottom: 1px solid var(--line);
}}

.info-row {{
    display: grid;
    grid-template-columns: 40% 60%;
    border-bottom: 1px solid var(--line);
}}

.info-row:last-child {{
    border-bottom: 0;
}}

.info-key,
.info-value {{
    padding: 10px 12px;
}}

.info-key {{
    color: var(--muted);
    font-size: .77rem;
}}

.info-value {{
    font-size: .82rem;
}}

.source-box {{
    margin-top: 22px;
    padding: 17px;
    border: 1px solid var(--line);
    border-radius: var(--radius);
    background: var(--panel2);
}}

.source-status {{
    color: var(--accent);
    font-size: .75rem;
    text-transform: uppercase;
    letter-spacing: .12em;
}}

.source-title {{
    font-family: Georgia, serif;
    margin-top: 6px;
}}

.explore-grid {{
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    margin-top: 22px;
}}

.explore-card {{
    border: 1px solid var(--line);
    background: var(--panel);
    padding: 17px;
    border-radius: var(--radius);
    cursor: pointer;
    transition:
        transform .2s ease,
        border-color .2s ease,
        background .2s ease;
}}

.explore-card:hover {{
    transform: translateY(-3px);
    border-color: var(--accent);
    background: var(--panel2);
}}

.explore-card small {{
    display: block;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: .1em;
    font-size: .63rem;
}}

.explore-card strong {{
    display: block;
    margin-top: 5px;
    font-family: Georgia, serif;
    font-size: 1rem;
}}

.questions {{
    display: grid;
    gap: 8px;
}}

.question {{
    padding: 13px 15px;
    border: 1px solid var(--line);
    border-radius: 10px;
    background: var(--panel2);
}}

.question::before {{
    content: "→";
    color: var(--accent);
    margin-right: 10px;
}}

.timeline {{
    padding: 22px;
    margin-top: 22px;
}}

.timeline-track {{
    display: grid;
    grid-template-columns: repeat(5, minmax(100px, 1fr));
    gap: 10px;
    overflow-x: auto;
}}

.timeline-item {{
    border-left: 2px solid var(--accent);
    padding: 10px 12px;
    min-width: 140px;
}}

.timeline-year {{
    color: var(--accent);
    font-size: .75rem;
}}

.timeline-name {{
    font-family: Georgia, serif;
    margin-top: 5px;
}}

.discovery {{
    margin-top: 22px;
    padding: 22px;
    border: 1px dashed var(--line);
    border-radius: var(--radius);
    background: color-mix(in srgb, var(--accent) 3%, var(--panel));
}}

.discovery-title {{
    color: var(--accent);
    font-size: .7rem;
    text-transform: uppercase;
    letter-spacing: .16em;
}}

.discovery h3 {{
    margin: 8px 0;
    font-family: Georgia, serif;
    font-weight: 500;
}}

.mobile-nav {{
    display: none;
}}

.overlay {{
    display: none;
}}

.search-results {{
    position: absolute;
    z-index: 500;
    left: 0;
    right: 0;
    top: calc(100% + 8px);
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 12px;
    box-shadow: var(--shadow);
    max-height: 360px;
    overflow: auto;
}}

.search-result {{
    padding: 11px 13px;
    border-bottom: 1px solid var(--line);
    cursor: pointer;
}}

.search-result:last-child {{
    border-bottom: 0;
}}

.search-result:hover {{
    background: var(--panel2);
}}

.search-result small {{
    display: block;
    color: var(--muted);
    font-size: .67rem;
}}

.empty {{
    padding: 22px;
    color: var(--muted);
    text-align: center;
}}

.footer {{
    margin: 45px 0 15px;
    padding: 20px 0;
    border-top: 1px solid var(--line);
    color: var(--muted);
    font-size: .76rem;
    display: flex;
    justify-content: space-between;
    gap: 15px;
    flex-wrap: wrap;
}}

body.layout-terminal {{
    font-family: "Courier New", monospace;
}}

body.layout-terminal .hero h1,
body.layout-terminal .article-header h2,
body.layout-terminal h3,
body.layout-terminal .brand-title {{
    font-family: "Courier New", monospace;
}}

body.layout-terminal .hero {{
    border-radius: 3px;
}}

body.layout-manuscript {{
    background:
        radial-gradient(circle at center, #18150f, #080806 70%);
}}

body.layout-manuscript .article-card,
body.layout-manuscript .hero {{
    border-radius: 2px;
}}

body.layout-manuscript .article-card {{
    background:
        linear-gradient(
            rgba(217,208,188,.025),
            rgba(217,208,188,.025)
        ),
        var(--panel);
}}

body.layout-casefile .article-card {{
    border-left: 4px solid var(--accent);
}}

body.layout-museum .explore-card {{
    border-radius: 2px;
}}

body.layout-minimal .sidebar {{
    opacity: .78;
}}

@media (max-width: 1050px) {{
    .app {{
        grid-template-columns: 205px minmax(0, 1fr);
    }}

    .content-grid {{
        grid-template-columns: 1fr;
    }}

    .infobox {{
        display: grid;
        grid-template-columns: repeat(2, 1fr);
    }}

    .infobox-title {{
        grid-column: 1 / -1;
    }}
}}

@media (max-width: 760px) {{
    .site {{
        padding: 10px;
    }}

    .topbar-inner {{
        padding: 10px;
        flex-wrap: wrap;
    }}

    .brand {{
        flex: 1;
    }}

    .search {{
        order: 5;
        flex-basis: 100%;
    }}

    .app {{
        display: block;
    }}

    .sidebar {{
        display: none;
        position: fixed;
        z-index: 300;
        left: 0;
        top: 0;
        bottom: 0;
        width: min(82vw, 320px);
        height: 100vh;
        background: var(--bg);
        border-right: 1px solid var(--line);
        padding: 80px 18px 20px;
    }}

    body.menu-open .sidebar {{
        display: block;
    }}

    .mobile-nav {{
        display: inline-flex;
    }}

    .hero {{
        padding: 25px 19px;
    }}

    .hero h1 {{
        font-size: 2.2rem;
    }}

    .explore-grid {{
        grid-template-columns: 1fr;
    }}

    .infobox {{
        display: block;
    }}

    .timeline-track {{
        grid-template-columns: repeat(5, 145px);
    }}

    .overlay {{
        position: fixed;
        inset: 0;
        z-index: 200;
        background: rgba(0,0,0,.65);
    }}

    body.menu-open .overlay {{
        display: block;
    }}

    .footer {{
        display: block;
    }}

    .footer > * {{
        margin-bottom: 8px;
    }}
}}

@media (max-width: 430px) {{
    .top-actions .desktop-only {{
        display: none;
    }}

    .hero h1 {{
        font-size: 1.9rem;
    }}

    .article-card {{
        padding: 18px 15px;
    }}

    .article-header h2 {{
        font-size: 1.8rem;
    }}
}}

@media (prefers-reduced-motion: reduce) {{
    *,
    *::before,
    *::after {{
        scroll-behavior: auto !important;
        animation-duration: .001ms !important;
        transition-duration: .001ms !important;
    }}
}}
"""

    html_document = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<meta name="description"
      content="Forbidden Lore Archive — an interactive fictional knowledge archive.">

<meta name="theme-color"
      content="{theme["bg"]}">

<title>Forbidden Lore Archive</title>

<style>
{css}
</style>
</head>

<body class="layout-{layout}">

<noscript>
    <div class="no-script">
        JavaScript is required for the interactive archive.
    </div>
</noscript>

<header class="topbar">

    <div class="topbar-inner">

        <button
            class="icon-btn mobile-nav"
            id="menuButton"
            aria-label="Open navigation">
            ☰
        </button>

        <a href="#top" class="brand">
            <div class="brand-title">FORBIDDEN LORE</div>
            <div class="brand-sub">Knowledge Archive</div>
        </a>

        <div class="search">

            <input
                id="searchInput"
                type="search"
                autocomplete="off"
                placeholder="Search the archive..."
                aria-label="Search the archive">

            <div
                id="searchResults"
                class="search-results"
                hidden>
            </div>

        </div>

        <div class="top-actions">

            <button
                class="icon-btn desktop-only"
                id="randomButton"
                title="Discover another article">
                ⤨
            </button>

            <button
                class="icon-btn"
                id="closeMenuButton"
                hidden>
                ×
            </button>

        </div>

    </div>

</header>


<div class="overlay" id="overlay"></div>


<div class="site" id="top">

    <div class="app">

        <aside class="sidebar" id="sidebar">

            <div class="sidebar-section">

                <div class="sidebar-label">
                    Archive
                </div>

                <button class="nav-item" data-action="home">
                    Overview
                </button>

                <button class="nav-item" data-action="random">
                    Random discovery
                </button>

                <button class="nav-item" data-action="timeline">
                    Historical timeline
                </button>

            </div>


            <div class="sidebar-section">

                <div class="sidebar-label">
                    Original worlds
                </div>

                <div id="worldNav"></div>

            </div>


            <div class="sidebar-section">

                <div class="sidebar-label">
                    Reference collections
                </div>

                <div id="canonNav"></div>

            </div>


            <div class="sidebar-section">

                <div class="sidebar-label">
                    Article types
                </div>

                <div id="typeNav"></div>

            </div>

        </aside>


        <main class="main">

            <section class="hero">

                <div class="eyebrow">
                    Archive session
                </div>

                <h1 id="heroTitle">
                    Forbidden Lore Archive
                </h1>

                <p id="heroDescription">
                    A constantly changing reference environment for
                    fictional worlds, histories, characters, documents,
                    civilizations and unresolved mysteries.
                </p>

                <div class="hero-meta">

                    <span class="tag">
                        Static
                    </span>

                    <span class="tag">
                        Browser memory
                    </span>

                    <span class="tag">
                        Session #{random.randint(1000, 9999)}
                    </span>

                    <span class="tag">
                        Interface: {esc(theme["name"])}
                    </span>

                </div>

            </section>


            <div class="content-grid">

                <article class="article">

                    <div class="article-card">

                        <header class="article-header">

                            <div class="eyebrow" id="articleType">
                                {esc(dynamic_article["type"])}
                            </div>

                            <h2 id="articleTitle">
                                {esc(dynamic_article["title"])}
                            </h2>

                            <p id="articleSubtitle">
                                {esc(dynamic_article["subtitle"])}
                            </p>

                        </header>


                        <div id="articleBody">

                        </div>


                        <div class="source-box">

                            <div class="source-status">
                                Source status
                            </div>

                            <div
                                class="source-title"
                                id="sourceStatus">
                                {esc(dynamic_article["source_status"])}
                            </div>

                            <p id="sourceText">
                                This entry belongs to the fictional
                                archive layer. Its internal sources,
                                scholars and documents are part of the
                                constructed setting.
                            </p>

                        </div>

                    </div>


                    <section class="discovery">

                        <div class="discovery-title">
                            Continue your investigation
                        </div>

                        <h3 id="discoveryTitle">
                            Follow the evidence
                        </h3>

                        <p id="discoveryText">
                            Every refresh produces another route through
                            the archive.
                        </p>

                    </section>


                    <section class="timeline" id="timelineSection">

                        <div class="eyebrow">
                            Selected chronology
                        </div>

                        <h3>
                            Related historical sequence
                        </h3>

                        <div
                            class="timeline-track"
                            id="timeline">
                        </div>

                    </section>


                    <section class="explore-grid" id="relatedGrid">
                    </section>

                </article>


                <aside>

                    <div class="infobox">

                        <div class="infobox-title">
                            Archive record
                        </div>

                        <div class="info-row">
                            <div class="info-key">Subject</div>
                            <div class="info-value" id="infoSubject">
                            </div>
                        </div>

                        <div class="info-row">
                            <div class="info-key">World</div>
                            <div class="info-value" id="infoWorld">
                            </div>
                        </div>

                        <div class="info-row">
                            <div class="info-key">Period</div>
                            <div class="info-value" id="infoYear">
                            </div>
                        </div>

                        <div class="info-row">
                            <div class="info-key">Classification</div>
                            <div class="info-value" id="infoType">
                            </div>
                        </div>

                        <div class="info-row">
                            <div class="info-key">Researcher</div>
                            <div class="info-value" id="infoAuthor">
                            </div>
                        </div>

                        <div class="info-row">
                            <div class="info-key">Reference</div>
                            <div class="info-value" id="infoSource">
                            </div>
                        </div>

                    </div>


                    <div class="panel" style="margin-top:22px; padding:18px;">

                        <div class="eyebrow">
                            Questions to investigate
                        </div>

                        <div
                            class="questions"
                            id="questions"
                            style="margin-top:12px;">
                        </div>

                    </div>

                </aside>

            </div>


            <footer class="footer">

                <div>
                    FORBIDDEN LORE ARCHIVE
                </div>

                <div>
                    Original fictional material is identified as such.
                    Canon references are not presented as invented canon.
                </div>

                <div>
                    Session memory only · Refresh resets state
                </div>

            </footer>

        </main>

    </div>

</div>


<script>

"use strict";


// ============================================================
// EMBEDDED DATA
// ============================================================

const ARCHIVE_DATA = {data_json};

const INITIAL_ARTICLE = {article_json};


// ============================================================
// SESSION MEMORY
// ============================================================

const memory = {{
    currentArticle: INITIAL_ARTICLE,
    visited: [],
    searchTerm: "",
    selectedWorld: null,
    selectedType: null,
    menuOpen: false,
    layout: "{layout}",
    theme: "{esc(theme["name"])}"
}};


// ============================================================
// DOM HELPERS
// ============================================================

function $(selector) {{
    return document.querySelector(selector);
}}

function createElement(tag, className, text = "") {{
    const element = document.createElement(tag);

    if (className) {{
        element.className = className;
    }}

    if (text) {{
        element.textContent = text;
    }}

    return element;
}}


// ============================================================
// HTML ESCAPING
// ============================================================

function escapeHTML(value) {{
    const div = document.createElement("div");
    div.textContent = value ?? "";
    return div.innerHTML;
}}


// ============================================================
// ARTICLE RENDERING
// ============================================================

function renderArticle(article) {{

    memory.currentArticle = article;

    if (!memory.visited.includes(article.title)) {{
        memory.visited.push(article.title);
    }}

    $("#articleType").textContent = article.type;

    $("#articleTitle").textContent = article.title;

    $("#articleSubtitle").textContent = article.subtitle;

    $("#infoSubject").textContent = article.title;

    $("#infoWorld").textContent = article.world;

    $("#infoYear").textContent = article.year;

    $("#infoType").textContent = article.type;

    $("#infoAuthor").textContent = article.author;

    $("#infoSource").textContent = article.source;

    $("#sourceStatus").textContent = article.source_status;

    const body = $("#articleBody");

    body.innerHTML = "";

    const opening = createElement("p");

    opening.textContent = article.opening;

    body.appendChild(opening);


    const callout = createElement("div", "callout");

    callout.textContent =
        "Archive note: the following reconstruction contains " +
        "internal fictional scholarship, disputed records and " +
        "deliberately incomplete evidence.";

    body.appendChild(callout);


    article.sections.forEach(section => {{

        const wrapper = createElement("section", "article-section");

        const heading = createElement("h3");

        heading.textContent = section[0];

        const paragraph = createElement("p");

        paragraph.textContent = section[1];

        wrapper.appendChild(heading);

        wrapper.appendChild(paragraph);

        body.appendChild(wrapper);

    }});


    const questions = $("#questions");

    questions.innerHTML = "";

    article.questions.forEach(question => {{

        const item = createElement("div", "question");

        item.textContent = question;

        questions.appendChild(item);

    }});


    const related = $("#relatedGrid");

    related.innerHTML = "";

    article.related.forEach(name => {{

        const card = createElement("div", "explore-card");

        const small = createElement(
            "small",
            "",
            "Related record"
        );

        const strong = createElement(
            "strong",
            "",
            name
        );

        card.appendChild(small);

        card.appendChild(strong);

        card.addEventListener("click", () => {{
            discoverByName(name);
        }});

        related.appendChild(card);

    }});


    renderTimeline(article);

    $("#discoveryTitle").textContent =
        "The archive contains another connection.";

    $("#discoveryText").textContent =
        "You have explored " +
        memory.visited.length +
        " record" +
        (memory.visited.length === 1 ? "" : "s") +
        " during this session. Follow a related record or refresh " +
        "the page to receive a different archive.";

}}


// ============================================================
// TIMELINE
// ============================================================

function renderTimeline(article) {{

    const timeline = $("#timeline");

    timeline.innerHTML = "";

    const source = [
        ...ARCHIVE_DATA.events
    ].sort(() => Math.random() - 0.5)
     .slice(0, 5);

    source.forEach(event => {{

        const item = createElement("div", "timeline-item");

        const year = createElement(
            "div",
            "timeline-year",
            event.year
        );

        const name = createElement(
            "div",
            "timeline-name",
            event.name
        );

        item.appendChild(year);

        item.appendChild(name);

        item.addEventListener("click", () => {{
            discoverByName(event.name);
        }});

        timeline.appendChild(item);

    }});
}}


// ============================================================
// RANDOM ARTICLE GENERATOR
// ============================================================

function generateRandomArticle() {{

    const world =
        ARCHIVE_DATA.worlds[
            Math.floor(Math.random() * ARCHIVE_DATA.worlds.length)
        ];

    const types = [
        "Civilization",
        "Character",
        "Historical Event",
        "Faction",
        "Artifact",
        "Document",
        "Battle",
        "Political System",
        "Religion",
        "Technology",
        "Location",
        "Historical Mystery",
        "Cosmic Event",
        "Language",
        "Dynasty"
    ];

    const type =
        types[Math.floor(Math.random() * types.length)];

    const subjects = [
        "The Silent Census",
        "The Northern Dynasty",
        "The Seventh Archive",
        "The Lost Expedition",
        "The Kareth Dispute",
        "The Ashen Treaty",
        "The Unnamed Observatory",
        "The Final Provincial Record",
        "The Glass Rain",
        "The Forgotten Succession",
        "The Black Ledger",
        "The Seven-Day Silence",
        "The Empty Throne",
        "The Broken Calendar",
        "The Ninth Seal"
    ];

    const title =
        subjects[Math.floor(Math.random() * subjects.length)];

    const scholars = [
        "Ilyan Varek",
        "Sera Valen",
        "Merovan Edras",
        "Tavian Kesh",
        "Neris Orin",
        "Alden Taryn"
    ];

    const author =
        scholars[Math.floor(Math.random() * scholars.length)];

    const years = [
        "17 A.E.",
        "91 A.E.",
        "238 A.E.",
        "417 A.E.",
        "527 A.E.",
        "611 A.E.",
        "842 A.E.",
        "1187 A.E.",
        "1454 A.E.",
        "Unknown",
        "Uncertain"
    ];

    const year =
        years[Math.floor(Math.random() * years.length)];

    const relatedPool = [
        ...ARCHIVE_DATA.worlds.map(x => x.name),
        ...ARCHIVE_DATA.characters.map(x => x.name),
        ...ARCHIVE_DATA.events.map(x => x.name),
        ...ARCHIVE_DATA.factions.map(x => x.name),
        ...ARCHIVE_DATA.artifacts.map(x => x.name),
        ...ARCHIVE_DATA.documents.map(x => x.title)
    ];

    const shuffled =
        relatedPool.sort(() => Math.random() - 0.5);

    const related = shuffled
        .filter(x => x !== title)
        .slice(0, 3);

    const questions = [
        "Who created it?",
        "When did it appear?",
        "Where did it originate?",
        "Why did it become important?",
        "How did it change over time?",
        "Who opposed it?",
        "What evidence survives?",
        "What remains uncertain?",
        "Which sources disagree?",
        "What happened afterward?",
        "How does it connect to other events?",
        "Which interpretations are disputed?"
    ].sort(() => Math.random() - 0.5).slice(0, 6);

    const sourceTitles = [
        "Administrative Records of the Northern Provinces",
        "Notes on Early Elarian Chronology",
        "The Northern Annals",
        "Archaeological Survey of the Kareth Basin",
        "Political Institutions of Early Taryn",
        "The Seven Calendars",
        "Studies in Imperial Succession"
    ];

    const statuses = [
        "Disputed",
        "Partially preserved",
        "Reconstructed",
        "Incomplete",
        "Apocryphal",
        "Uncertain"
    ];

    return {{
        title: title,
        subtitle: type + " · " + world.name,
        type: type,
        world: world.name,
        year: year,
        author: author,

        opening:
            title +
            " is associated with the historical record of " +
            world.name +
            ". Surviving material suggests that the subject was " +
            "important during a period of political and cultural change, " +
            "although the chronology remains incomplete.",

        sections: [
            [
                "Historical context",
                "The available record places the subject within a " +
                "period of political and cultural change. Contemporary " +
                "accounts are limited, and later historians reconstructed " +
                "the sequence from incomplete material."
            ],
            [
                "Development",
                "Later references become more frequent and suggest " +
                "connections with trade, administration, military " +
                "organization or religious practice. The surviving " +
                "records do not establish a single explanation."
            ],
            [
                "Evidence",
                "The principal evidence consists of manuscripts, " +
                "inscriptions, administrative fragments and later " +
                "commentary. Several sources were copied long after " +
                "the events they describe."
            ],
            [
                "Competing interpretations",
                author +
                " argues that the conventional interpretation gives " +
                "too much weight to later chronicles. Other scholars " +
                "place greater importance on administrative evidence."
            ],
            [
                "Unresolved questions",
                "Several references imply that additional records " +
                "once existed. None has been conclusively recovered."
            ]
        ],

        questions: questions,

        related: related,

        source:
            sourceTitles[
                Math.floor(Math.random() * sourceTitles.length)
            ],

        source_status:
            statuses[
                Math.floor(Math.random() * statuses.length)
            ]
    }};
}}


// ============================================================
// DISCOVERY
// ============================================================

function discoverRandom() {{

    const article = generateRandomArticle();

    renderArticle(article);

    window.scrollTo({{
        top: 0,
        behavior: "smooth"
    }});

}}


function discoverByName(name) {{

    const world =
        ARCHIVE_DATA.worlds.find(x => x.name === name);

    if (world) {{

        const article = {{
            title: world.name,
            subtitle: world.type + " · " + world.era,
            type: "World",
            world: world.name,
            year: world.founded,
            author: "Archive reconstruction",

            opening: world.description,

            sections: [
                [
                    "Geography",
                    world.name +
                    " contains the following recorded regions: " +
                    world.regions.join(", ") +
                    "."
                ],
                [
                    "Political structure",
                    "The surviving record describes the political system " +
                    "as " + world.government + "."
                ],
                [
                    "Economy",
                    "Historical reconstruction identifies " +
                    world.currency +
                    " as the principal recorded currency."
                ],
                [
                    "Language",
                    "The principal recorded language is " +
                    world.language +
                    "."
                ],
                [
                    "Historical questions",
                    "The dates associated with the foundation and later " +
                    "development remain subject to interpretation."
                ]
            ],

            questions: [
                "When was the world established?",
                "Who ruled it?",
                "What languages were spoken?",
                "How did its political system function?",
                "What caused major historical changes?",
                "Which records survive?"
            ],

            related: [
                ...ARCHIVE_DATA.events
                    .filter(x => x.world === world.name)
                    .map(x => x.name)
                    .slice(0, 3)
            ],

            source: "World reconstruction archive",

            source_status: "Original fictional setting"
        }};

        renderArticle(article);

        closeMenu();

        return;
    }}

    const character =
        ARCHIVE_DATA.characters.find(x => x.name === name);

    if (character) {{

        renderArticle({{
            title: character.name,
            subtitle: character.role + " · " + character.world,
            type: "Character",
            world: character.world,
            year: character.period,
            author: "Character archive",

            opening: character.description,

            sections: [
                [
                    "Role",
                    character.name +
                    " is recorded as a " +
                    character.role +
                    " in the fictional historical archive."
                ],
                [
                    "Historical context",
                    "The character is associated with " +
                    character.world +
                    " and the period " +
                    character.period + "."
                ],
                [
                    "Recorded legacy",
                    "Later records interpret the figure differently, " +
                    "particularly when discussing political responsibility."
                ],
                [
                    "Sources",
                    "References include fictional chronicles, later " +
                    "historical commentary and reconstructed records."
                ]
            ],

            questions: [
                "Who was this person?",
                "What did they change?",
                "Who opposed them?",
                "What sources mention them?",
                "When did they disappear from the record?",
                "How reliable are the accounts?"
            ],

            related: [
                character.world,
                ...ARCHIVE_DATA.events
                    .filter(x => x.world === character.world)
                    .map(x => x.name)
                    .slice(0, 2)
            ],

            source: "Biographical archive",

            source_status: "Reconstructed"
        }});

        closeMenu();

        return;
    }}

    discoverRandom();
}}


// ============================================================
// SEARCH INDEX
// ============================================================

function buildSearchIndex() {{

    const index = [];

    ARCHIVE_DATA.worlds.forEach(item => {{
        index.push({{
            name: item.name,
            category: "World",
            searchable:
                item.name + " " +
                item.type + " " +
                item.description
        }});
    }});

    ARCHIVE_DATA.characters.forEach(item => {{
        index.push({{
            name: item.name,
            category: "Character",
            searchable:
                item.name + " " +
                item.world + " " +
                item.role + " " +
                item.description
        }});
    }});

    ARCHIVE_DATA.events.forEach(item => {{
        index.push({{
            name: item.name,
            category: "Event",
            searchable:
                item.name + " " +
                item.world + " " +
                item.type + " " +
                item.description
        }});
    }});

    ARCHIVE_DATA.factions.forEach(item => {{
        index.push({{
            name: item.name,
            category: "Faction",
            searchable:
                item.name + " " +
                item.world + " " +
                item.type + " " +
                item.description
        }});
    }});

    ARCHIVE_DATA.artifacts.forEach(item => {{
        index.push({{
            name: item.name,
            category: "Artifact",
            searchable:
                item.name + " " +
                item.world + " " +
                item.classification + " " +
                item.description
        }});
    }});

    ARCHIVE_DATA.documents.forEach(item => {{
        index.push({{
            name: item.title,
            category: "Document",
            searchable:
                item.title + " " +
                item.world + " " +
                item.type + " " +
                item.excerpt
        }});
    }});

    ARCHIVE_DATA.canonGroups.forEach(group => {{

        group.items.forEach(item => {{

            index.push({{
                name: item,
                category: group.name,
                searchable: item + " " + group.name
            }});

        }});

    }});

    return index;
}}

const SEARCH_INDEX = buildSearchIndex();


// ============================================================
// SEARCH
// ============================================================

function performSearch(query) {{

    const container = $("#searchResults");

    query = query.trim().toLowerCase();

    memory.searchTerm = query;

    if (!query) {{
        container.hidden = true;
        container.innerHTML = "";
        return;
    }}

    const results = SEARCH_INDEX
        .filter(item =>
            item.searchable.toLowerCase().includes(query)
        )
        .slice(0, 12);

    container.innerHTML = "";

    if (!results.length) {{

        const empty = createElement(
            "div",
            "empty",
            "No matching archive record."
        );

        container.appendChild(empty);

    }} else {{

        results.forEach(result => {{

            const row = createElement(
                "div",
                "search-result"
            );

            const title = createElement(
                "strong",
                "",
                result.name
            );

            const category = createElement(
                "small",
                "",
                result.category
            );

            row.appendChild(title);

            row.appendChild(category);

            row.addEventListener("click", () => {{

                discoverByName(result.name);

                $("#searchInput").value = "";

                container.hidden = true;

            }});

            container.appendChild(row);

        }});

    }}

    container.hidden = false;
}}


// ============================================================
// SIDEBAR
// ============================================================

function buildNavigation() {{

    const worldNav = $("#worldNav");

    ARCHIVE_DATA.worlds.forEach(world => {{

        const button = createElement(
            "button",
            "nav-item",
            world.name
        );

        button.addEventListener("click", () => {{
            discoverByName(world.name);
        }});

        worldNav.appendChild(button);

    }});


    const canonNav = $("#canonNav");

    ARCHIVE_DATA.canonGroups.forEach(group => {{

        const button = createElement(
            "button",
            "nav-item",
            group.name
        );

        button.addEventListener("click", () => {{

            const item =
                group.items[
                    Math.floor(
                        Math.random() * group.items.length
                    )
                ];

            showReferenceCollection(group.name, item);

        }});

        canonNav.appendChild(button);

    }});


    const typeNav = $("#typeNav");

    const types = [
        "Civilization",
        "Character",
        "Historical Event",
        "Faction",
        "Artifact",
        "Document",
        "Battle",
        "Political System",
        "Religion",
        "Technology",
        "Location",
        "Historical Mystery",
        "Cosmic Event"
    ];

    types.forEach(type => {{

        const button = createElement(
            "button",
            "nav-item",
            type
        );

        button.addEventListener("click", () => {{

            showTypeCollection(type);

        }});

        typeNav.appendChild(button);

    }});
}}


// ============================================================
// REFERENCE COLLECTION
// ============================================================

function showReferenceCollection(groupName, item) {{

    renderArticle({{
        title: item,
        subtitle: groupName + " reference",
        type: "Reference entry",
        world: groupName,
        year: "Published fictional universe",
        author: "Reference index",

        opening:
            item +
            " is indexed here as part of the " +
            groupName +
            " collection. This section is a reference/navigation " +
            "entry and does not create new official canon.",

        sections: [
            [
                "Scope",
                "The archive records the work or category so that " +
                "readers can navigate related fictional material."
            ],
            [
                "Canon boundary",
                "Published canon should be distinguished from fan " +
                "interpretation, original fiction and alternate-universe " +
                "material."
            ],
            [
                "Related exploration",
                "Use the search system to discover other entries or " +
                "return to the original fictional archive."
            ],
            [
                "Archive note",
                "This site does not claim that its original fictional " +
                "records are official material from the referenced work."
            ]
        ],

        questions: [
            "What is this work?",
            "What is its fictional setting?",
            "Who are its major characters?",
            "What themes does it explore?",
            "Which official sources document it?",
            "Which entries are fan-created?"
        ],

        related: [
            ...groupName === "DC"
                ? ["Batman", "Superman", "Justice League"]
                : groupName === "Marvel"
                ? ["Spider-Man", "Avengers", "X-Men"]
                : ["Original Worlds", "Random discovery", "Historical timeline"]
        ],

        source: "Reference index",

        source_status: "Reference / navigation"
    }});

    closeMenu();
}}


// ============================================================
// TYPE COLLECTION
// ============================================================

function showTypeCollection(type) {{

    const possible = [
        ...ARCHIVE_DATA.events,
        ...ARCHIVE_DATA.characters,
        ...ARCHIVE_DATA.factions,
        ...ARCHIVE_DATA.artifacts
    ];

    const matching =
        possible.filter(item => {{

            const itemType =
                item.type ||
                item.role ||
                item.classification ||
                "";

            return itemType
                .toLowerCase()
                .includes(type.toLowerCase());

        }});

    if (matching.length) {{

        const item =
            matching[Math.floor(Math.random() * matching.length)];

        discoverByName(item.name);

    }} else {{

        discoverRandom();

    }}

    closeMenu();
}}


// ============================================================
// MENU
// ============================================================

function openMenu() {{

    document.body.classList.add("menu-open");

    memory.menuOpen = true;

    $("#menuButton").setAttribute(
        "aria-label",
        "Close navigation"
    );

}}

function closeMenu() {{

    document.body.classList.remove("menu-open");

    memory.menuOpen = false;

    $("#menuButton").setAttribute(
        "aria-label",
        "Open navigation"
    );

}}


// ============================================================
// EVENT LISTENERS
// ============================================================

$("#searchInput").addEventListener(
    "input",
    event => performSearch(event.target.value)
);

$("#randomButton").addEventListener(
    "click",
    discoverRandom
);

$("#menuButton").addEventListener(
    "click",
    () => {{

        if (memory.menuOpen) {{
            closeMenu();
        }} else {{
            openMenu();
        }}

    }}
);

$("#overlay").addEventListener(
    "click",
    closeMenu
);

document.querySelectorAll(
    "[data-action]"
).forEach(button => {{

    button.addEventListener(
        "click",
        () => {{

            const action =
                button.dataset.action;

            if (action === "random") {{
                discoverRandom();
            }}

            if (action === "home") {{
                window.scrollTo({{
                    top: 0,
                    behavior: "smooth"
                }});
            }}

            if (action === "timeline") {{
                $("#timelineSection").scrollIntoView({{
                    behavior: "smooth"
                }});
            }}

            closeMenu();

        }}
    );

}});

document.addEventListener(
    "keydown",
    event => {{

        if (
            event.key === "/" &&
            document.activeElement.tagName !== "INPUT"
        ) {{

            event.preventDefault();

            $("#searchInput").focus();

        }}

        if (event.key === "Escape") {{

            closeMenu();

            $("#searchResults").hidden = true;

        }}

    }}
);

document.addEventListener(
    "click",
    event => {{

        const search =
            document.querySelector(".search");

        if (!search.contains(event.target)) {{
            $("#searchResults").hidden = true;
        }}

    }}
);


// ============================================================
// INITIALIZE
// ============================================================

buildNavigation();

renderArticle(INITIAL_ARTICLE);

</script>

</body>
</html>
"""

    return html_document


# ============================================================
# GENERATE FILE
# ============================================================

def main():

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    document = build_html()

    OUTPUT_FILE.write_text(
        document,
        encoding="utf-8"
    )

    print()
    print("=" * 60)
    print("FORBIDDEN LORE WIKI GENERATED")
    print("=" * 60)
    print()
    print(f"Output: {OUTPUT_FILE.resolve()}")
    print()
    print("Generated as a SINGLE static HTML file.")
    print()
    print("No database")
    print("No localStorage")
    print("No sessionStorage")
    print("No login/signup")
    print("No backend")
    print("Browser memory only")
    print()
    print("Open:")
    print(f"  {OUTPUT_FILE}")
    print()


if __name__ == "__main__":
    main()
