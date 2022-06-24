from turtle import st
from fastapi import FastAPI
from has_aircraft_in_given_x_y_coordinate import HasAircraftInGiven

app = FastAPI()

# @app.get("/img/airplane")
# def HasAircraftInGiven(image_id: str = None, x_loc: int, y_loc: int):
