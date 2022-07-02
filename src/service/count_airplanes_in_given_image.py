from image_from_s3 import image_from_s3
from PIL import ImageDraw
import pandas as pd
from pathlib import Path

def count_airplanes_in_given_image(image_id):
   ## Input image_id and compute how many aircraft contains in the given image
   ## if image_id has no found responding image, throw error: no such image

    path = Path(__file__).parent / "airplane.csv"
    with path.open() as f:
        plane = pd.read_csv(f)
    path2 = Path(__file__).parent / "image_planes_num.csv"
    with path2.open() as f1:
        df = pd.read_csv(f1)
        
    # check if picture is found
    df1 = df[df['index']==image_id]
    if len(df1) == 0:
        return "No image found related to the image_id. Try effective image_id"
    
    test = plane[plane["image_id"]==image_id]
    test.reset_index(drop=True, inplace=True)
    
    # try:
    #     img = image_from_s3(image_id)
    #     image = ImageDraw.Draw(img)
    # except: 
    #     return "Failed to download image from S3."
    
    # for i in range(len(test.index)):
    #     tuple = (test.at[i, "Xmin"].item(), test.at[i,"Ymin"].item(), test.at[i, "Xmax"].item(), test.at[i, "Ymax"].item())
    #     rect = image.rectangle(tuple, outline="red", width=5)
    
    # img.show()
    result = {}
    result['number_of_airplanes'] = df1.loc[: ,"count"].sum().item()
    return result;


print(count_airplanes_in_given_image("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg"))
# print(count_airplanes_in_given_image(""))