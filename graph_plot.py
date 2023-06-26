from import_data import import_df_for_bokeh
from graph_style import apply_default_style, apply_dotplot_style
from bokeh.models import ColumnDataSource, Circle
from bokeh.plotting import figure
from bokeh.io import show
import df_manipulations

def P_acidity_flavor(datapath):
    #Get the necessary data
    cds = df_manipulations.get_df_acidity_flavor(datapath)

    #Create the plot
    plot = figure(width = 800, height = 800)
    plot.circle(x = "Flavor", y = "Acidity", color = "Color", size = 4, source = cds)
    plot = apply_dotplot_style(plot)
    show(plot)

    #TODO: improve code organization, add label names, add title, maybe change the scale limits

P_acidity_flavor(import_df_for_bokeh("df_arabica_clean.csv"))
