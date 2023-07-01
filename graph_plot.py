import df_manipulations
from import_data import import_df_for_bokeh
from graph_style import apply_default_style, apply_map_style

from bokeh.models import BasicTicker, ColorBar, LinearColorMapper, ColumnDataSource, Whisker, HoverTool, Range1d, LabelSet
from bokeh.plotting import figure
from bokeh.palettes import Viridis256, Category20b, Category20
from bokeh.transform import transform, linear_cmap, factor_cmap, dodge

arabica_coffee_data = import_df_for_bokeh("df_arabica_clean.csv")

# 1 graph
def L_aroma_aftertaste(datapath):
    axis = df_manipulations.df_aroma_aftertaste(datapath)

    # Creating CDS object
    data = {"x": [value[0] for value in axis.values()],
            "y": [value[1] for value in axis.values()],
            "countries": [key for key in axis.keys()]}

    source = ColumnDataSource(data=data)

    tooltips = [
        ('Country', "@countries"),
        ("Mean Aftertaste", "@x"),
        ('Mean Aroma', '@y')]

    # Creating the plot
    plot = figure(width=1200, height=750, tooltips=tooltips)

    plot.circle(x="x", y="y", source=source, fill_color="#732C02",
                line_color="#732C02", size=12)

    # Points' labels
    labels = LabelSet(x="x", y="y", text="countries",
                      text_font_size="9pt", text_font="Modern Love", text_font_style="bold",
                      x_offset=10, y_offset=1, source=source)

    # Axis
    plot.x_range = Range1d(7.2, 8.1)
    plot.y_range = Range1d(7.1, 8)

    plot.xaxis.axis_label = "Mean aroma"
    plot.yaxis.axis_label = "Mean aftertaste"
    plot.title.text = "Mean aroma and aftertaste by country"

    plot.ygrid.minor_grid_line_color = "#aaaaaa"
    plot.ygrid.minor_grid_line_dash = 'dotted'
    plot.xgrid.minor_grid_line_color = "#aaaaaa"
    plot.xgrid.minor_grid_line_dash = 'dotted'

    plot.add_layout(labels)

    plot = apply_default_style(plot)

    return plot

# 2 graph
def L_variety_method(datapath):
    df = df_manipulations.df_variety_method(datapath=datapath)

    # Group the DataFrame by "Variety" and "Processing Method" and calculate the count
    grouped = df.groupby(["Variety", "Processing Method"]).size().unstack()
    varieties = grouped.index.tolist()

    # Creating CDS object
    source = ColumnDataSource(grouped)

    # Color palette for the bars
    colors = Category20[len(grouped.columns)]

    # Create the plot
    plot = figure(x_range=varieties, height=750, width=1200)

    # Stacked bar chart for each processing method
    for index, method in enumerate(grouped.columns):
        plot.vbar(x=varieties, top=grouped[method], width=0.8, color=colors[index],
                  legend_label=method)

    # Legends
    plot.legend.location = "center"
    plot.add_layout(plot.legend[0], 'right')

    # Axis label and title
    plot.xaxis.axis_label = "Coffee varieties"
    plot.yaxis.axis_label = "Number of lots"
    plot.title.text = "Processing methods by coffee variety"

    plot.xaxis.major_label_orientation = "vertical"

    plot.ygrid.grid_line_color = "grey"
    plot.ygrid.minor_grid_line_color = "#999999"
    plot.ygrid.minor_grid_line_dash = 'dotted'

    plot = apply_default_style(plot)

    return plot

# 3 graph
def L_country_kilos(datapath):
    df = df_manipulations.df_country_kilos(datapath)
    df = df.sort_values("Kilos of Coffee")

    # Create plot
    plot = figure(y_range=df["Countries"], width=1200,
                  height=750, title="Coffee Production by Country")
    source = ColumnDataSource(df)

    # Add glyph
    plot.hbar(y='Countries', right='Kilos of Coffee', fill_color="#1680a4",
              line_color="#1680a4", height=0.5, source=source)

    # Add annotations
    plot.text(x='Kilos of Coffee', y='Countries', text='Kilos of Coffee', text_baseline='middle', text_align='left',
              source=source, text_font_size='9pt', text_font_style="italic", x_offset=5)

    # Apply elements of style
    plot = apply_default_style(plot)
    plot.yaxis.axis_label = "Countries"
    plot.xaxis.axis_label = "Kilos of Coffee"

    plot.xaxis.major_label_text_color = None

    return plot

