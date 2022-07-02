from PIL import ImageDraw, Image
from image_from_s3 import image_from_s3
import pandas as pd
from pathlib import Path
import io

def download_image_with_top_airplanes(image_id, limit_of_number, isMaximum):
    try:
      if limit_of_number < 0 or limit_of_number > 10: 
         return "limit_of_image should between [1,10]"     
    except TypeError:
      return "Please enter two integer number."
      
    # Read csv file about all airplanes with coordinate
    path = Path(__file__).parent / "airplane.csv"
    with path.open() as f:
        plane = pd.read_csv(f)
    try:
        img_data = image_from_s3(image_id)
        img = Image.open(io.BytesIO(img_data))
        image = ImageDraw.Draw(img)
    except: 
        return "Failed to download image from S3."

    test = plane[plane["image_id"]==image_id]
    test.insert(0, "plane_size", test["width"]+test["height"])
    if(isMaximum == True):
        test1 = test.sort_values("plane_size", ascending=False)
    else: 
        test1 = test.sort_values("plane_size", ascending=True)
    test1.reset_index(drop=True, inplace=True)

    # Add Bounding Boxes on most biggest or smallest airplanes on image
    if(len(test1.index) >= limit_of_number):
        maximum = limit_of_number
    else: 
        maximum = len(test1.index)

    for i in range(maximum):
        tuple = (test1.at[i, "Xmin"], test1.at[i,"Ymin"], test1.at[i, "Xmax"], test1.at[i, "Ymax"])
        image.rectangle(tuple, outline="red", width=5)   # Draw the rectangle
        i+=1

    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format="jpeg")
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr;

# print(download_image_with_top_airplanes("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg", 1, True));