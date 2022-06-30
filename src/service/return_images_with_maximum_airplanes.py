from image_from_s3 import image_from_s3
from read_csv_from_s3 import read_csv_from_s3
from collections import defaultdict


def return_images_with_maximum_airplanes(number_of_image):
    #check data address
    try:
      df = read_csv_from_s3("image_planes_num.csv")      
    except:
        return "Failed to read csv from S3."

    #check input numbers
    try:
      if number_of_image < 0 or number_of_image > 10:
         return "limit_of_image should between [1,10]"
         
    except TypeError:
      return "Please enter integer number."
      

    withSum = df.groupby(["index"])["count"].sum().reset_index(name="sum")
    df2 = withSum.sort_values(by="sum", ascending=False)
    df3 = df2.head(number_of_image)['index']
    # print(df2)

    result = defaultdict(dict)
    num = 0
    # print pictures
    for i in df3:
      img = image_from_s3(i)
      img.show()
      result[num]["img_id"] = i
      result[num]["num_of_airplanes"] = df2[df2["index"]==i]['sum'].item()
      num += 1;

    return result;

# return_images_with_maximum_airplanes(3)