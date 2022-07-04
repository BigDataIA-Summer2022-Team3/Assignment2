import streamlit as st
import requests
import io
from PIL import Image


# Initialization
if "token" not in st.session_state:
    st.session_state["token"] = ""


def load_token(dbusername): # To do: get hashed password
    url = "http://127.0.0.1:5001/token"
    header = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    pw = dbusername + "pw"
    data = {
                "grant_type":"",  "scope": "", "client_id": "", "client_secret": "",
                "username": dbusername, "password": pw   # to do 
            }
    
    authentication = requests.post(url, data, header) 
    st.json(authentication.json())     
    # token = authentication.json()["access_token"]
    # if(st.session_state["token"] == "" ): 
        # st.session_state["token"] = token

name = "zhijie"
load_token(name)

token = st.session_state["token"] 
st.warning("token: " + token)
header = {"Authorization": "Bearer "+ token, "accept": "application/json"}


def api5():
    st.header("API 5: Search for images by numbers of airplanes")
    st.sidebar.subheader("Search by numbers of airplanes")

    fun5val1 = st.sidebar.number_input("contain aircraft number [Pick a number between (20,100)]",20 ,100)
    fun5val2 = st.sidebar.number_input("limit of number [Pick a number between (1,10)]",1 ,10)

    if st.sidebar.button("Select"):
        url = f'https://127.0.0.1:5001/img/airplanes/givenNumber?contain_aircraft_number={fun5val1}&limit_of_image={fun5val2}'
        header = {"Authorization": "Bearer "+ token, "accept": "application/json"}
        res = requests.get(url=url, headers = header)
        meta = res.json()
        
        if(res.text[0] == '"'):
            st.write(f"No image in database has {fun5val1} airplanes. Please try another one")            
        else: 
            st.write(f"Congratulations! You find it the image with {fun5val1} airplanes 🎉")
            meta = res.json()
            for i in range(len(meta)):
                i_id = meta[str(i)]["img_id"]

                img_url = f"http://127.0.0.1:5001/s3/img?image_id={i_id}"
                response = requests.get(url = img_url, headers = header)
                i = Image.open(io.BytesIO(response.content))
                st.image(i)

            st.subheader("Metadata:")
            st.json( res.json() )

api5();