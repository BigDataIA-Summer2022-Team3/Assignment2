import boto3
import io
from PIL import Image
import config

# ACKEY = os.environ["ACKEY"]
# SCKEY = os.environ["SCKEY"]

ACKEY = config.ACKEY
SCKEY = config.SCKEY

s3 = boto3.resource('s3',
                    region_name = 'us-east-1',
                    aws_access_key_id= ACKEY,
                    aws_secret_access_key= SCKEY)

def image_from_s3(image_id):

    bucket = s3.Bucket('damg-aircraft-dev')
    image = bucket.Object("images/"+str(image_id))
    
    img_data = image.get().get('Body').read()
    print("Download image: " + str(image_id) )

# Image.open(io.BytesIO(img_data))
    return img_data

