import boto3 
import os
import pandas as pd
import config

# ACKEY = os.environ["ACKEY"]
# SCKEY = os.environ["SCKEY"]

ACKEY = config.ACKEY
SCKEY = config.SCKEY

s3 = boto3.client('s3',
                    region_name = 'us-east-1',
                    aws_access_key_id= ACKEY,
                    aws_secret_access_key= SCKEY)

def read_csv_from_s3(key):
    """ key: file_name
    """
    s3_bucket_name='damg-aircraft' 

    obj = s3.get_object(Bucket = s3_bucket_name,
                        Key = 'meta/'+str(key)
                        )
    data = pd.read_csv(obj['Body'])
    print("Loaded csv!")
    return data
