import streamlit as st
import matplotlib.pyplot as plt
from utils.data_loader import load_data

st.title("📊 Charts")

df = load_data()

# Funding by sector
sector_data = df.groupby("sector")["amount_($m)"].sum().sort_values(ascending=False)

fig, ax = plt.subplots()
sector_data.head(10).plot(kind="bar", ax=ax)
ax.set_title("Top Sectors by Funding")

st.pyplot(fig)