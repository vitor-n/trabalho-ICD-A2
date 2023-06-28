import pandas as pd
from import_data import import_df_for_bokeh
from bokeh.models import ColumnDataSource, GeoJSONDataSource
import json

def df_aroma_aftertaste(datapath):
    """
    Creates the disctionary used in the aroma x aftertaste plot

    Entries: {country : [mean aroma, mean aftertaste]}
    """

    #Fixing bad names in "Country of Origin" column
    new_df = pd.DataFrame(datapath)
    new_df["Country of Origin"] = new_df["Country of Origin"].replace(["Tanzania, United Republic Of"], "Tanzania")
    new_df["Country of Origin"] = new_df["Country of Origin"].replace(["United States (Hawaii)"], "Hawaii")
    
    #Counts how many times each country occurs and puts that in a dictionary
    countries_and_amount_occurences = new_df["Country of Origin"].value_counts().to_frame().reset_index()
    countries_and_amount_occurences.columns = ["Countries", "Amount of Occurences"]
    dict_countries_and_amount_occurences = dict(zip(countries_and_amount_occurences["Countries"],
                                                    countries_and_amount_occurences["Amount of Occurences"]))

    #Creates a dicionary of which the keys are different countries and
    #the values are lists of the total aroma and aftertaste
    aroma_aftertaste = {}
    for index_of_table in range(len(datapath["Country of Origin"])):

        country = datapath["Country of Origin"][index_of_table]
        aroma = datapath["Aroma"][index_of_table]
        aftertaste = datapath["Aftertaste"][index_of_table]

        #If the country already exists in aroma_aftertaste, its value will be the current value of aroma and aftertaste.
        #Otherwise, we add the existing value in aroma_aftertaste with the current values
        if country not in aroma_aftertaste:
            aroma_aftertaste[country] = [aroma, aftertaste]
        else:
            aroma_aftertaste[country] = [ x + y for x, y in zip(aroma_aftertaste[country], [aroma, aftertaste]) ]

    #Divide the associated with each country by its amount of occurences,
    #giving us a dictionary with the mean values
    mean_aroma_aftertaste = aroma_aftertaste
    for country1 in dict_countries_and_amount_occurences:
        for country2 in aroma_aftertaste:
            if country1 == country2:
                mean_aroma_aftertaste[country1] = [x / dict_countries_and_amount_occurences[country1] for x in aroma_aftertaste[country1]]
    
    return mean_aroma_aftertaste

def df_variety_method(datapath):
    """
    Creates the dataframe used in the variety x method plot

    Columns: "Variety", "Processing Method"
    """
    
    #Creating new dataframe for manipulation
    df_varieties_method = datapath

    #Deleting rows with missing values
    df_varieties_method = df_varieties_method.dropna(subset="Processing Method")
    df_varieties_method = df_varieties_method.dropna(subset="Variety")
    df_varieties_method = df_varieties_method[df_varieties_method["Variety"] != "unknown"]
    df_varieties_method = df_varieties_method[df_varieties_method["Variety"] != "unknow"]
    
    #Fixing bad names in "Processing Method" column
    df_varieties_method ["Processing Method"] = df_varieties_method ["Processing Method"].replace(["SEMI-LAVADO"], "Semi Washed")
    df_varieties_method ["Processing Method"] = df_varieties_method ["Processing Method"].replace(["Honey,Mossto"], "Mossto / Honey")
    df_varieties_method ["Processing Method"] = df_varieties_method ["Processing Method"].replace(["Pulped natural / honey"], "Pulped Natural / Honey")
    df_varieties_method ["Processing Method"] = df_varieties_method ["Processing Method"].replace(["Anaerobico 1000h"], "Double Anaerobic Washed")

    #Fixing bad names in the "Variety" column
    df_varieties_method["Variety"] = df_varieties_method["Variety"].str.replace("+", ",")
    df_varieties_method["Variety"] = df_varieties_method["Variety"].str.replace(" and ", ",")
    df_varieties_method["Variety"] = df_varieties_method["Variety"].str.replace(" Y ", ",")
    df_varieties_method["Variety"] = df_varieties_method["Variety"].str.replace(", ", ",")
    df_varieties_method["Variety"] = df_varieties_method["Variety"].str.replace(" , ", ",")
    df_varieties_method["Variety"] = df_varieties_method["Variety"].str.replace(" & ", ",")
    df_varieties_method["Variety"] = df_varieties_method["Variety"].str.replace("-", ",")
    df_varieties_method["Variety"] = df_varieties_method["Variety"].str.replace(" ,", ",")
    df_varieties_method["Variety"] = df_varieties_method["Variety"].str.lower()

    new_varieties = [] #list that will contain lists containing varieties
    new_methods = [] #list that will contain the respective methods
    for index in range(len(df_varieties_method["Variety"])):
        split_varieties = df_varieties_method["Variety"].iloc[index].split(",")
        new_varieties.append(split_varieties)
        times = 0
        while times < len(split_varieties):
            new_methods.append(df_varieties_method["Processing Method"].iloc[index])
            times += 1

    #Fixing bad names in "Variety" column
    for index in range(len(new_varieties)):
        if new_varieties[index] == ["typica bourbon caturra catimor"]:
            new_varieties[index] = ["typica", "bourbon", "caturra", "catimor"]
            new_methods.insert(index + 1, new_methods[index])
            new_methods.insert(index + 2, new_methods[index])
            new_methods.insert(index + 3, new_methods[index])
        elif new_varieties[index] == ["typica gesha"]:
            new_varieties[index] = ["typica", "gesha"]
            new_methods.insert(index + 1, new_methods[index])

    #Smoothing the entries
    smooth_new_varieties = []
    smooth_new_methods = new_methods
    for list in new_varieties:
        for element in list:
            smooth_new_varieties.append(element)
            

    #Fixing capitalization
    smooth_new_varieties = [variety.title() for variety in smooth_new_varieties]
    for index in range(len(smooth_new_varieties)):
        if smooth_new_varieties[index] == "Colombia Blend":
            smooth_new_varieties[index] = "Colombia"
        elif smooth_new_varieties[index] == "Shg":
            smooth_new_varieties[index] = "SHG"
        elif smooth_new_varieties[index] == "Sl28":
            smooth_new_varieties[index] = "SL28"
        elif smooth_new_varieties[index] == "Sl34":
            smooth_new_varieties[index] = "SL43"
        elif smooth_new_varieties[index] == "Sl14":
            smooth_new_varieties[index] = "SL14"

    new_df = {
        "Variety" : smooth_new_varieties,
        "Processing Method" : smooth_new_methods
    }

    return pd.DataFrame(new_df)

