from pathlib import Path
import html
import json
import random
import textwrap


# ============================================================
# FORBIDDEN LORE WIKI
# COMPLETE STATIC-SITE GENERATOR
# ============================================================

OUTPUT_DIR = Path("site")
OUTPUT_FILE = OUTPUT_DIR / "index.html"

random.seed(742913)


# ============================================================
# ORIGINAL WORLDS
# ============================================================

WORLDS = [
    {
        "name": "Elaria",
        "era": "The Late Imperial Cycle",
        "status": "Fragmentary",
        "description": (
            "A continent whose surviving histories contain several incompatible "
            "chronologies. Royal records frequently contradict temple archives."
        ),
        "keywords": ["empire", "chronology", "temples", "archives"],
    },
    {
        "name": "Vael Taryn",
        "era": "The River Kingdom Period",
        "status": "Documented",
        "description": (
            "A river-dominated civilization remembered for merchant leagues, "
            "fortified crossings and unusually detailed commercial records."
        ),
        "keywords": ["river", "merchant", "kingdom", "trade"],
    },
    {
        "name": "Ashen Realms",
        "era": "Post-Cataclysmic Age",
        "status": "Restricted",
        "description": (
            "A collection of territories that survived an unnamed catastrophe. "
            "Many maps disagree about the location of its former capitals."
        ),
        "keywords": ["cataclysm", "maps", "ruins", "survivors"],
    },
    {
        "name": "Kharad Vey",
        "era": "Third Crown Dynasty",
        "status": "Disputed",
        "description": (
            "A mountain civilization whose royal succession records appear "
            "to contain an intentionally removed generation."
        ),
        "keywords": ["mountains", "dynasty", "succession", "royalty"],
    },
    {
        "name": "Namaris",
        "era": "Age of Glass",
        "status": "Unverified",
        "description": (
            "A coastal world described by travelers as a place where cities "
            "were built around enormous translucent mineral formations."
        ),
        "keywords": ["coast", "glass", "cities", "minerals"],
    },
    {
        "name": "Orthell",
        "era": "The Broken Calendar",
        "status": "Fragmentary",
        "description": (
            "An old civilization whose historians stopped using numbered years "
            "after an unexplained astronomical event."
        ),
        "keywords": ["calendar", "astronomy", "historians", "years"],
    },
    {
        "name": "Serevan",
        "era": "The Northern Campaigns",
        "status": "Restricted",
        "description": (
            "A militarized federation whose surviving battlefield reports "
            "frequently omit the names of defeated commanders."
        ),
        "keywords": ["war", "federation", "military", "campaigns"],
    },
    {
        "name": "Ilyr",
        "era": "The First Maritime Age",
        "status": "Unresolved",
        "description": (
            "An island civilization known almost entirely through navigation "
            "logs written by people who never claimed to have visited it."
        ),
        "keywords": ["islands", "navigation", "sea", "logs"],
    },
]


# ============================================================
# CHARACTERS
# ============================================================

