from import_data import import_df_for_bokeh
from graph_style import apply_default_style
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.io import show

def P_acidity_flavor(datapath):
    df = import_df_for_bokeh(datapath)
    cld = ColumnDataSource(df)
    p = figure()
    p.circle(x = "Acidity", y = "Flavor", source = cld)
    p = apply_default_style(p)
    show(p)

P_acidity_flavor("df_arabica_clean.csv")
