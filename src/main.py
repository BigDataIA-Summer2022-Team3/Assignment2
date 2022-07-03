from random import random
import logging,logging.config
import random
import string
from datetime import datetime, timedelta
from typing import Union
from fastapi import Depends, FastAPI, HTTPException, status, Request, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from service.download_image_with_top_airplanes import download_image_with_top_airplanes
from service.image_from_s3 import image_from_s3
from service.has_aircraft_in_given_x_y_coordinate import has_aircraft_in_given_x_y_coordinate
from service.display_top_aircraft import display_top_aircraft
from service.count_airplanes_in_given_image import count_airplanes_in_given_image
from service.image_with_bounding_airplane import image_with_bounding_airplane
from service.return_images_with_given_number_of_aircraft import return_images_with_given_number_of_aircraft
from service.return_images_with_maximum_airplanes import return_images_with_maximum_airplanes
from service.return_images_with_truncated_aircraft import return_images_with_truncated_aircraft
from service.get_coordinates_of_all_airplanes import get_coordinates_of_all_airplanes

logging.config.fileConfig('log/logging.conf')
logger = logging.getLogger(__name__)

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    },
    "yijun": {
        "username": "yijun",
        "full_name": "yijun_lin",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$d3/0FX35PD6KE7xXNAYtl.XEPZQf3dXZp6cINNXctetqbauvQ44BS",
        "disabled": False,
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]

@app.middleware("http")
async def log_requests(request: Request, call_next):
   idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
   
   logger.info(f"{request.url.path}")
   #start_time = time.time()
   response = await call_next(request) 
   #process_time = (time.time() - start_time) * 1000
   return response;


@app.get("/img/airplane/location")
def Has_Aircraft_in_Given_Location(x_loc: int, y_loc: int, image_id: str, 
                                    current_user: User = Depends(get_current_active_user)):
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
async def Get_all_Coordinates(image_id: str, current_user: User = Depends(get_current_active_user)):
   """Documentation:
   Return coordinates of all airplanes in an image, in form of Xmin, Ymin, Xmax, Ymax"""
   result = get_coordinates_of_all_airplanes(image_id)
   if(result == "No image found related to the image_id. Try effective image_id"):
      logger.warn("Invalid_Image_ID_Input")
   return result;


@app.get("/img/display")
async def Display_Top_Aircraft(image_id: str, limit_of_number: int=1, isMaximum: bool=True,
                                current_user: User = Depends(get_current_active_user) ):
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
async def Count_Airplanes(image_id: str, current_user: User = Depends(get_current_active_user)):
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
async def Return_Images_with_Given_Number_of_Aircraft(contain_aircraft_number: int=20, limit_of_image: int=1, 
                                                        current_user: User = Depends(get_current_active_user) ):
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
async def Return_Images_with_Maximum_Aircraft(number_of_image: int=1, current_user: User = Depends(get_current_active_user)):
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
async def Return_Image_with_Truncated_Aircraft(number_of_image: int=1, current_user: User = Depends(get_current_active_user)):
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
async def Download_image_from_s3(image_id: str, current_user: User = Depends(get_current_active_user)):
   """Read one image data from S3"""
   img_data = image_from_s3(image_id)
   return Response(content=img_data, media_type="image/jpg");


@app.get("/s3/img/airplanes")
async def Download_image_with_top_airplanes(image_id: str, limit_of_number: int=1, isMaximum: bool = True,
                                            current_user: User = Depends(get_current_active_user) ):
   """Read image data from S3 with bounding boxes in Top airplanes of biggest or smallest

   If [isMaximum]: True,  Get the biggest airplane with bounding boxes
   
      [isMaximum]: False, Get the smallest airplane with bounding boxes"""
   img_data = download_image_with_top_airplanes(image_id, limit_of_number, isMaximum)
   return Response(content=img_data, media_type="image/jpeg");


@app.get("/s3/img/location")
async def Download_image_with_bounding_airplane(image_id: str, Xmin: int, Ymin: int, Xmax: int, Ymax: int, 
                                                current_user: User = Depends(get_current_active_user) ):
   """Draw the bounding box on input location"""
   img_data = image_with_bounding_airplane(image_id, Xmin, Ymin, Xmax, Ymax)
   return Response(content=img_data, media_type="image/jpeg");


