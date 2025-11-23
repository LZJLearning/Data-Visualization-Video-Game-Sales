import pandas as pd
import streamlit as st
from pathlib import Path

@st.cache_data(show_spinner=False)
def load_data():
    df = pd.read_csv('data/vgsales.csv')
    df.columns = [c.strip().replace(' ', '_') for c in df.columns]
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    for col in ['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df
