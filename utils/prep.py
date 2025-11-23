import pandas as pd
REGIONS = ['NA_Sales','EU_Sales','JP_Sales','Other_Sales']

def clean_and_enrich(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    df2 = df.dropna(subset=['Year','Global_Sales']).copy()
    df2['Year'] = df2['Year'].astype(int)
    return df2

def make_tables(df: pd.DataFrame):
    raw = clean_and_enrich(df)
    tables = {'raw': raw}
    if not raw.empty:
        tables['timeseries_global'] = raw.groupby('Year', as_index=False)['Global_Sales'].sum()
        cols = [c for c in REGIONS if c in raw.columns]
        if cols:
            melted = raw[['Year']+cols].melt(id_vars=['Year'], value_vars=cols, var_name='Region', value_name='Regional_Sales')
            mapping = {'NA_Sales':'NA','EU_Sales':'EU','JP_Sales':'JP','Other_Sales':'Other'}
            melted['Region'] = melted['Region'].map(mapping)
            tables['timeseries_regions'] = melted.groupby(['Year','Region'], as_index=False)['Regional_Sales'].sum()
    return tables

def apply_filters(df: pd.DataFrame, years=None):
    if df.empty:
        return df
    if years:
        ymin,ymax = years
        return df[(df['Year']>=ymin)&(df['Year']<=ymax)]
    return df

def kpis(df: pd.DataFrame):
    if df.empty:
        return {'global_sales':0,'titles':0,'top_genre':'-','top_publisher':'-'}
    gs = df['Global_Sales'].sum()
    titles = df.shape[0]
    top_genre = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False).index[0] if 'Genre' in df.columns else '-'
    top_pub = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).index[0] if 'Publisher' in df.columns else '-'
    return {'global_sales':gs,'titles':titles,'top_genre':top_genre,'top_publisher':top_pub}

def data_quality_report(df: pd.DataFrame):
    if df.empty:
        return {'missing':pd.DataFrame(),'duplicates':pd.DataFrame()}
    missing = df.isna().mean().reset_index()
    missing.columns=['column','missing_ratio']
    dups = df[df.duplicated(subset=['Name','Platform','Year'],keep=False)] if all(c in df.columns for c in ['Name','Platform','Year']) else pd.DataFrame()
    return {'missing':missing,'duplicates':dups}
