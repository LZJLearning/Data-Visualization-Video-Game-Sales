import streamlit as st
from io import StringIO

def render(df):
    st.header("I Introducation")
    st.write("""
             I visualize and analyze the sales performance of electronic games across multiple gaming platforms, 
             sales in different regions, and publisher data provided by this dataset.  
             I will use data to tell players in the gaming industry what types of games 
             should be developed and on which platform they should be published, making it easier to succeed
             """)
    buf=StringIO()
    df.info(buf=buf)
    st.subheader("Dataset structure")
    
    description = """
    Fields include:
    - Rank - Ranking of overall sales
    - Name - The game's name
    - Platform - Platform of the game's release (will, PC, PS4, etc.)
    - Year - Year of the game's release
    - Genre - Genre of the game
    - Publisher - Publisher of the game
    - NA_Sales - Sales in North America (in millions)
    - EU_Sales - Sales in Europe (in millions)
    - JP_Sales - Sales in Japan (in millions)
    - Other_Sales - Sales in the rest of the world (in millions)
    - Global_Sales - Total worldwide sales
    - There are 16,598 records. 2 records were dropped due to incomplete information.
    """
    st.write(description)
    info_str = buf.getvalue()
    st.code(info_str)