def df_country_kilos(datapath):
    """
    Creates the dataframe used in the country x kilos plot

    Columns: "Countries", "Kilos of Coffee"
    """
    
    #Creating dataframe for manipulation
    df_country_total_kilos = datapath

    #Fixing bad names in "Country of Origin" column
    df_country_total_kilos["Country of Origin"] = df_country_total_kilos["Country of Origin"].replace(["Tanzania, United Republic Of"], "Tanzania")
    df_country_total_kilos["Country of Origin"] = df_country_total_kilos["Country of Origin"].replace(["United States (Hawaii)"], "Hawaii")

    #Deleting suspiciously high values
    df_country_total_kilos = df_country_total_kilos.drop(labels=[35, 116], axis=0)
    
    #Deleting missing values
    df_country_total_kilos = df_country_total_kilos.dropna(subset="Number of Bags")
    df_country_total_kilos = df_country_total_kilos.dropna(subset="Bag Weight")

    #Taking only the numerical part of "Bag Weight"'s registers
    for index in range(len(df_country_total_kilos["Bag Weight"])):
        entry = df_country_total_kilos["Bag Weight"].iloc[index].replace(",", ".")
        entry = entry.split(" ")
        df_country_total_kilos["Bag Weight"].iloc[index] = float(entry[0])
   
    list_of_kilos = [] #list that will contain the kilos of each lot, associated to country
    for index in range(len(df_country_total_kilos["Number of Bags"])):
        kilos = int(df_country_total_kilos["Number of Bags"].iloc[index])*int(df_country_total_kilos["Bag Weight"].iloc[index])
        list_of_kilos.append(kilos)
    
    list_of_all_countries = [country for country in df_country_total_kilos["Country of Origin"]]
    countries = [] #list that will contain countries without repetition
    kilos_per_country = [] #list that will contain the kilos of each country in order
    for index in range(len(list_of_kilos)):
        if list_of_all_countries[index] not in countries:
            countries.append(list_of_all_countries[index])
            kilos_per_country.append(list_of_kilos[index])
        else:
            for subindex in range(len(countries)):
                if countries[subindex] == list_of_all_countries[index]:
                    kilos_per_country[subindex] += list_of_kilos[index]

    new_df = {
        "Countries" : countries,
        "Kilos of Coffee" : kilos_per_country
    }

    return pd.DataFrame(new_df)

def get_df_acidity_flavor(dataframe):
    #Groups dataframe by flavor and acidity columns
    grouped_dataframe = dataframe.groupby(["Acidity", "Flavor"])

    #Get the count of how many times each pair of flavor and acidity appeared
    #(scores are binned, so points overlap if this isn't done)
    count_dataframe = grouped_dataframe.size().to_frame().reset_index()
    count_dataframe = count_dataframe.rename(columns = {0: "count"})

    #Color schale to the points
    color_scale = ["#939393", "#7E7E7E", "#696969", "#545454",
                   "#3F3F3F", "#2A2A2A", "#151515", "#000000"]

    #Auxiliary function to help adding the color scheme to the dataframe
    def get_color_by_row(row):
        number = int(row["count"]) - 1
        return color_scale[number]

    #Create a new column with the color corresponding to the number of times
    #each pair appeared
    count_dataframe["Color"] = count_dataframe.apply(get_color_by_row, axis = 1)

    #Create collumn with size (using count directily would make the dots very small)
    count_dataframe["Size"] = count_dataframe["count"] + 3

    return ColumnDataSource(count_dataframe)

