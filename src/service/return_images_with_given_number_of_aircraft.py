from image_from_s3 import image_from_s3
from read_csv_from_s3 import read_csv_from_s3

"""Documentation: 
    1. Definition: user enter a number X and limit number of image Y, function will fund those picture has X aircraft, and return Y pieces of picture, Y should small or eauql 10.
    2. Steps: 1) function will read data from particular address
                 if system find get the data, it will continue running
                 if system can't find the address, it will return "Sorry, the data missing."
              2) check X, Y
                 if X, Y are correct, system will continue running
                 if user enter wrong type info, it will return "Please enter integer number"
                 if X,Y < 0, it will return "The number should be positive"
                 if Y > 10, it will return "limit_of_image should between [1,10]"
              3) fund picture
                 if system find match pictures, and those pictures number >= user need's number, function will return Y pieces of picture
                 if system find match pictures, but those pictures number < user need's number, function will return those pictures it found and "Sorry, we don't have more pictures"
                 if system didn't find match picture, function will return "Sorry, we don't find your needed"
    """
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
      

    # print pictures
    for i in df4:
      img = image_from_s3(i)
      img.show()
      print("image_id: "+ i)

    # found picture less than user needed
    if df4.count() < limit_of_image:
      print("Sorry, we don't have more pictures.")
   
    return "Finish"

# print(return_images_with_given_number_of_aircraft(30, 3))