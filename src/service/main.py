from fastapi import FastAPI
from has_aircraft_in_given_x_y_coordinate import has_aircraft_in_given_x_y_coordinate
from display_biggest_aircraft import display_biggest_aircraft
from count_airplanes_in_given_image import count_airplanes_in_given_image
from return_images_with_given_number_of_aircraft import return_images_with_given_number_of_aircraft
from return_images_with_maximum_airplanes import return_images_with_maximum_airplanes
from return_images_with_truncated_aircraft import return_images_with_truncated_aircraft
from get_coordinates_of_all_airplanes import get_coordinates_of_all_airplanes

app = FastAPI()


@app.get("/img/airplane/location")
def HasAircraftInGivenLocation(x_loc: int, y_loc: int, image_id: str):
    """image_id should be str, x_loc & y_loc is int between (0, 2560)

    Definition: Input image_id and x, y coordinate in the image
    Find if there is airplane in the location, display the whole image with bounding box on the very airplane
    if the given location is contained in one airplane, the coordinate of this airplane will be returned as Xmin, Ymin, Xmax, Ymax
    """
    if(image_id == None):
       image_id = "5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg"
        #todo
    result = has_aircraft_in_given_x_y_coordinate(image_id, x_loc, y_loc);
    return result;


@app.get("/img/airplanes/coordinates")
async def GetCoordinates(image_id):
   """Documentation"""
   result = get_coordinates_of_all_airplanes(image_id)
   return result;


@app.get("/img/display")
async def DisplayBiggestAircraft(image_id: str, limit_of_number: int=5, isMaximum: bool=True):
    """image_id should be str, limit_of_number is maximum of output airplanes
    Set isMaximum to True: get most biggest airplanes on the image
    Otherwise: get smallest airplanes
    
    Definition: On chosen image, display biggest or smallest airplanes with red bounding boxes, and return their coordinates
    """
    result = display_biggest_aircraft(image_id, limit_of_number, isMaximum)
    return result;


@app.get("/img/airplanes/count")
async def CountAirplanes(image_id: str):
    """Documentation: 
    1. Definition: user enter a image_id, return how many aircraft image
    2. Steps: 1) Read csv data from S3 
              2) Enter a valid image id
               load image info from the csv file and get sum of aircraft
    """
    result = count_airplanes_in_given_image(image_id)
    return result;


@app.get("/img/airplanes/givenNumber")
async def ReturnImagesWithGivenNumberOfAircraft(contain_aircraft_number: int, limit_of_image: int=5):
    """Documentation: 
    1. Definition: user enter a number X and limit number of image Y, find those picture has X aircraft, and return Y pictures.
         X is recommended to be within 20 and 100
    2. Steps: 1) Read csv of all images info from S3
              2) check X, Y should be integer
                 if user enter wrong type, it will return "Please enter integer number"
                 if X or Y < 0, it will return "The number should be positive"
                 Y should be no more than 10
              3) Find image contains requested number of airplanes
                 if images match, and those pictures number >= user need's number, return Y pieces of picture
                 if images match, but those pictures number < user need's number, return those pictures it found and "Sorry, we don't have more pictures"
                 if don't find match picture, return "No image in database has matching number of airplanes"
    """
    result = return_images_with_given_number_of_aircraft(contain_aircraft_number, limit_of_image)
    return result;


@app.get("/img/airplanes/maximum")
async def ReturnImagesWithMaximumAircraft(number_of_image: int=1):
    """Documentation: 
    1. Definition: user enter num of image X, The system will return the top X pictures with the most aircraft, X should small or equal than 10
    2. Steps: 1) Read csv image info from S3
              2) user enter a num of image, 
                 if user enter a wrong type num, system will return "Please enter integer number"
                 if num of image < 0, or num of image > 10, it will return "The number should between [1,10]"
              3) find picture and return top X pictures
    """
    result = return_images_with_maximum_airplanes(number_of_image)
    return result;


@app.get("/img/airplanes/truncated")
async def ReturnImageWithTruncatedAircraft(number_of_image: int=3):
    """Documentation: 
    1. Definition: user enter num of image X, The system will return the top X pictures with the most truncated aircraft, X should small or equal than 10
    2. Steps: 1) function will read data from particular address
                 if system find get the data, it will continue running
                 if system can't find the address, it will return "Sorry, the data missing."
              2) user enter a num of image, 
                 if user enter a correct num, it will continue running
                 if user enter a wrong type num, system will return "Please enter integer number"
                 if num of image < 0, or num of image > 10, it will return "The number should between [1,10]"
              3) fund picture
                 function will return top X pictures
    """
    result = return_images_with_truncated_aircraft(number_of_image)
    return result;