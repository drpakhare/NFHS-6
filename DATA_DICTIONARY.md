# Data Dictionary — NFHS India Explorer

This dataset is a tidy/long compilation of India's National Family Health Survey (NFHS) **fact-sheet** indicators for rounds 3, 4, 5 and 6, for India and all states/UTs at Urban/Rural/Total levels.

## Files

| File | Description |
|---|---|
| `NFHS_Combined_Database_3to6.xlsx` | 5-sheet workbook: README, Master_Long, Indicator_Dictionary, Harmonized_Coverage, Trend_Total |
| `dashboard/data/nfhs_full.csv` | Full tidy table (every row incl. blanks) |
| `dashboard/data/nfhs.parquet` | Same table in Parquet (for SQL / programmatic use) |
| `dashboard/data/data.js` | Dictionary-encoded data + metadata used by the dashboard |
| `dashboard/data/india_states.geojson` | India state/UT boundaries (2020), for the map |

## Columns (Master_Long / nfhs_full.csv)

| Column | Meaning |
|---|---|
| `state` | State/UT name (or 'India'). Standardised across rounds. |
| `round` | NFHS round: NFHS-3, NFHS-4, NFHS-5, NFHS-6. |
| `year` | Survey field-work years for the round. |
| `area` | Urban, Rural or Total. |
| `section` | Source fact-sheet section heading (where available). |
| `indicator` | Indicator wording as printed in that round's fact sheet. |
| `harmonized_indicator` | Canonical name aligning the same indicator across rounds (84 indicators). Blank for non-harmonised indicators. |
| `value` | Numeric value of the estimate. |
| `value_raw` | Original cell text (may include 'NA' or footnote markers). |
| `data_flag` | 'Parenthesised estimate…' = small/unweighted sample (NFHS-5 convention). |
| `source` | Provenance of the row (PDF / xls / sparse xlsx). |

## Geography notes

- **Manipur** is absent from NFHS-6 (field-work not completed).
- **Ladakh** appears only from NFHS-5; **Dadra & Nagar Haveli** and **Daman & Diu** are separate UTs in NFHS-3/4 but a single merged UT in NFHS-5/6.

## Harmonised indicators (84)

`C` = comparability: ✓ comparable / ⚠ definition changed across rounds. Round columns show ● where the indicator has data.

