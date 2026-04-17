# 🏏 IPL Data Analysis

An in-depth Exploratory Data Analysis (EDA) of the Indian Premier League (IPL) — one of the world's biggest cricket tournaments — using Python and Jupyter Notebook. This project uncovers patterns in match outcomes, player performances, team dominance, toss decisions, and venue statistics across multiple IPL seasons.

---

## 📌 Project Overview

The Indian Premier League generates a goldmine of cricket data across every ball, wicket, and run. This project explores that data to answer questions like:

- Which teams have been the most dominant across IPL seasons?
- Which batters and bowlers have had the greatest impact?
- Does winning the toss actually influence match results?
- Which venues favour batting or bowling sides?
- How do run rates and scoring patterns differ across seasons?

---

## 📁 Repository Structure

```
IPL-Data-Analysis/
└── IPL Data Analysis/
    ├── matches.csv          # Match-level data (result, toss, venue, teams, winner)
    ├── deliveries.csv       # Ball-by-ball data (runs, wickets, bowler, batsman)
    ├── IPL_Analysis.ipynb   # Main Jupyter Notebook with full EDA
    └── visuals/             # Exported charts and plots
```

---

## 🔧 Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.x** | Core programming language |
| **Pandas** | Data loading, cleaning, and aggregation |
| **NumPy** | Numerical computations |
| **Matplotlib** | Plotting and chart generation |
| **Seaborn** | Statistical visualizations |
| **Jupyter Notebook** | Interactive analysis environment |

---

## 🔍 Key Analyses Performed

### 🧹 Data Cleaning & Preprocessing
- Handled null values in player, venue, and result columns
- Standardised team names across seasons (franchise renaming over the years)
- Merged `matches.csv` and `deliveries.csv` for ball-level match context
- Parsed season/year from match date fields

### 🏆 Team Performance Analysis
- Most matches won per team across all seasons
- Season-by-season championship breakdown
- Win percentage by team — home vs. away
- Head-to-head records between rival franchises

### 🪙 Toss Analysis
- Toss win vs. match win correlation
- Preferred toss decisions (bat/field) by team and venue
- Impact of toss decision on match outcome percentage

### 🏟️ Venue & Ground Analysis
- Stadiums with the highest average first-innings scores
- Venues most favourable to chasing teams
- City-wise match distribution across seasons

### 🏏 Batting Analysis
- Top run-scorers across all IPL seasons
- Highest strike rates among batters (min. threshold for qualification)
- Most sixes and fours hit — overall and season-wise
- Orange Cap holders per season

### 🎳 Bowling Analysis
- Top wicket-takers across all IPL seasons
- Best economy rates among bowlers
- Most dot balls bowled
- Purple Cap holders per season

### 📊 Visualizations Produced
- Bar charts — top run-scorers, wicket-takers, and title winners
- Heatmaps — team vs. team win matrix; toss decision by venue
- Line charts — average match scores across seasons
- Pie/donut charts — toss decision breakdown (bat vs. field)
- Count plots — dismissal types, match results by margin

---

## 📈 Key Insights

- **Mumbai Indians** have won the most IPL titles, establishing themselves as the most successful franchise
- Toss winners choose to **field first** the majority of the time in recent seasons, reflecting a preference for chasing
- **Wankhede Stadium (Mumbai)** and **Eden Gardens (Kolkata)** are among the highest-scoring venues
- A handful of elite all-rounders consistently appear in both top batting and top bowling lists
- Average first-innings scores have risen steadily across seasons, reflecting T20's evolving batting depth
- The **death overs (16–20)** account for a disproportionate share of boundaries and sixes

---

## 🚀 Getting Started

### Prerequisites

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Running the Analysis

1. **Clone the repository**

```bash
git clone https://github.com/AADITYA-NAHAR-JAIN/IPL-Data-Analysis.git
cd IPL-Data-Analysis/IPL\ Data\ Analysis
```

2. **Launch Jupyter Notebook**

```bash
jupyter notebook
```

3. Open `IPL_Analysis.ipynb` and run all cells to reproduce the full analysis.

---

## 📦 Dataset

The project uses the popular **IPL dataset** available on [Kaggle](https://www.kaggle.com/datasets/nowke9/ipldata), containing data from IPL Season 1 (2008) onwards:

| File | Description |
|------|-------------|
| `matches.csv` | One row per match — teams, toss, venue, winner, result margin |
| `deliveries.csv` | One row per ball — batsman, bowler, runs, extras, wicket info |

---

## 🤝 Contributing

Contributions and new analyses are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-analysis`)
3. Commit your changes (`git commit -m 'Add player form analysis'`)
4. Push to the branch (`git push origin feature/new-analysis`)
5. Open a Pull Request

---

## 👤 Author

**Aaditya Nahar Jain**
- GitHub: [@AADITYA-NAHAR-JAIN](https://github.com/AADITYA-NAHAR-JAIN)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
