import pandas as pd

def analyze_data(df):
    analysis = {}
    analysis['shape'] = df.shape
    analysis['columns'] = df.columns.tolist()
    analysis['dtypes'] = df.dtypes.astype(str).to_dict()
    analysis['summary'] = df.describe().to_string()
    analysis['nulls'] = df.isnull().sum().to_dict()
    analysis['sample'] = df.head(5).to_string()

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    analysis['numeric_cols'] = numeric_cols

    if numeric_cols:
        analysis['top_column'] = df[numeric_cols].sum().idxmax()
        analysis['top_value'] = df[numeric_cols].sum().max()

    return analysis