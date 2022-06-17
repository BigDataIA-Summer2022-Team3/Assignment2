import pandas as pd
import os



def count_airplanes_in_given_image(image_id):
    """Documentation:
    1. Definition
    2. Steps
    3. Unit test(corner cases)
    """

    # use 014de911-7810-4f7d-8967-3e5402209f4a.jpg as example
   ## Input image_id and compute how many aircraft contains in the given image
   ## return integer
   ## if image_id has no found responding image, throw error: no such image

    df = pd.read_csv("../data/processed/image_planes_num.csv")
    df1 = df[df['index']==True]
    return df1.loc[: ,"count"].sum()