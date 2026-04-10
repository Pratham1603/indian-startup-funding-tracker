import streamlit as st
from utils.data_loader import load_data

st.title("🌍 Explore Data")

df = load_data()

# 🔥 Clean + sort sector
sector_list = sorted(
    df["sector"]
    .dropna()
    .str.strip()
    .unique()
)

# 🔥 Clean + sort series
series_list = sorted(
    df["series"]
    .dropna()
    .str.strip()
    .unique()
)

# Dropdowns
sector = st.multiselect(
    "Select Sector",
    sector_list,
    default=[]
)

series = st.multiselect(
    "Select Series",
    series_list,
    default=[]
)

# Filtering
filtered = df.copy()

if sector and "All" not in sector:
    filtered = filtered[
        filtered["sector"].astype(str).str.strip().isin(sector)
    ]

if series and "All" not in series:
    filtered = filtered[
        filtered["series"].astype(str).str.strip().isin(series)
    ]


filtered = filtered.sort_values(by="amount_($m)", ascending=False)

# Output
st.dataframe(filtered)