CHARACTERS = [
    {
        "name": "Nera Kesh",
        "world": "Ashen Realms",
        "role": "Cartographer",
        "period": "Post-Cataclysmic Age",
        "description": (
            "A fictional mapmaker whose surviving charts contain coastlines "
            "not found on any contemporary map."
        ),
    },
    {
        "name": "Ilyan Voss",
        "world": "Elaria",
        "role": "Imperial Archivist",
        "period": "Late Imperial Cycle",
        "description": (
            "An archivist credited with preserving three contradictory versions "
            "of the same imperial succession."
        ),
    },
    {
        "name": "Seren Vale",
        "world": "Vael Taryn",
        "role": "Merchant-Prince",
        "period": "River Kingdom Period",
        "description": (
            "A fictional merchant ruler whose private ledgers mention a city "
            "that does not appear on any surviving map."
        ),
    },
    {
        "name": "Maer Oth",
        "world": "Kharad Vey",
        "role": "Royal Genealogist",
        "period": "Third Crown Dynasty",
        "description": (
            "The genealogist responsible for a royal lineage that contains "
            "a forty-two-year absence."
        ),
    },
    {
        "name": "Tessa Arin",
        "world": "Namaris",
        "role": "Glasswright",
        "period": "Age of Glass",
        "description": (
            "A fictional artisan whose surviving notes describe structures "
            "that appear impossible for the technology of her period."
        ),
    },
    {
        "name": "Corven Dhal",
        "world": "Serevan",
        "role": "Field Commander",
        "period": "Northern Campaigns",
        "description": (
            "A commander whose battlefield reports repeatedly refer to an "
            "unnamed unit identified only by a black geometric mark."
        ),
    },
    {
        "name": "Oren Pell",
        "world": "Orthell",
        "role": "Astronomer",
        "period": "Broken Calendar",
        "description": (
            "An astronomer whose final surviving observation predicts an event "
            "that appears to have occurred several centuries earlier."
        ),
    },
    {
        "name": "Lysa Mer",
        "world": "Ilyr",
        "role": "Navigator",
        "period": "First Maritime Age",
        "description": (
            "A navigator whose log contains precise coordinates for an island "
            "that disappears from every later chart."
        ),
]


# ============================================================
# EVENTS
# ============================================================

EVENTS = [
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
    {
        "name": "The Burning of the Northern Ledger",
        "year": "312 A.C.",
        "world": "Vael Taryn",
        "type": "Destruction",
        "description": (
            "A merchant archive reportedly disappeared during a fire that "
            "destroyed only one building in an otherwise untouched district."
        ),
    },
    {
        "name": "The Ashfall Crossing",
        "year": "Unknown",
        "world": "Ashen Realms",
        "type": "Migration",
        "description": (
            "A population movement referenced by five different settlements "
            "but by no surviving government."
        ),
    },
    {
        "name": "The Empty Coronation",
        "year": "Year 0",
        "world": "Kharad Vey",
        "type": "Succession crisis",
        "description": (
            "A coronation recorded in ceremonial documents but absent from "
            "every surviving royal genealogy."
        ),
    },
    {
        "name": "The Glass Tide",
        "year": "Approx. 88 AG",
        "world": "Namaris",
        "type": "Natural anomaly",
        "description": (
            "A coastal event during which large mineral formations reportedly "
            "appeared along several miles of shoreline."
        ),
    },
    {
        "name": "The Last Calendar Night",
        "year": "Unknown",
        "world": "Orthell",
        "type": "Astronomical event",
        "description": (
            "The final dated astronomical observation before the civilization "
            "abandoned conventional numbered years."
        ),
    },
    {
        "name": "The Black Standard Campaign",
        "year": "641 N.C.",
        "world": "Serevan",
        "type": "Military campaign",
        "description": (
            "A campaign described in official reports without identifying "
            "the force that supposedly commanded it."
        ),
    },
    {
        "name": "The Vanishing Meridian",
        "year": "Uncertain",
        "world": "Ilyr",
        "type": "Navigational anomaly",
        "description": (
            "A sequence of navigation records that all terminate at nearly "
            "the same unexplained coordinate."
        ),
    },
]


# ============================================================
# FACTIONS
# ============================================================

FACTIONS = [
    {
        "name": "Kareth League",
        "world": "Vael Taryn",
        "type": "Merchant alliance",
        "description": (
            "A fictional commercial coalition controlling several northern "
            "river crossings."
        ),
    },
    {
        "name": "Order of the Hollow Crown",
        "world": "Kharad Vey",
        "type": "Royal institution",
        "description": (
            "A ceremonial order responsible for preserving disputed succession "
            "records."
        ),
    },
    {
        "name": "Ash Registry",
        "world": "Ashen Realms",
        "type": "Archive network",
        "description": (
            "A loose network of record keepers who catalogued settlements "
            "after the cataclysm."
        ),
    },
    {
        "name": "The Meridian Court",
        "world": "Ilyr",
        "type": "Maritime authority",
        "description": (
            "A fictional authority mentioned only in navigation documents."
        ),
    },
    {
        "name": "Glasswright Compact",
        "world": "Namaris",
        "type": "Guild",
        "description": (
            "An artisan organization associated with the construction of "
            "large translucent structures."
        ),
    },
    {
        "name": "The Calendar Keepers",
        "world": "Orthell",
        "type": "Scholarly order",
        "description": (
            "A group of astronomers and historians who preserved pre-Broken "
            "Calendar records."
        ),
    },
]


# ============================================================
# ARTIFACTS
# ============================================================

ARTIFACTS = [
    {
        "name": "The Black Meridian Map",
        "world": "Ashen Realms",
        "type": "Map",
        "status": "Partially recovered",
        "description": (
            "A map showing a coastline that appears nowhere in surviving "
            "geographical surveys."
        ),
    },
    {
        "name": "The Kareth Ledger",
        "world": "Vael Taryn",
        "type": "Financial record",
        "status": "Referenced",
        "description": (
            "A commercial ledger believed to contain evidence of a missing "
            "trade route."
        ),
    },
    {
        "name": "Crownless Seal",
        "world": "Kharad Vey",
        "type": "Royal insignia",
        "status": "Authenticity disputed",
        "description": (
            "A seal bearing the symbols of a monarch absent from official "
            "royal succession lists."
        ),
    },
    {
        "name": "The Ninth Star Lens",
        "world": "Orthell",
        "type": "Astronomical instrument",
        "status": "Unverified",
        "description": (
            "A fictional instrument said to reveal an additional reference "
            "point in the night sky."
        ),
    },
    {
        "name": "Glass Memory Tablet",
        "world": "Namaris",
        "type": "Inscribed mineral",
        "status": "Fragmentary",
        "description": (
            "A translucent tablet containing writing visible only from "
            "certain angles."
        ),
    },
]


# ============================================================
# DOCUMENTS
# ============================================================

DOCUMENTS = [
    {
        "name": "The Ash Registry, Volume IV",
        "world": "Ashen Realms",
        "type": "Administrative archive",
        "condition": "Fragmentary",
        "description": (
            "A fictional registry containing population records from "
            "settlements believed to have disappeared."
        ),
    },
    {
        "name": "Ledger of the Northern Crossing",
        "world": "Vael Taryn",
        "type": "Commercial document",
        "condition": "Referenced only",
        "description": (
            "A missing merchant ledger known through quotations in later "
            "financial disputes."
        ),
    },
    {
        "name": "Chronicle of the Empty Crown",
        "world": "Kharad Vey",
        "type": "Royal chronicle",
        "condition": "Disputed",
        "description": (
            "A chronicle describing a succession event absent from official "
            "genealogical records."
        ),
    },
    {
        "name": "The Last Meridian Log",
        "world": "Ilyr",
        "type": "Navigation log",
        "condition": "Partial",
        "description": (
            "A navigation document terminating at coordinates shared by "
            "several unrelated voyages."
        ),
    },
]


# ============================================================
# QUESTIONS
# ============================================================

QUESTIONS = [
    {
        "question": "Why do six Elarian archives contain the same seven-day gap?",
        "status": "Unresolved",
        "related": "The Seven-Day Silence",
    },
    {
        "question": "Who constructed the coastline shown on Nera Kesh's map?",
        "status": "No accepted answer",
        "related": "The Black Meridian Map",
    },
    {
        "question": "Why was one royal generation removed from Kharad Vey records?",
        "status": "Disputed",
        "related": "Order of the Hollow Crown",
    },
    {
        "question": "Did the Vanishing Meridian represent a real location?",
        "status": "Unverified",
        "related": "The Last Meridian Log",
    },
    {
        "question": "Why did Orthell abandon numbered years?",
        "status": "Multiple theories",
        "related": "The Last Calendar Night",
    },
]


# ============================================================
# REFERENCE UNIVERSES
# ============================================================

REFERENCE_UNIVERSES = [
    {
        "name": "Anime",
        "description": (
            "Reference category for Japanese animated fictional universes."
        ),
    },
    {
        "name": "Manhwa",
        "description": (
            "Reference category for Korean comics and their fictional settings."
        ),
    },
    {
        "name": "Manhua",
        "description": (
            "Reference category for Chinese comics and their fictional settings."
        ),
    },
    {
        "name": "Donghua",
        "description": (
            "Reference category for Chinese animated fictional universes."
        ),
    },
    {
        "name": "Light Novels",
        "description": (
            "Reference category for serialized Japanese light-novel fiction."
        ),
    },
    {
        "name": "Comics",
        "description": (
            "Reference category covering major comic-book fictional universes."
        ),
    },
    {
        "name": "DC",
        "description": (
            "Reference category for DC fictional universes and characters."
        ),
    },
    {
        "name": "Marvel",
        "description": (
            "Reference category for Marvel fictional universes and characters."
        ),
    },
]


# ============================================================
# ARCHIVE TYPES
# ============================================================

ARCHIVE_TYPES = [
    "Characters",
    "Historical Events",
    "Factions",
    "Artifacts",
    "Documents",
    "Worlds",
    "Questions",
    "Conflicts",
    "Political Systems",
    "Locations",
    "Chronologies",
    "Unresolved Records",
]


# ============================================================
# ARTICLE TYPES
# ============================================================

ARTICLE_TYPES = [
    "Historical Record",
    "Recovered Document",
    "Biographical File",
    "Chronological Entry",
    "Restricted Report",
    "Cross-Reference",
    "Archaeological Note",
    "Political Record",
    "Military Record",
    "Unresolved Case",
]


# ============================================================
# THEMES / LAYOUT MODES
# ============================================================

THEMES = [
    {
        "name": "Obsidian Archive",
        "class": "theme-obsidian",
    },
    {
        "name": "Paper Registry",
        "class": "theme-paper",
    },
    {
        "name": "Redacted Bureau",
        "class": "theme-redacted",
    },
    {
        "name": "Cold Repository",
        "class": "theme-cold",
    },
]


LAYOUTS = [
    "layout-standard",
    "layout-wide-record",
    "layout-split-record",
    "layout-documentary",
]


# ============================================================
# HELPERS
# ============================================================

def esc(value):
    return html.escape(str(value), quote=True)


def slug(value):
    value = str(value).lower().strip()
    result = []
    for char in value:
        if char.isalnum():
            result.append(char)
        elif char in " _-/":
            result.append("-")
    output = "".join(result)
    while "--" in output:
        output = output.replace("--", "-")
    return output.strip("-")


def record_id(prefix, index):
    return f"{prefix.upper()}-{index + 1:03d}"


def archive_code():
    return f"ARCH-{random.randint(1000, 9999)}"


def build_search_data():
    records = []

    for index, item in enumerate(WORLDS):
        records.append(
            {
                "id": record_id("WRL", index),
                "type": "World",
                "name": item["name"],
                "world": item["name"],
                "status": item["status"],
                "description": item["description"],
            }
        )

    for index, item in enumerate(CHARACTERS):
        records.append(
            {
                "id": record_id("CHR", index),
                "type": "Character",
                "name": item["name"],
                "world": item["world"],
                "status": "Archived",
                "description": item["description"],
            }
        )

    for index, item in enumerate(EVENTS):
        records.append(
            {
                "id": record_id("EVT", index),
                "type": "Historical Event",
                "name": item["name"],
                "world": item["world"],
                "status": "Archived",
                "description": item["description"],
            }
        )

    for index, item in enumerate(FACTIONS):
        records.append(
            {
                "id": record_id("FAC", index),
                "type": "Faction",
                "name": item["name"],
                "world": item["world"],
                "status": "Archived",
                "description": item["description"],
            }
        )

    for index, item in enumerate(ARTIFACTS):
        records.append(
            {
                "id": record_id("ART", index),
                "type": "Artifact",
                "name": item["name"],
                "world": item["world"],
                "status": item["status"],
                "description": item["description"],
            }
        )

    for index, item in enumerate(DOCUMENTS):
        records.append(
            {
                "id": record_id("DOC", index),
                "type": "Document",
                "name": item["name"],
                "world": item["world"],
                "status": item["condition"],
                "description": item["description"],
            }
        )

    for index, item in enumerate(QUESTIONS):
        records.append(
            {
                "id": record_id("QST", index),
                "type": "Unresolved Question",
                "name": item["question"],
                "world": item["related"],
                "status": item["status"],
                "description": item["question"],
            }
        )

    return records


SEARCH_DATA = build_search_data()


# ============================================================
# CSS
# ============================================================

CSS = r"""
/* ============================================================
   FORBIDDEN LORE WIKI
   ARCHIVAL INTERFACE
   ============================================================ */

:root {
    --bg: #11110f;
    --bg-2: #161612;
    --panel: #181814;
    --panel-2: #1d1d18;
    --paper: #d7d0bd;
    --paper-dim: #aaa38f;
    --paper-faint: #777363;
    --ink: #151512;
    --line: rgba(215, 208, 189, 0.20);
    --line-strong: rgba(215, 208, 189, 0.42);
    --red: #8f302d;
    --red-bright: #b64a44;
    --yellow: #b49a55;
    --green: #6e8b69;
    --blue: #63798c;
    --black: #090908;
    --shadow: rgba(0, 0, 0, 0.45);
    --serif: Georgia, "Times New Roman", serif;
    --sans: "Arial Narrow", Arial, Helvetica, sans-serif;
    --mono: "Courier New", Courier, monospace;
}

* {
    box-sizing: border-box;
}

html {
    min-width: 320px;
    background: var(--bg);
    color: var(--paper);
    scroll-behavior: smooth;
}

body {
    margin: 0;
    min-height: 100vh;
    background:
        radial-gradient(circle at 20% 10%, rgba(255,255,255,0.025), transparent 25%),
        radial-gradient(circle at 80% 70%, rgba(143,48,45,0.035), transparent 28%),
        linear-gradient(90deg, rgba(255,255,255,0.012) 1px, transparent 1px),
        linear-gradient(rgba(255,255,255,0.008) 1px, transparent 1px),
        var(--bg);
    background-size: auto, auto, 37px 37px, 37px 37px, auto;
    font-family: var(--sans);
    overflow-x: hidden;
}

body::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 1000;
    opacity: 0.09;
    background:
        repeating-linear-gradient(
            0deg,
            rgba(255,255,255,0.04) 0,
            rgba(255,255,255,0.04) 1px,
            transparent 1px,
            transparent 4px
        );
    mix-blend-mode: overlay;
}

button,
input {
    font: inherit;
}

button {
    color: inherit;
}

a {
    color: inherit;
}

::selection {
    background: var(--red);
    color: #fff;
}

/* ============================================================
   FRAME
   ============================================================ */

.archive-shell {
    width: min(1600px, 100%);
    margin: 0 auto;
    min-height: 100vh;
    border-left: 1px solid var(--line);
    border-right: 1px solid var(--line);
}

.archive-topline {
    min-height: 44px;
    display: grid;
    grid-template-columns: minmax(250px, 1fr) auto auto;
    gap: 0;
    align-items: center;
    border-bottom: 1px solid var(--line-strong);
    background: rgba(7, 7, 6, 0.82);
}

.archive-brand {
    min-width: 0;
    padding: 10px 18px;
    font-family: var(--mono);
    font-size: 11px;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.archive-edition,
.archive-status {
    height: 100%;
    display: flex;
    align-items: center;
    padding: 10px 16px;
    border-left: 1px solid var(--line);
    font-family: var(--mono);
    font-size: 10px;
    letter-spacing: 0.11em;
    text-transform: uppercase;
    white-space: nowrap;
}

.archive-status::before {
    content: "";
    width: 7px;
    height: 7px;
    margin-right: 8px;
    border-radius: 50%;
    background: var(--green);
    box-shadow: 0 0 10px rgba(110,139,105,0.35);
}

/* ============================================================
   MAIN GRID
   ============================================================ */

.archive-body {
    display: grid;
    grid-template-columns: 238px minmax(0, 1fr);
    min-height: calc(100vh - 44px);
}

.archive-sidebar {
    border-right: 1px solid var(--line-strong);
    background:
        linear-gradient(180deg, rgba(255,255,255,0.018), transparent 20%),
        rgba(10, 10, 9, 0.72);
}

.sidebar-inner {
    position: sticky;
    top: 0;
    max-height: 100vh;
    overflow-y: auto;
    padding: 17px 0 24px;
}

.sidebar-section {
    padding: 0 14px 17px;
    margin-bottom: 15px;
    border-bottom: 1px solid var(--line);
}

.sidebar-label {
    margin-bottom: 8px;
    color: var(--paper-faint);
    font-family: var(--mono);
    font-size: 9px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
}

.sidebar-nav {
    display: flex;
    flex-direction: column;
}

.sidebar-link {
    display: flex;
    align-items: baseline;
    gap: 7px;
    padding: 5px 6px;
    border: 0;
    background: transparent;
    color: var(--paper-dim);
    text-align: left;
    font-family: var(--mono);
    font-size: 10px;
    letter-spacing: 0.05em;
    cursor: pointer;
    transition:
        background 120ms ease,
        color 120ms ease,
        padding-left 120ms ease;
}

.sidebar-link::before {
    content: "/";
    color: var(--paper-faint);
}

.sidebar-link:hover,
.sidebar-link.active {
    padding-left: 11px;
    background: rgba(215,208,189,0.055);
    color: var(--paper);
}

.sidebar-link.active {
    border-left: 2px solid var(--red);
}

.sidebar-ref {
    display: block;
    padding: 5px 6px;
    color: var(--paper-faint);
    font-family: var(--mono);
    font-size: 9px;
    line-height: 1.5;
}

/* ============================================================
   CONTENT
   ============================================================ */

.archive-content {
    min-width: 0;
    padding: 0;
}

.content-toolbar {
    min-height: 49px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 14px;
    padding: 8px 18px;
    border-bottom: 1px solid var(--line);
    background: rgba(15,15,13,0.80);
}

.breadcrumb {
    min-width: 0;
    overflow: hidden;
    color: var(--paper-faint);
    font-family: var(--mono);
    font-size: 9px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    white-space: nowrap;
    text-overflow: ellipsis;
}

.breadcrumb strong {
    color: var(--paper-dim);
}

.toolbar-actions {
    display: flex;
    gap: 6px;
    flex-shrink: 0;
}

.toolbar-button {
    border: 1px solid var(--line);
    background: transparent;
    color: var(--paper-dim);
    padding: 6px 9px;
    font-family: var(--mono);
    font-size: 9px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    cursor: pointer;
}

.toolbar-button:hover {
    border-color: var(--line-strong);
    color: var(--paper);
    background: rgba(215,208,189,0.04);
}

.record-stage {
    padding: 23px;
}

/* ============================================================
   RECORD HEADER
   ============================================================ */

.record-header {
    position: relative;
    border-top: 1px solid var(--line-strong);
    border-bottom: 1px solid var(--line-strong);
    padding: 23px 24px 20px;
    background:
        linear-gradient(90deg, rgba(215,208,189,0.022), transparent 60%),
        rgba(19,19,16,0.70);
}

.record-header::after {
    content: "ARCHIVAL COPY";
    position: absolute;
    top: 18px;
    right: 22px;
    padding: 5px 8px;
    border: 1px solid rgba(143,48,45,0.55);
    color: rgba(182,74,68,0.80);
    font-family: var(--mono);
    font-size: 8px;
    letter-spacing: 0.18em;
    transform: rotate(-2deg);
}

.record-kicker {
    margin-bottom: 12px;
    color: var(--paper-faint);
    font-family: var(--mono);
    font-size: 9px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
}

.record-title {
    max-width: 980px;
    margin: 0;
    color: var(--paper);
    font-family: var(--serif);
    font-size: clamp(34px, 5vw, 68px);
    font-weight: normal;
    line-height: 0.98;
    letter-spacing: -0.035em;
}

.record-subtitle {
    max-width: 880px;
    margin: 15px 0 0;
    color: var(--paper-dim);
    font-family: var(--mono);
    font-size: 10px;
    line-height: 1.65;
    text-transform: uppercase;
    letter-spacing: 0.07em;
}

.record-meta {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    margin-top: 23px;
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
}

.meta-cell {
    min-width: 0;
    padding: 11px 13px;
    border-right: 1px solid var(--line);
}

.meta-cell:last-child {
    border-right: 0;
}

.meta-label {
    display: block;
    margin-bottom: 5px;
    color: var(--paper-faint);
    font-family: var(--mono);
    font-size: 8px;
    letter-spacing: 0.13em;
    text-transform: uppercase;
}

.meta-value {
    display: block;
    color: var(--paper);
    font-family: var(--mono);
    font-size: 10px;
    line-height: 1.4;
}

/* ============================================================
   RECORD GRID
   ============================================================ */

.record-grid {
    display: grid;
    grid-template-columns: minmax(0, 1fr) 270px;
    gap: 0;
    border-bottom: 1px solid var(--line-strong);
}

.record-main {
    min-width: 0;
    border-right: 1px solid var(--line-strong);
}

.record-aside {
    min-width: 0;
    background: rgba(7,7,6,0.28);
}

.archive-block {
    padding: 21px 23px;
    border-bottom: 1px solid var(--line);
}

.archive-block:last-child {
    border-bottom: 0;
}

.block-heading {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 12px;
}

.block-title {
    margin: 0;
    color: var(--paper);
    font-family: var(--mono);
    font-size: 10px;
    font-weight: normal;
    letter-spacing: 0.13em;
    text-transform: uppercase;
}

.block-code {
    color: var(--paper-faint);
    font-family: var(--mono);
    font-size: 8px;
    white-space: nowrap;
}

.archive-text {
    max-width: 880px;
    margin: 0;
    color: var(--paper-dim);
    font-family: var(--serif);
    font-size: 16px;
    line-height: 1.72;
}

.archive-text + .archive-text {
    margin-top: 13px;
}

/* ============================================================
   CLASSIFICATION
   ============================================================ */

.classification-box {
    display: inline-block;
    min-width: 205px;
    margin: 2px 0 4px;
    border: 1px solid var(--line-strong);
}

.classification-heading {
    padding: 7px 10px;
    border-bottom: 1px solid var(--line);
    color: var(--paper-faint);
    font-family: var(--mono);
    font-size: 8px;
    letter-spacing: 0.16em;
    text-transform: uppercase;
}

.classification-value {
    padding: 10px;
    color: var(--red-bright);
    font-family: var(--mono);
    font-size: 15px;
    font-weight: bold;
    letter-spacing: 0.10em;
    text-transform: uppercase;
}

/* ============================================================
   REFERENCE LIST
   ============================================================ */

.reference-list {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    border-top: 1px solid var(--line);
    border-left: 1px solid var(--line);
}

.reference-item {
    min-width: 0;
    padding: 9px 10px;
    border-right: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
}

.reference-id {
    display: block;
    color: var(--yellow);
    font-family: var(--mono);
    font-size: 9px;
}

.reference-name {
    display: block;
    margin-top: 3px;
    color: var(--paper-dim);
    font-family: var(--serif);
    font-size: 13px;
    line-height: 1.3;
}

/* ============================================================
   ASIDE
   ============================================================ */

.aside-block {
    padding: 17px 15px;
    border-bottom: 1px solid var(--line);
}

.aside-label {
    margin-bottom: 8px;
    color: var(--paper-faint);
    font-family: var(--mono);
    font-size: 8px;
    letter-spacing: 0.16em;
    text-transform: uppercase;
}

.aside-value {
    color: var(--paper-dim);
    font-family: var(--mono);
    font-size: 10px;
    line-height: 1.55;
}

.stamp {
    display: inline-block;
    padding: 5px 7px;
    border: 1px solid var(--red);
    color: var(--red-bright);
    font-family: var(--mono);
    font-size: 8px;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    transform: rotate(-1deg);
}

.margin-note {
    padding: 11px;
    border-left: 2px solid var(--yellow);
    background: rgba(180,154,85,0.035);
    color: var(--paper-dim);
    font-family: var(--serif);
    font-size: 13px;
    font-style: italic;
    line-height: 1.55;
}

.redacted-line {
    display: inline;
    padding: 0 4px;
    background: #050504;
    color: #050504;
    user-select: none;
}

.redacted-line:hover {
    color: var(--paper-dim);
}

/* ============================================================
   DISCOVERY STRIP
   ============================================================ */

.discovery-strip {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    border-bottom: 1px solid var(--line-strong);
}

.discovery-cell {
    min-width: 0;
    padding: 17px 18px;
    border-right: 1px solid var(--line);
}

.discovery-cell:last-child {
    border-right: 0;
}

.discovery-label {
    margin-bottom: 7px;
    color: var(--paper-faint);
    font-family: var(--mono);
    font-size: 8px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
}

.discovery-value {
    color: var(--paper);
    font-family: var(--serif);
    font-size: 17px;
    line-height: 1.25;
}

.discovery-small {
    margin-top: 5px;
    color: var(--paper-faint);
    font-family: var(--mono);
    font-size: 8px;
}

/* ============================================================
   SEARCH
   ============================================================ */

.search-overlay {
    position: fixed;
    inset: 0;
    z-index: 900;
    display: none;
    align-items: flex-start;
    justify-content: center;
    padding: 10vh 18px 30px;
    background: rgba(4,4,3,0.91);
    backdrop-filter: blur(7px);
}

.search-overlay.open {
    display: flex;
}

.search-panel {
    width: min(850px, 100%);
    border: 1px solid var(--line-strong);
    background: #11110f;
    box-shadow: 0 30px 90px var(--shadow);
}

.search-top {
    display: flex;
    align-items: center;
    border-bottom: 1px solid var(--line);
}

.search-input {
    flex: 1;
    min-width: 0;
    border: 0;
    outline: 0;
    background: transparent;
    color: var(--paper);
    padding: 17px;
    font-family: var(--mono);
    font-size: 13px;
}

.search-input::placeholder {
    color: var(--paper-faint);
}

.search-close {
    border: 0;
    border-left: 1px solid var(--line);
    background: transparent;
    color: var(--paper-faint);
    padding: 17px;
    cursor: pointer;
    font-family: var(--mono);
    font-size: 10px;
}

.search-results {
    max-height: 65vh;
    overflow-y: auto;
}

.search-result {
    display: grid;
    grid-template-columns: 85px minmax(0, 1fr);
    gap: 12px;
    padding: 12px 16px;
    border-bottom: 1px solid var(--line);
    cursor: pointer;
}

.search-result:hover {
    background: rgba(215,208,189,0.045);
}

.search-result-id {
    color: var(--yellow);
    font-family: var(--mono);
    font-size: 8px;
}

.search-result-title {
    color: var(--paper);
    font-family: var(--serif);
    font-size: 16px;
}

.search-result-meta {
    margin-top: 3px;
    color: var(--paper-faint);
    font-family: var(--mono);
    font-size: 8px;
    text-transform: uppercase;
}

.search-result-description {
    margin-top: 7px;
    color: var(--paper-dim);
    font-family: var(--serif);
    font-size: 12px;
    line-height: 1.45;
}

/* ============================================================
   MOBILE MENU
   ============================================================ */

.mobile-menu-button {
    display: none;
    border: 1px solid var(--line);
    background: transparent;
    color: var(--paper-dim);
    padding: 6px 9px;
    font-family: var(--mono);
    font-size: 9px;
    cursor: pointer;
}

.mobile-drawer {
    display: none;
}

/* ============================================================
   FOOTER
   ============================================================ */

.archive-footer {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 20px;
    padding: 15px 18px;
    border-top: 1px solid var(--line-strong);
    color: var(--paper-faint);
    font-family: var(--mono);
    font-size: 8px;
    line-height: 1.6;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

.archive-footer-right {
    text-align: right;
}

/* ============================================================
   SPECIAL MODES
   ============================================================ */

.theme-paper {
    --bg: #201f1a;
    --panel: #25231d;
    --panel-2: #29271f;
    --paper: #d9cfb9;
}

.theme-redacted {
    --red: #9f3935;
    --red-bright: #c24c45;
}

.theme-cold {
    --paper: #c8d0d0;
    --paper-dim: #9ea8a8;
    --paper-faint: #6d7777;
    --line: rgba(200,208,208,0.18);
    --line-strong: rgba(200,208,208,0.37);
}

/* ============================================================
   RESPONSIVE
   ============================================================ */

@media (max-width: 1050px) {
    .archive-body {
        grid-template-columns: 205px minmax(0, 1fr);
    }

    .record-grid {
        grid-template-columns: minmax(0, 1fr) 225px;
    }

    .record-meta {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .meta-cell:nth-child(2) {
        border-right: 0;
    }

    .meta-cell:nth-child(-n+2) {
        border-bottom: 1px solid var(--line);
    }

    .discovery-strip {
        grid-template-columns: 1fr;
    }

    .discovery-cell {
        border-right: 0;
        border-bottom: 1px solid var(--line);
    }

    .discovery-cell:last-child {
        border-bottom: 0;
    }
}

@media (max-width: 760px) {
    .archive-topline {
        grid-template-columns: minmax(0, 1fr) auto;
    }

    .archive-edition {
        display: none;
    }

    .archive-body {
        display: block;
    }

    .archive-sidebar {
        display: none;
    }

    .mobile-menu-button {
        display: block;
    }

    .content-toolbar {
        padding: 8px 12px;
    }

    .toolbar-button {
        display: none;
    }

    .record-stage {
        padding: 12px;
    }

    .record-header {
        padding: 20px 16px 17px;
    }

    .record-header::after {
        position: static;
        display: inline-block;
        margin-top: 16px;
    }

    .record-title {
        font-size: clamp(34px, 11vw, 54px);
    }

    .record-meta {
        grid-template-columns: 1fr 1fr;
    }

    .record-grid {
        display: block;
    }

    .record-main {
        border-right: 0;
    }

    .record-aside {
        border-top: 1px solid var(--line-strong);
    }

    .archive-block {
        padding: 18px 16px;
    }

    .archive-text {
        font-size: 15px;
    }

    .reference-list {
        grid-template-columns: 1fr;
    }

    .archive-footer {
        grid-template-columns: 1fr;
    }

    .archive-footer-right {
        text-align: left;
    }

    .mobile-drawer {
        position: fixed;
        inset: 44px 0 0;
        z-index: 700;
        overflow-y: auto;
        padding: 15px;
        background: #0b0b0a;
        border-top: 1px solid var(--line-strong);
    }

    .mobile-drawer.open {
        display: block;
    }

    .mobile-drawer .sidebar-section {
        margin-bottom: 10px;
    }
}

@media (max-width: 480px) {
    .archive-brand {
        padding-left: 11px;
        font-size: 9px;
    }

    .archive-status {
        padding: 9px 10px;
        font-size: 8px;
    }

    .record-meta {
        grid-template-columns: 1fr;
    }

    .meta-cell {
        border-right: 0;
        border-bottom: 1px solid var(--line);
    }

    .meta-cell:last-child {
        border-bottom: 0;
    }

    .classification-box {
        width: 100%;
        min-width: 0;
    }

    .toolbar-actions {
        gap: 3px;
    }
}
"""


# ============================================================
# JAVASCRIPT
# ============================================================

JS_TEMPLATE = r"""
const ARCHIVE_DATA = __SEARCH_DATA__;

const originalWorlds = __WORLDS__;
const characters = __CHARACTERS__;
const events = __EVENTS__;
const factions = __FACTIONS__;
const artifacts = __ARTIFACTS__;
const documents = __DOCUMENTS__;
const questions = __QUESTIONS__;

const archiveTypes = __ARCHIVE_TYPES__;
const referenceUniverses = __REFERENCE_UNIVERSES__;

const sessionSeen = new Set();
let currentRecord = null;

const $ = (selector) => document.querySelector(selector);

function escapeHTML(value) {
    return String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}

function choose(array) {
    return array[Math.floor(Math.random() * array.length)];
}

function shuffle(array) {
    return [...array].sort(() => Math.random() - 0.5);
}

function randomFromDifferent(collection, count) {
    return shuffle(collection).slice(0, Math.min(count, collection.length));
}

function makeRecordId() {
    return "REC-" + String(Math.floor(10000 + Math.random() * 90000));
}

function statusFor(record) {
    const statuses = [
        "RESTRICTED",
        "FRAGMENTARY",
        "UNVERIFIED",
        "DISPUTED",
        "ARCHIVED",
        "UNRESOLVED"
    ];

    if (record.status && record.status !== "Archived") {
        return record.status.toUpperCase();
    }

    return choose(statuses);
}

function makeNarrative(record) {
    const openings = [
        "The surviving record is incomplete, but several independent references allow the archive to establish a provisional reconstruction.",
        "No single source provides a complete account. The present entry is assembled from surviving references, later citations and disputed archival fragments.",
        "The chronology remains uncertain. What follows is the archive's current reconstruction rather than an assertion of uncontested historical fact.",
        "The record enters the collection because its references repeatedly appear in otherwise unrelated documents.",
        "The available evidence is insufficient for a final conclusion, although the surviving material is unusually consistent in several important details."
    ];

    const middle = [
        `The primary record identifies ${record.name} in connection with ${record.world || "an unidentified historical setting"}.`,
        `Later documents preserve references to ${record.name}, although their descriptions differ in terminology and date.`,
        `Archivists have repeatedly cross-referenced this record with material originating outside its immediate collection.`,
        `Several secondary records appear to describe the same subject without using the same name.`,
        `The surviving catalogue places this entry among records whose provenance remains incomplete.`
    ];

    const endings = [
        "The absence of evidence has therefore been retained as part of the record rather than silently removed.",
        "Until a stronger source is recovered, the contradictory material remains attached to the entry.",
        "Researchers should therefore distinguish between documented details and later interpretation.",
        "The archive currently preserves multiple possibilities instead of selecting a single definitive explanation.",
        "No final classification has been assigned beyond the current archival status."
    ];

    return [
        choose(openings),
        choose(middle),
        choose(endings)
    ];
}

function makeReferences(record) {
    const related = ARCHIVE_DATA
        .filter(item => item.id !== record.id)
        .filter(item =>
            item.world === record.world ||
            item.type === record.type
        );

    const pool = related.length
        ? related
        : ARCHIVE_DATA.filter(item => item.id !== record.id);

    return randomFromDifferent(pool, 4);
}

function selectRecord() {
    const available = ARCHIVE_DATA.filter(item => !sessionSeen.has(item.id));

    let record;

    if (available.length) {
        record = choose(available);
    } else {
        sessionSeen.clear();
        record = choose(ARCHIVE_DATA);
    }

    sessionSeen.add(record.id);
    return record;
}

function buildReferencesHTML(references) {
    return references.map(item => `
        <div class="reference-item" data-record-id="${escapeHTML(item.id)}">
            <span class="reference-id">${escapeHTML(item.id)}</span>
            <span class="reference-name">${escapeHTML(item.name)}</span>
        </div>
    `).join("");
}

function buildRecord(record) {
    currentRecord = record;

    const references = makeReferences(record);
    const status = statusFor(record);
    const archiveNumber = makeRecordId();

    const narrative = makeNarrative(record);

    const classifications = [
        "RESTRICTED",
        "FRAGMENTARY",
        "ARCHIVED",
        "DISPUTED",
        "UNVERIFIED",
        "UNRESOLVED"
    ];

    const classification =
        status === "ARCHIVED"
            ? choose(classifications)
            : status;

    const recordType = record.type || choose([
        "Historical Record",
        "Recovered Document",
        "Restricted Report",
        "Cross-Reference",
        "Unresolved Case"
    ]);

    const referenceWorld =
        record.world ||
        choose(originalWorlds).name;

    const articleTitle = escapeHTML(record.name);
    const articleType = escapeHTML(recordType);
    const world = escapeHTML(referenceWorld);

    const recordHtml = `
        <div class="record-header">
            <div class="record-kicker">
                Restricted Historical Collection · ${escapeHTML(archiveNumber)}
            </div>

            <h1 class="record-title">${articleTitle}</h1>

            <p class="record-subtitle">
                ${articleType} · ${world} · Archive Status ${escapeHTML(status)}
            </p>

            <div class="record-meta">
                <div class="meta-cell">
                    <span class="meta-label">Record</span>
                    <span class="meta-value">${escapeHTML(record.id)}</span>
                </div>

                <div class="meta-cell">
                    <span class="meta-label">Classification</span>
                    <span class="meta-value">${escapeHTML(classification)}</span>
                </div>

                <div class="meta-cell">
                    <span class="meta-label">Source State</span>
                    <span class="meta-value">${escapeHTML(record.status || "Fragmentary")}</span>
                </div>

                <div class="meta-cell">
                    <span class="meta-label">Collection</span>
                    <span class="meta-value">Forbidden Lore · 01</span>
                </div>
            </div>
        </div>

        <div class="record-grid">
            <main class="record-main">

                <section class="archive-block">
                    <div class="block-heading">
                        <h2 class="block-title">Archival Summary</h2>
                        <span class="block-code">${escapeHTML(record.id)}</span>
                    </div>

                    <p class="archive-text">
                        ${escapeHTML(record.description)}
                    </p>

                    ${narrative.map(text => `
                        <p class="archive-text">${escapeHTML(text)}</p>
                    `).join("")}
                </section>

                <section class="archive-block">
                    <div class="block-heading">
                        <h2 class="block-title">Classification</h2>
                        <span class="block-code">SEC. 04</span>
                    </div>

                    <div class="classification-box">
                        <div class="classification-heading">
                            Archive Classification
                        </div>
                        <div class="classification-value">
                            ${escapeHTML(classification)}
                        </div>
                    </div>
                </section>

                <section class="archive-block">
                    <div class="block-heading">
                        <h2 class="block-title">References</h2>
                        <span class="block-code">CROSS-INDEX</span>
                    </div>

                    <div class="reference-list">
                        ${buildReferencesHTML(references)}
                    </div>
                </section>

                <section class="archive-block">
                    <div class="block-heading">
                        <h2 class="block-title">Archivist Note</h2>
                        <span class="block-code">NOTE ${Math.floor(Math.random() * 900 + 100)}</span>
                    </div>

                    <div class="margin-note">
                        The record has been retained because the contradictions
                        surrounding it are themselves historically significant.
                        <span class="redacted-line">classification withheld</span>
                        remains attached to the original file.
                    </div>
                </section>

            </main>

            <aside class="record-aside">

                <div class="aside-block">
                    <div class="aside-label">Record Status</div>
                    <div class="stamp">${escapeHTML(status)}</div>
                </div>

                <div class="aside-block">
                    <div class="aside-label">Archive Location</div>
                    <div class="aside-value">
                        Collection 01<br>
                        Shelf ${Math.floor(Math.random() * 90 + 10)}<br>
                        Box ${Math.floor(Math.random() * 900 + 100)}<br>
                        File ${Math.floor(Math.random() * 9000 + 1000)}
                    </div>
                </div>

                <div class="aside-block">
                    <div class="aside-label">World Reference</div>
                    <div class="aside-value">
                        ${world}
                    </div>
                </div>

                <div class="aside-block">
                    <div class="aside-label">Confidence</div>
                    <div class="aside-value">
                        ${Math.floor(Math.random() * 35 + 50)}%
                        <br>
                        <span style="color:var(--paper-faint)">
                            provisional reconstruction
                        </span>
                    </div>
                </div>

                <div class="aside-block">
                    <div class="aside-label">Cross-Reference Count</div>
                    <div class="aside-value">
                        ${Math.floor(Math.random() * 40 + 7)} surviving references
                    </div>
                </div>

            </aside>
        </div>

        <div class="discovery-strip">
            <div class="discovery-cell">
                <div class="discovery-label">Current Discovery</div>
                <div class="discovery-value">
                    ${escapeHTML(record.name)}
                </div>
                <div class="discovery-small">
                    ${escapeHTML(record.type)}
                </div>
            </div>

            <div class="discovery-cell">
                <div class="discovery-label">Related World</div>
                <div class="discovery-value">
                    ${world}
                </div>
                <div class="discovery-small">
                    Cross-referenced archive
                </div>
            </div>

            <div class="discovery-cell">
                <div class="discovery-label">Next Action</div>
                <div class="discovery-value">
                    Trace references
                </div>
                <div class="discovery-small">
                    Press D for another record
                </div>
            </div>
        </div>
    `;

    $("#record-stage").innerHTML = recordHtml;

    document.title = `${record.name} · Forbidden Lore Wiki`;

    document.querySelectorAll("[data-record-id]").forEach(node => {
        node.addEventListener("click", () => {
            const id = node.dataset.recordId;
            const found = ARCHIVE_DATA.find(item => item.id === id);

            if (found) {
                sessionSeen.add(found.id);
                buildRecord(found);
                window.scrollTo({ top: 0, behavior: "smooth" });
            }
        });
    });
}

function openSearch() {
    const overlay = $("#search-overlay");
    overlay.classList.add("open");

    const input = $("#search-input");
    input.value = "";
    input.focus();

    renderSearchResults("");
}

function closeSearch() {
    $("#search-overlay").classList.remove("open");
}

function renderSearchResults(query) {
    const target = $("#search-results");
    const normalized = query.trim().toLowerCase();

    const results = ARCHIVE_DATA.filter(item => {
        if (!normalized) {
            return true;
        }

        const searchable = [
            item.id,
            item.type,
            item.name,
            item.world,
            item.status,
            item.description
        ].join(" ").toLowerCase();

        return searchable.includes(normalized);
    }).slice(0, 40);

    if (!results.length) {
        target.innerHTML = `
            <div style="padding:24px;color:var(--paper-faint);font-family:var(--mono);font-size:10px;">
                NO MATCHING RECORDS FOUND.
            </div>
        `;
        return;
    }

    target.innerHTML = results.map(item => `
        <div class="search-result" data-search-id="${escapeHTML(item.id)}">
            <div>
                <div class="search-result-id">
                    ${escapeHTML(item.id)}
                </div>
            </div>

            <div>
                <div class="search-result-title">
                    ${escapeHTML(item.name)}
                </div>

                <div class="search-result-meta">
                    ${escapeHTML(item.type)}
                    ·
                    ${escapeHTML(item.world || "UNKNOWN")}
                </div>

                <div class="search-result-description">
                    ${escapeHTML(item.description)}
                </div>
            </div>
        </div>
    `).join("");

    document.querySelectorAll("[data-search-id]").forEach(node => {
        node.addEventListener("click", () => {
            const id = node.dataset.searchId;
            const found = ARCHIVE_DATA.find(item => item.id === id);

            if (found) {
                sessionSeen.add(found.id);
                closeSearch();
                buildRecord(found);
                window.scrollTo({ top: 0, behavior: "smooth" });
            }
        });
    });
}

function toggleMobileMenu() {
    $("#mobile-drawer").classList.toggle("open");
}

function closeMobileMenu() {
    $("#mobile-drawer").classList.remove("open");
}

function randomDiscovery() {
    buildRecord(selectRecord());
    closeMobileMenu();
    window.scrollTo({ top: 0, behavior: "smooth" });
}

function navigateToType(type) {
    const found = ARCHIVE_DATA.filter(item => item.type === type);

    if (found.length) {
        buildRecord(choose(found));
    } else {
        buildRecord(choose(ARCHIVE_DATA));
    }

    closeMobileMenu();
    window.scrollTo({ top: 0, behavior: "smooth" });
}

function openTimeline() {
    const record = choose(events);

    const timelineRecord = {
        id: "TIM-" + String(Math.floor(100 + Math.random() * 900)),
        type: "Historical Timeline",
        name: record.name,
        world: record.world,
        status: "TIMELINE ENTRY",
        description: record.description
    };

    buildRecord(timelineRecord);
    closeMobileMenu();
    window.scrollTo({ top: 0, behavior: "smooth" });
}

function showReferenceUniverse() {
    const reference = choose(referenceUniverses);

    const record = {
        id: "REF-" + String(Math.floor(100 + Math.random() * 900)),
        type: "Reference Universe",
        name: reference.name,
        world: "Reference Collection",
        status: "REFERENCE",
        description: reference.description
    };

    buildRecord(record);
    closeMobileMenu();
    window.scrollTo({ top: 0, behavior: "smooth" });
}

document.addEventListener("DOMContentLoaded", () => {
    buildRecord(selectRecord());

    $("#random-button").addEventListener("click", randomDiscovery);
    $("#search-button").addEventListener("click", openSearch);
    $("#search-close").addEventListener("click", closeSearch);
    $("#mobile-menu-button").addEventListener("click", toggleMobileMenu);

    $("#search-input").addEventListener("input", event => {
        renderSearchResults(event.target.value);
    });

    $("#search-overlay").addEventListener("click", event => {
        if (event.target === $("#search-overlay")) {
            closeSearch();
        }
    });

    document.querySelectorAll("[data-action='discover']").forEach(button => {
        button.addEventListener("click", randomDiscovery);
    });

    document.querySelectorAll("[data-action='timeline']").forEach(button => {
        button.addEventListener("click", openTimeline);
    });

    document.querySelectorAll("[data-action='reference']").forEach(button => {
        button.addEventListener("click", showReferenceUniverse);
    });

    document.querySelectorAll("[data-type]").forEach(button => {
        button.addEventListener("click", () => {
            navigateToType(button.dataset.type);
        });
    });

    document.addEventListener("keydown", event => {
        if (
            event.key === "/" &&
            document.activeElement !== $("#search-input")
        ) {
            event.preventDefault();
            openSearch();
        }

        if (event.key.toLowerCase() === "d") {
            if (document.activeElement !== $("#search-input")) {
                randomDiscovery();
            }
        }

        if (event.key === "Escape") {
            closeSearch();
            closeMobileMenu();
        }
    });
});
"""


# ============================================================
# HTML
# ============================================================

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <meta
        name="description"
        content="The Forbidden Lore Wiki — an archival interface for fictional civilizations, histories, characters, artifacts, documents and forgotten worlds."
    >

    <meta
        name="robots"
        content="index, follow"
    >

    <meta
        property="og:title"
        content="The Forbidden Lore Wiki"
    >

    <meta
        property="og:description"
        content="A fictional archival interface for forbidden histories, characters, worlds, artifacts and documents."
    >

    <meta
        property="og:type"
        content="website"
    >

    <title>The Forbidden Lore Wiki</title>

    <style>
        __CSS__
    </style>
</head>

<body class="__THEME__">

<div class="archive-shell">

    <header class="archive-topline">

        <div class="archive-brand">
            FORBIDDEN LORE WIKI
        </div>

        <div class="archive-edition">
            ARCHIVE 01 · EDITION 07
        </div>

        <div class="archive-status">
            STATUS: ACTIVE
        </div>

    </header>


    <div class="archive-body">

        <aside class="archive-sidebar">

            <div class="sidebar-inner">

                <div class="sidebar-section">

                    <div class="sidebar-label">
                        Index
                    </div>

                    <nav class="sidebar-nav">

                        <button
                            class="sidebar-link active"
                            data-action="discover"
                        >
                            DISCOVER
                        </button>

                        <button
                            class="sidebar-link"
                            data-action="discover"
                        >
                            ARCHIVE
                        </button>

                        <button
                            class="sidebar-link"
                            data-action="timeline"
                        >
                            TIMELINE
                        </button>

                        <button
                            class="sidebar-link"
                            data-type="World"
                        >
                            WORLDS
                        </button>

                        <button
                            class="sidebar-link"
                            data-type="Faction"
                        >
                            FACTIONS
                        </button>

                        <button
                            class="sidebar-link"
                            data-type="Character"
                        >
                            CHARACTERS
                        </button>

                        <button
                            class="sidebar-link"
                            data-type="Artifact"
                        >
                            ARTIFACTS
                        </button>

                        <button
                            class="sidebar-link"
                            data-type="Document"
                        >
                            DOCUMENTS
                        </button>

                    </nav>

                </div>


                <div class="sidebar-section">

                    <div class="sidebar-label">
                        Reference Universes
                    </div>

                    <nav class="sidebar-nav">

                        <button
                            class="sidebar-link"
                            data-action="reference"
                        >
                            ANIME
                        </button>

                        <button
                            class="sidebar-link"
                            data-action="reference"
                        >
                            MANHWA
                        </button>

                        <button
                            class="sidebar-link"
                            data-action="reference"
                        >
                            MANHUA
                        </button>

                        <button
                            class="sidebar-link"
                            data-action="reference"
                        >
                            DONGHUA
                        </button>

                        <button
                            class="sidebar-link"
                            data-action="reference"
                        >
                            LIGHT NOVELS
                        </button>

                        <button
                            class="sidebar-link"
                            data-action="reference"
                        >
                            COMICS
                        </button>

                        <button
                            class="sidebar-link"
                            data-action="reference"
                        >
                            DC
                        </button>

                        <button
                            class="sidebar-link"
                            data-action="reference"
                        >
                            MARVEL
                        </button>

                    </nav>

                </div>


                <div class="sidebar-section">

                    <div class="sidebar-label">
                        Archive Types
                    </div>

                    <div class="sidebar-ref">
                        CHARACTERS<br>
                        HISTORICAL EVENTS<br>
                        FACTIONS<br>
                        ARTIFACTS<br>
                        DOCUMENTS<br>
                        WORLDS<br>
                        QUESTIONS<br>
                        CONFLICTS<br>
                        POLITICAL SYSTEMS<br>
                        LOCATIONS<br>
                        CHRONOLOGIES<br>
                        UNRESOLVED RECORDS
                    </div>

                </div>


                <div class="sidebar-section">

                    <div class="sidebar-label">
                        Archive Notice
                    </div>

                    <div class="sidebar-ref">
                        Original fiction is identified as original material.
                        Referenced universes are navigation references.
                    </div>

                </div>

            </div>

        </aside>


        <main class="archive-content">

            <div class="content-toolbar">

                <div class="breadcrumb">
                    FORBIDDEN LORE WIKI
                    ·
                    RESTRICTED HISTORICAL COLLECTION
                    ·
                    <strong>ACTIVE RECORD</strong>
                </div>

                <div class="toolbar-actions">

                    <button
                        id="search-button"
                        class="toolbar-button"
                    >
                        Search /
                    </button>

                    <button
                        id="random-button"
                        class="toolbar-button"
                    >
                        Random Discovery
                    </button>

                    <button
                        id="mobile-menu-button"
                        class="mobile-menu-button"
                    >
                        INDEX
                    </button>

                </div>

            </div>


            <div
                id="mobile-drawer"
                class="mobile-drawer"
            >

                <div class="sidebar-section">

                    <div class="sidebar-label">
                        Index
                    </div>

                    <nav class="sidebar-nav">

                        <button
                            class="sidebar-link"
                            data-action="discover"
                        >
                            DISCOVER
                        </button>

                        <button
                            class="sidebar-link"
                            data-action="timeline"
                        >
                            TIMELINE
                        </button>

                        <button
                            class="sidebar-link"
                            data-type="World"
                        >
                            WORLDS
                        </button>

                        <button
                            class="sidebar-link"
                            data-type="Faction"
                        >
                            FACTIONS
                        </button>

                        <button
                            class="sidebar-link"
                            data-type="Character"
                        >
                            CHARACTERS
                        </button>

                        <button
                            class="sidebar-link"
                            data-type="Artifact"
                        >
                            ARTIFACTS
                        </button>

                        <button
                            class="sidebar-link"
                            data-type="Document"
                        >
                            DOCUMENTS
                        </button>

                    </nav>

                </div>


                <div class="sidebar-section">

                    <div class="sidebar-label">
                        Reference Universes
                    </div>

                    <nav class="sidebar-nav">

                        <button
                            class="sidebar-link"
                            data-action="reference"
                        >
                            ANIME
                        </button>

                        <button
                            class="sidebar-link"
                            data-action="reference"
                        >
                            MANHWA
                        </button>

                        <button
                            class="sidebar-link"
                            data-action="reference"
                        >
                            MANHUA
                        </button>

                        <button
                            class="sidebar-link"
                            data-action="reference"
                        >
                            DONGHUA
                        </button>

                        <button
                            class="sidebar-link"
                            data-action="reference"
                        >
                            LIGHT NOVELS
                        </button>

                        <button
                            class="sidebar-link"
                            data-action="reference"
                        >
                            COMICS
                        </button>

                        <button
                            class="sidebar-link"
                            data-action="reference"
                        >
                            DC
                        </button>

                        <button
                            class="sidebar-link"
                            data-action="reference"
                        >
                            MARVEL
                        </button>

                    </nav>

                </div>

            </div>


            <section
                id="record-stage"
                class="record-stage"
            >
                <div class="record-header">
                    <div class="record-kicker">
                        LOADING ARCHIVAL RECORD
                    </div>

                    <h1 class="record-title">
                        Initializing Archive
                    </h1>
                </div>
            </section>


            <footer class="archive-footer">

                <div>
                    FORBIDDEN LORE WIKI · FICTIONAL ARCHIVE
                    <br>
                    ORIGINAL FICTION IS IDENTIFIED AS ORIGINAL MATERIAL.
                    REFERENCED UNIVERSES ARE NAVIGATION REFERENCES.
                </div>

                <div class="archive-footer-right">
                    NO DATABASE · NO LOGIN · NO LOCAL STORAGE
                    <br>
                    BROWSER MEMORY ONLY
                </div>

            </footer>

        </main>

    </div>

</div>


<div
    id="search-overlay"
    class="search-overlay"
>

    <div class="search-panel">

        <div class="search-top">

            <input
                id="search-input"
                class="search-input"
                type="search"
                autocomplete="off"
                spellcheck="false"
                placeholder="SEARCH ARCHIVE RECORDS..."
            >

            <button
                id="search-close"
                class="search-close"
            >
                ESC
            </button>

        </div>

        <div
            id="search-results"
            class="search-results"
        ></div>

    </div>

</div>


<script>
__JS__
</script>

</body>
</html>
"""


# ============================================================
# BUILD HTML
# ============================================================

def build_html():
    theme = random.choice(THEMES)["class"]

    data_json = json.dumps(
        SEARCH_DATA,
        ensure_ascii=False,
        separators=(",", ":")
    )

    worlds_json = json.dumps(
        WORLDS,
        ensure_ascii=False,
        separators=(",", ":")
    )

    characters_json = json.dumps(
        CHARACTERS,
        ensure_ascii=False,
        separators=(",", ":")
    )

    events_json = json.dumps(
        EVENTS,
        ensure_ascii=False,
        separators=(",", ":")
    )

    factions_json = json.dumps(
        FACTIONS,
        ensure_ascii=False,
        separators=(",", ":")
    )

    artifacts_json = json.dumps(
        ARTIFACTS,
        ensure_ascii=False,
        separators=(",", ":")
    )

    documents_json = json.dumps(
        DOCUMENTS,
        ensure_ascii=False,
        separators=(",", ":")
    )

    questions_json = json.dumps(
        QUESTIONS,
        ensure_ascii=False,
        separators=(",", ":")
    )

    archive_types_json = json.dumps(
        ARCHIVE_TYPES,
        ensure_ascii=False,
        separators=(",", ":")
    )

    reference_json = json.dumps(
        REFERENCE_UNIVERSES,
        ensure_ascii=False,
        separators=(",", ":")
    )

    js = (
        JS_TEMPLATE
        .replace("__SEARCH_DATA__", data_json)
        .replace("__WORLDS__", worlds_json)
        .replace("__CHARACTERS__", characters_json)
        .replace("__EVENTS__", events_json)
        .replace("__FACTIONS__", factions_json)
        .replace("__ARTIFACTS__", artifacts_json)
        .replace("__DOCUMENTS__", documents_json)
        .replace("__QUESTIONS__", questions_json)
        .replace("__ARCHIVE_TYPES__", archive_types_json)
        .replace("__REFERENCE_UNIVERSES__", reference_json)
    )

    html_output = (
        HTML_TEMPLATE
        .replace("__CSS__", CSS)
        .replace("__JS__", js)
        .replace("__THEME__", theme)
    )

    return html_output


# ============================================================
# MAIN
# ============================================================

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    output = build_html()

    OUTPUT_FILE.write_text(
        output,
        encoding="utf-8"
    )

    print("=" * 62)
    print("FORBIDDEN LORE WIKI GENERATED")
    print("=" * 62)
    print(f"Output: {OUTPUT_FILE}")
    print(f"Records: {len(SEARCH_DATA)}")
    print("Static HTML: YES")
    print("Database: NO")
    print("localStorage: NO")
    print("sessionStorage: NO")
    print("IndexedDB: NO")
    print("Login/Signup: NO")
    print("Backend: NO")
    print("Browser memory: YES")
    print("=" * 62)


if __name__ == "__main__":
    main()
