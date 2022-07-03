import streamlit as st
import requests
import io
from PIL import Image


def load_token():
    if "token" not in st.session_state:
        st.session_state["token"] = ""

    url = "http://127.0.0.1:5001/token"
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

def api1():
    st.header("API 1: Search aircraft by Location")
    st.sidebar.subheader("Search aircraft in an Location")
    if "token" not in st.session_state:
        st.session_state["token"] = ""

    fun1val1 = st.sidebar.number_input("x_loc: [Pick a number between (0,2560)]",0 ,2560 ,step = 100)
    fun1val2 = st.sidebar.number_input("y_loc: [Pick a number between (0,2560)]",0 ,2560 ,step = 100)
    fun1val3 = st.sidebar.text_input("image_id", max_chars= 50)
    if st.sidebar.button("Select"):
        # (f"https://damg7245-zhijie.herokuapp.com/img/airplane/location?x_loc={fun1val1}&y_loc={fun1val2}&image_id={fun1val3}")
        
        url = f"http://127.0.0.1:5001/img/airplane/location?x_loc={fun1val1}&y_loc={fun1val2}&image_id={fun1val3}"
        header = {"Authorization": "Bearer "+ token, "accept": "application/json"}
        res = requests.get(url=url, headers = header)
        meta = res.json()

        if(res.text[0] == '"'):
            st.write("No image found related to your image id. Try effective image id") 
        else:
            if(meta["has_airplane"] == False):
                st.write("No airplane in this place, try another location.")
            else: 
                st.write("There is a airplane! 🎉")
                xmin, ymin, xmax, ymax = meta["coordinate"]["Xmin"], meta["coordinate"]["Ymin"], meta["coordinate"]["Xmax"], meta["coordinate"]["Ymax"];
                response = requests.get(f"http://damg7245-zhijie.herokuapp.com/s3/img/location?image_id={fun1val3}&Xmin={xmin}&Ymin={ymin}&Xmax={xmax}&Ymax={ymax}")
                i = Image.open(io.BytesIO(response.content))
                st.image(i)
           
            st.subheader("Metadata:")
            st.json( meta )

api1()    


