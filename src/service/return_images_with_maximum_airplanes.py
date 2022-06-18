from image_from_s3 import image_from_s3
from read_csv_from_s3 import read_csv_from_s3

"""Documentation: 
    1. Definition: user enter num of image X, The system will return the top X pictures with the most aircraft, X should small or equal than 10
    2. Steps: 1) function will read data from particular address
                 if system find get the data, it will continue running
                 if system can't find the address, it will return "Sorry, the data missing."
              2) user enter a num of image, 
                 if user enter a correct num, it will continue running
                 if user enter a wrong type num, system will return "Please enter integer number"
                 if num of image < 0, or num of image > 10, it will return "The number should between [1,10]"
              3) fund picture
                 function will return top X pictures
    """
def return_images_with_maximum_airplanes(number_of_image):
    #check data address
    try:
      df = read_csv_from_s3("image_planes_num.csv")
      
    except:
        return "Sorry, the data missing."
        

    #check input numbers
    try:
      if number_of_image < 0 or number_of_image > 10:
         return "limit_of_image should between [1,10]"
         
    except TypeError:
      return "Please enter integer number."
      

    withSum = df.groupby(["index"])["count"].sum().reset_index(name="sum")
    df2 = withSum.sort_values(by="sum", ascending=False)
    df3 = df2.head(number_of_image)['index']

    # print pictures
    for i in df3:
      img = image_from_s3(i)
      img.show()
      print("image_id: "+ i)

    return "Finish"

# return_images_with_maximum_airplanes(6)