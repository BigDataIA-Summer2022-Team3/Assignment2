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
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.markdown("# Functions Page")
    def api1():
        st.header("API 1: Search aircraft in Location")
        st.sidebar.header("API 1: Search aircraft in an Location")
        fun1val1 = st.sidebar.number_input("x_loc: [Pick a number between (0,2560)]",0 ,2560 ,step = 100)
        fun1val2 = st.sidebar.number_input("y_loc: [Pick a number between (0,2560)]",0 ,2560 ,step = 100)
        fun1val3 = st.sidebar.text_input("image_id", max_chars= 50)
        if st.sidebar.button("Select"):
            st.write('Finish1')
    
    def api2():
        st.header("API 2: Get airplanes coordinate in picture")
        st.sidebar.header("API 2: Get airplanes coordinate in picture")
        fun2val1 = st.sidebar.text_input("image_id", max_chars= 50)
        if st.sidebar.button("Select"):
            st.write('Finish2')
        
    def api3():
        st.header("API 3: Display the biggest or smallest aircraft in chosen picture")
        st.sidebar.header("API 3: Display the big or small aircraft in picture")
        fun3val1 = st.sidebar.text_input("image id", max_chars= 50)
        fun3val2 = st.sidebar.number_input("limit of number (Pick a number between (1,10))",1 ,10)
        fun3val3 = st.sidebar.selectbox("choose big or small", ["Big", "Small"])
        if st.sidebar.button("Select"):
            st.write('Finish3')
        
    def api4():
        st.header("API 4: Display the big or small aircraft in picture")
        st.sidebar.header("API 4: Display the big or small aircraft in picture")
        fun4val1 = st.sidebar.text_input("image id", max_chars= 50)
        if st.sidebar.button("Select"):
            st.write('Finish4')
        
    def api5():
        st.header("API 5: Search numbers of airplanes")
        st.sidebar.header("API 5: Search numbers of airplanes")
        fun5val1 = st.sidebar.number_input("contain aircraft number (Pick a number between (20,100))",20 ,100 ,step = 10)
        fun5val2 = st.sidebar.number_input("limit of number (Pick a number between (1,10))",1 ,10)
        if st.sidebar.button("Select"):
            st.write('Finish5')
        
    def api6():
        st.header("API 6: Search picture that contains maximum number of airplanes")
        st.sidebar.header("API 6: Search maximum airplanes of picture")
        fun6val1 = st.sidebar.number_input("number of image: [Pick a number between (1,10)]",1 ,10)
        if st.sidebar.button("Select"):
            st.write('Finish6')
        
    def api7():
        st.header("API 7: Search maximum truncated airplanes of picture")
        st.sidebar.header("API 7: Search maximum truncated airplanes of picture")
        fun7val1 = st.sidebar.number_input("number of image [Pick a number between (1,10)]",1 ,10)
        if st.sidebar.button("Select"):
            st.write('Finish7')
        

    funNum = {
        "API 1": api1,
        "API 2": api2,
        "API 3": api3,
        "API 4": api4,
        "API 5": api5,
        "API 6": api6,
        "API 7": api7
    }

    selectFun = st.sidebar.selectbox("choose API", funNum.keys())
    funNum[selectFun]()
else:
    st.markdown('# Please go to streamlitMain login')