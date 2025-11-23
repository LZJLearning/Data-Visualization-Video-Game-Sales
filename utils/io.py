import pandas as pd
import streamlit as st
from pathlib import Path

@st.cache_data(show_spinner=False)
def load_data() -> pd.DataFrame:
    path = Path('data/vgsales.csv')
    if not path.exists():
        st.error('数据文件未找到')
        return pd.DataFrame()
    df = pd.read_csv(path)
    df.columns = [c.strip().replace(' ', '_') for c in df.columns]
    if 'Year' in df.columns:
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    for col in ['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df
