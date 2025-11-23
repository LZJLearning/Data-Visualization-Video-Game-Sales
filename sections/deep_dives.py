import streamlit as st
import pandas as pd
import time
from utils.viz import heatmap_genre_platform,bubble_chart_frame,scatter_publisher_sales

def render(df, tables):
    st.subheader("深入分析：全球销量与类型、平台关系")

    # —— 初始化会话状态（避免 AttributeError）
    st.session_state.setdefault('play_bubble', False)
    st.session_state.setdefault('bubble_year_idx', 0)

    # —— 动态气泡图：单图播放/暂停，固定 1.25×
    st.subheader("动态气泡图：地区随年份变化（纵轴=全球销量）")

    # 准备动画数据：合并地区-年份销量 + 全球-年份销量
    regions_ts = tables['timeseries_regions']  # Year, Region, Regional_Sales
    global_ts = tables['timeseries_global'].rename(columns={'Global_Sales': 'Global_Sales_Year'})  # Year, Global_Sales_Year
    bubble_df = regions_ts.merge(global_ts, on='Year', how='left')

    years = sorted(bubble_df['Year'].unique().tolist())

    # 控制按钮：播放 / 暂停 / 重置
    btn_play, btn_pause, btn_reset = st.columns([1, 1, 1])
    with btn_play:
        if st.button("▶ 播放"):
            st.session_state['play_bubble'] = True
            st.rerun()
    with btn_pause:
        if st.button("⏸ 暂停"):
            st.session_state['play_bubble'] = False
            st.rerun()
    with btn_reset:
        if st.button("⟲ 重置"):
            st.session_state['play_bubble'] = False
            st.session_state['bubble_year_idx'] = 0
            st.rerun()

    # 单图占位，用于每帧刷新
    placeholder = st.empty()

    # 当前帧索引与年份（有默认值，不会报错）
    idx = st.session_state['bubble_year_idx']
    year_now = years[idx]
    frame_now = bubble_df[bubble_df['Year'] == year_now]

    # 渲染当前帧（单图）
    chart = bubble_chart_frame(frame_now, f"地区 vs 全球销量（气泡大小=地区销量）— 年份 {year_now}")
    placeholder.altair_chart(chart, use_container_width=True)

    # 如果处于播放状态：固定 1.25×（每帧 0.8s），更新索引并重绘
    if st.session_state['play_bubble']:
        time.sleep(0.8)
        if idx < len(years) - 1:
            # 还没到最后一年 → 前进一帧
            st.session_state['bubble_year_idx'] += 1
        else:
            # 最后一年 → 自动停止播放
            st.session_state['play_bubble'] = False
        st.rerun()

    heatmap_genre_platform(df, "全球销量与类型、平台的关系（热力图）")

    st.subheader("发布商是否影响游戏销量？（每点代表一款游戏）")
    scatter_publisher_sales(df)
    




