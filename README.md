# 🇮🇳 Indian Startup Funding Tracker

A Streamlit dashboard that tracks Indian startup funding rounds from 2024 onwards — updated weekly. Search companies, filter by sector and series, explore trends, and find the most-funded startups across industries.

---

## 🚀 Features

- 🔍 **Search** — fuzzy search by company name
- 🎛️ **Filter** — by sector, funding series, amount range, and date
- 📊 **Charts** — sector-wise funding, weekly trends, series distribution
- 🏆 **Leaderboard** — top funded companies with news source links
- 📥 **Export** — download filtered results as CSV

---

## 🗂️ Project Structure

```
indian-startup-funding-tracker/
│
├── app.py                  # Main Streamlit entry point
├── data/
│   └── funding_data.csv    # Exported Notion table (updated weekly)
├── pages/
│   ├── 1_Search.py         # Company search & detail card
│   ├── 2_Explore.py        # Filter + sortable table
│   ├── 3_Charts.py         # Visual analytics
│   └── 4_Leaderboard.py    # Top funded companies
├── utils/
│   └── data_loader.py      # Cached data loading & preprocessing
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Streamlit | App framework |
| pandas | Data manipulation |
| plotly | Interactive charts |
| rapidfuzz | Fuzzy company name search |
| Notion API *(optional)* | Live data sync |

---

## ⚡ Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/indian-startup-funding-tracker.git
cd indian-startup-funding-tracker

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your data
# Export your Notion table as CSV → save to data/funding_data.csv

# 4. Run the app
streamlit run app.py
```

---

## 📋 Data Schema

| Column | Description |
|---|---|
| `company_name` | Name of the startup |
| `amount_usd` | Funding amount in USD (millions) |
| `series` | Funding stage (Seed, Pre-A, A, B, C, etc.) |
| `sector` | Industry sector |
| `headquarters` | City / State |
| `date` | Date of funding announcement |
| `source_url` | News article link |

---

## 📅 Data Updates

Data is sourced from public news and updated weekly. Original tracking started January 2024.

---

## 🙌 Contributing

PRs welcome! If you find a missing funding round, feel free to open an issue.

---

## 📬 Connect

Built by [@YOUR_TWITTER](https://twitter.com/YOUR_TWITTER) as part of a public ML/data learning journey.