| Indicator | Group | C | N3 | N4 | N5 | N6 |
|---|---|:--:|:--:|:--:|:--:|:--:|
| ANC visit in first trimester (%) | Maternal Health (ANC/Delivery/PNC) | ✓ | ● | ● | ● | ● |
| ANC: 4+ visits (%) | Maternal Health (ANC/Delivery/PNC) | ✓ | ● | ● | ● | ● |
| All women 15-49 anaemic (%) | Anaemia | ⚠ | ● | ● | ● | · |
| Births delivered by caesarean section (%) | Maternal Health (ANC/Delivery/PNC) | ✓ | ● | ● | ● | ● |
| Breastfed child 6-23m adequate diet (%) | Child Feeding & Nutrition | ⚠ | · | ● | ● | ● |
| C-section in private facility (%) | Maternal Health (ANC/Delivery/PNC) | ✓ | ● | ● | ● | ● |
| C-section in public facility (%) | Maternal Health (ANC/Delivery/PNC) | ✓ | ● | ● | ● | ● |
| Child 6-8m solid/semi-solid + breastmilk (%) | Child Feeding & Nutrition | ✓ | ● | ● | ● | ● |
| Child <6m exclusively breastfed (%) | Child Feeding & Nutrition | ✓ | ● | ● | ● | ● |
| Child ARI/fever taken to facility (%) | Childhood Diseases | ✓ | ● | ● | ● | ● |
| Child breastfed within 1 hour of birth (%) | Child Feeding & Nutrition | ✓ | ● | ● | ● | ● |
| Child fully immunized/vaccinated (%) | Child Immunization & Vit-A | ⚠ | ● | ● | · | · |
| Child fully vaccinated (card or recall) (%) | Child Immunization & Vit-A | ⚠ | · | · | ● | ● |
| Child received 3 doses polio (%) | Child Immunization & Vit-A | ✓ | ● | ● | ● | ● |
| Child received BCG (%) | Child Immunization & Vit-A | ✓ | ● | ● | ● | ● |
| Child received measles/MCV 1st dose (%) | Child Immunization & Vit-A | ✓ | ● | ● | ● | ● |
| Child received vitamin A dose (%) | Child Immunization & Vit-A | ✓ | ● | ● | ● | ● |
| Child w/ diarrhoea given ORS (%) | Childhood Diseases | ✓ | ● | ● | ● | · |
| Child w/ diarrhoea given zinc (%) | Childhood Diseases | ✓ | · | ● | ● | · |
| Children 6-59m anaemic (%) | Anaemia | ⚠ | ● | ● | ● | · |
| Children under 5 severely wasted (%) | Child Feeding & Nutrition | ✓ | ● | ● | ● | ● |
| Children under 5 stunted (%) | Child Feeding & Nutrition | ✓ | ● | ● | ● | ● |
| Children under 5 underweight (%) | Child Feeding & Nutrition | ✓ | ● | ● | ● | ● |
| Children under 5 wasted (%) | Child Feeding & Nutrition | ✓ | ● | ● | ● | ● |
| Ever-married women experienced spousal violence (%) | Women's Empowerment & Violence | ⚠ | ● | ● | ● | ● |
| FP: Any method (%) | Family Planning | ⚠ | ● | ● | · | ● |
| FP: Any modern method (%) | Family Planning | ⚠ | ● | ● | ● | ● |
| FP: Condom (%) | Family Planning | ✓ | ● | ● | · | · |
| FP: Female sterilization (%) | Family Planning | ✓ | ● | ● | ● | ● |
| FP: IUD/PPIUD (%) | Family Planning | ✓ | ● | ● | ● | · |
| FP: Male sterilization (%) | Family Planning | ✓ | ● | ● | ● | ● |
| FP: Pill (%) | Family Planning | ✓ | ● | ● | · | · |
| Female population age 6+ who ever attended school (%) | Education & Adults | ✓ | ● | ● | ● | ● |
| HH member covered by health insurance/scheme (%) | Maternal Health (ANC/Delivery/PNC) | ✓ | ● | ● | ● | ● |
| Households using clean fuel for cooking (%) | Population & Household | ⚠ | ● | ● | ● | · |
| Households using improved sanitation facility (%) | Population & Household | ⚠ | ● | ● | ● | · |
| Households using iodized salt (%) | Population & Household | ✓ | ● | ● | ● | ● |
| Households with electricity (%) | Population & Household | ✓ | ● | ● | ● | ● |
| Households with improved drinking-water source (%) | Population & Household | ⚠ | ● | ● | ● | ● |
| Infant mortality rate (per 1000) | Marriage, Fertility & Mortality | ✓ | ● | ● | ● | · |
| Institutional births (%) | Maternal Health (ANC/Delivery/PNC) | ✓ | ● | ● | ● | ● |
| Institutional births in public facility (%) | Maternal Health (ANC/Delivery/PNC) | ✓ | ● | ● | ● | ● |
| Last birth protected vs neonatal tetanus (%) | Maternal Health (ANC/Delivery/PNC) | ✓ | ● | ● | ● | ● |
| Married women participate in HH decisions (%) | Women's Empowerment & Violence | ⚠ | ● | ● | ● | ● |
| Men (15-49) who are literate (%) | Education & Adults | ✓ | ● | ● | ● | · |
| Men (15-49) with 10+ years schooling (%) | Education & Adults | ✓ | · | · | ● | ● |
| Men 15-49 anaemic (%) | Anaemia | ⚠ | ● | ● | ● | · |
| Men 25-29 married before age 21 (%) | Marriage, Fertility & Mortality | ✓ | ● | ● | ● | ● |
| Men BMI below normal (%) | Adult Nutrition (BMI) | ⚠ | ● | ● | ● | ● |
| Men comprehensive knowledge HIV/AIDS (%) | HIV/AIDS Knowledge | ✓ | ● | ● | ● | · |
| Men overweight/obese (%) | Adult Nutrition (BMI) | ✓ | ● | ● | ● | ● |
| Men who consume alcohol (%) | Tobacco & Alcohol | ✓ | ● | ● | ● | ● |
| Men who ever used the internet (%) | Education & Adults | ✓ | · | · | ● | ● |
| Men who use any tobacco (%) | Tobacco & Alcohol | ✓ | ● | ● | ● | ● |
| Mother received MCP card (%) | Maternal Health (ANC/Delivery/PNC) | ✓ | · | ● | ● | ● |
| Mother took IFA 100+ days (%) | Maternal Health (ANC/Delivery/PNC) | ✓ | ● | ● | ● | ● |
| Non-pregnant women anaemic (%) | Anaemia | ⚠ | ● | ● | ● | · |
| PNC for mother within 2 days (%) | Maternal Health (ANC/Delivery/PNC) | ✓ | ● | ● | ● | ● |
| Population below age 15 years (%) | Population & Household | ✓ | ● | ● | ● | ● |
| Pregnant women anaemic (%) | Anaemia | ⚠ | ● | ● | ● | · |
| Prevalence of ARI symptoms (%) | Childhood Diseases | ✓ | ● | ● | ● | ● |
| Prevalence of diarrhoea, last 2 weeks (%) | Childhood Diseases | ✓ | ● | ● | ● | ● |
| Sex ratio at birth, last 5 years (f per 1000 males) | Population & Household | ✓ | ● | ● | ● | · |
| Sex ratio of total population (f per 1000 males) | Population & Household | ✓ | ● | ● | ● | · |
| Total child 6-23m adequate diet (%) | Child Feeding & Nutrition | ⚠ | · | ● | ● | ● |
| Total fertility rate (children per woman) | Marriage, Fertility & Mortality | ✓ | ● | ● | ● | ● |
| Total unmet need for FP (%) | Family Planning | ✓ | ● | ● | ● | ● |
| Under-five mortality rate (per 1000) | Marriage, Fertility & Mortality | ✓ | ● | ● | ● | · |
| Unmet need for spacing (%) | Family Planning | ✓ | ● | ● | ● | ● |
| Women (15-49) who are literate (%) | Education & Adults | ✓ | ● | ● | ● | · |
| Women (15-49) with 10+ years schooling (%) | Education & Adults | ✓ | ● | ● | ● | ● |
| Women 15-19 already mothers/pregnant (%) | Marriage, Fertility & Mortality | ✓ | ● | ● | ● | ● |
| Women 15-24 hygienic menstrual protection (%) | Women's Empowerment & Violence | ✓ | · | ● | ● | ● |
| Women 20-24 married before age 18 (%) | Marriage, Fertility & Mortality | ✓ | ● | ● | ● | ● |
| Women BMI below normal (%) | Adult Nutrition (BMI) | ⚠ | ● | ● | ● | ● |
| Women comprehensive knowledge HIV/AIDS (%) | HIV/AIDS Knowledge | ✓ | ● | ● | ● | · |
| Women overweight/obese (%) | Adult Nutrition (BMI) | ✓ | ● | ● | ● | ● |
| Women owning house/land (%) | Women's Empowerment & Violence | ✓ | · | ● | ● | · |
| Women paid in cash for work (%) | Women's Empowerment & Violence | ✓ | ● | ● | ● | ● |
| Women who consume alcohol (%) | Tobacco & Alcohol | ✓ | ● | ● | ● | ● |
| Women who ever used the internet (%) | Education & Adults | ✓ | · | · | ● | ● |
| Women who use any tobacco (%) | Tobacco & Alcohol | ✓ | ● | ● | ● | ● |
| Women with own bank/savings account (%) | Women's Empowerment & Violence | ✓ | ● | ● | ● | ● |
| Women with own mobile phone (%) | Women's Empowerment & Violence | ✓ | · | ● | ● | ● |

