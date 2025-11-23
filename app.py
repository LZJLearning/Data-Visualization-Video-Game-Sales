
import streamlit as st
import pandas as pd
from utils.io import load_data
from utils.prep import make_tables, apply_filters, data_quality_report
from sections import intro, overview, deep_dives, conclusions

# 页面配置
st.set_page_config(page_title="Video Game Sales — Data Storytelling", layout="wide")

# 注入 CSS：侧边栏背景改为蓝色
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #E3F2FD; } /* 蓝色 */
    </style>
""", unsafe_allow_html=True)

# 标题与数据来源
st.title("🎮 Video Game Sales — Data Storytelling Dashboard")
st.caption("Source: vgsales.csv | https://www.kaggle.com/datasets/gregorut/videogamesales")

# 加载与预聚合（缓存）
@st.cache_data(show_spinner=False)
def get_tables():
    df = load_data()
    tables = make_tables(df)
    return df, tables

raw_df, tables = get_tables()

# 侧边栏：两个 LOGO + 个人信息 + 仅年份筛选（最大值封顶到 2016）
with st.sidebar:
    st.image("assets/EFREI-logo.png")
    st.image("assets/WUT-Logo.png")
    st.markdown("**Professor:  Mano Mathew**")
    st.markdown("**Email:  mano.mathew@efrei.fr**")
    st.markdown("**Author:  ZIJIAN LIANG**")
    st.markdown("**Email:  zijian.liang@efrei.net**")
    st.markdown(
        """
        <a href="https://github.com/你的仓库地址" target="_blank">
            <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/github.svg"
                 width="40" style="margin: 0 auto; display: block;">
        </a>
        """,
        unsafe_allow_html=True
    )

years_all = sorted(raw_df['Year'].dropna().unique().tolist()) if 'Year' in raw_df.columns else []
year_min = int(min(years_all)) if years_all else 1980
year_cap_max = 2016
default_max = int(min(max(years_all), year_cap_max)) if years_all else year_cap_max
    
filtered_df_for_deep = apply_filters(raw_df, years=(year_min, default_max))
filtered_tables_for_deep = make_tables(filtered_df_for_deep)


# 页面各分区
intro.render(raw_df)
overview.render(raw_df)  # ← 趋势的最大年份滑块在这里处理
deep_dives.render(filtered_df_for_deep, filtered_tables_for_deep) # ← 热力图使用默认筛选到 2016 的数据
conclusions.render(raw_df)

# =========================
# 数据质量（仅缺失比例，百分比格式）
# =========================
st.markdown("### 数据质量")
quality_report = data_quality_report(raw_df)

# 将缺失比例转为百分数字符串（如 1.63%）
missing = quality_report['missing'].copy()
if not missing.empty and 'missing_ratio' in missing.columns:
    missing['missing_ratio'] = (missing['missing_ratio'] * 100).round(2).astype(str) + '%'

st.write("缺失比例：")
st.dataframe(missing)

# =========================
# 清洗前 / 后对比表
# =========================
st.markdown("### 清洗前后对比")
rows_before = int(raw_df.shape[0])
rows_after = int(filtered_tables_for_deep.get("raw", raw_df).shape[0])
loss_ratio = (rows_before - rows_after) / rows_before * 100 if rows_before > 0 else 0

compare_df = pd.DataFrame({
    "清洗前行数": [rows_before],
    "清洗后行数": [rows_after],
    "损失比率(%)": [round(loss_ratio, 2)]
})
st.dataframe(compare_df)
