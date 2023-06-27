import df_manipulations
from import_data import import_df_for_bokeh
from graph_style import apply_default_style, apply_dotplot_style, apply_map_style
from bokeh.models import BasicTicker, ColorBar, LinearColorMapper, ColumnDataSource, Whisker
from bokeh.models import Range1d, ColorBar
from bokeh.plotting import figure
from bokeh.palettes import Viridis256, Category20b
from bokeh.transform import transform, linear_cmap, factor_cmap
from bokeh.io import show

arabica_coffee_data = import_df_for_bokeh("df_arabica_clean.csv")

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
    cores = list(Viridis256)
    cores.append("#FFFFFF") #To make all the countries without production white
    color_scheme = linear_cmap("Overall_mean", tuple(cores[::-1]), 7, 8)

    #Creates a list of tuples that tells the plot the tooltips to be displayed
    tooltips = [("Country", "@ADMIN"),
                ("Overall Score", "@Overall_mean")]

    #Create the plot (width includes legend width and height include title
    #height in order to have the map with proper proportions)
    plot = figure(width = 1330, height = 735, tooltips = tooltips,
                  title = "Mean of overall scores for coffees, by country")
    plot.patches('xs', 'ys', source = world_map, line_color='black',
                 line_width=0.25, fill_alpha=1, fill_color = color_scheme)

    #Create color legend and add to the plot
    color_legend = ColorBar(color_mapper = color_scheme["transform"],
                            width = 50, height = 680)
    plot.add_layout(color_legend, "right")

    #Set axis limits to fit world map
    plot.x_range = Range1d(-180, 180)
    plot.y_range = Range1d(-90, 90)

    #Apply map style
    plot = apply_map_style(plot)
    show(plot)

#P_map_mean_overall(import_df_for_bokeh("df_arabica_clean.csv"))

def P_boxplot_altitude_by_country(datapath):
    #Get all the necessary data
    source, country_list, outliers = df_manipulations.get_cds_altitude_country(datapath)

    #Create the plot (x_range says wich categories X axis have)
    #The tools were removed because they don't make sense in the boxplot
    plot = figure(x_range = country_list, toolbar_location = None,
                  tools = "", width = 1280, height = 720)

    #To do a boxplot in bokeh, it's necessay to plot three elements individualy:
    #The whiskers, the boxes (plotted as bars) and the outliers

    #Adding the whiskers
    whiskers = Whisker(base = "Country of Origin", upper = "upper",
                       lower = "lower", source = source)
    plot.add_layout(whiskers)

    #Adding the boxes
    #Creates a color map to color each box with a color
    color_map = factor_cmap("Country of Origin", Category20b[20], country_list)
    #Plotting the boxes
    plot.vbar("Country of Origin", 0.75, "q2", "q3", source = source,
              color = color_map, line_color = "black")
    plot.vbar("Country of Origin", 0.75, "q1", "q2", source = source,
              color = color_map, line_color = "black")

    #Plotting the outliers as dots
    plot.circle("Country of Origin", "Altitude", source = outliers,
                size = 6, color =  "#732C02")

    #Set title and axis labels
    plot.xaxis.axis_label = "Country of Origin"
    plot.yaxis.axis_label = "Altitude"
    plot.title.text = "Distribution of altitudes of coffee production by country"

    #Apply default style
    plot = apply_default_style(plot)
    plot.xaxis.major_label_orientation = 45

    show(plot)

P_boxplot_altitude_by_country(arabica_coffee_data)

def V_sensorial_attr_correlation(datapath):

    # Get the correlation matrix using the provided data
    df = df_manipulations.get_correlation_matrix(datapath)

    # Define colors for the heatmap
    colors = list(Viridis256)

    # Create a color mapper based on the min and max correlation values
    color_mapper = LinearColorMapper(palette=colors, low=df.correlation.min(), high=df.correlation.max())

    # Create a Bokeh figure for the heatmap
    p = figure(
        width=800,
        height=800,
        title="Correlation between sensorial attributes",
        x_range=list(df.sensory_variables1.drop_duplicates()),
        y_range=list(reversed(df.sensory_variables2.drop_duplicates())),
        toolbar_location=None,
        tools="",
        x_axis_location="above")

    # Add rectangles representing the correlation values to the figure
    p.rect(
        x="sensory_variables1",
        y="sensory_variables2",
        width=1,
        height=1,
        source=ColumnDataSource(df),
        line_color=None,
        color=transform('correlation', color_mapper))

    # Create a color bar to represent the correlation values
    color_bar = ColorBar(
        color_mapper=color_mapper,
        location=(0, 0),
        ticker=BasicTicker(desired_num_ticks=20))

    # Add the color bar to the figure
    p.add_layout(color_bar, "right")

    # Display the heatmap
    show(p)
