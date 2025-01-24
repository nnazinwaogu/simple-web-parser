#Author - Nnazirim Nwaogu

#Imports
import pandas as pd

def decode_secret(url):
    #Constants specific to the document from the url
    #Used to index into the 
    X_COORD_INDEX = 0
    Y_COORD_INDEX = 2
    CHAR_COORD_INDEX = 1
    #Fetch the content of url as an HTML using pandas object pd and html5lib and
    #read the content of the HTML into a singleton list of a Dataframe using pd
    data_frame_list = pd.read_html(url, flavor='html5lib')

    #Store the Dataframe from the list
    data_frame = data_frame_list[0]

    #Sorting through the data to find the largest X and Y values to know how large to make grid (2D array)
    data_frame_sorted = data_frame.sort_values(by=[Y_COORD_INDEX, X_COORD_INDEX], axis=0, ascending=False, ignore_index=True)

    #Grab the largest x and y values
    largest_x = data_frame_sorted.iat[1,0]
    largest_y = data_frame_sorted.iat[1,2]

    #Create grid (2D array), using the largest x and y values as the bounds of the grid
    largest_x_int = int(largest_x)
    largest_y_int = int(largest_y)
    #increasing both by one accounts for python's zero indexing
    #instantiating the array this way takes care of the shallow copy issue
    #fill the array with blank spaces
    grid = [[' ' for i in range(largest_x_int+1)] for j in range(largest_y_int+1)]

    #The following logic puts each character into the grid via their coordinates
    #First, need to know how many rows of data there are
    rows = data_frame.index
    row_size = rows.max()

    current_row = 1 #start at one since row 0 contains the table headers
    while(current_row <= row_size):
        #Get the Character as well as it's x,y coordinates from the dataframe
        x_str = data_frame_sorted.iat[current_row, X_COORD_INDEX]
        y_str = data_frame_sorted.iat[current_row, Y_COORD_INDEX]
        ch = data_frame_sorted.iat[current_row, CHAR_COORD_INDEX]
        #Cast the x,y coordinates into integers from strings
        x = int(x_str)
        y = int(y_str)
        #Place character at the x and y coordinates in the grid
        grid[y][x] = ch
        #go unto the next row
        current_row = current_row + 1

    #print the grid of characters
    #starting at the back of the array ensures that the elements are printed with the correct orientation
    for row in grid[::-1]:
        #*row only prints the element from the array, not the additional '[,]', sep='' sets the seperation between elements to none
        print(*row, sep='')
    return None
