from bokeh.models import ColumnDataSource
import pandas as pd 

def import_df_for_bokeh(path):
    df = pd.read_csv(path)
    return df