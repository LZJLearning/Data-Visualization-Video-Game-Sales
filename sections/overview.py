import streamlit as st
from utils.prep import apply_filters, make_tables
from utils.viz import line_chart_timeseries, single_region_line_chart, pie_chart_region_share,region_sales_choropleth_map

def render(raw_df):
    
    #place
    kpi_box = st.container()

    # trend
    left, right = st.columns([3, 3])
    with left:
        st.subheader("Trend：Annual trend analysis")
    # Year range
    years_all = sorted(raw_df['Year'].dropna().unique().tolist())
    year_min = int(min(years_all)) 
    year_cap_max = 2016
    default_max = int(min(max(years_all), year_cap_max)) 
    with right:
        max_year = st.slider("Years", min_value=year_min, max_value=year_cap_max, value=default_max)

    df_year = apply_filters(raw_df, years=(year_min, max_year))
    local_tables = make_tables(df_year)
    
    # kpi container
    with kpi_box:
        st.subheader("KPIs")
        global_sales = df_year['Global_Sales'].sum()
        current_year_sales = raw_df.loc[raw_df['Year'] == max_year, 'Global_Sales'].sum()
        prev_year_sales = raw_df.loc[raw_df['Year'] == (max_year - 1), 'Global_Sales'].sum()
        delta_pct = (current_year_sales - prev_year_sales) / prev_year_sales * 100.0
        # 格式为 +X.XX% / -X.XX%
        delta_str = f"{delta_pct:+.2f}%"

        st.metric("Global sales(sum)", f"{global_sales:.2f} M", delta=delta_str)

    # line
    line_chart_timeseries(local_tables['timeseries_global'], 'Year', 'Global_Sales', 'Global Sales by Year')
    st.write("""
             Early (1980-1995): Low sales, not exceeding 100 million per year;  
             In 2000, sales grew rapidly, especially after 2006, with annual sales exceeding 500 million and reaching its peak in 2008, with annual sales exceeding 600 million;  
             From this, it can be seen that the years 2006 to 2009 were the ‘golden age’ of the gaming industry;  
             But after 2010 years, game sales will continue to decline, and its development focus and business model may change
             """)
    st.write("—————————————————————————————————————————————————————————————————")

    # Pie
    st.subheader("The proportion of regional sales in global sales")
    region_share = local_tables['timeseries_regions'].groupby('Region', as_index=False)['Regional_Sales'].sum()
    pie_chart_region_share(region_share, "The proportion of sales in each region to global sales")

    st.write("""
             The North American market accounts for 50 percent of global game sales, 
             highlighting its position as the largest and most mature single player gaming market in the world.  
             Reason analysis: Economic and cultural influence; Mainstream console manufacturers such as Microsoft (Xbox) and Sony (PlayStation) 
    """)

    #map
    st.subheader("Regional Sales Map")
    region_sales_choropleth_map(region_share, raw_df)
    
    description ="""
    - In North America, Europe, and other regions, Action games (including subcategories such as GTA, Assassin's Creed, Call of Duty, etc.)
    have become the best-selling genre, reflecting a common preference among Western players for instant feedback, high-intensity stimulation, and sensory impact.
    - The Japanese market is the only "exception" in the global mainstream market, dominated by Role Playing games such as Final Fantasy, Dragon Quest, Pokémon, and Monster Hunter. 
    This reflects the unique love of Japanese players for growth, complex storytelling, and system immersion.
    """
    st.write(description)
    st.write("—————————————————————————————————————————————————————————————————")