# 4 graph
def P_acidity_flavor(datapath):
    # Get the necessary data
    source = df_manipulations.get_df_acidity_flavor(datapath)

    tooltips = [
        ("Flavor score", "@Flavor"),
        ("Acidity score", "@Acidity"),
        ("Occurencies", "@count")
    ]

    # Create the plot
    plot = figure(width=1200, height=750, tooltips=tooltips)
    plot.circle(x="Flavor", y="Acidity", size="Size",
                color="#732C02", source=source)

    # Set title and axis labels
    plot.xaxis.axis_label = "Score on Flavor"
    plot.yaxis.axis_label = "Score on Acidity"
    plot.title.text = "Relation between coffee scores on Flavor and Acidity"

    plot.ygrid.minor_grid_line_color = "#aaaaaa"
    plot.ygrid.minor_grid_line_dash = 'dotted'
    plot.xgrid.minor_grid_line_color = "#aaaaaa"
    plot.xgrid.minor_grid_line_dash = 'dotted'

    # Apply plot style
    plot = apply_default_style(plot)

    return plot

# 5 graph
def P_map_mean_overall(datapath):
    # Get the map data
    world_map = df_manipulations.get_geojson_with_coffee_data(datapath)

    # Create a color mapping to the countries in map based on overall atribute
    cores = list(Viridis256)
    # To make all the countries without production white
    cores.append("#e4e5e7")
    color_scheme = linear_cmap("Overall_mean", tuple(cores[::-1]), 7.3, 7.9)

    # Creates a list of tuples that tells the plot the tooltips to be displayed
    tooltips = [("Country", "@ADMIN"),
                ("Overall Score", "@Overall_mean")]

    # Create the plot (width includes legend width and height include title
    # height in order to have the map with proper proportions)
    plot = figure(width=1200, height=750, tooltips=tooltips,
                  title="Mean of overall scores for coffees, by country")
    plot.patches('xs', 'ys', source=world_map, line_color='black',
                 line_width=0.25, fill_alpha=1, fill_color=color_scheme)

    # Create color legend and add to the plot
    color_legend = ColorBar(color_mapper=color_scheme["transform"],
                            width=40)
    plot.add_layout(color_legend, "right")

    # Set axis limits to fit world map
    plot.x_range = Range1d(-180, 180)
    plot.y_range = Range1d(-90, 90)

    # Apply map style
    plot = apply_map_style(plot)

    return plot

# 6 graph
def P_boxplot_altitude_by_country(datapath):
    # Get all the necessary data
    source, country_list, outliers = df_manipulations.get_cds_altitude_country(
        datapath)

    # Create the plot (x_range says wich categories X axis have)
    # The tools were removed because they don't make sense in the boxplot
    plot = figure(x_range=country_list, toolbar_location=None,
                  tools="", width=1200, height=750)

    # To do a boxplot in bokeh, it's necessay to plot three elements individualy:
    # The whiskers, the boxes (plotted as bars) and the outliers

    # Adding the whiskers
    whiskers = Whisker(base="Country of Origin", upper="upper",
                       lower="lower", source=source)
    plot.add_layout(whiskers)

    # Adding the boxes
    # Creates a color map to color each box with a color
    color_map = factor_cmap("Country of Origin", Category20b[20], country_list)
    # Plotting the boxes
    plot.vbar("Country of Origin", 0.75, "q2", "q3", source=source,
              color=color_map, line_color="black")
    plot.vbar("Country of Origin", 0.75, "q1", "q2", source=source,
              color=color_map, line_color="black")

    # Plotting the outliers as dots
    plot.circle("Country of Origin", "Altitude", source=outliers,
                size=6, color="#732C02")

    # Set title and axis labels
    plot.xaxis.axis_label = "Country of Origin"
    plot.yaxis.axis_label = "Altitude"
    plot.title.text = "Distribution of altitudes of coffee production by country"

    # Apply default style
    plot = apply_default_style(plot)
    plot.xaxis.major_label_orientation = 45

    plot.ygrid.minor_grid_line_color = "#999999"
    plot.ygrid.minor_grid_line_dash = 'dotted'

    return plot

