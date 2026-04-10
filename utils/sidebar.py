import streamlit as st

def show_sidebar():
    # Hide default nav
    st.markdown("""
        <style>
        [data-testid="stSidebarNav"] { display: none; }
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.title("Indian Startup Funding Tracker")
    st.sidebar.caption("Updated weekly · 2024 onwards")
    st.sidebar.divider()

    # Custom nav
    st.sidebar.page_link("app.py",            label="🏠 Home")
    st.sidebar.page_link("pages/1_Search.py", label="🔍 Search")
    st.sidebar.page_link("pages/2_Explore.py",label="🌍 Explore")
    st.sidebar.page_link("pages/3_Charts.py", label="📊 Charts")
    st.sidebar.page_link("pages/4_Leaderboard.py", label="🏆 Leaderboard")

    st.sidebar.divider()