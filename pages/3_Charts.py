import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from utils.data_loader import load_data

st.set_page_config(layout="wide")

st.title("📊 Advanced Funding Analytics")

df = load_data()

# -----------------------------
# 🧹 CLEAN DATA
# -----------------------------
df["sector"] = df["sector"].astype(str).str.strip()
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# -----------------------------
# 🔍 FILTERS
# -----------------------------
st.sidebar.header("🔍 Filters")

top_n = st.sidebar.slider("Top N Sectors", 5, 20, 10)

# -----------------------------
# 📊 1. TOP SECTORS BAR CHART
# -----------------------------
st.subheader("🏆 Top Sectors by Funding")

sector_data = (
    df.groupby("sector")["amount_($m)"]
    .sum()
    .sort_values(ascending=False)
    .head(top_n)
)

fig1, ax1 = plt.subplots(figsize=(6, 5))
sector_data.plot(kind="barh", ax=ax1)

ax1.set_title("Top Sectors by Funding ($M)")
ax1.set_xlabel("Funding ($M)")
ax1.set_ylabel("Sector")
ax1.invert_yaxis()
ax1.yaxis.set_label_position("right")
ax1.yaxis.tick_right()

st.pyplot(fig1)

# -----------------------------
# 📈 2. FUNDING TREND OVER TIME
# -----------------------------
st.subheader("📈 Funding Trend Over Time")

time_data = (
    df.dropna(subset=["date"])
    .groupby(df["date"].dt.to_period("M"))["amount_($m)"]
    .sum()
)

time_data.index = time_data.index.astype(str)

fig2, ax2 = plt.subplots(figsize=(15, 4))
time_data.plot(ax=ax2)

ax2.set_title("Monthly Funding Trend")
ax2.set_xlabel("Month")
ax2.set_ylabel("Funding ($M)")

# show every label as "Jan 2024" format
labels = [f"{idx[:4]}\n{idx[5:]}" for idx in time_data.index]  # year on top, month below
ax2.set_xticks(range(len(time_data)))
ax2.set_xticklabels(labels, fontsize=7)
ax2.tick_params(axis='x', rotation=45)

st.pyplot(fig2)

# -----------------------------
# 🥧 3. SECTOR DISTRIBUTION (PIE)
# -----------------------------
st.subheader("🥧 Sector Distribution")

sector_counts = df["sector"].value_counts().head(top_n)

fig3, ax3 = plt.subplots(figsize=(7, 7))
wedges, texts, autotexts = ax3.pie(
    sector_counts,
    labels=sector_counts.index,
    wedgeprops=dict(width=0.5),
    startangle=140,
    autopct="%1.1f%%",
    pctdistance=0.75,
    labeldistance=1.15      # pushes names outside the ring
)

for text in texts:
    text.set_fontsize(7)

for text in autotexts:
    text.set_fontsize(7)

ax3.set_title("Sector Share")

st.pyplot(fig3)
# -----------------------------
# 🏢 4. TOP COMPANIES
# -----------------------------
st.subheader("🏢 Top Companies by Funding")

company_data = (
    df.groupby("company")["amount_($m)"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig4, ax4 = plt.subplots()
company_data.plot(kind="barh", ax=ax4)

ax4.set_title("Top 10 Companies")
ax4.set_xlabel("Funding ($M)")

st.pyplot(fig4)