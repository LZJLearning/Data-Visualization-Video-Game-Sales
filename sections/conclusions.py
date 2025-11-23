import streamlit as st
import pandas as pd

def render(df):
    st.subheader('III Conclusion')
    
    # Top 20 table
    st.subheader("The Top 20 Games in Global Sales")
    top20 = df.sort_values('Global_Sales', ascending=False).head(20)
    st.dataframe(top20[['Name', 'Platform', 'Year', 'Genre', 'Publisher', 'Global_Sales']])

    st.markdown("""
                **Keys:**  
                1.**Market pattern:*** The global market is dominated by North America, supplemented by Europe, and has distinct Japanese characteristics. 
                 There is a fundamental 'East West culture' in players' tastes  
                2.**Success method:** The most successful works in history are often the perfect combination of specific game genres and platform ecosystems.  
                3.**Core competition:** A strong first party IP and hardware software closed-loop ecosystem 
                are the strongest moats for establishing long-term dominance, as Nintendo has proven.  
                  
                **Answer:**  
                1.Create cinematic and highly exciting action/shooting games for the European and American markets;
                 Deeply cultivate narrative driven and complex role-playing games for the Japanese market  
                2.Based on the characteristics of the platform, 
                is it a visual masterpiece that fully utilizes the performance of PS/PC, 
                a family friendly creative work that fits the Nintendo platform, 
                or a fragmented experience that utilizes the touch screen of mobile phones?
                 Remember to integrate the game with the platform.  
                3.Collaborating with powerful platforms or publishers, 
                data shows that a powerful publisher can provide crucial resources, market insights, and distribution channels, 
                greatly increasing the visibility and success rate of games.  
                (The table above proves Nintendo's strength as a publisher)
                  
                **Question**:  
                1.This dataset only includes the top 1000 games with physical sales,
                 which are relatively old and may not fully reflect the current market situation.  
                2.The rise of digital distribution and mobile games may affect the sales statistics of physical games
                  
                **Next**:  
                1.Addressing the 'Dataset Deficiency' - Incorporating Digital Revenue and Mobile Markets  
                2.Search for recent industry reports (such as Nintendo and Sony's financial reports) for verification      
    """)
    st.write("—————————————————————————————————————————————————————————————————")
    
