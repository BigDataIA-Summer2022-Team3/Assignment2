from random import random
from fastapi import FastAPI, Request, Response
import logging
import time
import random
import string
from download_image_with_top_airplanes import download_image_with_top_airplanes
from image_from_s3 import image_from_s3
from has_aircraft_in_given_x_y_coordinate import has_aircraft_in_given_x_y_coordinate
from display_top_aircraft import display_top_aircraft
from count_airplanes_in_given_image import count_airplanes_in_given_image
from image_with_bounding_airplane import image_with_bounding_airplane
from return_images_with_given_number_of_aircraft import return_images_with_given_number_of_aircraft
from return_images_with_maximum_airplanes import return_images_with_maximum_airplanes
from return_images_with_truncated_aircraft import return_images_with_truncated_aircraft
from get_coordinates_of_all_airplanes import get_coordinates_of_all_airplanes

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
   idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
   
   logger.info(f"{request.url.path}")
   
   response = await call_next(request)
 
   return response



@app.get("/img/airplane/location")
def Has_Aircraft_in_Given_Location(x_loc: int, y_loc: int, image_id: str):
   """image_id should be str, x_loc & y_loc is int between (0, 2560)

   Definition: Input image_id and x, y coordinate in the image
   Find if there is airplane in the location, display the whole image with bounding box on the very airplane
   if the given location is contained in one airplane, the coordinate of this airplane will be returned as Xmin, Ymin, Xmax, Ymax
   """
   
   result = has_aircraft_in_given_x_y_coordinate(image_id, x_loc, y_loc);
   if(result == "No image found related to the image_id. Try effective image_id"):
      logger.warn("Invalid_Image_ID_Input")
   elif(result == "Input X and Y should within (0,2560)"):
      logger.warn("Out_of_range_number")
   return result;


@app.get("/img/airplanes/coordinates")
async def Get_all_Coordinates(image_id):
   """Documentation:
   Return coordinates of all airplanes in an image, in form of Xmin, Ymin, Xmax, Ymax"""
   result = get_coordinates_of_all_airplanes(image_id)
   if(result == "No image found related to the image_id. Try effective image_id"):
      logger.warn("Invalid_Image_ID_Input")
   return result;


@app.get("/img/display")
async def Display_Top_Aircraft(image_id: str, limit_of_number: int=1, isMaximum: bool=True):
    """image_id should be str, limit_of_number [n] is maximum of output airplanes

   If [isMaximum]: True,  Get the coordinates of biggest [n] airplanes with bounding boxes
   
      [isMaximum]: False, Get the coordinates of smallest [n] airplanes with bounding boxes
    
    Definition: On chosen image, display biggest or smallest airplanes with red bounding boxes, and return their coordinates
    """
    result = display_top_aircraft(image_id, limit_of_number, isMaximum)
    if(result == "No image found related to the image_id. Try effective image_id"):
       logger.warn("Invalid_Image_ID_Input")
    elif(result == "Input X and Y should within (0,10)"):
       logger.warn("Out_of_range_number")

    return result;


@app.get("/img/airplanes/count")
async def Count_Airplanes(image_id: str):
   """Documentation: 
   1. Definition: user enter a image_id, return how many aircraft image
   2. Steps: 1) Read csv data from S3 
            
            2) Enter a valid image id
            load image info from the csv file and get sum of aircraft
   """
   result = count_airplanes_in_given_image(image_id)
   if(result == "No image found related to the image_id. Try effective image_id"):
      logger.warn("Invalid_Image_ID_Input")
   return result;


@app.get("/img/airplanes/givenNumber")
async def Return_Images_with_Given_Number_of_Aircraft(contain_aircraft_number: int=20, limit_of_image: int=1):
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
   if(result == "The number should be positive" or result == "Sorry, we don't find your needed" or result == "limit_of_image should between [1,10]"):
      logger.warn("Out of range number")
   return result;


@app.get("/img/airplanes/maximum")
async def Return_Images_with_Maximum_Aircraft(number_of_image: int=1):
   """Documentation: 
   1. Definition: user enter num of image X, The system will return the top X pictures with the most aircraft, X should small or equal than 10
   2. Steps:1) Read csv image info from S3

            2) user enter a num of image, 
               if user enter a wrong type num, system will return "Please enter integer number"
               if num of image < 0, or num of image > 10, it will return "The number should between [1,10]"
            
            3) find picture and return top X pictures
   """
   result = return_images_with_maximum_airplanes(number_of_image)
   if(result == "limit_of_image should between [1,10]"):
      logger.warn("Out_of_range_number")
   return result;


@app.get("/img/airplanes/truncated")
async def Return_Image_with_Truncated_Aircraft(number_of_image: int=1):
   """Documentation: 
   1. Definition: user enter num of image X, return the top X pictures with the most truncated aircraft, X should be Integer
   2. Steps: 1) Read data from S3

            2) user enter a num of image, 
               number_of_image should be within [1,10]
               if user enter a wrong type num, system will return "Please enter integer number"
               if num of image < 0, or num of image > 10, it will return "The number should between [1,10]"
            
            3) find picture and return top X pictures               
   """
   result = return_images_with_truncated_aircraft(number_of_image)
   if(result == "limit_of_image should between [1,10]"):
      logger.warn("Out of range number")
   return result;


@app.get("/s3/img")
async def Download_image_from_s3(image_id: str):
   """Read one image data from S3"""
   img_data = image_from_s3(image_id)
   return Response(content=img_data, media_type="image/jpg");


@app.get("/s3/img/airplanes")
async def Download_image_with_top_airplanes(image_id: str, limit_of_number: int=1, isMaximum: bool = True):
   """Read image data from S3 with bounding boxes in Top airplanes of biggest or smallest

   If [isMaximum]: True,  Get the biggest airplane with bounding boxes
   
      [isMaximum]: False, Get the smallest airplane with bounding boxes"""
   img_data = download_image_with_top_airplanes(image_id, limit_of_number, isMaximum)
   return Response(content=img_data, media_type="image/jpeg");


@app.get("/s3/img/location")
async def Download_image_with_bounding_airplane(image_id: str, Xmin: int, Ymin: int, Xmax: int, Ymax: int):
   """Draw the bounding box on input location"""
   img_data = image_with_bounding_airplane(image_id, Xmin, Ymin, Xmax, Ymax)
   return Response(content=img_data, media_type="image/jpeg");


