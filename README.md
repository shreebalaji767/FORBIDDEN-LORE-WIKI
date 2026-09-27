# FORBIDDEN-LORE-WIKI

A static, responsive fictional knowledge archive for exploring characters, worlds, factions, historical events, artifacts, documents, questions, and interconnected lore.

The project is designed to make fictional material feel like a serious archival reference system rather than a conventional random-content website.

## Features

- Fictional worlds and lore
- Anime-inspired worlds
- Manhwa-inspired worlds
- Manhua-inspired worlds
- Donghua-inspired worlds
- Light-novel-inspired worlds
- Comic-inspired worlds
- DC and Marvel reference categories
- Original fictional universes
- Characters
- Factions
- Historical events
- Artifacts
- Documents and manuscripts
- Lore questions
- Cross-references
- Connected discoveries
- Random discovery
- Search
- Responsive interface
- Desktop, tablet, and mobile support
- Dynamic presentation
- Browser-memory-only exploration state

## Important Content Boundary

The archive may discuss fictional universes and recognizable fictional properties.

References to existing copyrighted fictional universes are presented as references to those fictional works and should not be interpreted as official canon unless explicitly identified as such.

Original material created for this project is fictional and is not presented as historical fact.

The project is intended as an entertainment and fictional-knowledge experience.

## Architecture

This project does not require a database.

It does not require:

- PostgreSQL
- MySQL
- MongoDB
- Redis
- Supabase
- Firebase
- Authentication
- User accounts
- Login
- Signup
- Server-side sessions

The generated website operates as a static HTML application.

## Storage Policy

The project intentionally avoids persistent browser storage.

It does not use:

- `localStorage`
- `sessionStorage`
- IndexedDB
- Cookies for application state

Temporary state may exist in JavaScript memory while the page is open.

Refreshing or closing the page may therefore produce a different discovery experience.

## Project Structure

```text
FORBIDDEN-LORE-WIKI/
│
├── generate.py
├── requirements.txt
├── README.md
├── SECURITY.md
├── .gitignore
│
└── site/
    └── index.html
