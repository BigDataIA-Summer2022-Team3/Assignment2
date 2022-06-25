from PIL import ImageDraw
from image_from_s3 import image_from_s3
from read_csv_from_s3 import read_csv_from_s3

from fastapi import FastAPI
from collections import defaultdict

def has_aircraft_in_given_x_y_coordinate(image_id: str, x_loc: int, y_loc: int):
    """image_id should be str, x_loc & y_loc is int between (0, 2560)

    Definition: Input image_id and x, y coordinate in the image
    Find if there is airplane in the location, display the whole image with bounding box on the very airplane
    if no airplane in given location, give all bounding box coordinates with airplanes, 
    as list of tuple of (Xmin, Ymin, Xmax, Ymax)
    """
    # x_loc, y_loc = int(x_loc), int(y_loc)
    if(x_loc < 0 or x_loc > 2560 or y_loc < 0 or y_loc > 2560):
        return "Input X and Y should within (0,2560)"

    # Read csv file about all airplanes with coordinate and download related image from S3
    plane = read_csv_from_s3("airplane.csv")

    if(len(plane[plane["image_id"]==image_id]) == 0):
        return "No image found related to the image_id. Try effective image_id"

    try:
        img = image_from_s3(image_id)
        image = ImageDraw.Draw(img)

    except: 
        return "S3 error"
    
    # Filter with image_id and get all airplanes info on the image
    test = plane[plane["image_id"]==image_id]
    test.reset_index(drop=True, inplace=True)

    # Iterate through all airplanes, check if (x_loc, y_loc) with bounding box of (Xmin, Ymin) and (Xmax, Ymax)
    coordinate = defaultdict(dict)
    for i in range(len(test.index)):
        tuple = (test.at[i, "Xmin"].item(), test.at[i,"Ymin"].item(), test.at[i, "Xmax"].item(), test.at[i, "Ymax"].item())
        coordinate[i]["Xmin"] = test.at[i, "Xmin"].item()
        coordinate[i]["Ymin"] = test.at[i, "Ymin"].item()
        coordinate[i]["Xmax"] = test.at[i, "Xmax"].item()
        coordinate[i]["Ymax"] = test.at[i, "Ymax"].item()

        if(x_loc>=tuple[0] and x_loc <= tuple[2] and 
            y_loc >= tuple[1] and y_loc <= tuple[3]):
            rect = image.rectangle(tuple, outline="red", width=5)
            img.show()
            return {"image_id": image_id, "has_airplane": True, "coordinate": coordinate[i] }
            # "Found"
        i+=1

    sub_coordinate = dict((i, coordinate[i]) for i in range(3))
    return {"image_id": image_id, "has_airplane": False, "other_coordinate": sub_coordinate}

# print(has_aircraft_in_given_x_y_coordinate("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg",1600,500) )

# print(has_aircraft_in_given_x_y_coordinate("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg", 2000, 1600))

# has_aircraft_in_given_x_y_coordinate("12", 20,20)