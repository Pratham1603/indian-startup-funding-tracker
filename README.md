<h1 align="center">🇮🇳 Indian Startup Funding Tracker</h1>

---

<h2 align="center">Interactive Dashboard for Tracking Indian Startup Funding Trends</h2>

---

## 📌 Project Overview

Indian Startup Funding Tracker is a data-driven Streamlit web application designed to monitor and analyze startup funding activity across India from 2024 onwards.

The goal of this project is to transform raw funding data into actionable insights through an intuitive, interactive dashboard.

It enables users to explore funding rounds, identify high-growth sectors, track weekly investment trends, and discover top-funded startups — all in one place.

---

## 📈 Application Preview

### 🔍 Search Interface  
![App Preview](images/search.png)

### 🎛️ Explore & Filter  
![App Preview](images/explore.png)

### 📊 Charts & Trends  
![App Preview](images/charts.png)

### 🏆 Leaderboard  
![App Preview](images/leaderboard.png)

---

## 🎯 Problem Statement

Startup funding data is scattered across multiple news sources and platforms, making it difficult to:

* Track funding trends over time  
* Identify top-performing sectors  
* Analyze investment stages (Seed, Series A, etc.)  
* Discover high-growth startups  

The challenge was to:

* Build a centralized dataset of funding rounds  
* Enable fast and flexible filtering  
* Provide meaningful visual insights  
* Create a clean and scalable data exploration interface  

This project solves these problems by converting fragmented funding data into a structured analytical platform.

---

## 📊 Dataset

* **Format:** `.csv` (Exported from Notion)
* **Type:** Structured tabular dataset
* **Coverage:** Indian startup funding rounds (2024 → present)
* **Update Frequency:** Weekly
* **Source:** Public news articles

### Data Schema

| Column | Description |
|---|---|
| `company_name` | Startup name |
| `amount_usd` | Funding amount (in USD millions) |
| `series` | Funding stage (Seed, Pre-A, A, B, etc.) |
| `sector` | Industry sector |
| `headquarters` | Location (City/State) |
| `date` | Funding announcement date |
| `source_url` | News source link |

---

## ⚙️ Tools & Technologies Used

* **Python** – Core programming language  
* **Pandas** – Data cleaning and transformation  
* **Plotly** – Interactive visualizations  
* **Matplotlib** – Static chart rendering  
* **RapidFuzz** – Fuzzy search implementation  
* **Streamlit** – Multi-page web application framework  
* **Notion API (Optional)** – Automated data syncing  

---

## 🧱 Workflow Architecture
Notion Database / CSV
↓
Data Cleaning & Preprocessing
↓
Search & Filtering Engine
↓
Aggregation & Grouping (Sector / Series / Date)
↓
Visualization Layer (Charts & Trends)
↓
Interactive Dashboard (Streamlit)

---
