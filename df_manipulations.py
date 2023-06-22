import pandas as pd
from import_data import import_df_for_bokeh

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
    
    print(kilos_per_country)

    new_df = {
        "Countries" : countries,
        "Kilos of Coffee" : kilos_per_country
    }

    return pd.DataFrame(new_df)
