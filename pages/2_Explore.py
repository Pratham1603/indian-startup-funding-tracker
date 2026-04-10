import streamlit as st
import pandas as pd
from utils.data_loader import load_data

st.set_page_config(layout="wide")

# 🔥 CENTER LAYOUT
left, center, right = st.columns([1, 2, 1])

with center:

    st.title("🌍 Explore Data")

    df = load_data()

    # ✅ Clean columns
    df["sector"] = df["sector"].astype(str).str.strip()
    df["series"] = df["series"].astype(str).str.strip()

    # 🔍 Filters
    st.markdown("### 🔍 Filters")

    col1, col2 = st.columns(2)

    with col1:
        sector_list = sorted(df["sector"].dropna().unique())
        sector = st.multiselect("Select Sector", sector_list)

    with col2:
        series_list = sorted(df["series"].dropna().unique())
        series = st.multiselect("Select Series", series_list)

    # 💰 Amount filter
    min_amt, max_amt = int(df["amount_($m)"].min()), int(df["amount_($m)"].max())

    amount_range = st.slider(
        "Select Funding Range ($M)",
        min_value=min_amt,
        max_value=max_amt,
        value=(min_amt, max_amt)
    )

    # 🔥 FILTERING LOGIC
    filtered = df.copy()

    if sector:
        filtered = filtered[filtered["sector"].isin(sector)]

    if series:
        filtered = filtered[filtered["series"].isin(series)]

    filtered = filtered[
        (filtered["amount_($m)"] >= amount_range[0]) &
        (filtered["amount_($m)"] <= amount_range[1])
    ]

    # 🔽 Sort
    filtered = filtered.sort_values(by="amount_($m)", ascending=False)

    # ✅ CONDITION: show full UI only if filters selected
    show_full = bool(sector or series)

    # 🔥 SUMMARY (only when filters applied)
    if show_full:
        st.markdown("### 📊 Summary")

        col3, col4, col5 = st.columns(3)

        total_funding = filtered["amount_($m)"].sum()
        total_deals = filtered.shape[0]
        avg_funding = filtered["amount_($m)"].mean() if total_deals > 0 else 0

        col3.metric("💰 Total Funding ($M)", f"{total_funding:,.2f}")
        col4.metric("📄 Deals", total_deals)
        col5.metric("📊 Avg Deal ($M)", f"{avg_funding:,.2f}")

        st.markdown("---")
    else:
        st.info("👆 Apply Sector or Series filter to explore data")

    # 🔥 COMPANY SECTION
    st.markdown("### 🏢 Companies")

    company_list = filtered["company"].unique()
    st.write(f"Total Companies: {len(company_list)}")

    # 👉 Show names only when filters applied
    if show_full:
        st.write(company_list)

    # 🔥 DETAILED TABLE
    if show_full:
        st.markdown("---")
        st.markdown("### 📋 Detailed Results")

        filtered1 = filtered[["company", "amount_($m)", "date", "sector", "series", "hq"]].copy()

        # 👉 Fix date format
        filtered1["date"] = pd.to_datetime(filtered1["date"]).dt.date

        # 👉 Fix index
        filtered1 = filtered1.reset_index(drop=True)
        filtered1.index = filtered1.index + 1

        st.dataframe(
            filtered1,
            use_container_width=True,
            height=400
        )

        # 🔥 DOWNLOAD BUTTON
        csv = filtered1.to_csv(index=False).encode('utf-8')

        st.download_button(
            "⬇️ Download CSV",
            csv,
            "filtered_data.csv",
            "text/csv"
        )