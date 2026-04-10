import streamlit as st
from utils.data_loader import load_data

st.title("🏆 Leaderboard")

df = load_data()

top_companies = df.groupby("company")["amount_($m)"].sum().sort_values(ascending=False).head(10)

st.subheader("Top Funded Companies")
st.dataframe(top_companies)