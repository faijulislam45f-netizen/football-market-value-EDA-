# Football Player Market Value EDA (2010-2026)

## Overview
Exploratory Data Analysis on 1,025 records of top football players'
market values spanning 2010 to 2026. Built using Python, Pandas, and
Plotly Express to uncover patterns in player valuation, peak age,
position-based trends, and career decline.

---

## Dataset
| Detail | Info |
|--------|------|
| Source | Kaggle — Global Football Transfer Market 2010-2026 |
| File | player_market_values.csv |
| Rows | 1,025 |
| Columns | 6 |

**Columns:** `year`, `player_name`, `age`, `position`, `market_value_eur_m`, `is_peak_year`

---

## Key Findings

### 1. Messi vs Ronaldo Market Value Trajectory
- Ronaldo peaked at ~150M EUR in 2014 at age 29
- Messi peaked at ~230M EUR in 2019 at age 32
- Messi reached 80M EUR higher than Ronaldo's peak
- Both declined sharply post-2020 due to age factor

### 2. Position-wise Average Market Value
- RW (Right Winger) highest avg ~59M EUR
- GK (Goalkeeper) lowest avg ~18M EUR
- Attacking positions dominate market valuation

### 3. Peak Age Analysis
- Average peak age: **23.9 years**
- 86 out of 1,025 records marked as peak year
- Peak window: **23 to 27 years**

### 4. Market Value Decline After Age 28
- Age 28: ~57M EUR average
- Age 30: drops to ~30M EUR
- Age 36: drops to ~8M EUR
- Confirms the "football cliff" pattern post-30

### 5. Top 10 Players by Peak Market Value
- Lionel Messi — ~230M EUR
- Vinicius Jr — ~210M EUR
- Lamine Yamal — entered top 10 at age 16-17

---
## Visualizations
| File | Description |
|------|-------------|
| fig1_messi_ronaldo.png | Messi vs Ronaldo value trajectory (2010-2026) |
| fig2_position.png | Average market value by playing position |
| fig3_peak_age.png | Age distribution at peak market value |
| fig4_peak_age.png | Market value decline after age 28 |
| fig5_top10.png | Top 10 players by peak market value |

---

## Tools Used
- Python 3
- Pandas
- Plotly Express
- Kaleido (PNG export)
