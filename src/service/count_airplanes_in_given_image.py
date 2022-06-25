from read_csv_from_s3 import read_csv_from_s3


def count_airplanes_in_given_image(image_id):
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
        result = {}
        result['number_of_airplanes'] = df1.loc[: ,"count"].sum().item()
        return result;
    except:
        # return all locations of airplanes 
        return "Sorry, we don't find the picture. Please check you enter info."

# print(count_airplanes_in_given_image("d9399a45-6745-4e59-8903-90640b2ddf9f.jpg"))