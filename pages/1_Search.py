import streamlit as st
import pandas as pd
from utils.data_loader import load_data

st.title("🔍 Search Company")

df = load_data()

# Clean data
df["company"] = df["company"].astype(str).str.strip()
df["sector"] = df["sector"].astype(str).str.strip()
df["series"] = df["series"].astype(str).str.strip()
df["hq"] = df["hq"].astype(str).str.strip()

# Dropdown search
company_list = sorted(df["company"].dropna().unique())

selected_company = st.selectbox(
    "Select or search company",
    [""] + company_list
)

if selected_company:

    result = df[df["company"] == selected_company]

    if not result.empty:

        # 🔥 KPIs
        total_funding = result["amount_($m)"].sum()
        deals = result.shape[0]
        avg_funding = result["amount_($m)"].mean()
        latest_round = result.sort_values(by="date", ascending=False).iloc[0]

        st.markdown(f"## 🏢 {selected_company}")
        st.markdown("---")

        # KPI Cards
        col1, col2, col3 = st.columns(3)

        col1.metric("💰 Total Funding ($M)", f"{total_funding:.2f}")
        col2.metric("📄 Total Deals", deals)
        col3.metric("📊 Avg Deal ($M)", f"{avg_funding:.2f}")

        st.markdown("### 📌 Company Overview")

        col4, col5 = st.columns(2)

        col4.write(f"**🏭 Sector:** {latest_round['sector']}")
        col4.write(f"**📍 HQ:** {latest_round['hq']}")

        col5.write(f"**🚀 Latest Round:** {latest_round['series']}")
        col5.write(f"**📅 Last Funding Date:** {latest_round['date'].date()}")

        st.markdown("---")

        # 🔥 Funding Timeline (Text Based)
        st.markdown("### 📈 Funding History")

        for _, row in result.sort_values(by="date", ascending=False).iterrows():

            with st.container():
                st.markdown(
                    """
                    <div style='border:1px solid #444; border-radius:10px; padding:10px; margin-bottom:10px;'>
                    """,
                    unsafe_allow_html=True
                )

                col1, col2 = st.columns([3, 2])

                # LEFT SIDE
                with col1:
                    st.markdown(f"🔹 **{row['series']} round**")
                    st.markdown(f"💰 ${row['amount_($m)']}M")

                # RIGHT SIDE
                with col2:
                    st.markdown(f"📅 {row['date'].date()}")
                    st.markdown(f"📍 {row['hq']}")

                st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.warning("No data found for this company")