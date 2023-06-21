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

    df = pd.read_csv(path)

    cds = ColumnDataSource(df)

    return cds
