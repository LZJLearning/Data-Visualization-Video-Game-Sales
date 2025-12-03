import streamlit as st
import pandas as pd
from utils.io import load_data
from utils.prep import make_tables, apply_filters, data_quality_report
from sections import intro, overview, deep_dives, conclusions

# Page Configuration
st.set_page_config(page_title="Video Game Sales — Streamlit App", layout="wide")

# sider bule
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #E3F2FD; }
    </style>
     """, unsafe_allow_html=True)

# title and source
st.title("🎮 Video Game Sales — Streamlit App")
st.caption("Source: vgsales.csv | https://www.kaggle.com/datasets/gregorut/videogamesales")

# Down
@st.cache_data(show_spinner=False)
def get_tables():
    df = load_data()
    tables = make_tables(df)
    return df, tables

raw_df, tables = get_tables()
filtered_df_for_deep = apply_filters(raw_df, years=(1980, 2016))
filtered_tables_for_deep = make_tables(filtered_df_for_deep)

# sidebar
with st.sidebar:
    st.image("assets/EFREI-logo.png")
    st.image("assets/WUT-Logo.png")
    st.markdown("**Course: Data Visualization 2025**")
    st.markdown("**Professor:  Mano Mathew**")
    st.markdown("**Email:  mano.mathew@efrei.fr**")
    st.markdown("[Check out this LinkedIn](https://www.linkedin.com/in/manomathew/)", unsafe_allow_html=True)
    st.markdown("**Author:  ZIJIAN LIANG**")
    st.markdown("**Email:  zijian.liang@efrei.net**")
    #GitHub
    st.markdown("""
        <a href="https://github.com/LZJLearning/Data-Visualization-Video-Game-Sales/tree/Dev" target="_blank">
            <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/github.svg"
                 width="40" style="margin: 0 auto; display: block;">
        </a>
        """,unsafe_allow_html=True)

# py
intro.render(raw_df)
overview.render(raw_df)
deep_dives.render(filtered_df_for_deep, filtered_tables_for_deep)
conclusions.render(raw_df)

# Data Quality
st.markdown("### Data Quality")
quality_report = data_quality_report(raw_df)

missing = quality_report['missing'].copy()
missing['missing_ratio'] = (missing['missing_ratio'] * 100).round(2).astype(str) + '%'

st.write("Missing ratio:")
st.dataframe(missing)

# Data Before / After Table
st.markdown("### Comparison before and after cleaning")
rows_before = int(raw_df.shape[0])
rows_after = int(filtered_tables_for_deep.get("raw", raw_df).shape[0])
loss_ratio = (rows_before - rows_after) / rows_before * 100 

compare_df = pd.DataFrame({
    "Number of pre cleaning steps": [rows_before],
    "Number after cleaning": [rows_after],
    "Loss ratio (%)": [round(loss_ratio, 2)]
})
st.dataframe(compare_df)

st.write("Finally, there is data cleaning. The table below shows that the loss ratio of the dataset is 1.66%, show that the reliability of the data itself.")
st.write("If you want to learn more about my data visualization, you can download it from my GitHub.")
st.write("🎉 🎉 🎉 Thank you for watch!")