import streamlit as st

# Set the page title
st.set_page_config(page_title="Power BI Dashboard", layout="wide")

# Title of the app
st.title("Embedded Power BI Report")

# Embed Power BI using an iframe
power_bi_url = "https://iareacin-my.sharepoint.com/personal/23955a6715_iare_ac_in/_layouts/15/embed.aspx?UniqueId=35f25a83-2056-4842-b278-6df19544629a"

st.markdown(
    f"""
    <iframe src="{power_bi_url}" width="100%" height="600" frameborder="0" allowfullscreen></iframe>
    """,
    unsafe_allow_html=True
)

# Footer
st.markdown("Powered by Streamlit")
