from bokeh.models import ColumnDataSource
import pandas as pd

def cds_from_csv(path):
    """
    Convert a CSV file to a Bokeh ColumnDataSource.
    
        Parameters:
            path (str): Path to the CSV file.

        Returns:
            bokeh.models.ColumnDataSource: A ColumnDataSource object containing the data from the CSV file
    """

    sp_housing_df = pd.read_csv(path)

    sp_housing_df = sp_housing_df[sp_housing_df["area"] > 5]

    cds = ColumnDataSource(sp_housing_df)

    return cds
