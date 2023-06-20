import pandas as pd
from import_data import import_df_for_bokeh

def df_variety_method(datapath):
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
