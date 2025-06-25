
# 🏏 IPL 2024 Dashboard - Web Scraping and Data Pipeline Project

This project is an end-to-end data pipeline that scrapes, cleans, and prepares IPL 2024 data for visualization in a dashboard. It automates data extraction from ESPNcricinfo and processes everything—from match results and scorecards to player profiles and photos—so analysts and fans can explore rich insights from the tournament.

---

## 🚀 Project Purpose

The goal of this project is to create a robust, automated system to fetch IPL 2024 match data and player info from public sources, clean and structure it appropriately, and prepare it for downstream usage such as dashboards, reports, or analytics tools.

---

## ⚙️ How It Works

### 1. **Fetching Raw Match Data**
- **Script**: `web_scraping.py`
- Pulls the full IPL 2024 fixture and results page from ESPNcricinfo.
- Saves the page to `results.html` for offline processing and stability.

---

### 2. **Parsing Match Details**
- **Script**: `parsing.py`
- Reads `results.html`, extracts each match’s:
  - Winner
  - Loser
  - Margin
  - Match Date
  - Scorecard URL
- Results are saved into `results.csv` for structured access.

---

### 3. **Downloading Full Scorecards**
- **Script**: `scorecard_scrapping.py`
- Takes the scorecard URLs from `results.csv` and downloads the **full HTML** scorecard for each match.
- HTML files are saved in a `scorecard/` directory with a sequential naming format.

---

### 4. **Scraping Player Profile Links**
- **Script**: `players_scrapping.py`
- Parses each downloaded scorecard to extract **unique player profile URLs**.
- Cleans and deduplicates player names.
- Stores these links for the photo scraping step.

---

### 5. **Downloading Player Profile Pages**
- **Script**: `photos_scrapping.py`
- Uses rotating **proxies** and **random user-agents** to mimic human browsing.
- Fetches each player's ESPNcricinfo profile page and saves it locally to `players/`.

---

### 6. **Data Cleaning (Jupyter Notebook)**
- **Notebook**: `Data Cleaning.ipynb`
- Post-scraping, this notebook is used to:
  - Normalize formats
  - Clean inconsistencies
  - Prepare datasets for visual dashboards like Power BI, Tableau, or Plotly Dash.

---

## 🧠 Key Highlights

- 🌐 **Web scraping with anti-blocking techniques** (proxy rotation + random headers)
- 🧼 **Comprehensive data cleaning** for dashboard readiness
- 🧩 **Modular architecture** for scalable scraping and future automation
- 🗃️ All data saved locally, enabling reproducibility and offline access
- 📊 Integrates easily with frontend tools to create dashboards (like the one in `IPL 2024 Dashboard.pdf`)

---

## 📌 Final Output

The final result is a polished IPL 2024 data dashboard (refer to `IPL 2024 Dashboard.pdf`) that provides:
- Match outcomes
- Winning margins
- Player stats & photos
- Timeline-based insights

---

## 🧪 Future Improvements

- Automate with scheduling (e.g., using `cron` or `Airflow`)
- Add error handling and logging
- Include real-time updates and alerts
- Expand to fantasy stats and player comparisons

---
