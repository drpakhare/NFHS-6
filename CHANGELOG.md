# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/), and this project adheres to
[Semantic Versioning](https://semver.org/).

## [1.1.0] — 2026-05-30

### Added
- **Blood pressure and blood glucose indicators** (12 harmonised series — blood sugar
  high / very high / raised, and mildly / moderately–severely / on-medication elevated
  blood pressure, each split women/men) in a new **"Hypertension & Blood Sugar"** group.
  These were measured from NFHS-4 onward (absent in NFHS-3) and are flagged as
  *definition changed across rounds* (measurement method, cut-offs, and NFHS-5/6
  on-medication composites differ).
- Harmonised indicator count increased from 84 to **96** (52 in all four rounds,
  29 in three, 15 in two).

### Changed
- Regenerated the Excel workbook, CSV, Parquet, dashboard data, data dictionary and
  comparability/definition metadata to include the new indicators.

## [1.0.0] — 2026-05-30

First public release.

### Added
- Harmonised long-format database of NFHS fact-sheet indicators for rounds 3, 4, 5 and 6
  (India + all states/UTs, Urban/Rural/Total), distributed as a 5-sheet Excel workbook,
  CSV and Parquet.
- NFHS-6 (2023-24) indicators extracted from the official IIPS Fact Sheets PDF.
- 84 harmonised indicators aligned across rounds, with comparability flags
  (comparable vs definition-changed) and per-round indicator wording.
- Frontend-only dashboard (vanilla JS + Plotly, Plotly bundled locally):
  - Interactive India choropleth with no-data states shown in grey and an optional
    values-on-map overlay (included automatically in downloaded images).
  - Cross-round trend charts with state labels and gaps for unmeasured rounds.
  - State comparison (ranked bars).
  - Data explorer with round/state/area/keyword filters and CSV/Excel downloads,
    plus an in-browser SQL panel (DuckDB-WASM).
  - Cascading indicator group → indicator dropdowns; selection persists across tabs.
  - Round-aware indicator lists (only indicators measured in the selected round).
  - Shareable deep links (current view encoded in the URL).
  - Per-chart CSV and PNG downloads with descriptive filenames.
- Data-use disclaimer, author/acknowledgement and citation placeholders.

### Notes
- Underlying estimates are © IIPS / Government of India; this is a derived compilation.
