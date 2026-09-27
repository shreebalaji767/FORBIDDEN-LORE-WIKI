from pathlib import Path
import html
import json
import random
import re


# ============================================================
# FORBIDDEN LORE WIKI
# Complete static-site generator
# Python generates ONE self-contained HTML file.
#
# No database
# No localStorage
# No sessionStorage
# No login/signup
# No backend
# Browser memory only
# ============================================================

OUTPUT_DIR = Path("site")
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
            "that he opposed imperial expansion into the Kareth Marches."
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
        "world": "The Ashen Realms",
        "role": "Cartographer",
        "period": "Post-Cataclysmic Age",
        "description": (
            "A fictional mapmaker whose surviving charts contain coastlines "
            "not found on any contemporary map."
        ),
    },
]


# ============================================================
# ORIGINAL EVENTS
# ============================================================

EVENTS = [
    {
        "name": "The First War of Broken Stars",
        "year": "Unknown",
        "world": "The Seven-Star Continuum",
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
        "world": "The Ashen Realms",
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
    },
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
        "world": "The Seven-Star Continuum",
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
    },
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
        "world": "The Seven-Star Continuum",
        "classification": "Astronomical instrument",
        "description": (
            "A fictional instrument whose calibration markings do not "
            "correspond to the surviving celestial calendar."
        ),
    },
    {
        "name": "The Black Ledger",
        "world": "The Ashen Realms",
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
        "world": "The Seven-Star Continuum",
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
# REFERENCE UNIVERSES
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
    value = re.sub(r"[^a-zA-Z0-9]+", "-", str(value).lower())
    return value.strip("-")


def all_lore_names():
    values = []

    values.extend(item["name"] for item in WORLDS)
    values.extend(item["name"] for item in CHARACTERS)
    values.extend(item["name"] for item in EVENTS)
    values.extend(item["name"] for item in FACTIONS)
    values.extend(item["name"] for item in ARTIFACTS)
    values.extend(item["title"] for item in DOCUMENTS)

    return values


def random_lore_reference(exclude=None):
    values = all_lore_names()

    if exclude:
        values = [value for value in values if value != exclude]

    return random.choice(values)


def random_year():
    return random.choice(
        [
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
        ]
    )


def generated_scholar():
    first = random.choice(
        [
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
        ]
    )

    last = random.choice(
        [
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
        ]
    )

    return f"{first} {last}"


def generated_source():
    return random.choice(
        [
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
    )


# ============================================================
# DYNAMIC ARTICLE GENERATOR
# ============================================================

def build_dynamic_article():
    world = random.choice(WORLDS)
    article_type = random.choice(ARTICLE_TYPES)

    prefixes = [
        "Northern",
        "Second",
        "Lost",
        "Silent",
        "Sevenfold",
        "Final",
        "Imperial",
        "Forgotten",
        "Outer",
        "Crownless",
    ]

    subjects = [
        "Dynasty",
        "Expedition",
        "Census",
        "War",
        "Treaty",
        "Chronicle",
        "Archive",
        "Observatory",
        "Succession",
        "Settlement",
        "Conspiracy",
        "Migration",
        "Rebellion",
        "Pilgrimage",
    ]

    title = (
        f"The {random.choice(prefixes)} "
        f"{random.choice(subjects)} of {random.choice(world['regions'])}"
    )

    related = []

    while len(related) < 4:
        candidate = random_lore_reference()
        if candidate not in related:
            related.append(candidate)

    scholar = generated_scholar()

    opening_templates = [
        (
            f"{title} is a reconstructed {article_type.lower()} associated "
            f"with {world['name']}. The surviving record is incomplete, "
            f"and later catalogues disagree about its original purpose."
        ),
        (
            f"References to {title} appear in several fictional archival "
            f"traditions connected with {world['name']}. No surviving "
            f"document provides a complete account."
        ),
        (
            f"Modern archival studies place {title} within the wider "
            f"historical development of {world['name']}. Its chronology "
            f"remains partially unresolved."
        ),
    ]

    sections = [
        [
            "Historical context",
            (
                f"The available record places this subject within the "
                f"{world['era']}. Contemporary accounts are limited, "
                f"while later historians reconstructed the sequence from "
                f"fragmentary material."
            ),
        ],
        [
            "Development",
            (
                "Later references become more frequent and suggest "
                "connections with administration, trade, military "
                "organization, religion or migration. No single "
                "interpretation accounts for every surviving source."
            ),
        ],
        [
            "Evidence",
            (
                f"The principal evidence consists of manuscripts, "
                f"inscriptions, administrative fragments and later "
                f"commentary. {scholar} notes that several sources "
                f"were copied long after the events they describe."
            ),
        ],
        [
            "Competing interpretations",
            (
                f"{scholar} argues that the conventional reconstruction "
                f"places excessive weight on later chronicles. Other "
                f"fictional historians give greater importance to "
                f"administrative and archaeological evidence."
            ),
        ],
        [
            "Unresolved questions",
            (
                "Several references imply that additional records once "
                "existed. None has been conclusively recovered, leaving "
                "important parts of the chronology uncertain."
            ),
        ],
    ]

    return {
        "title": title,
        "subtitle": f"{article_type} · {world['name']}",
        "type": article_type,
        "world": world["name"],
        "year": random_year(),
        "author": scholar,
        "opening": random.choice(opening_templates),
        "sections": sections,
        "questions": random.sample(QUESTIONS, 6),
        "related": related,
        "source": generated_source(),
        "source_status": random.choice(
            [
                "Reconstructed",
                "Partially preserved",
                "Disputed",
                "Incomplete",
                "Uncertain",
            ]
        ),
    }


# ============================================================
# INITIAL ARTICLE
# ============================================================

def build_initial_article():
    world = random.choice(WORLDS)

    return {
        "title": "The Forbidden Lore Archive",
        "subtitle": "Open historical index · fictional and referenced worlds",
        "type": "Archive",
        "world": world["name"],
        "year": "Current archive edition",
        "author": "Archive Editorial System",
        "opening": (
            "A research-oriented archive for fictional civilizations, "
            "characters, conflicts, artifacts, manuscripts and unresolved "
            "historical questions. Original material is presented as "
            "fictional reconstruction, while published universes are "
            "identified as reference categories rather than invented canon."
        ),
        "sections": [
            [
                "How the archive works",
                (
                    "Every discovery is assembled from the archive's "
                    "fictional records, reference categories and generated "
                    "research questions. The browser keeps exploration "
                    "state only in memory."
                ),
            ],
            [
                "Source boundaries",
                (
                    "Original worlds are clearly identified as original "
                    "fiction. Referenced anime, manga, manhwa, manhua, "
                    "donghua, light novels, comics, DC and Marvel entries "
                    "are navigation references and are not presented as "
                    "official canon."
                ),
            ],
            [
                "Research method",
                (
                    "Entries use the language of historical archives: "
                    "chronology, provenance, conflicting accounts, "
                    "documents, archaeological evidence and unresolved "
                    "questions."
                ),
            ],
            [
                "Discovery",
                (
                    "Use the search field, archive navigation or the "
                    "Discover button to move between worlds, people, "
                    "events, factions, artifacts and documents."
                ),
            ],
        ],
        "questions": [
            "What is currently known?",
            "Which sources survive?",
            "Which accounts disagree?",
            "What happened before the event?",
            "What happened afterward?",
            "Which questions remain unanswered?",
        ],
        "related": [
            "Vael Taryn",
            "The Seven-Day Silence",
            "The Ninth Imperial Seal",
            "The Chronicle of Edras",
        ],
        "source": "Forbidden Lore Archive",
        "source_status": "Archive index",
    }


# ============================================================
# DATA FOR JAVASCRIPT
# ============================================================

ARCHIVE_DATA = {
    "worlds": WORLDS,
    "characters": CHARACTERS,
    "events": EVENTS,
    "factions": FACTIONS,
    "artifacts": ARTIFACTS,
    "documents": DOCUMENTS,
    "canonGroups": CANON_GROUPS,
}


# ============================================================
# COMPLETE CSS
# ============================================================

CSS = r"""
:root {
    --bg: #090b0f;
    --panel: #11151b;
    --panel2: #171c23;
    --text: #e7e2d5;
    --muted: #92999f;
    --accent: #c5a86a;
    --accent2: #6d849b;
    --line: #2b3138;
    --paper: #d9d0bc;
    --radius: 14px;
    --shadow: 0 20px 70px rgba(0, 0, 0, .28);
}

* {
    box-sizing: border-box;
}

html {
    min-width: 320px;
    background: var(--bg);
    scroll-behavior: smooth;
}

body {
    margin: 0;
    min-height: 100vh;
    background:
        radial-gradient(circle at 15% 0%, rgba(255,255,255,.035), transparent 28rem),
        radial-gradient(circle at 90% 20%, rgba(255,255,255,.025), transparent 30rem),
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
    line-height: 1.65;
}

button,
input {
    font: inherit;
}

button {
    cursor: pointer;
}

button:focus-visible,
input:focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: 3px;
}

a {
    color: inherit;
}

::selection {
    background: var(--accent);
    color: #111;
}

.site-shell {
    min-height: 100vh;
}

.topbar {
    position: sticky;
    top: 0;
    z-index: 50;
    min-height: 72px;
    display: flex;
    align-items: center;
    gap: 20px;
    padding: 12px clamp(16px, 4vw, 48px);
    border-bottom: 1px solid var(--line);
    background: rgba(9, 11, 15, .92);
    backdrop-filter: blur(18px);
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
    min-width: max-content;
    user-select: none;
}

.brand-mark {
    width: 38px;
    height: 38px;
    display: grid;
    place-items: center;
    border: 1px solid var(--accent);
    color: var(--accent);
    font-family: Georgia, serif;
    font-weight: 700;
    font-size: 18px;
}

.brand-copy {
    display: flex;
    flex-direction: column;
    line-height: 1.1;
}

.brand-title {
    font-family: Georgia, "Times New Roman", serif;
    font-size: 16px;
    letter-spacing: .12em;
    text-transform: uppercase;
}

.brand-subtitle {
    margin-top: 5px;
    color: var(--muted);
    font-size: 10px;
    letter-spacing: .12em;
    text-transform: uppercase;
}

.search {
    position: relative;
    flex: 1;
    max-width: 720px;
    margin: 0 auto;
}

.search input {
    width: 100%;
    height: 44px;
    padding: 0 46px 0 16px;
    border: 1px solid var(--line);
    border-radius: 999px;
    background: var(--panel);
    color: var(--text);
}

.search input::placeholder {
    color: var(--muted);
}

.search-hint {
    position: absolute;
    right: 13px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--muted);
    font-size: 11px;
    pointer-events: none;
}

.search-results {
    position: absolute;
    top: calc(100% + 9px);
    left: 0;
    right: 0;
    max-height: 420px;
    overflow: auto;
    padding: 8px;
    border: 1px solid var(--line);
    border-radius: 14px;
    background: var(--panel);
    box-shadow: var(--shadow);
}

.search-result {
    display: flex;
    flex-direction: column;
    gap: 1px;
    padding: 11px 12px;
    border-radius: 9px;
}

.search-result:hover {
    background: var(--panel2);
}

.search-result strong {
    font-size: 13px;
}

.search-result small {
    color: var(--muted);
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: .08em;
}

.empty {
    padding: 16px;
    color: var(--muted);
    font-size: 13px;
}

.top-actions {
    display: flex;
    gap: 8px;
    min-width: max-content;
}

.icon-button,
.action-button {
    min-height: 42px;
    border: 1px solid var(--line);
    border-radius: 10px;
    background: var(--panel);
    color: var(--text);
}

.icon-button {
    width: 42px;
}

.action-button {
    padding: 0 15px;
}

.action-button:hover,
.icon-button:hover {
    border-color: var(--accent);
    color: var(--accent);
}

.menu-button {
    display: none;
}

.layout {
    display: grid;
    grid-template-columns: 280px minmax(0, 1fr);
    min-height: calc(100vh - 72px);
}

.sidebar {
    position: sticky;
    top: 72px;
    height: calc(100vh - 72px);
    overflow: auto;
    border-right: 1px solid var(--line);
    background: rgba(11, 14, 18, .65);
    padding: 28px 18px;
}

.nav-section {
    margin-bottom: 30px;
}

.nav-heading {
    margin: 0 10px 9px;
    color: var(--muted);
    font-size: 10px;
    letter-spacing: .16em;
    text-transform: uppercase;
}

.nav-item {
    width: 100%;
    display: block;
    padding: 9px 10px;
    border: 0;
    border-radius: 8px;
    background: transparent;
    color: var(--text);
    text-align: left;
    font-size: 13px;
}

.nav-item:hover {
    background: var(--panel2);
    color: var(--accent);
}

.main {
    min-width: 0;
    width: 100%;
}

.hero {
    position: relative;
    overflow: hidden;
    padding:
        clamp(55px, 8vw, 100px)
        clamp(20px, 7vw, 100px)
        55px;
    border-bottom: 1px solid var(--line);
}

.hero::after {
    content: "";
    position: absolute;
    width: 420px;
    height: 420px;
    right: -160px;
    top: -180px;
    border: 1px solid rgba(255,255,255,.045);
    border-radius: 50%;
    box-shadow:
        0 0 0 40px rgba(255,255,255,.012),
        0 0 0 80px rgba(255,255,255,.008);
    pointer-events: none;
}

.eyebrow {
    margin-bottom: 18px;
    color: var(--accent);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: .2em;
    text-transform: uppercase;
}

.hero h1 {
    max-width: 950px;
    margin: 0;
    font-family: Georgia, "Times New Roman", serif;
    font-size: clamp(42px, 7vw, 88px);
    font-weight: 500;
    letter-spacing: -.045em;
    line-height: .98;
}

.hero-description {
    max-width: 750px;
    margin: 25px 0 0;
    color: var(--muted);
    font-size: clamp(15px, 1.7vw, 18px);
}

.hero-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 30px;
}

.primary-button {
    min-height: 46px;
    padding: 0 19px;
    border: 1px solid var(--accent);
    border-radius: 9px;
    background: var(--accent);
    color: #10100d;
    font-weight: 750;
}

.primary-button:hover {
    filter: brightness(1.08);
}

.secondary-button {
    min-height: 46px;
    padding: 0 19px;
    border: 1px solid var(--line);
    border-radius: 9px;
    background: transparent;
    color: var(--text);
}

.secondary-button:hover {
    border-color: var(--accent);
    color: var(--accent);
}

.content {
    max-width: 1120px;
    margin: 0 auto;
    padding: 40px clamp(18px, 5vw, 60px) 80px;
}

.archive-meta {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
    margin-bottom: 40px;
}

.meta-cell {
    min-width: 0;
    padding: 18px 15px;
    border-right: 1px solid var(--line);
}

.meta-cell:last-child {
    border-right: 0;
}

.meta-label {
    margin-bottom: 5px;
    color: var(--muted);
    font-size: 9px;
    letter-spacing: .14em;
    text-transform: uppercase;
}

.meta-value {
    overflow-wrap: anywhere;
    font-size: 13px;
}

.article-layout {
    display: grid;
    grid-template-columns: minmax(0, 1fr) 270px;
    gap: 45px;
}

.article-header {
    padding-bottom: 30px;
    border-bottom: 1px solid var(--line);
}

.article-kicker {
    margin-bottom: 10px;
    color: var(--accent);
    font-size: 10px;
    letter-spacing: .16em;
    text-transform: uppercase;
}

.article-title {
    margin: 0;
    font-family: Georgia, "Times New Roman", serif;
    font-size: clamp(35px, 5vw, 62px);
    font-weight: 500;
    line-height: 1.02;
    letter-spacing: -.035em;
}

.article-subtitle {
    margin: 13px 0 0;
    color: var(--muted);
    font-size: 14px;
}

.article-opening {
    margin: 32px 0;
    padding: 22px 0 22px 22px;
    border-left: 2px solid var(--accent);
    font-family: Georgia, "Times New Roman", serif;
    font-size: clamp(18px, 2.2vw, 23px);
    line-height: 1.55;
}

.article-section {
    margin: 0 0 36px;
}

.article-section h2 {
    margin: 0 0 11px;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 25px;
    font-weight: 500;
}

.article-section p {
    margin: 0;
    color: #c9c7bf;
    font-size: 15px;
}

.article-aside {
    min-width: 0;
}

.aside-card {
    margin-bottom: 18px;
    padding: 18px;
    border: 1px solid var(--line);
    border-radius: 12px;
    background: var(--panel);
}

.aside-title {
    margin-bottom: 13px;
    color: var(--muted);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: .15em;
    text-transform: uppercase;
}

.question {
    padding: 9px 0;
    border-top: 1px solid var(--line);
    color: #c8c7c1;
    font-size: 12px;
}

.question:first-of-type {
    border-top: 0;
}

.related {
    display: flex;
    flex-direction: column;
    gap: 6px;
}

.related button {
    width: 100%;
    padding: 8px 0;
    border: 0;
    background: transparent;
    color: var(--text);
    text-align: left;
    font-size: 12px;
}

.related button:hover {
    color: var(--accent);
}

.timeline {
    margin-top: 55px;
    padding-top: 35px;
    border-top: 1px solid var(--line);
}

.timeline-title {
    margin-bottom: 20px;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 30px;
}

.timeline-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
}

.timeline-card {
    min-width: 0;
    padding: 18px;
    border: 1px solid var(--line);
    border-radius: 12px;
    background: var(--panel);
}

.timeline-year {
    color: var(--accent);
    font-size: 10px;
    letter-spacing: .12em;
    text-transform: uppercase;
}

.timeline-card h3 {
    margin: 8px 0 7px;
    font-family: Georgia, serif;
    font-size: 19px;
    font-weight: 500;
}

.timeline-card p {
    margin: 0;
    color: var(--muted);
    font-size: 12px;
}

.footer {
    padding: 35px clamp(18px, 5vw, 60px);
    border-top: 1px solid var(--line);
    color: var(--muted);
    font-size: 11px;
}

.footer-inner {
    max-width: 1120px;
    margin: auto;
    display: flex;
    justify-content: space-between;
    gap: 20px;
}

.menu-overlay {
    display: none;
}

.menu-open .menu-overlay {
    display: block;
}

.layout.classic .article-opening {
    background: linear-gradient(90deg, rgba(255,255,255,.018), transparent);
}

.layout.terminal .article-title {
    font-family:
        "SFMono-Regular",
        Consolas,
        "Liberation Mono",
        monospace;
    letter-spacing: -.025em;
}

.layout.terminal .article-opening {
    font-family:
        "SFMono-Regular",
        Consolas,
        monospace;
    font-size: 15px;
}

.layout.manuscript .article-section p,
.layout.manuscript .article-opening {
    font-family: Georgia, "Times New Roman", serif;
}

.layout.manuscript .article-title {
    font-family: Georgia, "Times New Roman", serif;
}

.layout.research .article-layout {
    grid-template-columns: minmax(0, 1fr) 310px;
}

.layout.museum .article-title {
    letter-spacing: .015em;
}

.layout.minimal .hero::after {
    display: none;
}

.layout.casefile .article-header {
    border-top: 3px solid var(--accent);
    padding-top: 20px;
}

@media (max-width: 1050px) {
    .layout {
        grid-template-columns: 235px minmax(0, 1fr);
    }

    .article-layout {
        grid-template-columns: minmax(0, 1fr) 230px;
        gap: 28px;
    }

    .timeline-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
}

@media (max-width: 820px) {
    .topbar {
        gap: 10px;
    }

    .brand-subtitle {
        display: none;
    }

    .menu-button {
        display: block;
        order: 4;
    }

    .top-actions .desktop-action {
        display: none;
    }

    .layout {
        display: block;
    }

    .sidebar {
        position: fixed;
        z-index: 45;
        top: 72px;
        left: 0;
        width: min(310px, 88vw);
        height: calc(100vh - 72px);
        transform: translateX(-105%);
        transition: transform .25s ease;
        box-shadow: var(--shadow);
        background: #0d1015;
    }

    .menu-open .sidebar {
        transform: translateX(0);
    }

    .menu-overlay {
        position: fixed;
        z-index: 40;
        inset: 72px 0 0;
        background: rgba(0,0,0,.58);
    }

    .article-layout {
        grid-template-columns: 1fr;
    }

    .article-aside {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 12px;
    }

    .aside-card {
        margin: 0;
    }
}

@media (max-width: 620px) {
    .topbar {
        min-height: 64px;
        padding: 9px 12px;
    }

    .sidebar {
        top: 64px;
        height: calc(100vh - 64px);
    }

    .menu-overlay {
        inset: 64px 0 0;
    }

    .brand-title {
        font-size: 13px;
    }

    .brand-mark {
        width: 34px;
        height: 34px;
    }

    .search-hint {
        display: none;
    }

    .search input {
        height: 40px;
        padding-left: 12px;
    }

    .top-actions {
        gap: 4px;
    }

    .icon-button {
        width: 38px;
        min-height: 38px;
    }

    .layout {
        min-height: calc(100vh - 64px);
    }

    .hero {
        padding: 48px 18px 42px;
    }

    .hero h1 {
        font-size: clamp(38px, 13vw, 58px);
    }

    .content {
        padding: 30px 15px 60px;
    }

    .archive-meta {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .meta-cell:nth-child(2) {
        border-right: 0;
    }

    .meta-cell:nth-child(-n+2) {
        border-bottom: 1px solid var(--line);
    }

    .article-title {
        font-size: 38px;
    }

    .article-opening {
        padding-left: 16px;
        font-size: 18px;
    }

    .article-aside {
        grid-template-columns: 1fr;
    }

    .timeline-grid {
        grid-template-columns: 1fr;
    }

    .footer-inner {
        flex-direction: column;
    }
}

@media (max-width: 430px) {
    .brand-copy {
        display: none;
    }

    .topbar {
        padding: 9px 10px;
    }

    .search {
        max-width: none;
    }

    .hero-actions {
        flex-direction: column;
    }

    .primary-button,
    .secondary-button {
        width: 100%;
    }

    .archive-meta {
        grid-template-columns: 1fr;
    }

    .meta-cell {
        border-right: 0;
        border-bottom: 1px solid var(--line);
    }

    .meta-cell:last-child {
        border-bottom: 0;
    }
}
"""


# ============================================================
# COMPLETE HTML
# ============================================================

def build_html():
    theme = random.choice(THEMES)
    layout = random.choice(LAYOUTS)

    initial_article = build_initial_article()

    data_json = json.dumps(
        ARCHIVE_DATA,
        ensure_ascii=False,
        separators=(",", ":"),
    )

    article_json = json.dumps(
        initial_article,
        ensure_ascii=False,
        separators=(",", ":"),
    )

    theme_css = (
        f":root{{--bg:{theme['bg']};"
        f"--panel:{theme['panel']};"
        f"--panel2:{theme['panel2']};"
        f"--text:{theme['text']};"
        f"--muted:{theme['muted']};"
        f"--accent:{theme['accent']};"
        f"--accent2:{theme['accent2']};"
        f"--line:{theme['line']};"
        f"--paper:{theme['paper']};}}"
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Forbidden Lore Wiki — The Historical Archive of Fictional Worlds</title>

<meta
    name="description"
    content="A research-style fictional lore archive covering original worlds, characters, civilizations, events, factions, artifacts, documents and reference universes."
>

<meta
    name="keywords"
    content="fictional lore wiki, fictional history, anime lore, manhwa lore, manhua lore, donghua, light novels, comics, DC, Marvel, worldbuilding, fictional encyclopedia"
>

<meta name="robots" content="index,follow">

<meta property="og:type" content="website">
<meta property="og:title" content="Forbidden Lore Wiki">
<meta property="og:description" content="A serious archive for fictional worlds, histories, characters, artifacts and unresolved lore.">

<style>
{CSS}
{theme_css}
</style>
</head>

<body class="layout {esc(layout)}">

<div class="site-shell">

<header class="topbar">

    <div class="brand">
        <div class="brand-mark">FL</div>

        <div class="brand-copy">
            <div class="brand-title">Forbidden Lore</div>
            <div class="brand-subtitle">Historical Archive</div>
        </div>
    </div>

    <div class="search">

        <input
            id="searchInput"
            type="search"
            autocomplete="off"
            spellcheck="false"
            placeholder="Search the archive..."
            aria-label="Search the archive"
        >

        <span class="search-hint">/</span>

        <div
            id="searchResults"
            class="search-results"
            hidden
        ></div>

    </div>

    <div class="top-actions">

        <button
            id="randomButton"
            class="action-button desktop-action"
            type="button"
        >
            Discover
        </button>

        <button
            id="menuButton"
            class="icon-button menu-button"
            type="button"
            aria-label="Open navigation"
            aria-expanded="false"
        >
            ☰
        </button>

    </div>

</header>


<div class="layout">

    <aside class="sidebar">

        <div class="nav-section">

            <div class="nav-heading">Archive</div>

            <button
                class="nav-item"
                data-action="home"
                type="button"
            >
                Archive Index
            </button>

            <button
                class="nav-item"
                data-action="random"
                type="button"
            >
                Random Discovery
            </button>

            <button
                class="nav-item"
                data-action="timeline"
                type="button"
            >
                Historical Timeline
            </button>

        </div>


        <div class="nav-section">

            <div class="nav-heading">Original Worlds</div>

            <div id="worldNav"></div>

        </div>


        <div class="nav-section">

            <div class="nav-heading">Reference Universes</div>

            <div id="canonNav"></div>

        </div>


        <div class="nav-section">

            <div class="nav-heading">Archive Types</div>

            <div id="typeNav"></div>

        </div>

    </aside>


    <div
        id="overlay"
        class="menu-overlay"
    ></div>


    <main class="main">

        <section class="hero">

            <div class="eyebrow">
                Restricted Historical Collection
            </div>

            <h1>
                The Forbidden<br>
                Lore Wiki
            </h1>

            <p class="hero-description">
                An archival interface for fictional civilizations,
                forgotten wars, impossible documents, characters,
                artifacts, political systems and the stories hidden
                between worlds.
            </p>

            <div class="hero-actions">

                <button
                    id="heroDiscover"
                    class="primary-button"
                    type="button"
                >
                    Discover Something Else
                </button>

                <button
                    class="secondary-button"
                    data-action="timeline"
                    type="button"
                >
                    Open Timeline
                </button>

            </div>

        </section>


        <div class="content">

            <div class="archive-meta">

                <div class="meta-cell">
                    <div class="meta-label">Collection</div>
                    <div class="meta-value">Forbidden Lore</div>
                </div>

                <div class="meta-cell">
                    <div class="meta-label">Edition</div>
                    <div class="meta-value">Archive 01</div>
                </div>

                <div class="meta-cell">
                    <div class="meta-label">Classification</div>
                    <div class="meta-value">Mixed Records</div>
                </div>

                <div class="meta-cell">
                    <div class="meta-label">State</div>
                    <div class="meta-value" id="archiveState">
                        Active
                    </div>
                </div>

            </div>


            <article id="articleContainer"></article>


            <section
                id="timelineSection"
                class="timeline"
            >

                <div class="timeline-title">
                    Selected Chronology
                </div>

                <div
                    id="timelineGrid"
                    class="timeline-grid"
                ></div>

            </section>

        </div>

    </main>

</div>


<footer class="footer">

    <div class="footer-inner">

        <div>
            FORBIDDEN LORE WIKI · FICTIONAL ARCHIVE
        </div>

        <div>
            Original fiction is identified as original material.
            Referenced universes are navigation references.
        </div>

    </div>

</footer>

</div>


<script>

"use strict";

const ARCHIVE_DATA = {data_json};

const INITIAL_ARTICLE = {article_json};


const memory = {{
    seen: [],
    searchTerm: "",
    menuOpen: false,
    discoveryCount: 0,
    currentArticle: null
}};


function $(selector) {{
    return document.querySelector(selector);
}}


function escapeHTML(value) {{
    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}}


function createElement(tag, className, text) {{

    const element = document.createElement(tag);

    if (className) {{
        element.className = className;
    }}

    if (text !== undefined) {{
        element.textContent = text;
    }}

    return element;
}}


function remember(value) {{

    if (!value) {{
        return;
    }}

    if (!memory.seen.includes(value)) {{
        memory.seen.push(value);
    }}

    if (memory.seen.length > 100) {{
        memory.seen.shift();
    }}
}}


function randomFrom(array) {{

    return array[
        Math.floor(Math.random() * array.length)
    ];

}}


function uniqueRandomFrom(array, count) {{

    const copy = [...array];
    const result = [];

    while (copy.length && result.length < count) {{

        const index =
            Math.floor(Math.random() * copy.length);

        result.push(
            copy.splice(index, 1)[0]
        );
    }}

    return result;
}}


function allNames() {{

    return [
        ...ARCHIVE_DATA.worlds.map(x => x.name),
        ...ARCHIVE_DATA.characters.map(x => x.name),
        ...ARCHIVE_DATA.events.map(x => x.name),
        ...ARCHIVE_DATA.factions.map(x => x.name),
        ...ARCHIVE_DATA.artifacts.map(x => x.name),
        ...ARCHIVE_DATA.documents.map(x => x.title)
    ];

}}


function getRandomName(exclude = []) {{

    const available =
        allNames().filter(
            name => !exclude.includes(name)
        );

    return randomFrom(
        available.length
            ? available
            : allNames()
    );
}}


// ============================================================
// DYNAMIC DISCOVERY
// ============================================================

function generateRandomArticle() {{

    const world = randomFrom(ARCHIVE_DATA.worlds);

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

    const prefixes = [
        "Northern",
        "Second",
        "Lost",
        "Silent",
        "Sevenfold",
        "Final",
        "Imperial",
        "Forgotten",
        "Outer",
        "Crownless",
        "Ashen",
        "Hidden",
        "Last",
        "Western"
    ];

    const nouns = [
        "Dynasty",
        "Expedition",
        "Census",
        "War",
        "Treaty",
        "Chronicle",
        "Archive",
        "Observatory",
        "Succession",
        "Settlement",
        "Conspiracy",
        "Migration",
        "Rebellion",
        "Pilgrimage",
        "Compact",
        "Protocol",
        "Inheritance"
    ];

    const locations = [
        ...world.regions,
        "the northern frontier",
        "the old capital",
        "the western archives",
        "the lower river",
        "the abandoned observatory"
    ];

    const title =
        "The " +
        randomFrom(prefixes) +
        " " +
        randomFrom(nouns) +
        " of " +
        randomFrom(locations);

    const type = randomFrom(types);

    const scholarNames = [
        "Ilyan Varek",
        "Sera Valen",
        "Merovan Edras",
        "Tavian Kesh",
        "Neris Orin",
        "Alden Taryn",
        "Mira Dovren",
        "Calen Voss"
    ];

    const scholar = randomFrom(scholarNames);

    const relatedPool = allNames();

    const related =
        uniqueRandomFrom(
            relatedPool.filter(
                item => item !== title
            ),
            4
        );

    return {{
        title: title,

        subtitle:
            type +
            " · " +
            world.name,

        type: type,

        world: world.name,

        year: randomFrom([
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
            "Uncertain"
        ]),

        author: scholar,

        opening:
            title +
            " is associated with the historical record of " +
            world.name +
            ". Surviving material suggests that the subject "
            +
            "was significant during a period of political and "
            +
            "cultural change, although the chronology remains "
            +
            "incomplete.",

        sections: [

            [
                "Historical context",

                "The available record places the subject within "
                +
                world.era +
                ". Contemporary accounts are limited, while "
                +
                "later historians reconstructed the sequence "
                +
                "from incomplete material."
            ],

            [
                "Development",

                "Later references become more frequent and "
                +
                "suggest connections with administration, trade, "
                +
                "military organization, religious practice or "
                +
                "migration. The surviving records do not "
                +
                "establish a single explanation."
            ],

            [
                "Evidence",

                "The principal evidence consists of manuscripts, "
                +
                "inscriptions, administrative fragments and "
                +
                "later commentary. Several sources were copied "
                +
                "long after the events they describe."
            ],

            [
                "Competing interpretations",

                scholar +
                " argues that the conventional interpretation "
                +
                "gives too much weight to later chronicles. "
                +
                "Other researchers place greater importance on "
                +
                "administrative evidence."
            ],

            [
                "Unresolved questions",

                "Several references imply that additional "
                +
                "records once existed. None has been conclusively "
                +
                "recovered."
            ]

        ],

        questions:
            uniqueRandomFrom(
                [
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
                ],
                6
            ),

        related: related,

        source: randomFrom([
            "Administrative Records of the Northern Provinces",
            "Notes on Early Elarian Chronology",
            "The Northern Annals",
            "Archaeological Survey of the Kareth Basin",
            "Political Institutions of Early Taryn",
            "The Seven Calendars",
            "Studies in Imperial Succession",
            "Fragments of the Old Chronicle",
            "The Ashen Historical Register"
        ]),

        source_status:
            randomFrom([
                "Reconstructed",
                "Partially preserved",
                "Disputed",
                "Incomplete",
                "Uncertain"
            ])
    }};

}}


// ============================================================
// ARTICLE RENDERING
// ============================================================

function renderArticle(article) {{

    memory.currentArticle = article;

    memory.discoveryCount += 1;

    remember(article.title);

    const container =
        $("#articleContainer");

    container.innerHTML = "";

    const wrapper =
        createElement(
            "div",
            "article-layout"
        );

    const main =
        createElement(
            "div",
            "article-main"
        );

    const header =
        createElement(
            "header",
            "article-header"
        );

    const kicker =
        createElement(
            "div",
            "article-kicker",
            article.type
        );

    const title =
        createElement(
            "h2",
            "article-title",
            article.title
        );

    const subtitle =
        createElement(
            "div",
            "article-subtitle",
            article.subtitle
        );

    header.appendChild(kicker);
    header.appendChild(title);
    header.appendChild(subtitle);

    main.appendChild(header);


    const opening =
        createElement(
            "div",
            "article-opening",
            article.opening
        );

    main.appendChild(opening);


    article.sections.forEach(section => {{

        const block =
            createElement(
                "section",
                "article-section"
            );

        const heading =
            createElement(
                "h2",
                "",
                section[0]
            );

        const paragraph =
            createElement(
                "p",
                "",
                section[1]
            );

        block.appendChild(heading);
        block.appendChild(paragraph);

        main.appendChild(block);

    }});


    const aside =
        createElement(
            "aside",
            "article-aside"
        );


    const metaCard =
        createElement(
            "div",
            "aside-card"
        );

    const metaTitle =
        createElement(
            "div",
            "aside-title",
            "Record"
        );

    metaCard.appendChild(metaTitle);


    [
        ["World", article.world],
        ["Date", article.year],
        ["Recorded by", article.author],
        ["Source", article.source],
        ["Status", article.source_status]
    ].forEach(item => {{

        const row =
            createElement(
                "div",
                "question"
            );

        row.textContent =
            item[0] +
            ": " +
            item[1];

        metaCard.appendChild(row);

    }});


    aside.appendChild(metaCard);


    const questionsCard =
        createElement(
            "div",
            "aside-card"
        );

    const questionsTitle =
        createElement(
            "div",
            "aside-title",
            "Questions to investigate"
        );

    questionsCard.appendChild(
        questionsTitle
    );


    article.questions.forEach(question => {{

        const item =
            createElement(
                "div",
                "question",
                question
            );

        questionsCard.appendChild(item);

    }});


    aside.appendChild(
        questionsCard
    );


    const relatedCard =
        createElement(
            "div",
            "aside-card"
        );

    const relatedTitle =
        createElement(
            "div",
            "aside-title",
            "Related records"
        );

    relatedCard.appendChild(
        relatedTitle
    );


    const relatedContainer =
        createElement(
            "div",
            "related"
        );


    article.related.forEach(name => {{

        const button =
            createElement(
                "button",
                "",
                name
            );

        button.type = "button";

        button.addEventListener(
            "click",
            () => discoverByName(name)
        );

        relatedContainer.appendChild(
            button
        );

    }});


    relatedCard.appendChild(
        relatedContainer
    );

    aside.appendChild(
        relatedCard
    );


    wrapper.appendChild(main);
    wrapper.appendChild(aside);

    container.appendChild(wrapper);

    updateArchiveState();

    window.scrollTo({{
        top: 0,
        behavior: "smooth"
    }});
}}


// ============================================================
// RECORD LOOKUP
// ============================================================

function findRecord(name) {{

    let result =
        ARCHIVE_DATA.worlds.find(
            x => x.name === name
        );

    if (result) {{
        return {{
            kind: "world",
            data: result
        }};
    }}


    result =
        ARCHIVE_DATA.characters.find(
            x => x.name === name
        );

    if (result) {{
        return {{
            kind: "character",
            data: result
        }};
    }}


    result =
        ARCHIVE_DATA.events.find(
            x => x.name === name
        );

    if (result) {{
        return {{
            kind: "event",
            data: result
        }};
    }}


    result =
        ARCHIVE_DATA.factions.find(
            x => x.name === name
        );

    if (result) {{
        return {{
            kind: "faction",
            data: result
        }};
    }}


    result =
        ARCHIVE_DATA.artifacts.find(
            x => x.name === name
        );

    if (result) {{
        return {{
            kind: "artifact",
            data: result
        }};
    }}


    result =
        ARCHIVE_DATA.documents.find(
            x => x.title === name
        );

    if (result) {{
        return {{
            kind: "document",
            data: result
        }};
    }}

    return null;
}}


// ============================================================
// RECORD ARTICLE BUILDERS
// ============================================================

function worldArticle(world) {{

    const related =
        ARCHIVE_DATA.events
            .filter(
                x => x.world === world.name
            )
            .map(
                x => x.name
            )
            .slice(0, 4);

    return {{
        title: world.name,

        subtitle:
            world.type +
            " · " +
            world.era,

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
                "The surviving record describes the political "
                +
                "system as " +
                world.government +
                "."
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
                "The dates associated with the foundation and "
                +
                "later development remain subject to "
                +
                "interpretation."
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

        related:
            related.length
                ? related
                : ["Random Discovery"],

        source: "World reconstruction archive",

        source_status: "Original fictional setting"
    }};
}}


function characterArticle(character) {{

    return {{

        title: character.name,

        subtitle:
            character.role +
            " · " +
            character.world,

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
                character.period +
                "."
            ],

            [
                "Recorded legacy",
                "Later records interpret the figure differently, "
                +
                "particularly when discussing political "
                +
                "responsibility."
            ],

            [
                "Sources",
                "References include fictional chronicles, later "
                +
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
                .filter(
                    x => x.world === character.world
                )
                .map(
                    x => x.name
                )
                .slice(0, 2)
        ],

        source: "Biographical archive",

        source_status: "Reconstructed"
    }};
}}


function eventArticle(event) {{

    return {{

        title: event.name,

        subtitle:
            event.type +
            " · " +
            event.world,

        type: "Historical Event",

        world: event.world,

        year: event.year,

        author: "Historical event register",

        opening: event.description,

        sections: [

            [
                "Event classification",
                event.name +
                " is catalogued as a " +
                event.type +
                " within the historical records of " +
                event.world +
                "."
            ],

            [
                "Historical record",
                "Accounts of the event vary between surviving "
                +
                "regional and institutional records."
            ],

            [
                "Consequences",
                "Later documents associate the event with changes "
                +
                "in political organization, population movement "
                +
                "or cultural memory."
            ],

            [
                "Source criticism",
                "Some accounts were preserved considerably later "
                +
                "than the event itself, making chronology an "
                +
                "important unresolved issue."
            ]

        ],

        questions: [
            "When did the event occur?",
            "Who participated?",
            "What caused it?",
            "Which records describe it?",
            "What changed afterward?",
            "Why do sources disagree?"
        ],

        related:
            ARCHIVE_DATA.events
                .filter(
                    x =>
                        x.world === event.world &&
                        x.name !== event.name
                )
                .map(
                    x => x.name
                )
                .slice(0, 4),

        source: "Historical event register",

        source_status: "Fictional reconstruction"
    }};
}}


function factionArticle(faction) {{

    return {{

        title: faction.name,

        subtitle:
            faction.type +
            " · " +
            faction.world,

        type: "Faction",

        world: faction.world,

        year: "Recorded period uncertain",

        author: "Institutional archive",

        opening: faction.description,

        sections: [

            [
                "Organization",
                faction.name +
                " is classified as a " +
                faction.type +
                " within the records of " +
                faction.world +
                "."
            ],

            [
                "Influence",
                "The surviving material suggests that the "
                +
                "organization influenced political, commercial, "
                +
                "religious or military developments."
            ],

            [
                "Membership",
                "Individual membership lists are incomplete, "
                +
                "and several names appear only in later copies."
            ],

            [
                "Historical uncertainty",
                "The exact period and extent of the organization's "
                +
                "influence remain disputed."
            ]

        ],

        questions: [
            "Who founded it?",
            "Who belonged to it?",
            "What did it control?",
            "Who opposed it?",
            "Which documents mention it?",
            "When did it disappear?"
        ],

        related: [
            faction.world,
            ...ARCHIVE_DATA.factions
                .filter(
                    x => x.name !== faction.name
                )
                .map(
                    x => x.name
                )
                .slice(0, 3)
        ],

        source: "Institutional archive",

        source_status: "Reconstructed"
    }};
}}


function artifactArticle(artifact) {{

    return {{

        title: artifact.name,

        subtitle:
            artifact.classification +
            " · " +
            artifact.world,

        type: "Artifact",

        world: artifact.world,

        year: "Date uncertain",

        author: "Object catalogue",

        opening: artifact.description,

        sections: [

            [
                "Classification",
                artifact.name +
                " is catalogued as a " +
                artifact.classification +
                "."
            ],

            [
                "Provenance",
                "The documented chain of ownership is incomplete. "
                +
                "Several references appear in later inventories."
            ],

            [
                "Physical record",
                "Descriptions differ between catalogues, leaving "
                +
                "open questions concerning the object's original "
                +
                "appearance and purpose."
            ],

            [
                "Authenticity",
                "No single surviving record conclusively resolves "
                +
                "the question of authenticity."
            ]

        ],

        questions: [
            "Who created it?",
            "Where was it found?",
            "What was it used for?",
            "Who owned it?",
            "Is it authentic?",
            "Where is it now?"
        ],

        related: [
            artifact.world,
            ...ARCHIVE_DATA.artifacts
                .filter(
                    x => x.name !== artifact.name
                )
                .map(
                    x => x.name
                )
                .slice(0, 3)
        ],

        source: "Object catalogue",

        source_status: "Authenticity disputed"
    }};
}}


function documentArticle(document) {{

    return {{

        title: document.title,

        subtitle:
            document.type +
            " · " +
            document.world,

        type: "Document",

        world: document.world,

        year: document.date,

        author: "Document archive",

        opening: document.excerpt,

        sections: [

            [
                "Document description",
                document.title +
                " is catalogued as a " +
                document.type +
                " associated with " +
                document.world +
                "."
            ],

            [
                "Preservation",
                "The archive classifies the document as " +
                document.status.toLowerCase() +
                "."
            ],

            [
                "Historical value",
                "The document provides evidence for reconstructing "
                +
                "administrative, political, cultural or military "
                +
                "history."
            ],

            [
                "Limitations",
                "The surviving text is insufficient to establish "
                +
                "every detail independently."
            ]

        ],

        questions: [
            "Who wrote it?",
            "When was it written?",
            "Who preserved it?",
            "What information does it contain?",
            "What is missing?",
            "Can it be independently verified?"
        ],

        related: [
            document.world,
            ...ARCHIVE_DATA.documents
                .filter(
                    x => x.title !== document.title
                )
                .map(
                    x => x.title
                )
                .slice(0, 3)
        ],

        source: "Document archive",

        source_status: document.status
    }};
}}


// ============================================================
// DISCOVERY BY NAME
// ============================================================

function discoverByName(name) {{

    const record =
        findRecord(name);

    if (!record) {{

        if (name === "Random Discovery") {{
            discoverRandom();
            return;
        }}

        discoverRandom();
        return;
    }}


    let article;

    if (record.kind === "world") {{
        article = worldArticle(record.data);
    }}

    if (record.kind === "character") {{
        article = characterArticle(record.data);
    }}

    if (record.kind === "event") {{
        article = eventArticle(record.data);
    }}

    if (record.kind === "faction") {{
        article = factionArticle(record.data);
    }}

    if (record.kind === "artifact") {{
        article = artifactArticle(record.data);
    }}

    if (record.kind === "document") {{
        article = documentArticle(record.data);
    }}

    renderArticle(article);

    closeMenu();
}}


// ============================================================
// RANDOM DISCOVERY
// ============================================================

function discoverRandom() {{

    let article;

    for (let attempt = 0; attempt < 8; attempt++) {{

        article =
            generateRandomArticle();

        if (
            !memory.seen.includes(
                article.title
            )
        {{
            break;
        }}
    }}

    renderArticle(article);
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
                item.name +
                " " +
                item.type +
                " " +
                item.description
        }});

    }});


    ARCHIVE_DATA.characters.forEach(item => {{

        index.push({{
            name: item.name,
            category: "Character",
            searchable:
                item.name +
                " " +
                item.world +
                " " +
                item.role +
                " " +
                item.description
        }});

    }});


    ARCHIVE_DATA.events.forEach(item => {{

        index.push({{
            name: item.name,
            category: "Historical Event",
            searchable:
                item.name +
                " " +
                item.world +
                " " +
                item.type +
                " " +
                item.description
        }});

    }});


    ARCHIVE_DATA.factions.forEach(item => {{

        index.push({{
            name: item.name,
            category: "Faction",
            searchable:
                item.name +
                " " +
                item.world +
                " " +
                item.type +
                " " +
                item.description
        }});

    }});


    ARCHIVE_DATA.artifacts.forEach(item => {{

        index.push({{
            name: item.name,
            category: "Artifact",
            searchable:
                item.name +
                " " +
                item.world +
                " " +
                item.classification +
                " " +
                item.description
        }});

    }});


    ARCHIVE_DATA.documents.forEach(item => {{

        index.push({{
            name: item.title,
            category: "Document",
            searchable:
                item.title +
                " " +
                item.world +
                " " +
                item.type +
                " " +
                item.excerpt
        }});

    }});


    ARCHIVE_DATA.canonGroups.forEach(group => {{

        group.items.forEach(item => {{

            index.push({{
                name: item,
                category: group.name,
                searchable:
                    item +
                    " " +
                    group.name
            }});

        }});

    }});


    return index;
}}


