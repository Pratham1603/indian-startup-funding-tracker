import streamlit as st

# Page config
st.set_page_config(
    page_title="Indian Startup Funding Tracker",
    layout="wide"
)

# 🔥 Center content using columns
left, center, right = st.columns([1, 2, 1])

with center:
    # Title
    st.markdown(
        "<h1 style='text-align: center;'>Indian Startup Funding Tracker</h1>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    # Subtitle
    st.markdown(
        "<h4 style='text-align: center;'>Analyze Startup Funding Trends in India</h4>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Navigation Guide
    st.markdown(
        """
        <div style='display: flex; justify-content: center;'>
            <table style='font-size:18px;'>
                <tr>
                    <td>🔍</td>
                    <td><b>Search</b></td>
                    <td>– Find specific companies</td>
                </tr>
                <tr>
                    <td>🌍</td>
                    <td><b>Explore</b></td>
                    <td>– Filter by sector & funding stage</td>
                </tr>
                <tr>
                    <td>📊</td>
                    <td><b>Charts</b></td>
                    <td>– Visual insights</td>
                </tr>
                <tr>
                    <td>🏆</td>
                    <td><b>Leaderboard</b></td>
                    <td>– Top funded startups</td>
                </tr>
            </table>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Footer
    st.markdown(
        "<p style='text-align: center; color: gray; font-size:14px;'>Built with ❤️ by <b>Pratham Harer</b></p>",
        unsafe_allow_html=True
    )