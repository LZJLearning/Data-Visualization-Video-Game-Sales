import pandas as pd
REGIONS = ['NA_Sales','EU_Sales','JP_Sales','Other_Sales']

def clean_and_enrich(df):
    df2 = df.dropna(subset=['Year','Global_Sales']).copy()
    df2['Year'] = df2['Year'].astype(int)
    return df2

def make_tables(df):
    raw = clean_and_enrich(df)
    tables = {}
    tables['raw'] = raw
    tables['timeseries_global'] = raw.groupby('Year')['Global_Sales'].sum().reset_index()

    cols = [c for c in REGIONS if c in raw.columns]
    melted = raw[['Year'] + cols].melt(id_vars=['Year'], value_vars=cols, var_name='Region', value_name='Regional_Sales')
    melted['Region'] = melted['Region'].map({'NA_Sales':'NA','EU_Sales':'EU','JP_Sales':'JP','Other_Sales':'Other'})
    tables['timeseries_regions'] = melted.groupby(['Year','Region'])['Regional_Sales'].sum().reset_index()
    return tables

def apply_filters(df, years=None):
    if years:
        ymin, ymax = years
        return df[(df['Year'] >= ymin) & (df['Year'] <= ymax)]
    return df

def kpis(df):
    gs = df['Global_Sales'].sum()
    titles = df.shape[0]
    top_genre = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False).index[0]
    top_pub = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).index[0]
    return {'global_sales': gs, 'titles': titles, 'top_genre': top_genre, 'top_publisher': top_pub}

def data_quality_report(df):
    missing = df.isna().mean().reset_index()
    missing.columns = ['column','missing_ratio']
    dups = df[df.duplicated(subset=['Name','Platform','Year'], keep=False)]
    return {'missing': missing, 'duplicates': dups}
