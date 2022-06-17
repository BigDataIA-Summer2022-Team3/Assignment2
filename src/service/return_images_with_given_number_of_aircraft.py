import pandas as pd
import os

def return_images_with_given_number_of_aircraft(contain_aircraft_number, limit_of_image) -> str:
    ## Input integer of how many aircraft contains 
    # Iterate through all images, find images that contains given number of aircraft
    # display up to 5 of them 
    # return number of these image

    # if no image contain such number of aircraft, return none
    # if input < 0 return error

    """

    """

    df = pd.read_csv("../data/processed/image_planes_num.csv")

    withSum = df.groupby(["index"])["count"].sum().reset_index(name="sum")
    df3 = withSum[withSum['sum'] == contain_aircraft_number]
    return df3.head(limit_of_image)