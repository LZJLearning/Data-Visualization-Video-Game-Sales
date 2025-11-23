import streamlit as st
from io import StringIO

def render(df):
    st.header("引言")
    st.write("这是一个关于游戏销售的数据集")
    buf=StringIO()
    df.info(buf=buf)
    st.subheader("数据集结构（df.info()）")
    st.code(buf.getvalue())
