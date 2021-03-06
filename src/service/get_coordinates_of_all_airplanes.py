from collections import defaultdict
import pandas as pd
from pathlib import Path

def get_coordinates_of_all_airplanes(image_id):
    # Read csv file about all airplanes with coordinate
    path = Path(__file__).parent / "airplane.csv"
    with path.open() as f:
        plane = pd.read_csv(f)
    
    df = plane[plane["image_id"]==image_id]
    if(len(df) == 0):
      return "No image found related to the image_id. Try effective image_id"
      
    df.reset_index(drop=True, inplace=True)

    coordinate = defaultdict(dict)
    for i in range(len(df.index)):
      coordinate[i]["Xmin"] = df.at[i, "Xmin"].item()
      coordinate[i]["Ymin"] = df.at[i, "Ymin"].item()
      coordinate[i]["Xmax"] = df.at[i, "Xmax"].item()
      coordinate[i]["Ymax"] = df.at[i, "Ymax"].item()
      i += 1

    coordinates = dict(coordinate)
    return {"image_id": image_id, "coordinates": coordinates}

# print(get_coordinates_of_all_airplanes("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg"))