const SEARCH_INDEX =
    buildSearchIndex();


// ============================================================
// SEARCH
// ============================================================

function performSearch(query) {{

    const container =
        $("#searchResults");

    query =
        query
            .trim()
            .toLowerCase();

    memory.searchTerm =
        query;

    if (!query) {{

        container.hidden = true;
        container.innerHTML = "";

        return;
    }}


    const results =
        SEARCH_INDEX
            .filter(
                item =>
                    item.searchable
                        .toLowerCase()
                        .includes(query)
            )
            .slice(0, 14);


    container.innerHTML = "";


    if (!results.length) {{

        container.appendChild(
            createElement(
                "div",
                "empty",
                "No matching archive record."
            )
        );

    }} else {{

        results.forEach(result => {{

            const row =
                createElement(
                    "div",
                    "search-result"
                );

            const title =
                createElement(
                    "strong",
                    "",
                    result.name
                );

            const category =
                createElement(
                    "small",
                    "",
                    result.category
                );

            row.appendChild(title);
            row.appendChild(category);

            row.addEventListener(
                "click",
                () => {{

                    discoverByName(
                        result.name
                    );

                    $("#searchInput").value = "";

                    container.hidden = true;
                }}
            );

            container.appendChild(row);

        }});

    }}

    container.hidden = false;
}}


