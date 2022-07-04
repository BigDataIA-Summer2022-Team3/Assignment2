from distutils.util import execute
import streamlit as st
import webbrowser
import streamlit.components.v1 as components
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import pymysql
import requests

st.markdown('# Login Page')
#need pymysql
#need "pip install streamlit-authenticator==0.1.5"
#usernames

usernames = ["zhijie", "yijun", "team4", "parth", "srikanth"]

#load passwords
file_path = Path(__file__).parent / "streamlitUserPW.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)
    
authenticator = stauth.Authenticate(usernames, usernames, hashed_passwords, "streamlitMain", "abcdef", cookie_expiry_days=0)

name, authentication_status, username = authenticator.login("Login" , "main")

def load_token(dbusername): #password if has
    url = "http://damg7245-zhijie.herokuapp.com/token"
    #url = "http://127.0.0.1:5001/token"
    header = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
                "grant_type":"",  "scope": "", "client_id": "", "client_secret": "",
                "username": dbusername, "password": dbusername + "pw"  # to do 
                
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
    
    con = pymysql.connect(host = '96.9.209.237', user = 'lemon', password = 'lemon@123', database = 'lemon', charset = "utf8")
    c = con.cursor()
    c.execute('select * from user_table where username = "%s"' % st.session_state.username)
    datainfo = c.fetchall()
    dbusername = datainfo[0][1]
    
    st.session_state
    load_token(dbusername) #dbpassword if has
    
    
    
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')

