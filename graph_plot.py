from import_data import import_df_for_bokeh
from graph_style import apply_default_style, apply_dotplot_style, apply_map_style
from bokeh.models import Range1d, ColorBar
from bokeh.plotting import figure
from bokeh.palettes import Greys256
from bokeh.transform import linear_cmap
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

#P_acidity_flavor(import_df_for_bokeh("df_arabica_clean.csv"))

def P_map_mean_overall(datapath):
    #Get the map data
    world_map = df_manipulations.get_geojson_with_coffee_data(datapath)

    #Create a color mapping to the countries in map based on overall atribute
    color_scheme = linear_cmap("Overall_mean", Greys256[::-1], 6.9, 8.1)

    #Creates a list of tuples that tells the plot the tooltips to be displayed
    tooltips = [("Country", "@ADMIN"),
                ("Overall Score", "@Overall_mean")]

    #Create the plot (width includes legend width and height include title
    #height in order to have the map with proper proportions)
    plot = figure(width = 1330, height = 735, tooltips = tooltips,
                  title = "Mean of overall scores for coffees, by country")
    plot.patches('xs', 'ys', source = world_map, line_color='black',
                 line_width=0.25, fill_alpha=1, fill_color = color_scheme)

    #Create color legend, stylize it and add to the plot
    color_legend = ColorBar(color_mapper = color_scheme["transform"],
                            width = 50, height = 690)
    color_legend.background_fill_color = "#EEEEEE"
    color_legend.background_fill_alpha = 1
    plot.add_layout(color_legend, "right")

    #Set axis limits to fit world map
    plot.x_range = Range1d(-180, 180)
    plot.y_range = Range1d(-90, 90)

    #Apply map style
    plot = apply_map_style(plot)
    show(plot)

P_map_mean_overall(import_df_for_bokeh("df_arabica_clean.csv"))
