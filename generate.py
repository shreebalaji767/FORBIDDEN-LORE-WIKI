from pathlib import Path
import html
import json
import random


# ============================================================
# FORBIDDEN LORE WIKI
# COMPLETE STATIC SITE GENERATOR
# ============================================================

OUTPUT_DIR = Path("site")
OUTPUT_FILE = OUTPUT_DIR / "index.html"

random.seed()


# ============================================================
# ORIGINAL WORLDS
# ============================================================

WORLDS = [
    {
        "name": "Elaria",
        "era": "Late Imperial Cycle",
        "status": "Fragmentary",
        "origin": "Original World",
        "description": (
            "A continent of imperial ruins, contradictory dynasties and "
            "temples whose records disagree about the same centuries."
        ),
        "keywords": [
            "empire",
            "temples",
            "chronology",
            "dynasty",
        ],
    },
    {
        "name": "Vael Taryn",
        "era": "River Kingdom Period",
        "status": "Documented",
        "origin": "Original World",
        "description": (
            "A river civilization dominated by merchant leagues, fortified "
            "crossings and trade routes that changed the political map."
        ),
        "keywords": [
            "river",
            "merchant",
            "kingdom",
            "trade",
        ],
    },
    {
        "name": "Ashen Realms",
        "era": "Post-Cataclysmic Age",
        "status": "Restricted",
        "origin": "Original World",
        "description": (
            "A broken collection of kingdoms surviving after a catastrophe "
            "whose actual cause was removed from most surviving histories."
        ),
        "keywords": [
            "cataclysm",
            "ruins",
            "survivors",
            "forbidden history",
        ],
    },
    {
        "name": "Kharad Vey",
        "era": "Third Crown Dynasty",
        "status": "Disputed",
        "origin": "Original World",
        "description": (
            "A mountain empire whose royal genealogies contain a deliberate "
            "absence that has never been satisfactorily explained."
        ),
        "keywords": [
            "mountains",
            "royalty",
            "dynasty",
            "succession",
        ],
    },
    {
        "name": "Namaris",
        "era": "Age of Glass",
        "status": "Unverified",
        "origin": "Original World",
        "description": (
            "A coastal civilization surrounding enormous translucent mineral "
            "formations whose origin remains unknown."
        ),
        "keywords": [
            "glass",
            "coast",
            "mineral",
            "architecture",
        ],
    },
    {
        "name": "Orthell",
        "era": "Broken Calendar",
        "status": "Fragmentary",
        "origin": "Original World",
        "description": (
            "An astronomical civilization that abandoned numbered years "
            "after recording an event that should not have been possible."
        ),
        "keywords": [
            "astronomy",
            "calendar",
            "stars",
            "history",
        ],
    },
    {
        "name": "Serevan",
        "era": "Northern Campaigns",
        "status": "Restricted",
        "origin": "Original World",
        "description": (
            "A militarized federation whose battlefield records repeatedly "
            "omit the identity of one particular army."
        ),
        "keywords": [
            "war",
            "military",
            "federation",
            "campaign",
        ],
    },
    {
        "name": "Ilyr",
        "era": "First Maritime Age",
        "status": "Unresolved",
        "origin": "Original World",
        "description": (
            "An island civilization known primarily through navigation logs "
            "written by people who claimed never to have reached it."
        ),
        "keywords": [
            "islands",
            "navigation",
            "sea",
            "meridian",
        ],
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
        "era": "Post-Cataclysmic Age",
        "status": "Missing",
        "description": (
            "A mapmaker whose surviving charts contain coastlines absent "
            "from every later geographical survey."
        ),
    },
    {
        "name": "Ilyan Voss",
        "world": "Elaria",
        "role": "Imperial Archivist",
        "era": "Late Imperial Cycle",
        "status": "Recorded",
        "description": (
            "An archivist credited with preserving three mutually "
            "contradictory versions of an imperial succession."
        ),
    },
    {
        "name": "Seren Vale",
        "world": "Vael Taryn",
        "role": "Merchant-Prince",
        "era": "River Kingdom Period",
        "status": "Recorded",
        "description": (
            "A merchant ruler whose private ledgers mention a city that "
            "does not appear on any surviving map."
        ),
    },
    {
        "name": "Maer Oth",
        "world": "Kharad Vey",
        "role": "Royal Genealogist",
        "era": "Third Crown Dynasty",
        "status": "Disputed",
        "description": (
            "The genealogist responsible for a royal lineage containing "
            "a forty-two-year absence."
        ),
    },
    {
        "name": "Tessa Arin",
        "world": "Namaris",
        "role": "Glasswright",
        "era": "Age of Glass",
        "status": "Unverified",
        "description": (
            "An artisan whose notes describe structures seemingly impossible "
            "for the known technology of her civilization."
        ),
    },
    {
        "name": "Corven Dhal",
        "world": "Serevan",
        "role": "Field Commander",
        "era": "Northern Campaigns",
        "status": "Restricted",
        "description": (
            "A commander whose reports repeatedly mention an unnamed unit "
            "identified only by a black geometric symbol."
        ),
    },
    {
        "name": "Oren Pell",
        "world": "Orthell",
        "role": "Astronomer",
        "era": "Broken Calendar",
        "status": "Missing",
        "description": (
            "An astronomer whose final observation predicts an astronomical "
            "event that appears to have occurred centuries earlier."
        ),
    },
    {
        "name": "Lysa Mer",
        "world": "Ilyr",
        "role": "Navigator",
        "era": "First Maritime Age",
        "status": "Unknown",
        "description": (
            "A navigator whose log contains coordinates for an island "
            "that disappears from every later chart."
        ),
    },
]


# ============================================================
# EVENTS
# ============================================================

