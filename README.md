# NFHS India Explorer — a harmonised NFHS-3 → NFHS-6 database & dashboard

<!-- After the Zenodo release, replace the line below with the DOI badge Zenodo gives you -->
<!-- [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX) -->
**DOI:** _add Zenodo DOI here after release_ · **License:** code MIT · data CC-BY-4.0

An open, **frontend-only** (no-server) database and dashboard of India's **National Family Health
Survey (NFHS)** fact-sheet indicators across four rounds — **NFHS-3 (2005–06), NFHS-4 (2015–16),
NFHS-5 (2019–21)** and the newly released **NFHS-6 (2023–24)** — for India and all states/UTs at
**Urban / Rural / Total** levels. Built for policymakers, researchers and journalists to **explore
and download** the data.

> ⚠️ **Disclaimer.** This is a derived compilation, **not produced or endorsed by IIPS or the
> Government of India**. Estimates carry survey error and are shown without significance testing.
> Indicator definitions changed across rounds, so cross-round comparisons may not be like-for-like
> (see the comparability flags). The original IIPS fact sheets are authoritative. Not for clinical,
> legal, financial or commercial decision-making. Map boundaries are illustrative only.

## What's here

```
.
├── dashboard/                       # the web app (open dashboard/index.html via a server)
│   ├── index.html
│   ├── lib/plotly-2.35.2.min.js     # bundled so it works offline / behind firewalls
│   └── data/                        # data.js, geo.js, parquet, csv, xlsx, geojson
├── NFHS_Combined_Database_3to6.xlsx # 5-sheet workbook (the database)
├── scripts/                         # extraction + harmonisation pipeline (reproducibility)
├── METHODS.md                       # how it was built
├── DATA_DICTIONARY.md               # columns + all 84 harmonised indicators + comparability
├── CHANGELOG.md  CITATION.cff  .zenodo.json  LICENSE
└── Fact Sheets/                     # original IIPS source files (see note below)
```

## Run / view the dashboard

Browsers block local `file://` data access, so serve the folder over http:

```bash
cd dashboard
python3 -m http.server 8000
# open http://localhost:8000
```

## Publish on GitHub Pages

1. Push this repository to GitHub.
2. Settings → Pages → Build from branch → `main` → **/ (root)**. The site lives at
   `https://<user>.github.io/<repo>/dashboard/`.
   (Or move the contents of `dashboard/` to the repo root if you prefer the site at `/`.)

## Get a citable DOI (Zenodo)

1. On [zenodo.org](https://zenodo.org) → log in with GitHub → enable this repository.
2. Fill in author ORCIDs/affiliations in `.zenodo.json` and `CITATION.cff`.
3. Create a GitHub **Release** (`v1.0.0`). Zenodo mints a DOI and archives the release.
4. Paste the DOI into the badge above, `CITATION.cff`, `.zenodo.json`, and the dashboard's
   **About & cite** tab.

> Note: Zenodo DOIs are citable and trackable but are **not** indexed by Google Scholar.
> For Scholar visibility, publish a short **data descriptor** (e.g. *Data in Brief*, a *Data Note*,
> or *Scientific Data*) that cites the Zenodo DOI. A district-level expansion is planned alongside it.

## How to cite

> Pakhare, A., & Joshi, A. (2026). *NFHS India Explorer: a harmonised NFHS-3 to NFHS-6 fact-sheet
> database and dashboard* (v1.0.0) [Software]. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX

Always also cite the source:

> International Institute for Population Sciences (IIPS). (2026). *National Family Health Survey
> (NFHS-6), 2023–24: India and State/UT Fact Sheets.* Mumbai: IIPS. (and the NFHS-5/4/3 reports.)

## Authors
Abhijit Pakhare · Ankur Joshi. Compiled with assistance from Anthropic's Claude (Cowork); the
authors verified the data and are responsible for its accuracy.

## Source files note
The `Fact Sheets/` folder holds the original IIPS publications. If you would rather not redistribute
them in a public repo, remove the folder (or add it to `.gitignore`) — the compiled dataset and
dashboard are self-contained without it. Always credit IIPS as the data source.
