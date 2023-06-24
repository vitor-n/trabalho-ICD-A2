from import_data import import_df_for_bokeh
from graph_style import apply_default_style, apply_dotplot_style
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.io import show
import df_manipulations

def P_acidity_flavor(datapath):
    df_size = df_manipulations.get_df_acidity_flavor(datapath)
    p = figure()
    p.circle(x = "Acidity", y = "Flavor", color = "Color", source = df_size)
    p = apply_dotplot_style(p)
    show(p)

P_acidity_flavor(import_df_for_bokeh("df_arabica_clean.csv"))
