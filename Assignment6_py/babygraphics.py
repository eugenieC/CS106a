"""
File: babygraphics.py
---------------------
Add your comments here
"""

import tkinter
from tkinter.constants import NW
from tkinter.constants import SW
import babynames
import babygraphicsgui as gui


# Provided constants to load and draw the baby data
FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE  = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (float): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_loc = GRAPH_MARGIN_SIZE + year_index*width
    return x_loc


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas
    width = canvas.winfo_width()    # get the width of the canvas
    height = canvas.winfo_height()  # get the height of the canvas
    # add your code here
    # margin border
    # top
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, WINDOW_WIDTH-GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE,fill='black' )
    # bottom
    canvas.create_line(GRAPH_MARGIN_SIZE, WINDOW_HEIGHT-GRAPH_MARGIN_SIZE, WINDOW_WIDTH-GRAPH_MARGIN_SIZE,WINDOW_HEIGHT-GRAPH_MARGIN_SIZE,fill='black' )
    # lines for year
    x_interval = int((WINDOW_WIDTH-2*GRAPH_MARGIN_SIZE)/len(YEARS))
    for i in range(len(YEARS)):
        x_cord = get_x_coordinate(x_interval,i)
        canvas.create_line(x_cord, 0, x_cord,WINDOW_HEIGHT,fill='black')
        canvas.create_text(x_cord+3, WINDOW_HEIGHT-GRAPH_MARGIN_SIZE+3, text=YEARS[i],anchor=NW,fill='black')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dictionary of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
        name_data (dictionary): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot
    """
    draw_fixed_lines(canvas)
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    # add your code here

    x_interval = int((WINDOW_WIDTH-2*GRAPH_MARGIN_SIZE)/len(YEARS))
    y_interval = (WINDOW_HEIGHT-2*GRAPH_MARGIN_SIZE)/MAX_RANK

    name_serial=0
    for name in lookup_names:
        #check name is on the name_data
        if name in name_data.keys():
            for yr in YEARS:
                yr_index = YEARS.index(yr)

                # should not the latest year
                if yr_index != (len(YEARS)-1):
                    yr_index_1 = yr_index + 1
                    yr_1 = YEARS[yr_index_1]
                    #check yr present on the name's
                    yr_included=0
                    if yr in name_data[name].keys():
                        yr_rank =name_data[name][yr]
                        yr_included=1
                    else:
                        yr_rank=MAX_RANK


                    yr_included_1=0
                    if yr_1 in name_data[name].keys():
                        yr_rank_1 =name_data[name][yr_1]
                        yr_included_1=1
                    else:
                        yr_rank_1=MAX_RANK


                    x_cord = get_x_coordinate(x_interval,yr_index)
                    y_cord = GRAPH_MARGIN_SIZE+int(yr_rank*y_interval)

                    x_cord_1 = get_x_coordinate(x_interval,yr_index_1)
                    y_cord_1 = GRAPH_MARGIN_SIZE+int(yr_rank_1*y_interval)


                    # canvas.create_text(100*yr_index, 250, text=x_cord,anchor=NW)
                    # canvas.create_text(100*yr_index, 350, text=y_cord,anchor=NW)

                    canvas.create_line(x_cord, y_cord, x_cord_1, y_cord_1,fill=COLORS[name_serial])

                    #name + rank
                    if yr_included==1:
                        name_rank_text = name + " " + str(yr_rank)
                    else:
                        name_rank_text = name + " *" 
                    canvas.create_text(x_cord, y_cord, text=name_rank_text,anchor=SW,fill=COLORS[name_serial])
                else:
                    if yr_included_1==1:
                        name_rank_text = name + " " + str(yr_rank_1)
                    else:
                        name_rank_text = name + " *"                    
                    canvas.create_text(x_cord_1, y_cord_1, text=name_rank_text,anchor=SW,fill=COLORS[name_serial])
            name_serial+=1



# main() code is provided for you
def main():
    import sys
    args = sys.argv[1:]
    global WINDOW_WIDTH
    global WINDOW_HEIGHT
    if len(args) == 2:
        WINDOW_WIDTH = int(args[0])
        WINDOW_HEIGHT = int(args[1])

    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Make window
    top = tkinter.Tk()
    top.wm_title('Baby Names Solution')
    canvas = gui.make_gui(top, WINDOW_WIDTH, WINDOW_HEIGHT, name_data, draw_names, babynames.search_names)

    # draw_fixed once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This needs to be called just once
    top.mainloop()


if __name__ == '__main__':
    main()