## Comparability cautions

- **All women 15-49 anaemic (%)** — NFHS-6 measured haemoglobin from venous blood, whereas earlier rounds used capillary blood — anaemia levels are not directly comparable across rounds.
- **Breastfed child 6-23m adequate diet (%)** — Infant and young child feeding (adequate diet) definition was revised across rounds.
- **Child fully immunized/vaccinated (%)** — Vaccination schedule and the basis of measurement (card-only vs card-or-recall; DPT vs pentavalent) changed across rounds.
- **Child fully vaccinated (card or recall) (%)** — Vaccination schedule and the basis of measurement (card-only vs card-or-recall; DPT vs pentavalent) changed across rounds.
- **Children 6-59m anaemic (%)** — NFHS-6 measured haemoglobin from venous blood, whereas earlier rounds used capillary blood — anaemia levels are not directly comparable across rounds.
- **Ever-married women experienced spousal violence (%)** — Age base changed (ever-married 15-49 in earlier rounds vs 18-49 in NFHS-5/6).
- **FP: Any method (%)** — The set of methods counted under 'any/modern method' differs slightly across rounds.
- **FP: Any modern method (%)** — The set of methods counted under 'any/modern method' differs slightly across rounds.
- **Households using clean fuel for cooking (%)** — The classification of 'improved' source/facility and clean fuel was refined across rounds.
- **Households using improved sanitation facility (%)** — The classification of 'improved' source/facility and clean fuel was refined across rounds.
- **Households with improved drinking-water source (%)** — The classification of 'improved' source/facility and clean fuel was refined across rounds.
- **Married women participate in HH decisions (%)** — Definition of household decision-making (which/how many decisions) changed across rounds.
- **Men 15-49 anaemic (%)** — NFHS-6 measured haemoglobin from venous blood, whereas earlier rounds used capillary blood — anaemia levels are not directly comparable across rounds.
- **Men BMI below normal (%)** — Pregnant women and other exclusions in the BMI base differ across rounds.
- **Non-pregnant women anaemic (%)** — NFHS-6 measured haemoglobin from venous blood, whereas earlier rounds used capillary blood — anaemia levels are not directly comparable across rounds.
- **Pregnant women anaemic (%)** — NFHS-6 measured haemoglobin from venous blood, whereas earlier rounds used capillary blood — anaemia levels are not directly comparable across rounds.
- **Total child 6-23m adequate diet (%)** — Infant and young child feeding (adequate diet) definition was revised across rounds.
- **Women BMI below normal (%)** — Pregnant women and other exclusions in the BMI base differ across rounds.