// ============================================================
// NAVIGATION
// ============================================================

function buildNavigation() {{

    const worldNav =
        $("#worldNav");

    ARCHIVE_DATA.worlds.forEach(
        world => {{

            const button =
                createElement(
                    "button",
                    "nav-item",
                    world.name
                );

            button.type = "button";

            button.addEventListener(
                "click",
                () =>
                    discoverByName(
                        world.name
                    )
            );

            worldNav.appendChild(
                button
            );

        }}
    );


    const canonNav =
        $("#canonNav");

    ARCHIVE_DATA.canonGroups.forEach(
        group => {{

            const button =
                createElement(
                    "button",
                    "nav-item",
                    group.name
                );

            button.type = "button";

            button.addEventListener(
                "click",
                () =>
                    showReferenceCollection(
                        group.name
                    )
            );

            canonNav.appendChild(
                button
            );

        }}
    );


    const typeNav =
        $("#typeNav");

    [
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
    ].forEach(type => {{

        const button =
            createElement(
                "button",
                "nav-item",
                type
            );

        button.type = "button";

        button.addEventListener(
            "click",
            () =>
                showTypeCollection(type)
        );

        typeNav.appendChild(
            button
        );

    }});
}}


// ============================================================
// REFERENCE COLLECTION
// ============================================================

