from image_from_s3 import image_from_s3
from read_csv_from_s3 import read_csv_from_s3
from collections import defaultdict


def return_images_with_truncated_aircraft(limit_of_images):
    #check data address
    try:
      df = read_csv_from_s3("image_planes_num.csv")
    except:
        return "Sorry, the data missing."
        

    #check input numbers
    try:
      if limit_of_images < 0 or limit_of_images > 10:
         return "limit_of_image should between [1,10]"
         
    except TypeError:
      return "Please enter integer number."
      

    hasTruncated = df[df['class'] == "Truncated_airplane"]
    df4 = hasTruncated.sort_values(by="count", ascending=False)
    df5 = df4.head(limit_of_images)['index']

    result = defaultdict(dict)
    num = 0
    for i in df5:
        img = image_from_s3(i)
        img.show()
        result[num]["img_id"] = i
        # result[num]['number_of_truncated_airplanes'] = df4[df4["index"]==i].count().item()
        num += 1;

    return result;

# return_images_with_truncated_aircraft(2)
        