from image_from_s3 import image_from_s3
from read_csv_from_s3 import read_csv_from_s3
from collections import defaultdict


def return_images_with_given_number_of_aircraft(contain_aircraft_number, limit_of_image=5):
    # check data address
    try:
      df = read_csv_from_s3("image_planes_num.csv")
    except:
        return "Sorry, the data missing."
        
    #check input numbers
    try:
      if contain_aircraft_number < 0 or limit_of_image < 0:
         return "The number should be positive"
         
      if limit_of_image > 10:
         return "limit_of_image should between [1,10]"
         
    except TypeError:
      return "Please enter two integer number."
      
    
    withSum = df.groupby(["index"])["count"].sum().reset_index(name="sum")
    df3 = withSum[withSum['sum'] == contain_aircraft_number]
    df4 = df3.head(limit_of_image)['index']

    # didn't found picture
    if df4.count() == 0:
      return "Sorry, we don't find your needed"
      
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
   
    return result;

# print(return_images_with_given_number_of_aircraft(30, 3))