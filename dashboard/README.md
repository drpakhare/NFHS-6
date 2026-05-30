# NFHS India Explorer — Rounds 3 → 6 (2005–2024)

An **open, frontend-only** dashboard and harmonised database of India's **National Family Health Survey (NFHS)** fact-sheet indicators across four rounds — **NFHS-3 (2005–06), NFHS-4 (2015–16), NFHS-5 (2019–21)** and the newly released **NFHS-6 (2023–24)** — for India and all states/UTs at **Urban / Rural / Total** levels.

Everything runs in the browser. **No server, no backend, no tracking.** Made for policymakers, researchers and journalists to **explore and download** the data.

## Features
- **Map** — interactive India choropleth by indicator / round / area; click a state to see its trend.
- **Trends** — multi-state line charts across all four rounds.
- **Compare states** — ranked bar chart for any indicator/round, India highlighted.
- **Data explorer** — filter by round/state/area/keyword; download filtered CSV, full CSV, or the 5-sheet Excel workbook.
- **SQL (DuckDB-WASM)** — optional in-browser SQL over the full table, with CSV export.

## Run it
Because browsers block local `file://` fetches (needed by the Parquet/DuckDB features), serve the folder over http:

```bash
cd dashboard
python3 -m http.server 8000
# open http://localhost:8000
```

The Map / Trends / Compare / filtered-download features also work when the file is opened directly; only the **Parquet download** and **SQL** tab require http hosting.

## Publish (free static hosting)
- **GitHub Pages:** push this folder to a repo, enable Pages on the `main` branch → live URL.
- Or drag-and-drop onto **Netlify** / **Cloudflare Pages** / **Vercel**.

## Make it citable (DOI)
1. Push to a public **GitHub** repo.
2. Link the repo in **Zenodo** (zenodo.org → GitHub → toggle the repo on).
3. Cut a **GitHub Release** (e.g. `v1.0.0`). Zenodo automatically mints a DOI and archives the release.
4. Add the DOI to `CITATION.cff` and the **About & cite** tab. GitHub will then show a “Cite this repository” button.

## Files
```
dashboard/
├── index.html                      # the whole app (vanilla JS + Plotly + DuckDB-WASM)
├── README.md  CITATION.cff  LICENSE
└── data/
    ├── data.js                     # compact inline data (dictionary-encoded)
    ├── geo.js / india_states.geojson
    ├── meta.json
    ├── nfhs.parquet                # full long table (for DuckDB / SQL)
    ├── nfhs_full.csv               # full long table (CSV)
    └── NFHS_Combined_Database_3to6.xlsx   # 5-sheet workbook
```

## Data notes (please read before publishing findings)
- **Manipur is absent from NFHS-6** (fieldwork not completed); present in earlier rounds.
- **Ladakh** appears only from NFHS-5; **Dadra & Nagar Haveli** and **Daman & Diu** are separate UTs in NFHS-3/4 but a single merged UT in NFHS-5/6 — these do not align across rounds.
- **Indicator definitions shifted** between rounds (age groups, denominators, vaccine schedules); harmonised series are *indicative*. Verify exact definitions in the source fact-sheet footnotes.
- **▲** marks parenthesised small-sample estimates (NFHS-5 convention).
- The **map boundary** GeoJSON is an open community dataset for visual reference only — not an authoritative border depiction.

## How to cite
**This tool / compiled dataset** (add your name + Zenodo DOI after release):
> Pakhare, A., & Joshi, A. (2026). *NFHS India Explorer: a harmonised NFHS-3 to NFHS-6 fact-sheet database and dashboard* (v1.0.0) [Software]. Zenodo. https://doi.org/10.5281/zenodo.20460014

**Always also cite the source:**
> International Institute for Population Sciences (IIPS). (2026). *National Family Health Survey (NFHS-6), 2023–24: India and State/UT Fact Sheets.* Mumbai: IIPS. (plus the NFHS-5/4/3 fact-sheet reports for earlier rounds.)

## Licence
Code: **MIT**. Compiled dataset: **CC-BY-4.0** (attribute IIPS as the original source). Underlying NFHS data © IIPS / Government of India.
