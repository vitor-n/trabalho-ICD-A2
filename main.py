from import_data import import_df_for_bokeh
import graph_plot

from bokeh.io import output_file, save

arabica_coffee = import_df_for_bokeh("df_arabica_clean.csv")

# 1 graph
plot = graph_plot.L_aroma_aftertaste(arabica_coffee) #Get plot object
output_file("graphs/larissa/graph1.html")            #Set output file
save(plot)                                           #Save in desired location

# 2 graph
plot = graph_plot.L_variety_method(arabica_coffee)
output_file("graphs/larissa/graph2.html")
save(plot)

# 3 graph
plot = graph_plot.L_country_kilos(arabica_coffee)
output_file("graphs/larissa/graph3.html")
save(plot)

# 4 graph
plot = graph_plot.P_acidity_flavor(arabica_coffee)
output_file("graphs/pedro/graph1.html")
save(plot)

# 5 graph
plot = graph_plot.P_map_mean_overall(arabica_coffee)
output_file("graphs/pedro/graph2.html")
save(plot)

# 6 graph
plot = graph_plot.P_boxplot_altitude_by_country(arabica_coffee)
output_file("graphs/pedro/graph3.html")
save(plot)

# 7 graph
plot = graph_plot.V_sensorial_attr_correlation(arabica_coffee)
output_file("graphs/vitor/graph1.html")
save(plot)

# 8 graph
plot = graph_plot.V_altitude_flavor(arabica_coffee)
output_file("graphs/vitor/graph2.html")
save(plot)

# 9 graph
plot = graph_plot.V_taste_means_by_color(arabica_coffee)
output_file("graphs/vitor/graph3.html")
save(plot)
