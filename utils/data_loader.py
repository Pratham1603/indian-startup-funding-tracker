import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("final_funding_data.csv")
    
    # Clean columns
    df.columns = df.columns.str.strip().str.lower()
    
    # Convert amount
    df["amount_($m)"] = pd.to_numeric(df["amount_($m)"], errors="coerce")
    
    # Convert date
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    
    return df