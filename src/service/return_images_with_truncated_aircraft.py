from image_from_s3 import image_from_s3
from read_csv_from_s3 import read_csv_from_s3

"""Documentation: 
    1. Definition: user enter num of image X, The system will return the top X pictures with the most truncated aircraft, X should small or equal than 10
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
def return_all_images_with_truncated_aircraft(limit_of_images):
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

   # print pictures
    for i in df5:
        img = image_from_s3(i)
        img.show()
        print("image_id: "+ i)

    return "Finish"

# return_all_images_with_truncated_aircraft(2)
        