import pandas as pd
from read_csv_from_s3 import read_csv_from_s3

"""Documentation: 
    1. Definition: user enter a picture id, system will return how much aircraft in the picture
    2. Steps: 1) function will read data from particular address
                 if system find get the data, it will continue running
                 if system can't find the address, it will return "Sorry, the data missing."
              2) user enter a picture id, 
                 if user enter a correct id, it will continue running
                 if user enter a wrong id, system will return "Sorry, we don't find the picture."
              3) function will get the sum and return the number
    """
def count_airplanes_in_given_image(image_id):

    # use 014de911-7810-4f7d-8967-3e5402209f4a.jpg as example
   ## Input image_id and compute how many aircraft contains in the given image
   ## return integer
   ## if image_id has no found responding image, throw error: no such image

    # check data address
    try:
        df = read_csv_from_s3("image_planes_num.csv")
        #df = pd.read_csv("D:\VisualStudioCodeProgram\Assignment1\data\processed\image_planes_num.csv")
    except FileNotFoundError:
        return "Sorry, the data missing."
        
    # check found picture, or not
    try:
        df1 = df[df['index']==image_id]
        if df1.loc[: ,"count"].sum() == 0:
            return  "Sorry, we don't find the picture. Please check you enter info."
        return df1.loc[: ,"count"].sum()
    except:
        return "Sorry, we don't find the picture. Please check you enter info."

# print(count_airplanes_in_given_image("d9399a45-6745-4e59-8903-90640b2ddf9f.jpg"))