import pandas as pd

"""
Definition: This server not working for user, it will creat a new table to save index_id, class, count. The table group bu index_id and class
        index_id: the id for picture 
        class: Airplane/Truncated_airplane
        count: num of Airplane/Truncated_airplane
"""
def create_second_table(CSVfile_address = "data/raw/MetaData.csv"):
    df = pd.read_csv(CSVfile_address)
    hn = df.groupby(["image_id","class"])["class"].count().reset_index(name="count")
    hn.to_csv("data/processed/image_planes_num2.csv")
    print("Finish")

create_second_table("data/raw/MetaData.csv")