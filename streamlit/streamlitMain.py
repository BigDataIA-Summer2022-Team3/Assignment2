import streamlit as st
import webbrowser
import streamlit.components.v1 as components
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import requests 

st.markdown('# Login Page')


#.text_input("X"), X can not use same key
#button can not use same key
if st.sidebar.button("Reset"):
    st.empty()

#need "pip install streamlit-authenticator==0.1.5"
#usernames
names = ["zhijie_li", "yijun_lin", "damg7245_team4", "parth_shah", "srikanth_krishnamurthy"]
usernames = ["zhijie", "yijun", "team4", "parth", "srikanth"]

#load passwords
file_path = Path(__file__).parent / "streamlitUserPW.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)
    
authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "streamlitMain", "abcdef", cookie_expiry_days=0)

name, authentication_status, username = authenticator.login("Login" , "main")

def load_token():
    url = "http://damg7245-zhijie.herokuapp.com/token"
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


# Initialization
if "token" not in st.session_state:
    st.session_state["token"] = ""

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'sidebar')
    st.markdown(f'# Welcome *{st.session_state["name"]}*')
    load_token();
    # st.warning(st.session_state["token"]) #

elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')

