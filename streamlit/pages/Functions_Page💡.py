import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import requests

names = ["zhijie_li", "yijun_lin", "damg7245_team4", "parth_shah", "srikanth_krishnamurthy"]
usernames = ["zhijie", "yijun", "team4", "parth", "srikanth"]

file_path = Path(__file__).parent.parent / "streamlitUserPW.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "streamlitMain", "abcdef", cookie_expiry_days=0)

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.markdown("## APIs Functions")
    def api1():
        st.header("API 1: Search aircraft by Location")
        st.sidebar.subheader("Search aircraft in an Location")
        fun1val1 = st.sidebar.number_input("x_loc: [Pick a number between (0,2560)]",0 ,2560 ,step = 100)
        fun1val2 = st.sidebar.number_input("y_loc: [Pick a number between (0,2560)]",0 ,2560 ,step = 100)
        fun1val3 = st.sidebar.text_input("image_id", max_chars= 50)
        if st.sidebar.button("Select"):
            res = requests.get(f"https://damg7245-zhijie.herokuapp.com/img/airplane/location?x_loc={fun1val1}&y_loc={fun1val2}&image_id={fun1val3}")
            # todo:  record time of API calling
            st.json( res.json() )
            st.write('Finish1')
    
    def api2():
        st.header("API 2: Get all airplanes' coordinate in picture")
        st.sidebar.subheader("API 2: Get airplanes coordinate in picture")
        fun2val1 = st.sidebar.text_input("image_id", max_chars= 50)
        if st.sidebar.button("Select"):
            res = requests.get(f"https://damg7245-zhijie.herokuapp.com/img/airplanes/coordinates?image_id={fun2val1}")
            st.json( res.json() )            
            st.write('Finish2')
        
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
            res = requests.get(f"https://damg7245-zhijie.herokuapp.com/img/display?image_id={fun3val1}&limit_of_number={fun3val2}&isMaximum={fun3val3}")
            st.json( res.json() ) 
            st.write('Finish3')
        
    def api4():
        st.header("API 4: Count airplanes in a picture")
        st.sidebar.subheader("Count airplanes in a picture")
        fun4val1 = st.sidebar.text_input("image id", max_chars= 50)
        if st.sidebar.button("Select"):
            res = requests.get(f"https://damg7245-zhijie.herokuapp.com/img/airplanes/count?image_id={fun4val1}")
            st.json( res.json() ) 
            st.write('Finish4')

        
    def api5():
        st.header("API 5: Search for images by numbers of airplanes")
        st.sidebar.subheader("Search by numbers of airplanes")
        fun5val1 = st.sidebar.number_input("contain aircraft number [Pick a number between (20,100)]",20 ,100)
        fun5val2 = st.sidebar.number_input("limit of number [Pick a number between (1,10)]",1 ,10)
        if st.sidebar.button("Select"):
            res = requests.get(f'https://damg7245-zhijie.herokuapp.com/img/airplanes/givenNumber?contain_aircraft_number={fun5val1}&limit_of_image={fun5val2}')
            # todo:  record time of API calling
            st.json( res.json() )
            st.write('Finish5')
        
    def api6():
        st.header("API 6: Get pictures that contains top number of airplanes")
        st.sidebar.subheader("Find most airplanes on one or more images")
        fun6val1 = st.sidebar.number_input("number of image: [Pick a number between (1,10)]",1 ,10)
        if st.sidebar.button("Select"):
            res = requests.get(f"https://damg7245-zhijie.herokuapp.com/img/airplanes/maximum?number_of_image={fun6val1}")
            st.json( res.json() )             
            st.write('Finish6')
        
    def api7():
        st.header("API 7: Get pictures that contains top number of truncated airplanes")
        st.sidebar.subheader("Find picture with most truncated airplanes")
        fun7val1 = st.sidebar.number_input("number of image [Pick a number between (1,10)]",1 ,10)
        if st.sidebar.button("Select"):
            res = requests.get(f"https://damg7245-zhijie.herokuapp.com/img/airplanes/truncated?number_of_image={fun7val1}")
            st.json( res.json() ) 
            st.write('Finish7')
        

    funNum = {
        "API 1: Search by Location": api1,
        "API 2: Get all coordinates": api2,
        "API 3: Get top size aircraft": api3,
        "API 4: Count airplanes": api4,
        "API 5: Search by number": api5,
        "API 6: Get top number aircraft": api6,
        "API 7: Get top number truncated": api7
    }

    selectFun = st.sidebar.selectbox("choose API", funNum.keys())
    funNum[selectFun]()
else:
    st.markdown('# Please go to streamlitMain login')