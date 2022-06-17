import pandas as pd
import os
from PIL import Image, ImageDraw

def has_aircraft_in_given_x_y_coordinate(image_id, x_loc, y_loc):
    ## Input image_id and x, y coordinate  x (0, 2560)
    #  if the location of the image has a aircraft, return true, else return false

    """if false, return [] all other geometry contains airplane
    
    if true return image which has bounds box on entered location"""
    plane = pd.read_csv("../data/processed/airplane.csv")

    img = Image.open(r"/Users/lizhijie_1/Downloads/Aircraft-Detection/images/"+str(image_id))
    image = ImageDraw.Draw(img)
    
    test = plane[plane["image_id"]==image_id]
    test.reset_index(drop=True, inplace=True)

    coordinate = []
    for i in range(len(test.index)):
        tuple = (test.at[i, "Xmin"], test.at[i,"Ymin"], test.at[i, "Xmax"], test.at[i, "Ymax"])
        coordinate.append(tuple)
        if(x_loc>=tuple[0] and x_loc <= tuple[2] and 
            y_loc >= tuple[1] and y_loc <= tuple[3]):
            rect = image.rectangle(tuple, outline="red", width=5)
            img.show()
            return "Found"
        i+=1

    return "No airplane in given coordinate, here is all location that has airplanes", coordinate;