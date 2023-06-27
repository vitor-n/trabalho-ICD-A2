
def apply_default_style(p):
    """
    
    Receives a Bokeh figure() object and applies style elements

        Parameter: Bokeh figure() object

        Return: figure() object with elements of style
        
    """
    
    #Axis
    p.xaxis.axis_label_text_font_size = '15px'
    p.yaxis.axis_label_text_font_size = "15px"
    p.xaxis.axis_label_text_font_style = "bold"
    p.yaxis.axis_label_text_font_style = "bold"
    p.yaxis.axis_label_text_font = "Modern Love"
    p.xaxis.axis_label_text_font = "Modern Love"

    #Title
    p.title.text_font = "Modern Love"
    p.title.text_font_size = "30px"
    p.title.align = "left"
    
    #Grid
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    #Background
    p.background_fill_color = "#FFC300"
    p.background_fill_alpha = 0.2

    #Toolbar
    p.toolbar.logo = None
    p.toolbar.autohide = True 

    return p

def apply_dotplot_style(p):
    """

    Receives a Bokeh figure() object and applies style elements meant for dotplots

        Parameter: Bokeh figure() object

        Return: figure() object with style applied
    """

    #Applies default style to get font styles and sizes
    p = apply_default_style(p)

    #Customize grids
    p.grid.grid_line_color = "lightgrey"
    p.grid.grid_line_alpha = 0.9
    p.grid.minor_grid_line_color = "lightgrey"
    p.grid.minor_grid_line_alpha = 0.5 #Weakier grids for minor ticks
    p.grid.minor_grid_line_dash = "dotdash"

    return p

def apply_map_style(p):
    """

    Receives a Bokeh figure() object and applies style elements meant for the map

        Parameter: Bokeh figure() object

        Return: figure() object with style applied
    """

    #Applies default style to get font styles and sizes
    p = apply_default_style(p)

    #Change background and gridlines to fit the map colors
    p.background_fill_color = "lightblue"
    p.background_fill_alpha = 1
    p.grid.grid_line_color = "white"
    p.grid.grid_line_alpha = 0.5

    #Remove minor ticks
    p.xaxis[0].ticker.num_minor_ticks = 0
    p.yaxis[0].ticker.num_minor_ticks = 0

    #Remove tick labels
    p.axis.major_label_text_font_size = "0px"

    return p
