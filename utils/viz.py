import streamlit as st
import altair as alt
import pandas as pd
import time
import numpy as np

def line_chart_timeseries(df, x, y, title=""):
    chart = alt.Chart(df).mark_line(point=True).encode(
        x=x,
        y=y,
        tooltip=[x, y]
    ).properties(title=title)
    st.altair_chart(chart, use_container_width=True)

def single_region_line_chart(df, title=""):
    chart = alt.Chart(df).mark_line(point=True).encode(
        x='Year',
        y='Regional_Sales',
        tooltip=['Year', 'Regional_Sales']
    ).properties(title=title)
    st.altair_chart(chart, use_container_width=True)
   
def pie_chart_region_share(df, title=""):
    # df 需要包含: Region, Regional_Sales
    chart = alt.Chart(df).mark_arc(innerRadius=0).encode(
        theta='Regional_Sales',
        color='Region',
        tooltip=['Region', 'Regional_Sales']
    ).properties(title=title)
    st.altair_chart(chart, use_container_width=True)

def bubble_chart_frame(df, title):
    """
    绘制某一帧气泡图（不渲染，返回 chart 对象）
    df 需要包含: Year, Region, Regional_Sales, Global_Sales_Year
    """
    chart = alt.Chart(df).mark_circle(opacity=0.8).encode(
        x='Regional_Sales',      # 横轴：该年该地区销量
        y='Global_Sales_Year',   # 纵轴：该年全球总销量
        size='Regional_Sales',   # 气泡大小：该年该地区销量
        color='Region',          # 颜色区分地区
        tooltip=['Region', 'Year', 'Regional_Sales', 'Global_Sales_Year']
    ).properties(title=title)
    return chart

def heatmap_genre_platform(df, title=""):
    heat_df = df.groupby(['Genre', 'Platform'], as_index=False)['Global_Sales'].sum()
    
    color_scale = alt.Scale(
        range=["#8B0000", "#FFC0CB"]  # 黑 → 亮红（低 → 高
    )

    chart = alt.Chart(heat_df).mark_rect().encode(
        x='Platform',
        y='Genre',
        color=alt.Color('Global_Sales', scale=color_scale, title='全球销量'),
        tooltip=['Genre', 'Platform', 'Global_Sales']
    ).properties(title=title, width=600, height=400)
    st.altair_chart(chart, use_container_width=True)

def scatter_publisher_sales(df, title='Publisher 对全球销量的影响（每点=一款游戏）'):
    # 取销量最高的前 20 个发布商
    top_publishers = (df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(20).index.tolist())
    
    dist = df[df['Publisher'].isin(top_publishers)].copy()
    dist = dist.dropna(subset=['Publisher', 'Global_Sales'])

    chart = alt.Chart(dist).mark_circle(size=60, opacity=0.7).encode(
        x='Publisher',y='Global_Sales',
        color='Genre',
        tooltip=['Name','Publisher','Platform','Genre',
            alt.Tooltip('Global_Sales', format='.2f')
            ]
    ).properties(height=350,title=title)

    st.altair_chart(chart, use_container_width=True)