EVENTS = [
    {
        "name": "The Seven-Day Silence",
        "year": "Unknown",
        "world": "Elaria",
        "type": "Historical Anomaly",
        "status": "Unresolved",
        "description": (
            "Six independent archives contain the same unexplained absence "
            "of dated records."
        ),
    },
    {
        "name": "The Burning of the Northern Ledger",
        "year": "312 A.C.",
        "world": "Vael Taryn",
        "type": "Destruction",
        "status": "Documented",
        "description": (
            "A merchant archive vanished during a fire that destroyed "
            "only one building in an otherwise untouched district."
        ),
    },
    {
        "name": "The Ashfall Crossing",
        "year": "Unknown",
        "world": "Ashen Realms",
        "type": "Migration",
        "status": "Fragmentary",
        "description": (
            "A population movement referenced by several settlements "
            "without a surviving government claiming responsibility."
        ),
    },
    {
        "name": "The Empty Coronation",
        "year": "Year 0",
        "world": "Kharad Vey",
        "type": "Succession Crisis",
        "status": "Disputed",
        "description": (
            "A coronation recorded by ceremonial documents but absent "
            "from every surviving royal genealogy."
        ),
    },
    {
        "name": "The Glass Tide",
        "year": "Approx. 88 AG",
        "world": "Namaris",
        "type": "Natural Anomaly",
        "status": "Unverified",
        "description": (
            "A coastal event during which enormous mineral formations "
            "reportedly appeared along several miles of shoreline."
        ),
    },
    {
        "name": "The Last Calendar Night",
        "year": "Unknown",
        "world": "Orthell",
        "type": "Astronomical Event",
        "status": "Restricted",
        "description": (
            "The final dated astronomical observation before Orthell "
            "abandoned conventional numbered years."
        ),
    },
    {
        "name": "The Black Standard Campaign",
        "year": "641 N.C.",
        "world": "Serevan",
        "type": "Military Campaign",
        "status": "Restricted",
        "description": (
            "A campaign described in official reports without identifying "
            "the force that supposedly commanded it."
        ),
    },
    {
        "name": "The Vanishing Meridian",
        "year": "Unknown",
        "world": "Ilyr",
        "type": "Navigational Anomaly",
        "status": "Unresolved",
        "description": (
            "A sequence of navigation records that terminate at nearly "
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
        "type": "Merchant Alliance",
        "status": "Documented",
        "description": (
            "A commercial coalition controlling several northern "
            "river crossings."
        ),
    },
    {
        "name": "Order of the Hollow Crown",
        "world": "Kharad Vey",
        "type": "Royal Institution",
        "status": "Restricted",
        "description": (
            "A ceremonial order responsible for preserving disputed "
            "succession records."
        ),
    },
    {
        "name": "Ash Registry",
        "world": "Ashen Realms",
        "type": "Archive Network",
        "status": "Fragmentary",
        "description": (
            "A loose network of record keepers who catalogued settlements "
            "after the cataclysm."
        ),
    },
    {
        "name": "The Meridian Court",
        "world": "Ilyr",
        "type": "Maritime Authority",
        "status": "Unknown",
        "description": (
            "A maritime authority mentioned only in navigation documents."
        ),
    },
    {
        "name": "Glasswright Compact",
        "world": "Namaris",
        "type": "Guild",
        "status": "Documented",
        "description": (
            "An artisan organization associated with the construction "
            "of enormous translucent structures."
        ),
    },
    {
        "name": "The Calendar Keepers",
        "world": "Orthell",
        "type": "Scholarly Order",
        "status": "Fragmentary",
        "description": (
            "Astronomers and historians who preserved pre-Broken "
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
        "status": "Partially Recovered",
        "description": (
            "A map showing a coastline that appears nowhere in surviving "
            "geographical surveys."
        ),
    },
    {
        "name": "The Kareth Ledger",
        "world": "Vael Taryn",
        "type": "Financial Record",
        "status": "Referenced",
        "description": (
            "A merchant ledger believed to contain evidence of a "
            "missing trade route."
        ),
    },
    {
        "name": "Crownless Seal",
        "world": "Kharad Vey",
        "type": "Royal Insignia",
        "status": "Disputed",
        "description": (
            "A seal bearing the symbols of a monarch absent from "
            "official succession lists."
        ),
    },
    {
        "name": "The Ninth Star Lens",
        "world": "Orthell",
        "type": "Astronomical Instrument",
        "status": "Unverified",
        "description": (
            "An instrument said to reveal an additional reference "
            "point in the night sky."
        ),
    },
    {
        "name": "Glass Memory Tablet",
        "world": "Namaris",
        "type": "Inscribed Mineral",
        "status": "Fragmentary",
        "description": (
            "A translucent tablet containing writing visible only "
            "from certain angles."
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
        "type": "Administrative Archive",
        "status": "Fragmentary",
        "description": (
            "A registry containing population records from settlements "
            "believed to have disappeared."
        ),
    },
    {
        "name": "Ledger of the Northern Crossing",
        "world": "Vael Taryn",
        "type": "Commercial Document",
        "status": "Referenced Only",
        "description": (
            "A missing merchant ledger known through quotations "
            "in later financial disputes."
        ),
    },
    {
        "name": "Chronicle of the Empty Crown",
        "world": "Kharad Vey",
        "type": "Royal Chronicle",
        "status": "Disputed",
        "description": (
            "A chronicle describing a succession event absent "
            "from official genealogical records."
        ),
    },
    {
        "name": "The Last Meridian Log",
        "world": "Ilyr",
        "type": "Navigation Log",
        "status": "Partial",
        "description": (
            "A navigation document terminating at coordinates shared "
            "by several unrelated voyages."
        ),
    },
]


# ============================================================
# QUESTIONS
# ============================================================

QUESTIONS = [
    {
        "question": (
            "Why do six Elarian archives contain the same seven-day gap?"
        ),
        "status": "Unresolved",
        "related": "The Seven-Day Silence",
    },
    {
        "question": (
            "Who constructed the coastline shown on Nera Kesh's map?"
        ),
        "status": "No Accepted Answer",
        "related": "The Black Meridian Map",
    },
    {
        "question": (
            "Why was one royal generation removed from Kharad Vey records?"
        ),
        "status": "Disputed",
        "related": "Order of the Hollow Crown",
    },
    {
        "question": (
            "Did the Vanishing Meridian represent a real location?"
        ),
        "status": "Unverified",
        "related": "The Last Meridian Log",
    },
    {
        "question": (
            "Why did Orthell abandon numbered years?"
        ),
        "status": "Multiple Theories",
        "related": "The Last Calendar Night",
    },
]


# ============================================================
# REFERENCE UNIVERSES
# ============================================================

REFERENCE_UNIVERSES = [
    {
        "name": "Anime",
        "symbol": "ア",
        "description": (
            "Animated fictional worlds, characters, histories, powers, "
            "organizations and mythologies originating from anime."
        ),
    },
    {
        "name": "Manhwa",
        "symbol": "한",
        "description": (
            "Korean comic worlds including fantasy kingdoms, modern "
            "supernatural settings, martial worlds and serialized lore."
        ),
    },
    {
        "name": "Manhua",
        "symbol": "漫",
        "description": (
            "Chinese comic universes spanning cultivation, mythology, "
            "historical fantasy and supernatural fiction."
        ),
    },
    {
        "name": "Donghua",
        "symbol": "动",
        "description": (
            "Chinese animated fictional worlds and their characters, "
            "mythologies, factions and historical settings."
        ),
    },
    {
        "name": "Light Novels",
        "symbol": "LN",
        "description": (
            "Serialized literary worlds containing extensive character, "
            "political, magical and chronological lore."
        ),
    },
    {
        "name": "Comics",
        "symbol": "CM",
        "description": (
            "Comic-book universes containing fictional histories, "
            "characters, organizations and alternate continuities."
        ),
    },
    {
        "name": "DC",
        "symbol": "DC",
        "description": (
            "Reference gateway for DC fictional universes and their "
            "characters, events, worlds and mythologies."
        ),
    },
    {
        "name": "Marvel",
        "symbol": "MV",
        "description": (
            "Reference gateway for Marvel fictional universes and their "
            "characters, events, worlds and mythologies."
        ),
    },
]


# ============================================================
# ARCHIVE TYPES
# ============================================================

ARCHIVE_TYPES = [
    "Characters",
    "Worlds",
    "Historical Events",
    "Factions",
    "Artifacts",
    "Documents",
    "Locations",
    "Chronologies",
    "Political Systems",
    "Wars",
    "Mythologies",
    "Unresolved Mysteries",
]


# ============================================================
# UTILITIES
# ============================================================

def esc(value):
    return html.escape(str(value), quote=True)


def make_id(prefix, number):
    return f"{prefix.upper()}-{number + 1:03d}"


# ============================================================
# SEARCH INDEX
# ============================================================

def build_search_data():

    records = []

    for i, item in enumerate(WORLDS):

        records.append(
            {
                "id": make_id("WORLD", i),
                "type": "World",
                "name": item["name"],
                "world": item["name"],
                "status": item["status"],
                "era": item["era"],
                "description": item["description"],
            }
        )

    for i, item in enumerate(CHARACTERS):

        records.append(
            {
                "id": make_id("CHAR", i),
                "type": "Character",
                "name": item["name"],
                "world": item["world"],
                "status": item["status"],
                "era": item["era"],
                "description": item["description"],
            }
        )

    for i, item in enumerate(EVENTS):

        records.append(
            {
                "id": make_id("EVENT", i),
                "type": "Historical Event",
                "name": item["name"],
                "world": item["world"],
                "status": item["status"],
                "era": item["year"],
                "description": item["description"],
            }
        )

    for i, item in enumerate(FACTIONS):

        records.append(
            {
                "id": make_id("FACTION", i),
                "type": "Faction",
                "name": item["name"],
                "world": item["world"],
                "status": item["status"],
                "era": "Unknown",
                "description": item["description"],
            }
        )

    for i, item in enumerate(ARTIFACTS):

        records.append(
            {
                "id": make_id("ARTIFACT", i),
                "type": "Artifact",
                "name": item["name"],
                "world": item["world"],
                "status": item["status"],
                "era": "Unknown",
                "description": item["description"],
            }
        )

    for i, item in enumerate(DOCUMENTS):

        records.append(
            {
                "id": make_id("DOCUMENT", i),
                "type": "Document",
                "name": item["name"],
                "world": item["world"],
                "status": item["status"],
                "era": "Unknown",
                "description": item["description"],
            }
        )

    for i, item in enumerate(QUESTIONS):

        records.append(
            {
                "id": make_id("QUESTION", i),
                "type": "Unresolved Mystery",
                "name": item["question"],
                "world": item["related"],
                "status": item["status"],
                "era": "Unknown",
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
   OCCULT ENCYCLOPEDIA / CLASSIFIED CODEX UI
   ============================================================ */

:root {
    --void: #080807;
    --black: #0d0c0a;
    --ink: #15130f;
    --ink-2: #1b1813;

    --bone: #e4dcc7;
    --bone-soft: #b9b09a;
    --bone-dim: #776f60;

    --blood: #8d2828;
    --blood-light: #bd4843;

    --gold: #ad8c48;
    --gold-light: #d1b66b;

    --ash: #46423a;

    --green: #667c5d;

    --line: rgba(228,220,199,0.17);
    --line-strong: rgba(228,220,199,0.34);

    --serif: Georgia, "Times New Roman", serif;
    --sans: Arial, Helvetica, sans-serif;
    --mono: "Courier New", monospace;
}


* {
    box-sizing: border-box;
}


html {
    min-width: 320px;
    background: var(--void);
    color: var(--bone);
    scroll-behavior: smooth;
}


body {
    margin: 0;
    min-height: 100vh;
    overflow-x: hidden;

    background:
        radial-gradient(
            ellipse at 50% -20%,
            rgba(141,40,40,0.10),
            transparent 45%
        ),
        radial-gradient(
            ellipse at 10% 80%,
            rgba(173,140,72,0.045),
            transparent 35%
        ),
        #080807;

    font-family: var(--sans);
}


body::before {
    content: "";

    position: fixed;
    inset: 0;

    pointer-events: none;
    z-index: 9999;

    opacity: .08;

    background:
        repeating-linear-gradient(
            0deg,
            transparent 0,
            transparent 3px,
            rgba(255,255,255,.05) 4px
        );

    mix-blend-mode: overlay;
}


body::after {
    content: "";

    position: fixed;
    inset: 0;

    pointer-events: none;

    opacity: .035;

    background-image:
        radial-gradient(
            circle at 20% 30%,
            #fff 0 1px,
            transparent 1px
        );

    background-size: 13px 13px;
}


button,
input {
    font: inherit;
}


button {
    color: inherit;
}


::selection {
    color: #fff;
    background: var(--blood);
}


/* ============================================================
   MASTER FRAME
   ============================================================ */

.lore-frame {
    width: min(1720px, 100%);
    min-height: 100vh;

    margin: 0 auto;

    border-left: 1px solid var(--line);
    border-right: 1px solid var(--line);
}


/* ============================================================
   HEADER
   ============================================================ */

.lore-header {
    min-height: 76px;

    display: grid;
    grid-template-columns: 1fr auto;

    border-bottom: 1px solid var(--line-strong);

    background:
        linear-gradient(
            90deg,
            rgba(255,255,255,.018),
            transparent 55%
        ),
        #0c0b09;
}


.brand-area {
    display: flex;
    align-items: center;

    padding: 14px 24px;
}


.brand-mark {
    position: relative;

    width: 39px;
    height: 39px;

    margin-right: 13px;

    display: grid;
    place-items: center;

    border: 1px solid var(--gold);

    color: var(--gold-light);

    font-family: var(--serif);
    font-size: 18px;

    transform: rotate(45deg);
}


.brand-mark span {
    transform: rotate(-45deg);
}


.brand-copy {
    min-width: 0;
}


.brand-title {
    margin: 0;

    color: var(--bone);

    font-family: var(--serif);
    font-size: 19px;
    font-weight: normal;

    letter-spacing: .16em;
    text-transform: uppercase;
}


.brand-subtitle {
    margin-top: 4px;

    color: var(--bone-dim);

    font-family: var(--mono);
    font-size: 8px;

    letter-spacing: .17em;
    text-transform: uppercase;
}


.header-right {
    display: flex;
    align-items: stretch;
}


.header-cell {
    min-width: 125px;

    display: flex;
    flex-direction: column;
    justify-content: center;

    padding: 10px 16px;

    border-left: 1px solid var(--line);
}


.header-label {
    margin-bottom: 4px;

    color: var(--bone-dim);

    font-family: var(--mono);
    font-size: 7px;

    letter-spacing: .17em;
    text-transform: uppercase;
}


.header-value {
    color: var(--bone-soft);

    font-family: var(--mono);
    font-size: 9px;

    letter-spacing: .08em;
    text-transform: uppercase;
}


.header-status {
    color: var(--green);
}


/* ============================================================
   MAIN NAV
   ============================================================ */

.lore-nav {
    min-height: 40px;

    display: flex;
    align-items: center;

    border-bottom: 1px solid var(--line);

    background: #0b0a08;

    overflow-x: auto;
}


.nav-item {
    flex: 0 0 auto;

    padding: 12px 17px;

    border: 0;
    border-right: 1px solid var(--line);

    background: transparent;

    color: var(--bone-dim);

    font-family: var(--mono);
    font-size: 8px;

    letter-spacing: .13em;
    text-transform: uppercase;

    cursor: pointer;
}


.nav-item:first-child {
    border-left: 1px solid var(--line);
}


.nav-item:hover,
.nav-item.active {
    color: var(--bone);

    background:
        linear-gradient(
            180deg,
            rgba(141,40,40,.14),
            transparent
        );
}


.nav-item.active {
    box-shadow: inset 0 -2px var(--blood);
}


/* ============================================================
   BODY
   ============================================================ */

.lore-body {
    display: grid;
    grid-template-columns: 250px minmax(0,1fr);

    min-height: calc(100vh - 116px);
}


/* ============================================================
   LEFT CODEX INDEX
   ============================================================ */

.codex-sidebar {
    border-right: 1px solid var(--line-strong);

    background:
        linear-gradient(
            180deg,
            rgba(255,255,255,.018),
            transparent 30%
        ),
        #0d0c0a;
}


.codex-sidebar-inner {
    position: sticky;
    top: 0;

    max-height: 100vh;

    overflow-y: auto;
}


.sidebar-heading {
    padding: 17px 17px 10px;

    color: var(--gold-light);

    font-family: var(--mono);
    font-size: 8px;

    letter-spacing: .2em;
    text-transform: uppercase;
}


.sidebar-rule {
    height: 1px;

    margin: 0 17px 10px;

    background: var(--line);
}


.codex-list {
    display: flex;
    flex-direction: column;
}


.codex-button {
    position: relative;

    width: 100%;

    padding: 8px 17px;

    border: 0;

    background: transparent;

    color: var(--bone-dim);

    text-align: left;

    font-family: var(--mono);
    font-size: 9px;

    letter-spacing: .04em;

    cursor: pointer;
}


.codex-button::before {
    content: "◇";

    margin-right: 8px;

    color: var(--ash);
}


.codex-button:hover,
.codex-button.active {
    color: var(--bone);

    background: rgba(228,220,199,.035);
}


.codex-button:hover::before,
.codex-button.active::before {
    color: var(--blood-light);
}


.sidebar-note {
    margin: 17px;

    padding: 13px;

    border: 1px solid var(--line);

    background:
        linear-gradient(
            135deg,
            rgba(173,140,72,.04),
            transparent
        );
}


.sidebar-note-title {
    margin-bottom: 8px;

    color: var(--bone-soft);

    font-family: var(--mono);
    font-size: 8px;

    letter-spacing: .13em;
    text-transform: uppercase;
}


.sidebar-note-text {
    color: var(--bone-dim);

    font-family: var(--serif);
    font-size: 12px;

    line-height: 1.55;
}


/* ============================================================
   CONTENT
   ============================================================ */

.lore-content {
    min-width: 0;

    background:
        radial-gradient(
            ellipse at 50% 0,
            rgba(228,220,199,.025),
            transparent 35%
        );
}


/* ============================================================
   CONTENT COMMAND BAR
   ============================================================ */

.command-bar {
    min-height: 46px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    gap: 12px;

    padding: 8px 18px;

    border-bottom: 1px solid var(--line);

    background: rgba(7,7,6,.70);
}


.command-path {
    min-width: 0;

    overflow: hidden;

    color: var(--bone-dim);

    font-family: var(--mono);
    font-size: 8px;

    letter-spacing: .08em;
    text-transform: uppercase;

    white-space: nowrap;
    text-overflow: ellipsis;
}


.command-path strong {
    color: var(--bone-soft);
}


.command-actions {
    display: flex;

    flex: 0 0 auto;

    gap: 5px;
}


.command-button {
    padding: 7px 10px;

    border: 1px solid var(--line);

    background: transparent;

    color: var(--bone-dim);

    font-family: var(--mono);
    font-size: 8px;

    letter-spacing: .08em;
    text-transform: uppercase;

    cursor: pointer;
}


.command-button:hover {
    border-color: var(--line-strong);

    color: var(--bone);

    background: rgba(228,220,199,.035);
}


.mobile-index {
    display: none;
}


/* ============================================================
   HERO / DISCOVERY
   ============================================================ */

.lore-stage {
    padding: 24px;
}


.codex-page {
    position: relative;

    border: 1px solid var(--line-strong);

    background:
        linear-gradient(
            90deg,
            rgba(228,220,199,.018),
            transparent 30%
        ),
        linear-gradient(
            180deg,
            rgba(173,140,72,.025),
            transparent 20%
        ),
        #11100d;

    box-shadow:
        0 25px 70px rgba(0,0,0,.28);
}


.codex-page::before {
    content: "";

    position: absolute;

    top: 0;
    bottom: 0;
    left: 52px;

    width: 1px;

    background: rgba(141,40,40,.16);

    pointer-events: none;
}


.codex-page::after {
    content: "";

    position: absolute;

    inset: 9px;

    border: 1px solid rgba(228,220,199,.035);

    pointer-events: none;
}


/* ============================================================
   RECORD HEADER
   ============================================================ */

.record-hero {
    position: relative;

    padding: 38px 48px 30px 72px;

    border-bottom: 1px solid var(--line-strong);
}


.record-seal {
    position: absolute;

    top: 27px;
    right: 31px;

    width: 74px;
    height: 74px;

    display: grid;
    place-items: center;

    border: 1px solid rgba(141,40,40,.7);

    color: var(--blood-light);

    font-family: var(--mono);
    font-size: 8px;

    letter-spacing: .12em;
    text-align: center;

    border-radius: 50%;

    transform: rotate(-8deg);
}


.record-seal::before {
    content: "";

    position: absolute;

    inset: 6px;

    border: 1px solid rgba(141,40,40,.35);

    border-radius: 50%;
}


.record-kicker {
    margin-bottom: 13px;

    color: var(--gold);

    font-family: var(--mono);
    font-size: 8px;

    letter-spacing: .23em;
    text-transform: uppercase;
}


.record-title {
    max-width: 850px;

    margin: 0;

    color: var(--bone);

    font-family: var(--serif);
    font-size: clamp(38px,6vw,82px);

    font-weight: normal;

    line-height: .92;

    letter-spacing: -.045em;
}


.record-subtitle {
    max-width: 800px;

    margin: 17px 0 0;

    color: var(--bone-soft);

    font-family: var(--serif);
    font-size: 17px;

    line-height: 1.5;
}


.record-origin {
    display: flex;
    flex-wrap: wrap;

    gap: 7px;

    margin-top: 22px;
}


.origin-tag {
    padding: 5px 8px;

    border: 1px solid var(--line);

    color: var(--bone-dim);

    font-family: var(--mono);
    font-size: 7px;

    letter-spacing: .12em;
    text-transform: uppercase;
}


/* ============================================================
   META STRIP
   ============================================================ */

.record-metadata {
    display: grid;
    grid-template-columns:
        minmax(100px,1fr)
        minmax(100px,1fr)
        minmax(100px,1fr)
        minmax(100px,1fr)
        minmax(100px,1fr);

    border-bottom: 1px solid var(--line-strong);

    background: rgba(0,0,0,.16);
}


.meta-item {
    min-width: 0;

    padding: 12px 14px;

    border-right: 1px solid var(--line);
}


.meta-item:last-child {
    border-right: 0;
}


.meta-label {
    display: block;

    margin-bottom: 5px;

    color: var(--bone-dim);

    font-family: var(--mono);
    font-size: 7px;

    letter-spacing: .15em;
    text-transform: uppercase;
}


.meta-value {
    display: block;

    color: var(--bone-soft);

    font-family: var(--mono);
    font-size: 9px;

    line-height: 1.35;

    word-break: break-word;
}


/* ============================================================
   RECORD BODY
   ============================================================ */

.record-layout {
    display: grid;
    grid-template-columns: minmax(0,1fr) 285px;
}


.record-main {
    min-width: 0;

    border-right: 1px solid var(--line-strong);
}


.lore-section {
    position: relative;

    padding: 25px 34px 25px 72px;

    border-bottom: 1px solid var(--line);
}


.lore-section:last-child {
    border-bottom: 0;
}


.section-number {
    position: absolute;

    top: 27px;
    left: 17px;

    color: var(--ash);

    font-family: var(--mono);
    font-size: 9px;
}


.section-heading {
    display: flex;
    align-items: baseline;
    justify-content: space-between;

    gap: 15px;

    margin-bottom: 14px;
}


.section-title {
    margin: 0;

    color: var(--bone);

    font-family: var(--mono);
    font-size: 9px;

    font-weight: normal;

    letter-spacing: .17em;
    text-transform: uppercase;
}


.section-code {
    color: var(--bone-dim);

    font-family: var(--mono);
    font-size: 7px;

    white-space: nowrap;
}


.lore-paragraph {
    max-width: 880px;

    margin: 0;

    color: var(--bone-soft);

    font-family: var(--serif);
    font-size: 16px;

    line-height: 1.75;
}


.lore-paragraph + .lore-paragraph {
    margin-top: 13px;
}


/* ============================================================
   CLASSIFICATION
   ============================================================ */

.classification {
    display: grid;
    grid-template-columns: 170px minmax(0,1fr);

    border: 1px solid var(--line);
}


.classification-label {
    padding: 12px;

    border-right: 1px solid var(--line);

    color: var(--bone-dim);

    font-family: var(--mono);
    font-size: 8px;

    letter-spacing: .1em;
    text-transform: uppercase;
}


.classification-value {
    padding: 12px;

    color: var(--blood-light);

    font-family: var(--mono);
    font-size: 11px;

    font-weight: bold;

    letter-spacing: .13em;
    text-transform: uppercase;
}


/* ============================================================
   LORE QUOTE
   ============================================================ */

.lore-quote {
    position: relative;

    margin: 0;

    padding: 19px 22px;

    border-left: 3px solid var(--gold);

    background:
        linear-gradient(
            90deg,
            rgba(173,140,72,.055),
            transparent
        );

    color: var(--bone-soft);

    font-family: var(--serif);
    font-size: 17px;

    font-style: italic;

    line-height: 1.65;
}


.lore-quote::before {
    content: "ARCHIVIST MARGIN";

    display: block;

    margin-bottom: 8px;

    color: var(--gold);

    font-family: var(--mono);
    font-size: 7px;

    font-style: normal;

    letter-spacing: .18em;
}


/* ============================================================
   REFERENCES
   ============================================================ */

.reference-grid {
    display: grid;
    grid-template-columns: repeat(2,minmax(0,1fr));

    border-top: 1px solid var(--line);
    border-left: 1px solid var(--line);
}


.reference {
    min-width: 0;

    padding: 12px;

    border-right: 1px solid var(--line);
    border-bottom: 1px solid var(--line);

    cursor: pointer;
}


.reference:hover {
    background: rgba(228,220,199,.035);
}


.reference-id {
    display: block;

    color: var(--gold);

    font-family: var(--mono);
    font-size: 7px;

    letter-spacing: .09em;
}


.reference-title {
    display: block;

    margin-top: 5px;

    color: var(--bone-soft);

    font-family: var(--serif);
    font-size: 14px;

    line-height: 1.3;
}


/* ============================================================
   SIDE LORE PANEL
   ============================================================ */

.record-aside {
    min-width: 0;

    background:
        linear-gradient(
            180deg,
            rgba(0,0,0,.16),
            rgba(173,140,72,.018)
        );
}


.aside-section {
    padding: 18px;

    border-bottom: 1px solid var(--line);
}


.aside-heading {
    margin-bottom: 10px;

    color: var(--gold);

    font-family: var(--mono);
    font-size: 7px;

    letter-spacing: .18em;
    text-transform: uppercase;
}


.aside-value {
    color: var(--bone-soft);

    font-family: var(--serif);
    font-size: 14px;

    line-height: 1.5;
}


.aside-mono {
    color: var(--bone-dim);

    font-family: var(--mono);
    font-size: 8px;

    line-height: 1.7;
}


.status-seal {
    display: inline-flex;
    align-items: center;

    padding: 7px 9px;

    border: 1px solid var(--blood);

    color: var(--blood-light);

    font-family: var(--mono);
    font-size: 8px;

    letter-spacing: .14em;
    text-transform: uppercase;
}


.world-symbol {
    width: 58px;
    height: 58px;

    display: grid;
    place-items: center;

    margin-bottom: 11px;

    border: 1px solid var(--gold);

    color: var(--gold-light);

    font-family: var(--serif);
    font-size: 21px;

    transform: rotate(45deg);
}


.world-symbol span {
    transform: rotate(-45deg);
}


.aside-list {
    margin: 0;
    padding: 0;

    list-style: none;
}


.aside-list li {
    padding: 7px 0;

    border-bottom: 1px dotted var(--line);

    color: var(--bone-dim);

    font-family: var(--mono);
    font-size: 8px;

    line-height: 1.45;
}


.aside-list li:last-child {
    border-bottom: 0;
}


/* ============================================================
   DISCOVERY FOOTER
   ============================================================ */

.discovery-bar {
    display: grid;
    grid-template-columns: repeat(3,minmax(0,1fr));

    border-top: 1px solid var(--line-strong);
}


.discovery-item {
    min-width: 0;

    padding: 16px 18px;

    border-right: 1px solid var(--line);
}


.discovery-item:last-child {
    border-right: 0;
}


.discovery-label {
    margin-bottom: 6px;

    color: var(--bone-dim);

    font-family: var(--mono);
    font-size: 7px;

    letter-spacing: .16em;
    text-transform: uppercase;
}


.discovery-value {
    color: var(--bone-soft);

    font-family: var(--serif);
    font-size: 15px;

    line-height: 1.35;
}


.discovery-small {
    margin-top: 4px;

    color: var(--bone-dim);

    font-family: var(--mono);
    font-size: 7px;
}


/* ============================================================
   SEARCH
   ============================================================ */

.search-overlay {
    position: fixed;
    inset: 0;

    z-index: 800;

    display: none;
    align-items: flex-start;
    justify-content: center;

    padding: 9vh 18px 30px;

    background: rgba(3,3,2,.94);

    backdrop-filter: blur(8px);
}


.search-overlay.open {
    display: flex;
}


.search-window {
    width: min(920px,100%);

    border: 1px solid var(--line-strong);

    background: #0d0c0a;

    box-shadow:
        0 35px 100px rgba(0,0,0,.65);
}


.search-titlebar {
    display: flex;
    align-items: center;

    border-bottom: 1px solid var(--line);
}


.search-icon {
    padding: 15px;

    color: var(--blood-light);

    font-family: var(--mono);
    font-size: 10px;
}


.search-input {
    flex: 1;

    min-width: 0;

    padding: 15px 5px;

    border: 0;
    outline: 0;

    background: transparent;

    color: var(--bone);

    font-family: var(--mono);
    font-size: 11px;
}


.search-input::placeholder {
    color: var(--bone-dim);
}


.search-close {
    padding: 15px;

    border: 0;
    border-left: 1px solid var(--line);

    background: transparent;

    color: var(--bone-dim);

    font-family: var(--mono);
    font-size: 8px;

    cursor: pointer;
}


.search-close:hover {
    color: var(--bone);
}


.search-results {
    max-height: 66vh;

    overflow-y: auto;
}


.search-result {
    display: grid;
    grid-template-columns: 100px minmax(0,1fr);

    gap: 15px;

    padding: 14px 16px;

    border-bottom: 1px solid var(--line);

    cursor: pointer;
}


.search-result:hover {
    background: rgba(228,220,199,.035);
}


.search-result-id {
    color: var(--gold);

    font-family: var(--mono);
    font-size: 8px;
}


.search-result-name {
    color: var(--bone);

    font-family: var(--serif);
    font-size: 17px;
}


.search-result-meta {
    margin-top: 4px;

    color: var(--bone-dim);

    font-family: var(--mono);
    font-size: 7px;

    letter-spacing: .08em;
    text-transform: uppercase;
}


.search-result-description {
    margin-top: 7px;

    color: var(--bone-soft);

    font-family: var(--serif);
    font-size: 12px;

    line-height: 1.45;
}


/* ============================================================
   MOBILE DRAWER
   ============================================================ */

.mobile-drawer {
    display: none;
}


/* ============================================================
   FOOTER
   ============================================================ */

.lore-footer {
    display: grid;
    grid-template-columns: 1fr auto;

    gap: 20px;

    padding: 16px 19px;

    border-top: 1px solid var(--line-strong);

    background: #090908;

    color: var(--bone-dim);

    font-family: var(--mono);
    font-size: 7px;

    letter-spacing: .07em;

    line-height: 1.7;

    text-transform: uppercase;
}


.footer-right {
    text-align: right;
}


/* ============================================================
   TABLET
   ============================================================ */

@media (max-width: 1100px) {

    .lore-body {
        grid-template-columns: 215px minmax(0,1fr);
    }

    .record-layout {
        grid-template-columns: minmax(0,1fr) 235px;
    }

    .record-seal {
        width: 62px;
        height: 62px;
    }

    .record-metadata {
        grid-template-columns: repeat(3,1fr);
    }

    .meta-item:nth-child(3) {
        border-right: 0;
    }

    .meta-item:nth-child(-n+3) {
        border-bottom: 1px solid var(--line);
    }
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 780px) {

    .lore-header {
        min-height: 64px;
    }

    .brand-area {
        padding: 11px 13px;
    }

    .brand-mark {
        width: 32px;
        height: 32px;

        margin-right: 10px;

        font-size: 14px;
    }

    .brand-title {
        font-size: 13px;

        letter-spacing: .10em;
    }

    .brand-subtitle {
        font-size: 6px;
    }

    .header-right {
        display: none;
    }

    .lore-nav {
        display: none;
    }

    .lore-body {
        display: block;
    }

    .codex-sidebar {
        display: none;
    }

    .mobile-index {
        display: block;
    }

    .command-bar {
        padding: 8px 11px;
    }

    .command-button {
        display: none;
    }

    .lore-stage {
        padding: 10px;
    }

    .codex-page::before {
        left: 29px;
    }

    .record-hero {
        padding: 29px 19px 24px 43px;
    }

    .record-seal {
        position: static;

        margin-top: 20px;
    }

    .record-title {
        font-size: clamp(38px,12vw,62px);
    }

    .record-subtitle {
        font-size: 15px;
    }

    .record-metadata {
        grid-template-columns: repeat(2,1fr);
    }

    .meta-item {
        border-bottom: 1px solid var(--line);
    }

    .meta-item:nth-child(2) {
        border-right: 0;
    }

    .meta-item:nth-child(3) {
        border-right: 1px solid var(--line);
    }

    .meta-item:last-child {
        border-right: 0;
    }

    .record-layout {
        display: block;
    }

    .record-main {
        border-right: 0;
    }

    .record-aside {
        border-top: 1px solid var(--line-strong);
    }

    .lore-section {
        padding: 22px 17px 22px 43px;
    }

    .section-number {
        left: 14px;
    }

    .lore-paragraph {
        font-size: 15px;
    }

    .classification {
        grid-template-columns: 1fr;
    }

    .classification-label {
        border-right: 0;
        border-bottom: 1px solid var(--line);
    }

    .reference-grid {
        grid-template-columns: 1fr;
    }

    .discovery-bar {
        grid-template-columns: 1fr;
    }

    .discovery-item {
        border-right: 0;
        border-bottom: 1px solid var(--line);
    }

    .discovery-item:last-child {
        border-bottom: 0;
    }

    .lore-footer {
        grid-template-columns: 1fr;
    }

    .footer-right {
        text-align: left;
    }

    .mobile-drawer {
        position: fixed;
        inset: 64px 0 0;

        z-index: 700;

        overflow-y: auto;

        padding: 15px;

        background: #0a0908;

        border-top: 1px solid var(--line-strong);
    }

    .mobile-drawer.open {
        display: block;
    }
}


/* ============================================================
   SMALL PHONES
   ============================================================ */

@media (max-width: 480px) {

    .brand-mark {
        display: none;
    }

    .brand-title {
        font-size: 12px;
    }

    .record-hero {
        padding-left: 37px;
    }

    .codex-page::before {
        left: 25px;
    }

    .record-metadata {
        grid-template-columns: 1fr;
    }

    .meta-item {
        border-right: 0 !important;
    }

    .meta-item:last-child {
        border-bottom: 0;
    }

    .lore-section {
        padding-left: 37px;
    }

    .section-number {
        left: 10px;
    }

    .search-result {
        grid-template-columns: 1fr;
        gap: 5px;
    }
}
"""


# ============================================================
# JAVASCRIPT
# ============================================================

JS_TEMPLATE = r"""
const ARCHIVE_DATA = __SEARCH_DATA__;

const WORLDS = __WORLDS__;
const CHARACTERS = __CHARACTERS__;
const EVENTS = __EVENTS__;
const FACTIONS = __FACTIONS__;
const ARTIFACTS = __ARTIFACTS__;
const DOCUMENTS = __DOCUMENTS__;
const QUESTIONS = __QUESTIONS__;
const REFERENCES = __REFERENCES__;

const seenRecords = new Set();

let currentRecord = null;


function $(selector) {
    return document.querySelector(selector);
}


function escapeHTML(value) {

    return String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}


function choose(array) {

    return array[
        Math.floor(
            Math.random() * array.length
        )
    ];
}


function shuffle(array) {

    return [...array].sort(
        () => Math.random() - 0.5
    );
}


function recordCode(prefix) {

    return (
        prefix.toUpperCase() +
        "-" +
        Math.floor(
            100 + Math.random() * 900
        )
    );
}


function randomArchiveLocation() {

    const vaults = [
        "THE LOWER VAULT",
        "NORTH ARCHIVE",
        "SEALED ANNEX",
        "BLACK LIBRARY",
        "WESTERN CATALOGUE",
        "SUBTERRANEAN INDEX",
        "UNNUMBERED COLLECTION",
    ];

    return choose(vaults);
}


function randomConfidence() {

    return Math.floor(
        41 + Math.random() * 54
    ) + "%";
}


function getStatus(record) {

    const options = [
        "RESTRICTED",
        "FRAGMENTARY",
        "UNRESOLVED",
        "DISPUTED",
        "UNVERIFIED",
        "ARCHIVED"
    ];

    if (
        record.status &&
        record.status !== "Recorded"
    ) {
        return String(
            record.status
        ).toUpperCase();
    }

    return choose(options);
}


function buildNarrative(record) {

    const first = [
        `The surviving material concerning ${record.name} is incomplete.`,
        `${record.name} appears in more than one surviving collection.`,
        `The earliest surviving reference to ${record.name} is itself fragmentary.`,
        `The archive contains conflicting descriptions of ${record.name}.`,
        `The historical identity of ${record.name} cannot be established from a single source.`
    ];

    const second = [
        "Later copies preserve details that are absent from the oldest known record.",
        "Several unrelated documents appear to describe the same subject without using identical terminology.",
        "The chronology attached to the entry has been reconstructed from secondary references.",
        "Some details may represent later interpretation rather than contemporary testimony.",
        "The contradictions have been preserved rather than harmonized."
    ];

    const third = [
        "No surviving authority provides a final explanation.",
        "The unanswered portion of the record remains part of the archive.",
        "Further evidence would be required before the entry could be considered settled.",
        "The archive therefore records uncertainty as a historical fact.",
        "Until additional material is recovered, competing interpretations remain attached to the file."
    ];

    return [
        choose(first),
        choose(second),
        choose(third)
    ];
}


function getRelated(record) {

    const sameWorld =
        ARCHIVE_DATA.filter(
            item =>
                item.id !== record.id &&
                item.world === record.world
        );

    const fallback =
        ARCHIVE_DATA.filter(
            item =>
                item.id !== record.id
        );

    const pool =
        sameWorld.length >= 4
            ? sameWorld
            : fallback;

    return shuffle(pool).slice(0,4);
}


function getWorldSymbol(name) {

    const symbols = [
        "✦",
        "◇",
        "☽",
        "✧",
        "◈",
        "⌘",
        "☿",
        "△"
    ];

    let hash = 0;

    for (
        let i = 0;
        i < String(name).length;
        i++
    ) {
        hash += String(name).charCodeAt(i);
    }

    return symbols[
        hash % symbols.length
    ];
}


function buildReferences(items) {

    return items.map(item => `

        <div
            class="reference"
            data-record="${escapeHTML(item.id)}"
        >

            <span class="reference-id">
                ${escapeHTML(item.id)}
            </span>

            <span class="reference-title">
                ${escapeHTML(item.name)}
            </span>

        </div>

    `).join("");
}


function renderRecord(record) {

    currentRecord = record;

    const status = getStatus(record);

    const related =
        getRelated(record);

    const narrative =
        buildNarrative(record);

    const archiveCode =
        recordCode("FLW");

    const confidence =
        randomConfidence();

    const location =
        randomArchiveLocation();

    const symbol =
        getWorldSymbol(
            record.world || record.name
        );

    const classification =
        status === "ARCHIVED"
            ? "CLASSIFIED LORE"
            : status;

    const era =
        record.era ||
        "ERA UNKNOWN";

    const origin =
        record.origin ||
        "ARCHIVAL RECORD";

    const html = `

        <article class="codex-page">


            <header class="record-hero">

                <div class="record-seal">

                    FORBIDDEN<br>
                    LORE<br>
                    ${escapeHTML(
                        archiveCode
                    )}

                </div>


                <div class="record-kicker">

                    FORBIDDEN ARCHIVE
                    ·
                    ${escapeHTML(
                        record.type
                    )}
                    ·
                    RECORD ${escapeHTML(
                        record.id
                    )}

                </div>


                <h1 class="record-title">

                    ${escapeHTML(
                        record.name
                    )}

                </h1>


                <p class="record-subtitle">

                    ${escapeHTML(
                        record.description
                    )}

                </p>


                <div class="record-origin">

                    <span class="origin-tag">
                        ${escapeHTML(origin)}
                    </span>

                    <span class="origin-tag">
                        ${escapeHTML(
                            record.world ||
                            "UNKNOWN WORLD"
                        )}
                    </span>

                    <span class="origin-tag">
                        ${escapeHTML(
                            era
                        )}
                    </span>

                </div>

            </header>


            <div class="record-metadata">


                <div class="meta-item">

                    <span class="meta-label">
                        Archive ID
                    </span>

                    <span class="meta-value">
                        ${escapeHTML(
                            record.id
                        )}
                    </span>

                </div>


                <div class="meta-item">

                    <span class="meta-label">
                        Classification
                    </span>

                    <span class="meta-value">
                        ${escapeHTML(
                            classification
                        )}
                    </span>

                </div>


                <div class="meta-item">

                    <span class="meta-label">
                        Era
                    </span>

                    <span class="meta-value">
                        ${escapeHTML(
                            era
                        )}
                    </span>

                </div>


                <div class="meta-item">

                    <span class="meta-label">
                        Provenance
                    </span>

                    <span class="meta-value">
                        ${escapeHTML(origin)}
                    </span>

                </div>


                <div class="meta-item">

                    <span class="meta-label">
                        Confidence
                    </span>

                    <span class="meta-value">
                        ${confidence}
                    </span>

                </div>


            </div>


            <div class="record-layout">


                <main class="record-main">


                    <section class="lore-section">

                        <span class="section-number">
                            I
                        </span>


                        <div class="section-heading">

                            <h2 class="section-title">
                                The Record
                            </h2>

                            <span class="section-code">
                                PRIMARY ACCOUNT
                            </span>

                        </div>


                        <p class="lore-paragraph">

                            ${escapeHTML(
                                record.description
                            )}

                        </p>

                    </section>


                    <section class="lore-section">

                        <span class="section-number">
                            II
                        </span>


                        <div class="section-heading">

                            <h2 class="section-title">
                                Recovered Lore
                            </h2>

                            <span class="section-code">
                                SECONDARY MATERIAL
                            </span>

                        </div>


                        ${narrative.map(
                            paragraph => `

                                <p class="lore-paragraph">
                                    ${escapeHTML(
                                        paragraph
                                    )}
                                </p>

                            `
                        ).join("")}

                    </section>


                    <section class="lore-section">

                        <span class="section-number">
                            III
                        </span>


                        <div class="section-heading">

                            <h2 class="section-title">
                                Classification
                            </h2>

                            <span class="section-code">
                                ARCHIVE DECISION
                            </span>

                        </div>


                        <div class="classification">

                            <div class="classification-label">
                                Current Status
                            </div>

                            <div class="classification-value">
                                ${escapeHTML(
                                    status
                                )}
                            </div>

                        </div>

                    </section>


                    <section class="lore-section">

                        <span class="section-number">
                            IV
                        </span>


                        <div class="section-heading">

                            <h2 class="section-title">
                                Archivist Fragment
                            </h2>

                            <span class="section-code">
                                MARGIN NOTE
                            </span>

                        </div>


                        <blockquote class="lore-quote">

                            The archive does not preserve
                            certainty. It preserves what survived.

                            What was erased may be more important
                            than what remains.

                        </blockquote>

                    </section>


                    <section class="lore-section">

                        <span class="section-number">
                            V
                        </span>


                        <div class="section-heading">

                            <h2 class="section-title">
                                Cross-References
                            </h2>

                            <span class="section-code">
                                ${related.length}
                                LINKED RECORDS
                            </span>

                        </div>


                        <div class="reference-grid">

                            ${buildReferences(
                                related
                            )}

                        </div>

                    </section>


                </main>


                <aside class="record-aside">


                    <section class="aside-section">

                        <div class="aside-heading">
                            Archive Condition
                        </div>

                        <div class="status-seal">
                            ${escapeHTML(
                                status
                            )}
                        </div>

                    </section>


                    <section class="aside-section">

                        <div class="world-symbol">
                            <span>
                                ${symbol}
                            </span>
                        </div>


                        <div class="aside-heading">
                            World / Realm
                        </div>

                        <div class="aside-value">

                            ${escapeHTML(
                                record.world ||
                                "Unknown Realm"
                            )}

                        </div>

                    </section>


                    <section class="aside-section">

                        <div class="aside-heading">
                            Archive Location
                        </div>

                        <div class="aside-mono">

                            ${escapeHTML(
                                location
                            )}

                            <br>

                            SHELF:
                            ${Math.floor(
                                10 +
                                Math.random() * 90
                            )}

                            <br>

                            VAULT:
                            ${Math.floor(
                                100 +
                                Math.random() * 900
                            )}

                            <br>

                            FILE:
                            ${Math.floor(
                                1000 +
                                Math.random() * 9000
                            )}

                        </div>

                    </section>


                    <section class="aside-section">

                        <div class="aside-heading">
                            Record Properties
                        </div>


                        <ul class="aside-list">

                            <li>
                                ORIGIN:
                                ${escapeHTML(origin)}
                            </li>

                            <li>
                                ERA:
                                ${escapeHTML(era)}
                            </li>

                            <li>
                                STATUS:
                                ${escapeHTML(status)}
                            </li>

                            <li>
                                CONFIDENCE:
                                ${confidence}
                            </li>

                            <li>
                                CROSS REFERENCES:
                                ${related.length}
                            </li>

                        </ul>

                    </section>


                    <section class="aside-section">

                        <div class="aside-heading">
                            Warning
                        </div>

                        <div class="aside-value">

                            Some records contained in
                            this collection are deliberately
                            incomplete.

                            <br><br>

                            Absence of evidence does not
                            constitute evidence of absence.

                        </div>

                    </section>


                </aside>

            </div>


            <div class="discovery-bar">


                <div class="discovery-item">

                    <div class="discovery-label">
                        Current Record
                    </div>

                    <div class="discovery-value">
                        ${escapeHTML(
                            record.name
                        )}
                    </div>

                    <div class="discovery-small">
                        ${escapeHTML(
                            record.id
                        )}
                    </div>

                </div>


                <div class="discovery-item">

                    <div class="discovery-label">
                        Follow the Lore
                    </div>

                    <div class="discovery-value">
                        Examine Cross-References
                    </div>

                    <div class="discovery-small">
                        Each reference leads somewhere else.
                    </div>

                </div>


                <div class="discovery-item">

                    <div class="discovery-label">
                        Forbidden Discovery
                    </div>

                    <div class="discovery-value">
                        Open Another Record
                    </div>

                    <div class="discovery-small">
                        Press D or use RANDOM LORE.
                    </div>

                </div>


            </div>


        </article>
    `;


    $("#lore-stage").innerHTML = html;


    document.title =
        record.name +
        " · Forbidden Lore Wiki";


    document
        .querySelectorAll(
            "[data-record]"
        )
        .forEach(element => {

            element.addEventListener(
                "click",
                () => {

                    const id =
                        element.dataset.record;

                    const target =
                        ARCHIVE_DATA.find(
                            item =>
                                item.id === id
                        );

                    if (target) {

                        seenRecords.add(
                            target.id
                        );

                        renderRecord(
                            target
                        );

                        window.scrollTo({
                            top: 0,
                            behavior: "smooth"
                        });

                    }

                }
            );

        });
}


function nextLore() {

    let available =
        ARCHIVE_DATA.filter(
            record =>
                !seenRecords.has(
                    record.id
                )
        );


    if (!available.length) {

        seenRecords.clear();

        available =
            [...ARCHIVE_DATA];

    }


    const record =
        choose(available);


    seenRecords.add(
        record.id
    );


    renderRecord(record);


    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}


function openSearch() {

    $("#search-overlay")
        .classList.add("open");

    $("#search-input").value = "";

    $("#search-input").focus();

    renderSearch("");
}


function closeSearch() {

    $("#search-overlay")
        .classList.remove("open");
}


function renderSearch(query) {

    const normalized =
        query
            .trim()
            .toLowerCase();


    const results =
        ARCHIVE_DATA
            .filter(record => {

                if (!normalized) {
                    return true;
                }

                const searchable = [
                    record.id,
                    record.type,
                    record.name,
                    record.world,
                    record.status,
                    record.era,
                    record.description
                ]
                    .join(" ")
                    .toLowerCase();

                return searchable.includes(
                    normalized
                );

            })
            .slice(0,50);


    if (!results.length) {

        $("#search-results").innerHTML = `

            <div
                style="
                    padding:25px;
                    color:var(--bone-dim);
                    font-family:var(--mono);
                    font-size:9px;
                "
            >
                NO LORE FOUND IN THE CURRENT CATALOGUE.
            </div>

        `;

        return;
    }


    $("#search-results").innerHTML =
        results.map(record => `

            <div
                class="search-result"
                data-search-record="${escapeHTML(
                    record.id
                )}"
            >

                <div>

                    <div class="search-result-id">
                        ${escapeHTML(
                            record.id
                        )}
                    </div>

                </div>


                <div>

                    <div class="search-result-name">
                        ${escapeHTML(
                            record.name
                        )}
                    </div>

                    <div class="search-result-meta">

                        ${escapeHTML(
                            record.type
                        )}

                        ·

                        ${escapeHTML(
                            record.world ||
                            "UNKNOWN"
                        )}

                        ·

                        ${escapeHTML(
                            record.status
                        )}

                    </div>

                    <div class="search-result-description">

                        ${escapeHTML(
                            record.description
                        )}

                    </div>

                </div>

            </div>

        `).join("");


    document
        .querySelectorAll(
            "[data-search-record]"
        )
        .forEach(element => {

            element.addEventListener(
                "click",
                () => {

                    const target =
                        ARCHIVE_DATA.find(
                            item =>
                                item.id ===
                                element.dataset
                                    .searchRecord
                        );

                    if (target) {

                        seenRecords.add(
                            target.id
                        );

                        closeSearch();

                        renderRecord(
                            target
                        );

                        window.scrollTo({
                            top: 0,
                            behavior: "smooth"
                        });

                    }

                }
            );

        });
}


function openTimeline() {

    const event =
        choose(EVENTS);


    const record = {

        id:
            "TIM-" +
            Math.floor(
                100 +
                Math.random() * 900
            ),

        type:
            "Chronological Record",

        name:
            event.name,

        world:
            event.world,

        era:
            event.year,

        status:
            event.status,

        origin:
            "Historical Timeline",

        description:
            event.description

    };


    seenRecords.add(
        record.id
    );


    renderRecord(record);

    closeMobile();

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}


function openReference(name) {

    const reference =
        REFERENCES.find(
            item =>
                item.name.toLowerCase() ===
                String(name).toLowerCase()
        ) ||
        choose(REFERENCES);


    const record = {

        id:
            "REF-" +
            Math.floor(
                100 +
                Math.random() * 900
            ),

        type:
            "Reference Universe",

        name:
            reference.name,

        world:
            "REFERENCE REALM",

        era:
            "CONTINUITY INDEX",

        status:
            "REFERENCE",

        origin:
            "Reference Universe",

        description:
            reference.description

    };


    renderRecord(record);

    closeMobile();

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}


function openType(type) {

    const candidates =
        ARCHIVE_DATA.filter(
            item =>
                item.type === type
        );


    if (candidates.length) {

        renderRecord(
            choose(candidates)
        );

    } else {

        renderRecord(
            choose(ARCHIVE_DATA)
        );

    }


    closeMobile();

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}


function toggleMobile() {

    $("#mobile-drawer")
        .classList.toggle("open");
}


function closeMobile() {

    $("#mobile-drawer")
        .classList.remove("open");
}


document.addEventListener(
    "DOMContentLoaded",
    () => {


        renderRecord(
            choose(ARCHIVE_DATA)
        );


        $("#random-lore")
            .addEventListener(
                "click",
                nextLore
            );


        $("#search-open")
            .addEventListener(
                "click",
                openSearch
            );


        $("#search-close")
            .addEventListener(
                "click",
                closeSearch
            );


        $("#mobile-index")
            .addEventListener(
                "click",
                toggleMobile
            );


        $("#search-input")
            .addEventListener(
                "input",
                event =>
                    renderSearch(
                        event.target.value
                    )
            );


        $("#search-overlay")
            .addEventListener(
                "click",
                event => {

                    if (
                        event.target ===
                        $("#search-overlay")
                    ) {

                        closeSearch();

                    }

                }
            );


        document
            .querySelectorAll(
                "[data-action='random']"
            )
            .forEach(button => {

                button.addEventListener(
                    "click",
                    nextLore
                );

            });


        document
            .querySelectorAll(
                "[data-action='timeline']"
            )
            .forEach(button => {

                button.addEventListener(
                    "click",
                    openTimeline
                );

            });


        document
            .querySelectorAll(
                "[data-reference]"
            )
            .forEach(button => {

                button.addEventListener(
                    "click",
                    () => {

                        openReference(
                            button.dataset.reference
                        );

                    }
                );

            });


        document
            .querySelectorAll(
                "[data-type]"
            )
            .forEach(button => {

                button.addEventListener(
                    "click",
                    () => {

                        openType(
                            button.dataset.type
                        );

                    }
                );

            });


        document.addEventListener(
            "keydown",
            event => {

                const searchActive =
                    document.activeElement ===
                    $("#search-input");


                if (
                    event.key === "/" &&
                    !searchActive
                ) {

                    event.preventDefault();

                    openSearch();

                }


                if (
                    event.key.toLowerCase() ===
                    "d" &&
                    !searchActive
                ) {

                    nextLore();

                }


                if (
                    event.key === "Escape"
                ) {

                    closeSearch();

                    closeMobile();

                }

            }
        );

    }
);
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
        content="Forbidden Lore Wiki — an encyclopedic archive of fictional worlds, characters, civilizations, artifacts, histories, factions and forbidden records."
    >

    <meta
        name="robots"
        content="index, follow"
    >

    <meta
        property="og:title"
        content="Forbidden Lore Wiki"
    >

    <meta
        property="og:description"
        content="A fictional lore encyclopedia and forbidden archive."
    >

    <meta
        property="og:type"
        content="website"
    >

    <title>
        Forbidden Lore Wiki
    </title>


    <style>

        __CSS__

    </style>

</head>


<body>


<div class="lore-frame">


    <!-- ======================================================
         HEADER
         ====================================================== -->

    <header class="lore-header">


        <div class="brand-area">


            <div class="brand-mark">

                <span>
                    F
                </span>

            </div>


            <div class="brand-copy">

                <h1 class="brand-title">
                    Forbidden Lore Wiki
                </h1>

                <div class="brand-subtitle">

                    Encyclopedia of Worlds,
                    Histories & Unresolved Lore

                </div>

            </div>


        </div>


        <div class="header-right">


            <div class="header-cell">

                <div class="header-label">
                    Catalogue
                </div>

                <div class="header-value">
                    FLW / 001
                </div>

            </div>


            <div class="header-cell">

                <div class="header-label">
                    Archive State
                </div>

                <div class="header-value header-status">
                    Active
                </div>

            </div>


        </div>


    </header>


    <!-- ======================================================
         NAVIGATION
         ====================================================== -->

    <nav class="lore-nav">


        <button
            class="nav-item active"
            data-action="random"
        >
            Discover
        </button>


        <button
            class="nav-item"
            data-type="World"
        >
            Worlds
        </button>


        <button
            class="nav-item"
            data-type="Character"
        >
            Characters
        </button>


        <button
            class="nav-item"
            data-type="Historical Event"
        >
            History
        </button>


        <button
            class="nav-item"
            data-type="Faction"
        >
            Factions
        </button>


        <button
            class="nav-item"
            data-type="Artifact"
        >
            Artifacts
        </button>


        <button
            class="nav-item"
            data-type="Document"
        >
            Documents
        </button>


        <button
            class="nav-item"
            data-type="Unresolved Mystery"
        >
            Mysteries
        </button>


        <button
            class="nav-item"
            data-action="timeline"
        >
            Timeline
        </button>


    </nav>


    <!-- ======================================================
         BODY
         ====================================================== -->

    <div class="lore-body">


        <!-- ==================================================
             SIDEBAR
             ================================================== -->

        <aside class="codex-sidebar">


            <div class="codex-sidebar-inner">


                <div class="sidebar-heading">
                    Codex Index
                </div>

                <div class="sidebar-rule"></div>


                <div class="codex-list">


                    <button
                        class="codex-button active"
                        data-action="random"
                    >
                        Random Lore
                    </button>


                    <button
                        class="codex-button"
                        data-type="World"
                    >
                        Original Worlds
                    </button>


                    <button
                        class="codex-button"
                        data-type="Character"
                    >
                        Characters
                    </button>


                    <button
                        class="codex-button"
                        data-type="Historical Event"
                    >
                        Historical Events
                    </button>


                    <button
                        class="codex-button"
                        data-type="Faction"
                    >
                        Factions & Orders
                    </button>


                    <button
                        class="codex-button"
                        data-type="Artifact"
                    >
                        Artifacts & Relics
                    </button>


                    <button
                        class="codex-button"
                        data-type="Document"
                    >
                        Lost Documents
                    </button>


                    <button
                        class="codex-button"
                        data-type="Unresolved Mystery"
                    >
                        Unresolved Mysteries
                    </button>


                    <button
                        class="codex-button"
                        data-action="timeline"
                    >
                        Chronologies
                    </button>


                </div>


                <div class="sidebar-heading">
                    Fictional Realms
                </div>

                <div class="sidebar-rule"></div>


                <div class="codex-list">


                    <button
                        class="codex-button"
                        data-reference="Anime"
                    >
                        Anime
                    </button>


                    <button
                        class="codex-button"
                        data-reference="Manhwa"
                    >
                        Manhwa
                    </button>


                    <button
                        class="codex-button"
                        data-reference="Manhua"
                    >
                        Manhua
                    </button>


                    <button
                        class="codex-button"
                        data-reference="Donghua"
                    >
                        Donghua
                    </button>


                    <button
                        class="codex-button"
                        data-reference="Light Novels"
                    >
                        Light Novels
                    </button>


                    <button
                        class="codex-button"
                        data-reference="Comics"
                    >
                        Comics
                    </button>


                    <button
                        class="codex-button"
                        data-reference="DC"
                    >
                        DC
                    </button>


                    <button
                        class="codex-button"
                        data-reference="Marvel"
                    >
                        Marvel
                    </button>


                </div>


                <div class="sidebar-note">

                    <div class="sidebar-note-title">
                        Archive Doctrine
                    </div>


                    <div class="sidebar-note-text">

                        A world may be fictional.

                        Its history does not have
                        to feel fictional.

                        <br><br>

                        Every entry is treated as
                        an archival record.

                    </div>

                </div>


            </div>


        </aside>


        <!-- ==================================================
             CONTENT
             ================================================== -->

        <main class="lore-content">


            <div class="command-bar">


                <div class="command-path">

                    FORBIDDEN LORE
                    /
                    ENCYCLOPEDIA
                    /
                    <strong>
                        ACTIVE RECORD
                    </strong>

                </div>


                <div class="command-actions">


                    <button
                        id="search-open"
                        class="command-button"
                    >
                        Search /
                    </button>


                    <button
                        id="random-lore"
                        class="command-button"
                    >
                        Random Lore
                    </button>


                    <button
                        id="mobile-index"
                        class="command-button mobile-index"
                    >
                        Index
                    </button>


                </div>


            </div>


            <!-- ==============================================
                 MOBILE DRAWER
                 ============================================== -->

            <div
                id="mobile-drawer"
                class="mobile-drawer"
            >


                <div class="sidebar-heading">
                    Codex Index
                </div>

                <div class="sidebar-rule"></div>


                <div class="codex-list">


                    <button
                        class="codex-button"
                        data-action="random"
                    >
                        Random Lore
                    </button>


                    <button
                        class="codex-button"
                        data-type="World"
                    >
                        Original Worlds
                    </button>


                    <button
                        class="codex-button"
                        data-type="Character"
                    >
                        Characters
                    </button>


                    <button
                        class="codex-button"
                        data-type="Historical Event"
                    >
                        Historical Events
                    </button>


                    <button
                        class="codex-button"
                        data-type="Faction"
                    >
                        Factions
                    </button>


                    <button
                        class="codex-button"
                        data-type="Artifact"
                    >
                        Artifacts
                    </button>


                    <button
                        class="codex-button"
                        data-type="Document"
                    >
                        Documents
                    </button>


                    <button
                        class="codex-button"
                        data-type="Unresolved Mystery"
                    >
                        Mysteries
                    </button>


                    <button
                        class="codex-button"
                        data-action="timeline"
                    >
                        Timeline
                    </button>


                </div>


                <div class="sidebar-heading">
                    Reference Universes
                </div>

                <div class="sidebar-rule"></div>


                <div class="codex-list">


                    <button
                        class="codex-button"
                        data-reference="Anime"
                    >
                        Anime
                    </button>


                    <button
                        class="codex-button"
                        data-reference="Manhwa"
                    >
                        Manhwa
                    </button>


                    <button
                        class="codex-button"
                        data-reference="Manhua"
                    >
                        Manhua
                    </button>


                    <button
                        class="codex-button"
                        data-reference="Donghua"
                    >
                        Donghua
                    </button>


                    <button
                        class="codex-button"
                        data-reference="Light Novels"
                    >
                        Light Novels
                    </button>


                    <button
                        class="codex-button"
                        data-reference="Comics"
                    >
                        Comics
                    </button>


                    <button
                        class="codex-button"
                        data-reference="DC"
                    >
                        DC
                    </button>


                    <button
                        class="codex-button"
                        data-reference="Marvel"
                    >
                        Marvel
                    </button>


                </div>


            </div>


            <!-- ==============================================
                 RECORD
                 ============================================== -->

            <section
                id="lore-stage"
                class="lore-stage"
            >

                <article class="codex-page">

                    <header class="record-hero">

                        <div class="record-kicker">
                            Initialising Forbidden Archive
                        </div>

                        <h1 class="record-title">
                            Loading Lore
                        </h1>

                    </header>

                </article>

            </section>


            <!-- ==============================================
                 FOOTER
                 ============================================== -->

            <footer class="lore-footer">


                <div>

                    FORBIDDEN LORE WIKI
                    ·
                    FICTIONAL ENCYCLOPEDIA

                    <br>

                    ORIGINAL WORLDS · REFERENCE UNIVERSES ·
                    CHARACTERS · HISTORY · ARTIFACTS · LORE

                    <br>

                    NO DATABASE · NO LOGIN · NO LOCAL STORAGE ·
                    NO SERVER-SIDE STATE

                </div>


                <div class="footer-right">

                    BROWSER MEMORY ONLY

                    <br>

                    ARCHIVE STATUS: ACTIVE

                </div>


            </footer>


        </main>


    </div>


</div>


<!-- ============================================================
     SEARCH WINDOW
     ============================================================ -->

<div
    id="search-overlay"
    class="search-overlay"
>


    <div class="search-window">


        <div class="search-titlebar">


            <div class="search-icon">
                ⌕
            </div>


            <input
                id="search-input"
                class="search-input"
                type="search"
                autocomplete="off"
                spellcheck="false"
                placeholder="Search worlds, characters, factions, artifacts, events..."
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

    replacements = {

        "__CSS__":
            CSS,

        "__SEARCH_DATA__":
            json.dumps(
                SEARCH_DATA,
                ensure_ascii=False,
                separators=(",", ":"),
            ),

        "__WORLDS__":
            json.dumps(
                WORLDS,
                ensure_ascii=False,
                separators=(",", ":"),
            ),

        "__CHARACTERS__":
            json.dumps(
                CHARACTERS,
                ensure_ascii=False,
                separators=(",", ":"),
            ),

        "__EVENTS__":
            json.dumps(
                EVENTS,
                ensure_ascii=False,
                separators=(",", ":"),
            ),

        "__FACTIONS__":
            json.dumps(
                FACTIONS,
                ensure_ascii=False,
                separators=(",", ":"),
            ),

        "__ARTIFACTS__":
            json.dumps(
                ARTIFACTS,
                ensure_ascii=False,
                separators=(",", ":"),
            ),

        "__DOCUMENTS__":
            json.dumps(
                DOCUMENTS,
                ensure_ascii=False,
                separators=(",", ":"),
            ),

        "__QUESTIONS__":
            json.dumps(
                QUESTIONS,
                ensure_ascii=False,
                separators=(",", ":"),
            ),

        "__REFERENCES__":
            json.dumps(
                REFERENCE_UNIVERSES,
                ensure_ascii=False,
                separators=(",", ":"),
            ),

    }


    js = JS_TEMPLATE

    for key, value in replacements.items():

        js = js.replace(
            key,
            value
        )


    output = HTML_TEMPLATE.replace(
        "__CSS__",
        CSS
    )


    output = output.replace(
        "__JS__",
        js
    )


    return output


# ============================================================
# MAIN
# ============================================================

def main():

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    output = build_html()


    OUTPUT_FILE.write_text(
        output,
        encoding="utf-8"
    )


    print("=" * 70)
    print("FORBIDDEN LORE WIKI")
    print("STATIC ENCYCLOPEDIA GENERATED")
    print("=" * 70)
    print(f"Output: {OUTPUT_FILE}")
    print(f"Indexed Records: {len(SEARCH_DATA)}")
    print()
    print("STATIC SITE: YES")
    print("DATABASE: NO")
    print("LOCAL STORAGE: NO")
    print("SESSION STORAGE: NO")
    print("INDEXED DB: NO")
    print("LOGIN: NO")
    print("SIGNUP: NO")
    print("BACKEND: NO")
    print("BROWSER MEMORY: YES")
    print("=" * 70)


if __name__ == "__main__":
    main()
