import streamlit as st
import pandas as pd

def render(df):
    st.subheader('结论与下一步')

    st.write("这里总结关键发现并提出下一步分析建议。")

    # 🔥🔥🔥 新增：前 20 游戏表格
    st.subheader("全球销量前 20 的游戏")

    top20 = df.sort_values('Global_Sales', ascending=False).head(20)
    st.dataframe(top20[['Name', 'Platform', 'Year', 'Genre', 'Publisher', 'Global_Sales']])
