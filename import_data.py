from bokeh.models import ColumnDataSource
import pandas as pd 

def import_df_for_bokeh(path):
    df = pd.read_csv(path)
    return df

def data_to_cds(df):
    cds = ColumnDataSource(df)
    return cds