function showReferenceCollection(
    groupName
) {{

    const group =
        ARCHIVE_DATA.canonGroups.find(
            x => x.name === groupName
        );

    if (!group) {{
        discoverRandom();
        return;
    }}


    const item =
        randomFrom(group.items);


    renderArticle({{

        title: item,

        subtitle:
            groupName +
            " reference",

        type: "Reference Entry",

        world: groupName,

        year: "Published fictional universe",

        author: "Reference Index",

        opening:
            item +
            " is indexed here as part of the " +
            groupName +
            " collection. This section is a "
            +
            "reference/navigation entry and does not "
            +
            "create new official canon.",

        sections: [

            [
                "Scope",
                "The archive records the work or category "
                +
                "so that readers can navigate related "
                +
                "fictional material."
            ],

            [
                "Canon boundary",
                "Published canon should be distinguished "
                +
                "from fan interpretation, original fiction "
                +
                "and alternate-universe material."
            ],

            [
                "Archive note",
                "This site does not claim that its original "
                +
                "fictional records are official material "
                +
                "from the referenced work."
            ],

            [
                "Further research",
                "Consult the official publications and "
                +
                "licensed source material when establishing "
                +
                "actual canon."
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

        related:
            group.items
                .filter(
                    x => x !== item
                )
                .slice(0, 4),

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
                .includes(
                    type.toLowerCase()
                );

        }});


    if (matching.length) {{

        const item =
            randomFrom(matching);

        discoverByName(
            item.name
        );

    }} else {{

        discoverRandom();

    }}

    closeMenu();
}}


// ============================================================
// TIMELINE
// ============================================================

function buildTimeline() {{

    const container =
        $("#timelineGrid");

    container.innerHTML = "";


    const records =
        [
            ...ARCHIVE_DATA.events
        ]
        .sort(
            () => Math.random() - .5
        )
        .slice(0, 6);


    records.forEach(event => {{

        const card =
            createElement(
                "article",
                "timeline-card"
            );

        const year =
            createElement(
                "div",
                "timeline-year",
                event.year
            );

        const title =
            createElement(
                "h3",
                "",
                event.name
            );

        const description =
            createElement(
                "p",
                "",
                event.description
            );

        card.appendChild(year);
        card.appendChild(title);
        card.appendChild(description);

        card.addEventListener(
            "click",
            () =>
                discoverByName(
                    event.name
                )
        );

        container.appendChild(
            card
        );

    }});
}}


// ============================================================
// MENU
// ============================================================

function openMenu() {{

    document.body.classList.add(
        "menu-open"
    );

    memory.menuOpen = true;

    $("#menuButton").setAttribute(
        "aria-expanded",
        "true"
    );

    $("#menuButton").setAttribute(
        "aria-label",
        "Close navigation"
    );
}}


function closeMenu() {{

    document.body.classList.remove(
        "menu-open"
    );

    memory.menuOpen = false;

    $("#menuButton").setAttribute(
        "aria-expanded",
        "false"
    );

    $("#menuButton").setAttribute(
        "aria-label",
        "Open navigation"
    );
}}


// ============================================================
// ARCHIVE STATUS
// ============================================================

function updateArchiveState() {{

    const element =
        $("#archiveState");

    element.textContent =
        memory.discoveryCount > 0
            ? "Active · " +
              memory.discoveryCount +
              " discoveries"
            : "Active";
}}


// ============================================================
// EVENT LISTENERS
// ============================================================

$("#searchInput").addEventListener(
    "input",
    event =>
        performSearch(
            event.target.value
        )
);


$("#randomButton").addEventListener(
    "click",
    discoverRandom
);


$("#heroDiscover").addEventListener(
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


document
    .querySelectorAll(
        "[data-action]"
    )
    .forEach(button => {{

        button.addEventListener(
            "click",
            () => {{

                const action =
                    button.dataset.action;


                if (
                    action === "random"
                ) {{
                    discoverRandom();
                }}


                if (
                    action === "home"
                ) {{
                    window.scrollTo({{
                        top: 0,
                        behavior: "smooth"
                    }});
                }}


                if (
                    action === "timeline"
                ) {{
                    $("#timelineSection")
                        .scrollIntoView({{
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
            document.activeElement.tagName !== "INPUT" &&
            document.activeElement.tagName !== "TEXTAREA"
        ) {{

            event.preventDefault();

            $("#searchInput").focus();

        }}


        if (
            event.key === "Escape"
        ) {{

            closeMenu();

            $("#searchResults").hidden =
                true;

        }}

    }}
);


document.addEventListener(
    "click",
    event => {{

        const search =
            document.querySelector(
                ".search"
            );

        if (
            !search.contains(
                event.target
            )
        ) {{
            $("#searchResults").hidden =
                true;
        }}

    }}
);


// ============================================================
// INITIALIZE
// ============================================================

buildNavigation();

buildTimeline();

renderArticle(
    INITIAL_ARTICLE
);

</script>

</body>
</html>
"""


# ============================================================
# GENERATE SITE
# ============================================================

def main():

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    document = build_html()

    OUTPUT_FILE.write_text(
        document,
        encoding="utf-8"
    )

    print()
    print("=" * 64)
    print("FORBIDDEN LORE WIKI GENERATED")
    print("=" * 64)
    print()
    print(f"Output: {OUTPUT_FILE.resolve()}")
    print()
    print("Single static HTML file")
    print("No database")
    print("No localStorage")
    print("No sessionStorage")
    print("No login/signup")
    print("No backend")
    print("Browser memory only")
    print()
    print("Render publish directory:")
    print("site")
    print()


if __name__ == "__main__":
    main()
