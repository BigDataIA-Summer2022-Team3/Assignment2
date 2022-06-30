# from turtle import st
from ast import If
from random import random
from fastapi import FastAPI, Request
from requests import request
from has_aircraft_in_given_x_y_coordinate import has_aircraft_in_given_x_y_coordinate
from display_smallest_aircraft import display_smallest_aircraft
from display_biggest_aircraft import display_biggest_aircraft
from count_airplanes_in_given_image import count_airplanes_in_given_image
from return_images_with_given_number_of_aircraft import return_images_with_given_number_of_aircraft
from return_images_with_maximum_airplanes import return_images_with_maximum_airplanes
from return_images_with_truncated_aircraft import return_images_with_truncated_aircraft
import json
from collections import defaultdict
import logging
import time
import random
import string

logging.config.fileConfig('logging.conf')

logger = logging.getLogger(__name__)

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem}||start request path={request.url.path}")
    start_time = time.time()
    
    response = await call_next(request)
    
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(f"rid={idem}||completed_in={formatted_process_time}ms||status_code={response.status_code}")
    
    return response

@app.get("/img/airplane/location")
def HasAircraftInGivenLocation(x_loc: int, y_loc: int, image_id: str):
    """image_id should be str, x_loc & y_loc is int between (0, 2560)

    Definition: Input image_id and x, y coordinate in the image
    Find if there is airplane in the location, display the whole image with bounding box on the very airplane
    if no airplane in given location, give all bounding box coordinates with airplanes, 
    as list of tuple of (Xmin, Ymin, Xmax, Ymax)
    """
    if(image_id == None):
       image_id = "5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg"
        #todo
    result = has_aircraft_in_given_x_y_coordinate(image_id, x_loc, y_loc);
    if(result == "No image found related to the image_id. Try effective image_id"):
       logger.warn("Invalid Image ID Input")
    elif(result == "Input X and Y should within (0,10)"):
       logger.warn("Out of range number")
    return result;

@app.get("/img/display/big")
async def DisplayBiggestAircraft(image_id: str, limit_of_number: int=5):
    """image_id should be str, limit_of_number is maximum of output airplanes, is int
    
    Definition: On chosen image, display biggest airplanes with red bounding boxes, and return their coordinates
    """
    result = display_biggest_aircraft(image_id, limit_of_number)
    if(result == "No image found related to the image_id. Try effective image_id"):
       logger.warn("Invalid Image ID Input")
    elif(result == "Input X and Y should within (0,2560)"):
       logger.warn("Out of range number")
    return result;

@app.get("/img/display/small")
async def DisplaySmallestAircraft(image_id: str, limit_of_number: int=5):
    """image_id should be str, limit_of_number is maximum of output airplanes, is int
    
    Definition: On chosen image, display smallest airplanes with red bounding boxes, and return their coordinates
    """
    result = display_smallest_aircraft(image_id, limit_of_number);
    if(result == "No image found related to the image_id. Try effective image_id"):
       logger.warn("Invalid Image ID Input")
    elif(result == "Input X and Y should within (0,10)"):
       logger.warn("Out of range number")
    return result;

@app.get("/img/airplanes/count")
async def CountAirplanes(image_id: str):
    """Documentation: 
    1. Definition: user enter a picture id, system will return how much aircraft in the picture
    2. Steps: 1) function will read data from particular address
                 if system find get the data, it will continue running
                 if system can't find the address, it will return "Sorry, the data missing."
              2) user enter a picture id, 
                 if user enter a correct id, it will continue running
                 if user enter a wrong id, system will return "Sorry, we don't find the picture."
              3) function will get the sum and return the number
    """
    result = count_airplanes_in_given_image(image_id)
    if(result == "Sorry, we don't find the picture. Please check you enter info."):
       logger.warn("Invalid Image ID Input")
    return result;

@app.get("/img/airplanes/givenNumber")
async def ReturnImagesWithGivenNumberOfAircraft(contain_aircraft_number: int, limit_of_image: int=5):
    """Documentation: 
    1. Definition: user enter a number X and limit number of image Y, function will fund those picture has X aircraft, and return Y pieces of picture, Y should small or eauql 10.
    2. Steps: 1) function will read data from particular address
                 if system find get the data, it will continue running
                 if system can't find the address, it will return "Sorry, the data missing."
              2) check X, Y
                 if X, Y are correct, system will continue running
                 if user enter wrong type info, it will return "Please enter integer number"
                 if X,Y < 0, it will return "The number should be positive"
                 if Y > 10, it will return "limit_of_image should between [1,10]"
              3) fund picture
                 if system find match pictures, and those pictures number >= user need's number, function will return Y pieces of picture
                 if system find match pictures, but those pictures number < user need's number, function will return those pictures it found and "Sorry, we don't have more pictures"
                 if system didn't find match picture, function will return "Sorry, we don't find your needed"
    """
    result = return_images_with_given_number_of_aircraft(contain_aircraft_number, limit_of_image)
    if(result == "The number should be positive" or result == "Sorry, we don't find your needed" or result == "limit_of_image should between [1,10]"):
       logger.warn("Out of range number")
    return result;

@app.get("/img/airplanes/maximum")
async def ReturnImagesWithMaximumAircraft(number_of_image: int=1):
    """Documentation: 
    1. Definition: user enter num of image X, The system will return the top X pictures with the most aircraft, X should small or equal than 10
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
    result = return_images_with_maximum_airplanes(number_of_image)
    if(result == "limit_of_image should between [1,10]"):
       logger.warn("Out of range number")
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
    if(result == "limit_of_image should between [1,10]"):
       logger.warn("Out of range number")
    return result;