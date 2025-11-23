import streamlit as st
import altair as alt
import pandas as pd
import time
import numpy as np
import plotly.express as px

def line_chart_timeseries(df, x, y, title):
    chart = alt.Chart(df).mark_line(point=True).encode(
        x=x,
        y=y,
        tooltip=[x, y]
    ).properties(title=title)
    st.altair_chart(chart, use_container_width=True)

def single_region_line_chart(df, title):
    chart = alt.Chart(df).mark_line(point=True).encode(
        x='Year',
        y='Regional_Sales',
        tooltip=['Year', 'Regional_Sales']
    ).properties(title=title)
    st.altair_chart(chart, use_container_width=True)
   
def pie_chart_region_share(df, title):
    total_sales = df['Regional_Sales'].sum()
    df['percent'] = (df['Regional_Sales'] / total_sales * 100).round(2)

    chart = alt.Chart(df).mark_arc(innerRadius=0).encode(
        theta='Regional_Sales',
        color='Region',
        tooltip=['Region', 'Regional_Sales','percent']
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

def heatmap_genre_platform(df, title):
    heat_df = df.groupby(['Genre', 'Platform'], as_index=False)['Global_Sales'].sum()
    
    color_scale = alt.Scale(
        range=["#8B0000", "#FFC0CB"]  # 黑 → 亮红（低 → 高)
    )

    chart = alt.Chart(heat_df).mark_rect().encode(
        x='Platform',
        y='Genre',
        color=alt.Color('Global_Sales', scale=color_scale, title='全球销量'),
        tooltip=['Genre', 'Platform', 'Global_Sales']
    ).properties(title=title, width=600, height=400)
    st.altair_chart(chart, use_container_width=True)

def scatter_publisher_sales(df, title):
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

def region_sales_choropleth_map(region_share, raw_df):

    # --- 区域国家列表 ---
    NA = ["United States", "Canada"]
    EU = [
        "United Kingdom", "Germany", "France", "Italy", "Spain", "Netherlands",
        "Belgium", "Sweden", "Poland", "Austria", "Finland", "Denmark",
        "Portugal", "Greece", "Czechia", "Hungary", "Ireland"
    ]
    JP = ["Japan"]

    # --- 销量字典 ---
    sales_dict = region_share.set_index("Region")["Regional_Sales"].to_dict()

    # --- 世界国家基本数据 ---
    world_df = px.data.gapminder().query("year == 2007")[["country", "iso_alpha"]]

    # 默认全部 Other
    world_df["Region"] = "Other"

    # 批量覆盖 NA/EU/JP
    world_df.loc[world_df["country"].isin(NA), "Region"] = "NA"
    world_df.loc[world_df["country"].isin(EU), "Region"] = "EU"
    world_df.loc[world_df["country"].isin(JP), "Region"] = "JP"

    # 根据 Region 映射销量
    world_df["Sales"] = world_df["Region"].map(sales_dict)

    sales_cols = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
    genre_melt = raw_df.melt(
    id_vars=["Genre"],
    value_vars=sales_cols,
    var_name="Region",
    value_name="Sales"
     )
    genre_melt["Region"] = genre_melt["Region"].map({
    "NA_Sales": "NA",
    "EU_Sales": "EU",
    "JP_Sales": "JP",
    "Other_Sales": "Other"
     })
    top_genre_df = (
    genre_melt.groupby(["Region", "Genre"])["Sales"]
    .sum()
    .reset_index()
     )
    top_genre_df = top_genre_df.loc[
    top_genre_df.groupby("Region")["Sales"].idxmax()
     ][["Region", "Genre"]].rename(columns={"Genre": "Top_Genre"})

    world_df = world_df.merge(top_genre_df, on="Region", how="left")

    fig = px.choropleth(
        world_df,
        locations="iso_alpha",
        color="Region",
        hover_name="country",
        hover_data={"Sales": True,"Top_Genre": True},
        color_discrete_map={
            "NA": "#1f77b4",
            "EU": "#2ca02c",
            "JP": "#d62728",
            "Other": "#9467bd",
        },
        title="Regional Sales Map (Other = all regions except NA/EU/JP)"
    )

    fig.update_layout(height=600, margin=dict(l=0, r=0, t=50, b=0))
    st.plotly_chart(fig, use_container_width=True)