def get_geojson_with_coffee_data(dataframe):
    #Group the dataframe by country
    grouped_dataframe = dataframe.groupby("Country of Origin")
    #Get a dictionary containing the mean of overall score for each country
    means = grouped_dataframe["Overall"].mean().to_dict()

    #Opens the GEOjson file containing the world map
    #File downloaded at https://datahub.io/core/geo-countries
    with open("countries.geojson", "r") as f:
        world_map = json.load(f)

    #Iter through each contry in the map dicitionary
    for country in world_map["features"]:
        #Add the value of the country overall score in the country info in GeoJSON
        #If it doesn't have a value, it gets a 0
        country_name = country["properties"]["ADMIN"]
        if country_name in means.keys():
            country["properties"]["Overall_mean"] = means[country_name]
        else:
            country["properties"]["Overall_mean"] = 0

    bokeh_map_data_source = GeoJSONDataSource(geojson = json.dumps(world_map))
    return bokeh_map_data_source

def get_cds_altitude_country(dataframe):
    #Gets dataframe with clean altitude data
    df = get_df_mean_altitude(dataframe[["Altitude", "Country of Origin"]])

    #Removes altitudes bigger than 4200 (they only appear in countries that
    #doesn't have lands so high, so its fair to assume they're wrong)
    df = df[df["Mean Altitude"] < 4200]
    #Removes countries with insuficcient data to plot a boxplot
    df = df[df["Country of Origin"] != "Myanmar"]
    df = df[df["Country of Origin"] != "Panama"]
    df = df[df["Country of Origin"] != "Madagascar"]
    #Group the dataframe by country
    grouped_dataframe = df.groupby("Country of Origin")
    #Gets a list of quantiles for altituteds, respecting country grouping
    quantiles = grouped_dataframe["Mean Altitude"].quantile([0.25, 0.5, 0.75])
    quantiles = quantiles.unstack().reset_index()
    quantiles.columns = ["Country of Origin", "q1", "q2", "q3"]

    #Adds basic quantil data to each row in original dataframe
    df = pd.merge(df, quantiles, on = "Country of Origin", how = "left")

    #Creates two columns with the whisker limits data
    quantil_distance = df["q3"] - df["q1"]
    df["upper"] = df["q3"] + (1.5 * quantil_distance)
    df["lower"] = df["q1"] - (1.5 * quantil_distance)

    cds = ColumnDataSource(df)
    country_list = df["Country of Origin"].unique()

    #Filter dataframe to get only rows where the value of altitude isn't between
    #whisker limits, in order to plot them
    outliers = df[~df["Mean Altitude"].between(df["lower"], df["upper"])]
    cds_outliers = ColumnDataSource(outliers)
    return cds,  country_list, cds_outliers

def get_correlation_matrix(dataframe):
    """
    Calculates the correlation matrix for the sensory attributes of the dataset.

    Args:
        dataframe (pandas.DataFrame): The input DataFrame containing the Arabica Coffee data.

    Returns:
        pandas.DataFrame: The correlation matrix with sensory variables as row and column indices,
                          and correlation values as the 'correlation' column.
    """

    # Specify the columns to consider for correlation
    columns = ["Aroma", "Flavor", "Aftertaste", "Acidity", "Body", "Balance", "Clean Cup", "Sweetness", "Overall", "Total Cup Points"]

    # Select the columns from the dataframe
    df = dataframe[columns]

    # Compute the correlation matrix
    df = df.corr()

    # Set index and column names for the correlation matrix
    df.index.name = 'sensory_variables1'
    df.columns.name = 'sensory_variables2'

    # Reshape the correlation matrix to a long format
    correlation_matrix = df.stack().rename("correlation").reset_index()

    return correlation_matrix

def get_df_mean_altitude(dataframe):
    
    df = dataframe.reset_index().dropna()

    mean_altitudes = []
    
    for index, row in df.iterrows():
        altitude = str(row["Altitude"])
        
        if '-' in altitude:
            min_altitude, max_altitude = altitude.split('-')
            mean_altitude = (int(min_altitude) + int(max_altitude)) / 2
        elif "A" in altitude:
            min_altitude, max_altitude = altitude.split('A')
            mean_altitude = (int(min_altitude) + int(max_altitude)) / 2
        elif "~" in altitude:
            min_altitude, max_altitude = altitude.split('~')
            mean_altitude = (int(min_altitude) + int(max_altitude)) / 2
        else:
            mean_altitude = int(altitude)
            
        mean_altitudes.append(mean_altitude)
    
    df['Mean Altitude'] = mean_altitudes

    return df
