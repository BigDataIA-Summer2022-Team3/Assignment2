import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ["zhijie_li", "yijun_lin", "damg7245_team4", "parth_shah", "srikanth_krishnamurthy"]
usernames = ["zhijie", "yijun", "team4", "parth", "srikanth"]

file_path = Path(__file__).parent.parent / "streamlitUserPW.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "streamlitMain", "abcdef", cookie_expiry_days=0)

if st.session_state["authentication_status"]:
    st.title(" Unit tests for APIs")
    st.subheader('Username')
    authenticator.logout('Logout', 'sidebar')

else:
    st.markdown('# Please go to streamlitMain login')    
