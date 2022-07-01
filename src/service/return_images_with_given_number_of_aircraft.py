from image_from_s3 import image_from_s3
from collections import defaultdict
import pandas as pd
from pathlib import Path

def return_images_with_given_number_of_aircraft(contain_aircraft_number, limit_of_image=5):
    #check input numbers
    try:
      if contain_aircraft_number < 0 or limit_of_image < 0:
        return "Both Input numbers should be positive"     
      if limit_of_image > 10:
        return "limit_of_image should between [1,10]"   
    except TypeError:
      return "Please enter two integer number."

    path2 = Path(__file__).parent / "image_planes_num.csv"
    with path2.open() as f1:
      df = pd.read_csv(f1)
    
    withSum = df.groupby(["index"])["count"].sum().reset_index(name="sum")
    df3 = withSum[withSum['sum'] == contain_aircraft_number]
    df4 = df3.head(limit_of_image)['index']

    # didn't found picture
    if df4.count() == 0:
      return "No image in database has {contained} airplanes. Please try another possible number".format(contained=contain_aircraft_number);
      
    result = defaultdict(dict)
    num = 0
    for i in df4:
      img = image_from_s3(i)
      img.show()
      result[num]["img_id"] = i
      num += 1;

    # found picture less than user needed
    if df4.count() < limit_of_image:
      print("Sorry, we don't have more pictures.")
   
    return dict(result);

# print(return_images_with_given_number_of_aircraft(30, 3))