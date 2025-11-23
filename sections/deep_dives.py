import streamlit as st
import pandas as pd
import time
from utils.viz import heatmap_genre_platform,bubble_chart_frame,scatter_publisher_sales

def render(df, tables):
    st.subheader("II Deep Analysis:")
    # init 
    st.session_state.setdefault('play_bubble', False)
    st.session_state.setdefault('bubble_year_idx', 0)

    # Dynamic Bubble Chart
    st.subheader("Dynamic Bubble Chart: Regional Changes over Years ")

    # Prepare animation data
    regions_ts = tables['timeseries_regions']  # Year, Region, Regional_Sales
    global_ts = tables['timeseries_global'].rename(columns={'Global_Sales': 'Global_Sales_Year'})  # Year, Global_Sales_Year
    bubble_df = regions_ts.merge(global_ts, on='Year', how='left')

    years = sorted(bubble_df['Year'].unique().tolist())

    # Control buttons
    btn_play, btn_pause, btn_reset = st.columns([1, 1, 1])
    with btn_play:
        if st.button("▶ Play"):
            st.session_state['play_bubble'] = True
            st.rerun()
    with btn_pause:
        if st.button("⏸ Stop"):
            st.session_state['play_bubble'] = False
            st.rerun()
    with btn_reset:
        if st.button("⟲ Reset"):
            st.session_state['play_bubble'] = False
            st.session_state['bubble_year_idx'] = 0
            st.rerun()

    #place
    placeholder = st.empty()

    
    idx = st.session_state['bubble_year_idx']
    year_now = years[idx]
    frame_now = bubble_df[bubble_df['Year'] == year_now]

    # Current frame
    chart = bubble_chart_frame(frame_now, f"Regional vs. Global Sales (Bubble Size=Regional Sales) - Year {year_now}")
    placeholder.altair_chart(chart, use_container_width=True)

    # fixed speed 1.25×（per frame 0.8s）
    if st.session_state['play_bubble']:
        time.sleep(0.8)
        if idx < len(years) - 1:
            st.session_state['bubble_year_idx'] += 1
        else:
            st.session_state['play_bubble'] = False
        st.rerun()
    
    st.markdown("""
                **The first stage (around 1980-1985):**  
                -North America (NA) dominated the market, while other bubbles were small and closely adhered to the bottom.  
                **The second stage (around 1985-1995):**  
                -The explosive growth of the Japanese (JP),Quickly forming a dual giant pattern with NA bubbles  
                -European (EU) is steadily growing, but its size is still significantly smaller than that of NA and JP.   
                -Factor: Nintendo's revival-the release of NES (FC) not only saved the North American gaming market, but also pushed Japanese games to the world,
                making Japan leap from a follower to a rule maker in the industry  
                **The third stage (around 1995-2016):**  
                -NA return and the long-term maintenance of its position as the largest market.   
                -The EU continues to grow, becoming a stable and crucial second largest market.   
                -The growth of JP tends to flatten out.   
                -Other bubbles are becoming visible, symbolizing the activation of the potential of emerging markets.  
                -Factor: The rise of Sony and Microsoft, the success of the "Western" brands PlayStation and Xbox, 
                and the globalization of game genres such as European and American action and shooting games 
                represented by 'GTA' and 'Call of Duty' have become the global mainstream.  
    """)
    st.write("—————————————————————————————————————————————————————————————————")

    #heatmap
    heatmap_genre_platform(df, "The relationship between global sales, types, and platforms (heatmap)")
    st.markdown("""
                This heatmap clearly shows that action and sports games dominate on the Sony PS2, 
                motion sensing casual games break through on the Nintendo Wii, and online shooting games leader in a new era on the Microsoft Xbox 360.   
                This is not only a victory for the game, but also the ultimate victory for its platform ecosystem and market positioning.   
                **So The platform positioning determines the content ceiling**  
                PS2/PS3 has become a fertile ground for Action games with its all-around performance;   
                Wii dominates the leisure sports market with innovative motion sensing;   
                X360 has become a holy land for shooting games with its top-notch online services.   
                **A "killer app"**   
                perfectly fits the platform's characteristics (such as "Wii Sports" for Wii and "Halo" for Xbox) 
                can greatly drive hardware sales and define the platform's brand image.
                """)

    st.write("—————————————————————————————————————————————————————————————————")

    #scatter
    scatter_publisher_sales(df,"Does the publisher affect game sales? (Each point represents a game)")
    st.markdown("""
                **The scatter plot clearly indicates :** publishers have a significant and obvious impact on game sales  
                Nintendo is an absolute ruler;  
                Not only has it released a large number of games, but more importantly, 
                it has a staggering number of "super hits" that far exceed those of other publishers.  
                **Analysis:**  
                Nintendo is both a publisher and a console platform provider,
                with almost all of its best-selling games coming from internal or closely controlled studios, 
                ensuring ultimate quality and high brand recognition.  
                Therefore, in the gaming industry, 
                choosing a powerful publisher or becoming a publisher like Nintendo is the most efficient path to commercial success
                """)
    st.write("—————————————————————————————————————————————————————————————————")
    




