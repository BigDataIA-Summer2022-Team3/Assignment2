# from turtle import st
from fastapi import FastAPI
from has_aircraft_in_given_x_y_coordinate import has_aircraft_in_given_x_y_coordinate
from display_smallest_aircraft import display_smallest_aircraft
from display_biggest_aircraft import display_biggest_aircraft
from count_airplanes_in_given_image import count_airplanes_in_given_image
from return_images_with_given_number_of_aircraft import return_images_with_given_number_of_aircraft
from return_images_with_maximum_airplanes import return_images_with_maximum_airplanes
from return_images_with_truncated_aircraft import return_images_with_truncated_aircraft
import json
from collections import defaultdict

app = FastAPI()

@app.get("/img/airplane/location")
def HasAircraftInGivenLocation(x_loc: int, y_loc: int, image_id: str):
    if(image_id == None):
       image_id = "5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg"
        #todo
    result = has_aircraft_in_given_x_y_coordinate(image_id, x_loc, y_loc);
    return result;

@app.get("/img/display/big")
async def DisplayBiggestAircraft(image_id: str, limit_of_number: int=5):
    result = display_biggest_aircraft(image_id, limit_of_number)
    return result;

@app.get("/img/display/small")
async def DisplaySmallestAircraft(image_id: str, limit_of_number: int=5):
    result = display_smallest_aircraft(image_id, limit_of_number); 
    return result;

@app.get("/img/airplanes/count")
async def CountAirplanes(image_id: str):
    result = count_airplanes_in_given_image(image_id)
    return result;

@app.get("/img/airplanes/givenNumber")
async def ReturnImagesWithGivenNumberOfAircraft(contain_aircraft_number: int, limit_of_image: int=5):
    result = return_images_with_given_number_of_aircraft(contain_aircraft_number, limit_of_image)
    return result;

@app.get("/img/airplanes/maximum")
async def ReturnImagesWithMaximumAircraft(number_of_image: int=1):
    result = return_images_with_maximum_airplanes(number_of_image)
    return result;

@app.get("/img/airplanes/truncated")
async def ReturnImagesWithMaximumAircraft(number_of_image: int=3):
    result = return_images_with_truncated_aircraft(number_of_image)
    return result;