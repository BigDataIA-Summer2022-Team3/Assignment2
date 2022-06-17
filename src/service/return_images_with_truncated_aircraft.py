import pandas as pd
# import os

def return_all_images_with_truncated_aircraft(limit_of_images):
    """ Input 5 would reutrn at most 5 image_id of truncated images
    """
    df = pd.read_csv("../../data/processed/image_planes_num.csv")

    hasTruncated = df[df['class'] == "Truncated_airplane"]
    df4 = hasTruncated.sort_values(by="count", ascending=False)
    return df4.head(limit_of_images)

        