# 7 graph
def V_sensorial_attr_correlation(datapath):

    # Get the correlation matrix using the provided data
    df = df_manipulations.get_correlation_matrix(datapath)

    tooltips=[
            ('Correlation', '@correlation'),
            ('Attribute 1', "@sensory_variables1"),
            ("Attribute 2", "@sensory_variables2")]

    source = ColumnDataSource(df)

    # Define colors for the heatmap
    colors = list(Viridis256)

    # Create a color mapper based on the min and max correlation values
    color_mapper = LinearColorMapper(
        palette=colors, low=df.correlation.min(), high=df.correlation.max())

    x_range=list(df.sensory_variables1.drop_duplicates())
    y_range=list(reversed(df.sensory_variables2.drop_duplicates()))

    # Create a Bokeh figure for the heatmap
    plot = figure(
        width=750,
        height=750,
        title="Correlation of score attributes",
        x_range=x_range,
        y_range=y_range,
        tooltips=tooltips,
        tools="save",
        x_axis_location="above")

    # Add rectangles representing the correlation values to the figure
    plot.rect(
        x="sensory_variables1",
        y="sensory_variables2",
        width=1,
        height=1,
        source=source,
        line_color=None,
        color=transform('correlation', color_mapper))

    # Create a color bar to represent the correlation values
    color_bar = ColorBar(
        color_mapper=color_mapper,
        location=(0, 0))

    # Add the color bar to the figure
    plot.add_layout(color_bar, "right")

    # Add hover tool to display correlation value

    plot = apply_default_style(plot)

    return plot

# 8 graph
def V_altitude_flavor(datapath):

    data = df_manipulations.get_df_mean_altitude(
        datapath[["Altitude", "Flavor", "Overall", "Country of Origin"]])

    source = ColumnDataSource(data)

    # Create hover tool to display correlation values
    tooltips = [
        ('Country of Origin', "@{Country of Origin}"),
        ("Mean Altitude", "@{Mean Altitude}{0.00} meters"),
        ('Flavor Score', '@Flavor')]

    plot = figure(width=1200, height=750, tooltips=tooltips)

    plot.circle_dot(x="Mean Altitude", y="Flavor", size=15, alpha=0.5,
                    color="#732C02", source=source)

    plot.yaxis.axis_label = "Score on Flavor"
    plot.xaxis.axis_label = "Mean Altitude"
    plot.title.text = "Flavor score and mean altitude"

    plot.ygrid.minor_grid_line_color = "#aaaaaa"
    plot.ygrid.minor_grid_line_dash = 'dotted'
    plot.xgrid.minor_grid_line_color = "#aaaaaa"
    plot.xgrid.minor_grid_line_dash = 'dotted'

    # Apply plot style
    plot = apply_default_style(plot)

    return plot

# 9 graph
def V_taste_means_by_color(datapath):
    # Get the data with means by color using df_manipulations.get_means_by_color function
    df = df_manipulations.get_means_by_color(datapath)

    # Create a ColumnDataSource with the data
    source = ColumnDataSource(data=df)

    tooltips = [
        ('Color', "@Color"),
        ("Mean Flavor", "@Flavor"),
        ('Mean Body', '@Body'),
        ('Mean Acidity', '@Acidity')]

    # Create a figure for the bar chart
    plot = figure(x_range=df.Color, y_range=(7, 9), width=1200,
                  height=750, tools="save", tooltips=tooltips)

    # Plot the mean flavor values as vertical bars, offsetting the x position
    plot.vbar(x=dodge('Color', -0.25, range=plot.x_range), top='Flavor', source=source,
              width=0.2, color="#b2e061", legend_label="Mean Flavor")

    # Plot the mean body values as vertical bars, offsetting the x position
    plot.vbar(x=dodge('Color', 0.0, range=plot.x_range), top='Body', source=source,
              width=0.2, color="#718dbf", legend_label="Mean Body")

    # Plot the mean acidity values as vertical bars, offsetting the x position
    plot.vbar(x=dodge('Color', 0.25, range=plot.x_range), top='Acidity', source=source,
              width=0.2, color="#bd7ebe", legend_label="Mean Acidity")

    # Customize the appearance of the figure
    plot = apply_default_style(plot)

    plot.legend.location = "top_right"
    plot.legend.orientation = "horizontal"

    plot.yaxis.axis_label = "Score"
    plot.xaxis.axis_label = "Green coffee color"
    plot.title.text = "Mean score in taste variables by green coffee color"

    # Customize grids appearance
    plot.ygrid.grid_line_color = "grey"
    plot.ygrid.minor_grid_line_color = "#999999"
    plot.ygrid.minor_grid_line_dash = 'dotted'

    return plot
