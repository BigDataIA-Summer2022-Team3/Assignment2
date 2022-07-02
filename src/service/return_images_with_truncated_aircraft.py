from image_from_s3 import image_from_s3
from collections import defaultdict
import pandas as pd
from pathlib import Path


def return_images_with_truncated_aircraft(limit_of_images):
    #check input numbers
    try:
      if limit_of_images < 0 or limit_of_images > 10:
         return "limit_of_image should between [1,10]"
    except TypeError:
      return "Please enter integer number."

    #check data address
    path2 = Path(__file__).parent / "image_planes_num.csv"
    with path2.open() as f1:
        df = pd.read_csv(f1)
        

    hasTruncated = df[df['class'] == "Truncated_airplane"]
    df4 = hasTruncated.sort_values(by="count", ascending=False)
    df5 = df4.head(limit_of_images)['index']

    result = defaultdict(dict)
    num = 0
    for i in df5:
        result[num]["img_id"] = i
        result[num]['number_of_truncated_airplanes'] = df4[df4["index"]==i]["count"].item()
        num += 1;

    return dict(result);

# print(return_images_with_truncated_aircraft(2))
        