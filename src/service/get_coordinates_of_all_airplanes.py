from read_csv_from_s3 import read_csv_from_s3
from collections import defaultdict

def get_coordinates_of_all_airplanes(image_id):
    # Read csv file about all airplanes with coordinate and download related image from S3
    try:
      plane = read_csv_from_s3("airplane.csv")
    except:
      return "Failed to read csv from S3."
    
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
    
    return {"image_id": image_id, "coordinates": coordinate}

# print(get_coordinates_of_all_airplanes("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg"))