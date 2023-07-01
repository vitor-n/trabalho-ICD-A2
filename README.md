# Trabalho A2 - Introdução a Ciência de Dados

by Larissa Lemos, Pedro Tokar and Vitor Nascimento

## About the Dataset

In the present work, we made visualizations about coffee quality using Bokeh. The dataset used was obtained from the Coffee Quality Institute, a reference institution in the evaluation and certification of coffee quality on a global scale. The dataset is avaiable at kaggle [Coffee Quality Data CQI](https://www.kaggle.com/datasets/fatihb/coffee-quality-data-cqi). The dataset contains data collected in May 2023, and include a wide range of coffee lots that were sent for evaluation.

## About Coffee and QCI

Coffee is a widely appreciated and consumed drink, playing a fundamental role in the culture and economy of various countries. Understanding and assessing coffee quality is of utmost importance for producers, exporters, roasters and baristas.The [Coffee Quality Institute](https://www.coffeeinstitute.org/) (QCI) plays a crucial role in this context, being responsible for establishing standards and guidelines for the evaluation and classification of coffee quality. Its work is essential to ensure excellence and consistency in the coffee market, promoting the appreciation and recognition of high-quality coffees.

## Module Descriptions

This project consists of several modules designed to perform specific tasks. Here's an overview of each module:

### df_manipulation.py
The `df_manipulation.py` module is responsible for manipulating, formatting, and cleaning the data from the database. It provides functions to perform various operations on the data, ensuring it is in the desired format for the desidered visualization.

### graph_plot.py
The `graph_plot.py` module's purpose is to create a Bokeh figure objects for visualizing the data. It contains functions that generate different types of plots based on the processed data.

### graph_style.py
The `graph_style.py` module applies predefined themes and styles to the Bokeh figures created in `graph_plot.py`. It provides two default styles.
### import_data.py
The `import_data.py` module handles the process of importing the data from the database into the Bokeh framework. It includes functions to establish connections, fetch data, and transform it into a format compatible with Bokeh's data structures. This module acts as a bridge between the database and the visualization components.

### main.py
The `main.py` module serves as the entry point for generating the HTML page with the visualizations. It utilizes the functions from the other modules to create the HTML pages for each graph. 


## The Webpage
The page is constructed using HTML's `<iframe>` tag to embed the graphs within the main page. JavaScript is employed to enable transitions between the graphs and text. You can see the page here: [Coffee Visualizations](https://vito0182.github.io/trabalho-ICD-A2/).
