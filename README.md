# 🎮 Video Game Sales Data Visualization App

## 📖 Project Overview
A comprehensive, interactive Streamlit dashboard for visualizing and analyzing video game sales data from 1980-2016. This application provides insights into global market trends, regional performance, platform dynamics, and publisher influence in the gaming industry.

## 🚀 Features
# 1. Data Overview & KPIs
Global Sales Trend Analysis:
 Interactive time series chart showing annual global sales (1980-2016)
Regional Market Share: 
 Pie chart visualizing sales distribution across NA, EU, JP, and Other regions
Interactive World Map:
 Choropleth map showing regional sales with genre preferences
Dynamic KPIs:
 Real-time metrics with year-over-year growth calculations
Year Range Filter: 
 Adjustable slider to analyze specific time periods

# 2. Deep Analytical Visualizations
Animated Bubble Chart: 
 Dynamic visualization showing regional sales evolution over time with play/pause/reset controls
Genre-Platform Heatmap: 
 Color-coded matrix revealing sales relationships between game genres and platforms
Publisher Performance Scatter Plot: 
 Interactive scatter plot showing top publishers' game sales distribution

# 3. Data Insights & Conclusions
Top 20 Games Leaderboard:
 Table of highest-selling games with detailed information
Actionable Insights:
 Data-driven recommendations for game developers and publishers
Industry Analysis:
 Comprehensive breakdown of market patterns and success factors

## 🛠️ Technology Stack
Python 3.10+
Streamlit: Interactive web application framework
Pandas: Data manipulation and analysis
Altair: Declarative statistical visualization library
Plotly: Interactive graphing and mapping library
NumPy: Numerical computing

## 📁 Project Structure
video-game-sales-app/
├── app.py                 # Main application entry point
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── data/
│   └── vgsales.csv       # Dataset (download from Kaggle)
├── assets/
│   ├── EFREI-logo.png    # University logos
│   └── WUT-Logo.png
├── utils/
│   ├── io.py            # Data loading and caching
│   ├── prep.py          # Data preprocessing and transformation
│   └── viz.py           # Visualization functions
└── sections/
    ├── intro.py         # Introduction section
    ├── overview.py      # Overview and KPIs section
    ├── deep_dives.py    # Deep analysis visualizations
    └── conclusions.py   # Conclusions and insights

## 📊 Dataset Information
# Source
Dataset: vgsales.csv
Platform: Kaggle
URL: https://www.kaggle.com/datasets/gregorut/videogamesales
Total Records: 16,598
Time Period: 1980-2016

# Data Fields
Rank: Overall sales ranking
Name: Game title
Platform: Platform of release (Wii, PS4, PC, etc.)
Year: Year of release
Genre: Game genre/category
Publisher: Publishing company
NA_Sales: Sales in North America (in millions)
EU_Sales: Sales in Europe (in millions)
JP_Sales: Sales in Japan (in millions)
Other_Sales: Sales in rest of the world (in millions)
Global_Sales: Total worldwide sales (in millions)

## 📈 Key Insights & Findings
# Market Analysis
Regional Dominance:
 North America accounts for 50% of global sales, followed by Europe (27%), Japan (13%), and Other regions (10%)
Golden Era:
 2006-2009 marked the peak period for video game sales, with annual sales exceeding 600 million units
Platform Specialization:
 PS2/PS3: Stronghold for action games
 Wii: Dominant in casual/sports games
 Xbox 360: Leading platform for shooter games
Publisher Power: 
 Nintendo demonstrates unparalleled success through its integrated hardware-software ecosystem

# Strategic Recommendations
Regional Targeting:
 For Western markets: Develop high-intensity action/shooter games
 For Japanese market: Focus on narrative-driven RPGs with complex systems
Platform Optimization:
 Align game design with platform strengths and audience preferences
 Consider platform ecosystem when developing exclusive titles
Publisher Partnerships:
 Collaborate with established publishers for market access and resources
 Consider Nintendo's integrated model as a long-term success strategy

## 🔍 Data Quality & Processing
# Cleaning Process
Initial Records: 16,598
Cleaned Records: 16,321
Data Loss: 277 records (1.66%)
Primary Cleaning: Removal of records with missing Year or Global_Sales values

# Data Validation 
Year conversion with error handling
Regional sales data normalization
Duplicate detection and handling
Comprehensive missing value analysis

## 👥 Project Team
# Developer
ZIJIAN LIANG - Primary Developer & Data Analyst
Email: zijian.liang@efrei.net
GitHub: [LZJLearning](https://github.com/LZJLearning/Data-Visualization-Video-Game-Sales/tree/main)

# Academic Supervision
Course: Data Visualization 2025
Professor: Mano Mathew
Email: mano.mathew@efrei.fr
Institutions: EFREI Paris 

## 📚 Academic Context
This project was developed as part of the Data Visualization course requirements, demonstrating:
 Practical application of data visualization principles
 Interactive dashboard development using modern tools
 Data storytelling and insight generation
 Professional documentation and deployment practices

## 🎯 Usage Instructions
# Navigation
Introduction: Overview of dataset and project objectives
Data Overview: Global trends, regional analysis, and KPIs
Deep Analysis: Advanced visualizations with interactive controls
Conclusions: Key findings and actionable insights

# Interactive Features
Use the year slider to analyze specific time periods
Click play/pause buttons to control the animated bubble chart
Hover over charts for detailed tooltip information
Explore the interactive world map with region-specific data

## 🔮 Future Enhancements
# Planned Features
Real-time Data Integration: Connect to live sales data APIs
Advanced Analytics: Machine learning predictions for game success
Mobile Optimization: Responsive design for mobile devices
Export Functionality: Download charts and reports as PDF/PNG

# Research Extensions
Digital Sales Inclusion: Incorporate digital distribution data
Mobile Gaming Analysis: Expand to include mobile game market
Sentiment Analysis: Integrate review and social media data
Competitive Analysis: Compare across different gaming companies

## 📝 License
This project is developed for academic purposes under the Data Visualization 2025 course. All data analysis and visualizations are created for educational use.

## 🙏 Acknowledgments
Kaggle Community for providing the vgsales dataset
Streamlit Team for the excellent framework
Altair & Plotly Teams for powerful visualization libraries
Professor Mano Mathew for guidance and supervision

# 🎮 Start exploring the world of video game sales data! Your next gaming industry insight awaits.