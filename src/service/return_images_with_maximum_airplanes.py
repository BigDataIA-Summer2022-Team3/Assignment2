from image_from_s3 import image_from_s3
from collections import defaultdict
import pandas as pd
from pathlib import Path

def return_images_with_maximum_airplanes(number_of_image):
    #check input numbers
    try:
      if number_of_image < 0 or number_of_image > 10:
         return "limit_of_image should between [1,10]"
         
    except TypeError:
      return "Please enter integer number."

    #check data address
    path2 = Path(__file__).parent / "image_planes_num.csv"
    with path2.open() as f1:
      df = pd.read_csv(f1)


    withSum = df.groupby(["index"])["count"].sum().reset_index(name="sum")
    df2 = withSum.sort_values(by="sum", ascending=False)
    df3 = df2.head(number_of_image)['index']

    result = defaultdict(dict)
    num = 0

    for i in df3:
      result[num]["img_id"] = i
      result[num]["num_of_airplanes"] = df2[df2["index"]==i]['sum'].item()
      num += 1;

    return dict(result);

# print(return_images_with_maximum_airplanes(2))