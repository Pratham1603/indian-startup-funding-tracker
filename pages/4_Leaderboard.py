import streamlit as st
from utils.data_loader import load_data
from utils.sidebar import show_sidebar
show_sidebar()

st.title("🏆 Leaderboard")

df = load_data()

top_companies = df.groupby("company")["amount_($m)"].sum().sort_values(ascending=False).head(40)

st.subheader("Top Funded Companies")
st.table(top_companies)