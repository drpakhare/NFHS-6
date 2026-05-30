# NFHS India Explorer — a harmonised NFHS-3 → NFHS-6 database & dashboard

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20460014.svg)](https://doi.org/10.5281/zenodo.20460014)

**DOI (all versions):** [10.5281/zenodo.20460014](https://doi.org/10.5281/zenodo.20460014) · **License:** code MIT · data CC-BY-4.0

An open, **frontend-only** (no-server) database and dashboard of India's **National Family Health
Survey (NFHS)** fact-sheet indicators across four rounds — **NFHS-3 (2005–06), NFHS-4 (2015–16),
NFHS-5 (2019–21)** and **NFHS-6 (2023–24)** — for India and all states/UTs at **Urban / Rural /
Total** levels. Built for policymakers, researchers and journalists to **explore and download** the
data. Live site: **https://drpakhare.github.io/NFHS-6/dashboard/**

> ⚠️ **Disclaimer.** This is a derived compilation, **not produced or endorsed by IIPS or the
> Government of India**. Estimates carry survey error and are shown without significance testing.
> Indicator definitions changed across rounds, so cross-round comparisons may not be like-for-like
> (see the comparability flags). The original IIPS fact sheets are authoritative. Not for clinical,
> legal, financial or commercial decision-making. Map boundaries are illustrative only.

## What's here

```
.
├── dashboard/                       # the web app (serve, then open in a browser)
│   ├── index.html
│   ├── lib/plotly-2.35.2.min.js     # bundled so it works offline / behind firewalls
│   └── data/                        # data.js, geo.js, parquet, csv, xlsx, geojson
├── NFHS_Combined_Database_3to6.xlsx # 5-sheet workbook (the database)
├── scripts/                         # extraction + harmonisation pipeline (reproducibility)
├── METHODS.md                       # how it was built
├── DATA_DICTIONARY.md               # columns + all 96 harmonised indicators + comparability
└── CHANGELOG.md  CITATION.cff  .zenodo.json  LICENSE
```

The original IIPS source publications are **not** redistributed here (excluded via `.gitignore`);
the compiled dataset and dashboard are self-contained without them.

## Run / view the dashboard locally

Browsers block local `file://` data access, so serve the folder over http:

```bash
cd dashboard
python3 -m http.server 8000
# open http://localhost:8000
```

## Publish on GitHub Pages

Settings → **Pages** → Deploy from a branch → `main` → **/ (root)**.
Site URL: `https://drpakhare.github.io/NFHS-6/dashboard/`

## Citable DOI via Zenodo

1. On [zenodo.org](https://zenodo.org), log in with GitHub and toggle this repository **ON**
   (do this *before* the release — authors and ORCIDs are pre-filled in `.zenodo.json`).
2. Create a GitHub **Release** tagged `v1.1.0`. Zenodo mints a version DOI and archives the release (the concept DOI above always points to the latest).
3. Paste the DOI into the badge above, `CITATION.cff`, and the dashboard's **About & cite** tab.

> Zenodo DOIs are citable and trackable but are **not** indexed by Google Scholar. For Scholar
> visibility, a short **data descriptor** (e.g. *Data in Brief* / a *Data Note*) citing the DOI is
> planned, alongside a district-level expansion of the database.

## How to cite

**APA**

> Pakhare, A., & Joshi, A. (2026). *NFHS India Explorer: a harmonised NFHS-3 to NFHS-6 fact-sheet
> database and dashboard* (Version v1.1.0) [Software]. Zenodo. https://doi.org/10.5281/zenodo.20460014

**BibTeX**

```bibtex
@software{pakhare_nfhs_explorer_2026,
  author    = {Pakhare, Abhijit and Joshi, Ankur},
  title     = {{NFHS India Explorer: a harmonised NFHS-3 to NFHS-6 fact-sheet database and dashboard}},
  year      = {2026},
  version   = {v1.1.0},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.20460014},
  url       = {https://doi.org/10.5281/zenodo.20460014}
}
```

**Always also cite the data source**

> International Institute for Population Sciences (IIPS). (2026). *National Family Health Survey
> (NFHS-6), 2023–24: India and State/UT Fact Sheets.* Mumbai: IIPS. (and the NFHS-5/4/3 reports.)

## Authors

**Abhijit Pakhare** (ORCID 0000-0003-2897-4141) and **Ankur Joshi** (ORCID 0000-0002-3766-376X),
Department of Community & Family Medicine, AIIMS Bhopal, India. Compiled with assistance from
Anthropic's Claude (Cowork); the authors verified the data and are responsible for its accuracy.

## Licence

Dashboard code: **MIT**. Compiled dataset: **CC-BY-4.0** (please attribute IIPS as the original
data source). Underlying NFHS estimates © IIPS / Government of India. See `LICENSE`.
