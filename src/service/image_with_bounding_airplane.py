from PIL import ImageDraw, Image
from image_from_s3 import image_from_s3
import io

def image_with_bounding_airplane(image_id, Xmin, Ymin, Xmax, Ymax):

    try:
        img_data = image_from_s3(image_id)
        img = Image.open(io.BytesIO(img_data))
        image = ImageDraw.Draw(img)
    except: 
        return "Failed to download image from S3."

    # Add Bounding Boxes on most biggest airplanes on image
    tuple = (Xmin, Ymin, Xmax, Ymax)
    image.rectangle(tuple, outline="red", width=5)   # Draw the rectangle

    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format="jpeg")
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr;