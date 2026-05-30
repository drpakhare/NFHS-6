# Methods — building the harmonised NFHS-3 to NFHS-6 database

This document describes how the combined database was compiled, so results are reproducible
and the limitations are explicit. It is also the basis for the planned data descriptor paper.

## 1. Sources

| Round | Years | Source file | Geography level |
|---|---|---|---|
| NFHS-6 | 2023–24 | Official IIPS Fact Sheets PDF (released May 2026) | India + 35 state/UT fact sheets |
| NFHS-5 | 2019–21 | `NFHS_5_Factsheets_Data.xls` (published fact-sheet data) | India + all states/UTs |
| NFHS-4 | 2015–16 | `NFHS-4 and 3 Fact Sheets Sparse.xlsx` | India + all states/UTs |
| NFHS-3 | 2005–06 | same sparse workbook | India + states (mostly Total only) |

All values are **fact-sheet (key-indicator) estimates**, not re-analysis of unit-level data.

## 2. Extraction

- **NFHS-6** was extracted from the PDF using coordinate-based parsing (`pdfplumber`):
  state/UT blocks were detected from page headers; the four right-aligned value columns
  (Urban, Rural, Total for NFHS-6, and the printed NFHS-5 Total) were located by x-position;
  indicator rows were rebuilt from the numbered list (1–101). The NFHS-5 trend column printed
  in the NFHS-6 PDF was **not** used — NFHS-5 values come from the NFHS-5 source file instead.
- **NFHS-5 / 4 / 3** were reshaped from their published tables into the same tidy long form.

## 3. Tidy (long) structure

One row per `state × round × area × indicator`, with a numeric `value`, the original
`value_raw` text, a `data_flag`, and provenance. See `DATA_DICTIONARY.md` for columns.

## 4. Standardisation

- **State/UT names** were standardised across rounds (e.g. *Maharastra* → Maharashtra,
  *Chattisgarh* → Chhattisgarh, *Delhi* → NCT of Delhi, *Andaman & Nicobar Islands* spelling).
- **Small-sample estimates**: NFHS-5 encoded parenthesised (small/unweighted-sample) estimates
  as negative numbers in the source file. These were converted to their absolute value and
  flagged in `data_flag`.

## 5. Harmonisation across rounds

Indicator wording differs between rounds. A curated crosswalk maps equivalent indicators to a
single **harmonised indicator** name using signature matching (required/excluded keyword sets),
with word-boundary matching to avoid false hits (e.g. "men" inside "women"). This yields
**84 harmonised indicators**: 52 present in all four rounds, 23 in three, 9 in two. Indicators
not in the crosswalk are retained with their original per-round wording (nothing is discarded).

### Comparability flags
Each harmonised indicator is labelled **comparable** or **definition changed across rounds**.
Known breaks flagged with caution include: anaemia (NFHS-6 used venous rather than capillary
blood), full immunisation (schedule and card-vs-recall basis), improved water/sanitation/clean-fuel
definitions, spousal-violence age base (15–49 vs 18–49), household decision-making definition,
adequate-diet (IYCF) definition, and BMI base exclusions. These flags are conservative and users
should still consult the source fact-sheet footnotes.

## 6. Geography for the map

State/UT boundaries (2020 vintage, with Ladakh separate and Dadra & Nagar Haveli and Daman & Diu
merged) were derived by dissolving an open community district-level GeoJSON to state level and
renaming to match the database. Boundaries are for visual reference only.

## 7. Validation

- Extracted NFHS-6 values were spot-checked against the source PDF (e.g. India TFR, stunting,
  institutional births, female sterilisation).
- All percentage indicators were range-checked (0–100) after the small-sample sign correction.
- Cross-round joins were verified by confirming every mapped state matches the GeoJSON.

## 8. Known limitations

- Fact-sheet estimates only; no unit-level re-analysis, no significance testing, no confidence
  intervals.
- Manipur absent from NFHS-6; Ladakh only from NFHS-5; DNH & DD geography differs across rounds.
- Definition changes mean some cross-round comparisons are not like-for-like (see flags).
- Figures may differ slightly from the source fact sheets due to extraction/rounding; the
  original IIPS fact sheets are authoritative.

## Reproducibility
The extraction/compilation scripts are available in the repository. Re-running them against the
source files regenerates `NFHS_Combined_Database_3to6.xlsx` and the dashboard data files.
