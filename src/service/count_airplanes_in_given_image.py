from read_csv_from_s3 import read_csv_from_s3
from image_from_s3 import image_from_s3
from PIL import ImageDraw

def count_airplanes_in_given_image(image_id):
   ## Input image_id and compute how many aircraft contains in the given image
   ## if image_id has no found responding image, throw error: no such image

    # check data address
    try:
        df = read_csv_from_s3("image_planes_num.csv")
        plane = read_csv_from_s3("airplane.csv")
    except:
        return "Failed to read csv from S3."
        
    # check if picture is found
    df1 = df[df['index']==image_id]
    if len(df1) == 0:
        return "No image found related to the image_id. Try effective image_id"
    
    test = plane[plane["image_id"]==image_id]
    test.reset_index(drop=True, inplace=True)
    
    try:
        img = image_from_s3(image_id)
        image = ImageDraw.Draw(img)
    except: 
        return "Failed to download image from S3."
    
    for i in range(len(test.index)):
        tuple = (test.at[i, "Xmin"].item(), test.at[i,"Ymin"].item(), test.at[i, "Xmax"].item(), test.at[i, "Ymax"].item())
        rect = image.rectangle(tuple, outline="red", width=5)
    
    img.show()
    result = {}
    result['number_of_airplanes'] = df1.loc[: ,"count"].sum().item()
    return result;


# print(count_airplanes_in_given_image("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg"))