import pandas as pd
import os

def return_images_with_maximum_airplanes(number_of_image):
    """
    Documentation:
    1. Definition
    2. Steps
    3. Unit test(corner cases)
    """

    df = pd.read_csv("../data/processed/image_planes_num.csv")

    withSum = df.groupby(["index"])["count"].sum().reset_index(name="sum")
    df2 = withSum.sort_values(by="sum", ascending=False)
    return df2.head(number_of_image);