from PIL import ImageDraw
from image_from_s3 import image_from_s3
from collections import defaultdict
import pandas as pd
from pathlib import Path

def display_top_aircraft(image_id, limit_of_number, isMaximum):
    try:
      if limit_of_number < 0 or limit_of_number > 10: 
         return "limit_of_image should between [1,10]"     
    except TypeError:
      return "Please enter two integer number."
      
    # Read csv file about all airplanes with coordinate
    path = Path(__file__).parent / "airplane.csv"
    with path.open() as f:
        plane = pd.read_csv(f)

    if(len(plane[plane["image_id"]==image_id]) == 0):
        return "No image found related to the image_id. Try effective image_id"
    
    try:
        img = image_from_s3(image_id)
        image = ImageDraw.Draw(img)
    except: 
        return "Failed to download image from S3."
    
    
    # Get all airplanes info on the image and sort with (Width and Height) of bounding boxes 
    test = plane[plane["image_id"]==image_id]
    test.insert(0, "plane_size", test["width"]+test["height"])
    if(isMaximum == True):
        test1 = test.sort_values("plane_size", ascending=False)
    else: 
        test1 = test.sort_values("plane_size", ascending=True)
    test1.reset_index(drop=True, inplace=True)

    # Add Bounding Boxes on most biggest airplanes on image
    coordinate = defaultdict(dict)
    if(len(test1.index) >= limit_of_number):
        maximum = limit_of_number
    else: 
        maximum = len(test1.index)
    for i in range(maximum):
        coordinate[i]["Xmin"] = test1.at[i, "Xmin"].item()
        coordinate[i]["Ymin"] = test1.at[i, "Ymin"].item()
        coordinate[i]["Xmax"] = test1.at[i, "Xmax"].item()
        coordinate[i]["Ymax"] = test1.at[i, "Ymax"].item()

        tuple = (test1.at[i, "Xmin"], test1.at[i,"Ymin"], test1.at[i, "Xmax"], test1.at[i, "Ymax"])
        rect = image.rectangle(tuple, outline="red", width=5)
        i+=1

    img.show()

    return dict(coordinate); 

# res = display_top_aircraft("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg",5, True)
# print(res)