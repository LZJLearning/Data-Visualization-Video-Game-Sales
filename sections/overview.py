import streamlit as st
from utils.prep import apply_filters, make_tables
from utils.viz import line_chart_timeseries, single_region_line_chart, pie_chart_region_share

def render(raw_df):
    
    # 1) 预先创建一个 KPI 容器（占位在页面更上方）
    kpi_box = st.container()

    # === 趋势：标题与最大年份滑块并排 ===
    left, right = st.columns([3, 3])
    with left:
        st.subheader("趋势：全球销量按年份")
    # 计算年份范围
    years_all = sorted(raw_df['Year'].dropna().unique().tolist())
    year_min = int(min(years_all)) 
    year_cap_max = 2016
    default_max = int(min(max(years_all), year_cap_max)) 
    with right:
        max_year = st.slider("最大年份", min_value=year_min, max_value=year_cap_max, value=default_max)

    # 基于滑块进行局部筛选（本 section 内部）
    df_year = apply_filters(raw_df, years=(year_min, max_year))
    local_tables = make_tables(df_year)
    
    # 4) 在“上方”的 KPI 容器里渲染动态 KPI（随滑块变化）
    with kpi_box:
        st.subheader("关键指标")
        global_sales = df_year['Global_Sales'].sum()
        current_year_sales = raw_df.loc[raw_df['Year'] == max_year, 'Global_Sales'].sum()
        prev_year_sales = raw_df.loc[raw_df['Year'] == (max_year - 1), 'Global_Sales'].sum()
        delta_pct = (current_year_sales - prev_year_sales) / prev_year_sales * 100.0
        # 格式为 +X.XX% / -X.XX%
        delta_str = f"{delta_pct:+.2f}%"

        st.metric("全球销量（合计）", f"{global_sales:.2f} M", delta=delta_str)

    # 折线图：全球销量按年份
    line_chart_timeseries(local_tables['timeseries_global'], 'Year', 'Global_Sales', 'Global Sales by Year')

    # === 各地区随时间趋势（一次只选一个地区） ===
    st.subheader("各地区随时间趋势")
    regions_all = local_tables['timeseries_regions']['Region'].unique().tolist()
    selected_region = st.selectbox("选择一个地区", regions_all)
    region_ts = local_tables['timeseries_regions'][local_tables['timeseries_regions']['Region'] == selected_region]
    single_region_line_chart(region_ts, f"{selected_region} 地区销量趋势")

    # === 饼图：各地区在全球销量的占比（基于当前年份筛选的区间） ===
    st.subheader("地区在全球销量中的占比")
    region_share = local_tables['timeseries_regions'].groupby('Region', as_index=False)['Regional_Sales'].sum()
    pie_chart_region_share(region_share, "各地区销量占全球销量的比例")
