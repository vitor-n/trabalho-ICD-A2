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
    plot = figure(width = 1000, height = 700)
    plot.circle(x = "Flavor", y = "Acidity", size = "Size", color = "#732C02", source = cds)

    #Set title and axis labels
    plot.xaxis.axis_label = "Score on Flavor"
    plot.yaxis.axis_label = "Score on Acidity"
    plot.title.text = "Relation between coffee scores on Flavor and Acidity"

    #Apply plot style
    plot = apply_dotplot_style(plot)
    show(plot)

    #TODO: maybe change the scale limits and size of circles

P_acidity_flavor(import_df_for_bokeh("df_arabica_clean.csv"))
