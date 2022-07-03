import streamlit as st
import requests
import io
from PIL import Image


def load_token():
    if "token" not in st.session_state:
        st.session_state["token"] = ""

    url = "https://damg7245-zhijie.herokuapp.com/token"
    header = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
                "grant_type":"",  "scope": "", "client_id": "", "client_secret": "",
                "username": "johndoe", "password": "secret"  # to do 
            }
    
    authentication = requests.post(url, data, header)      
    token = authentication.json()["access_token"]
    if(st.session_state["token"] == "" ): 
        st.session_state["token"] = token
    return token


token = load_token()

def api3():
        st.header("API 3: Display the top big or small aircraft in one picture")
        fun3val1 = st.sidebar.text_input("image id", max_chars= 50)
        fun3val2 = st.sidebar.number_input("limit of number [Pick a number between (1,10)]",1 ,10)
        fun3flag = st.sidebar.selectbox("Do you want to the most biggest or smallest aircraft", ["Big", "Small"])  # to do ["Big", "Small"]
        if(fun3flag == "Big"):
            fun3val3 = "True"
        elif(fun3flag == "Small"):
            fun3val3 = "False"
        if st.sidebar.button("Select"):
            url = f"https://damg7245-zhijie.herokuapp.com/img/display?image_id={fun3val1}&limit_of_number={fun3val2}&isMaximum={fun3val3}"
            header = {"Authorization": "Bearer "+ token, "accept": "application/json"}
            res = requests.get(url=url, headers = header)

            if(res.text[0] == '"'):
                st.write("No image found related to your image id. Try effective image id") 
            else:

                img_url = f"http://damg7245-zhijie.herokuapp.com/s3/img/airplanes?image_id={fun3val1}&limit_of_number={fun3val2}&isMaximum={fun3val3}"
                response = requests.get(url = img_url, headers = header)
                i = Image.open(io.BytesIO(response.content))
                st.write(f"You Get {fun3val2} {fun3flag}est  airplanes! 🎉")
                st.image(i)
                st.subheader("Metadata:")
                st.json( res.json() ) 

api3()    


