# import streamlit as st
# import streamlit.components.v1 as components
# import pickle
# from pathlib import Path
# import streamlit_authenticator as stauth

# names = ["zhijie_li", "yijun_lin", "damg7245_team4", "parth_shah", "srikanth_krishnamurthy"]
# usernames = ["zhijie", "yijun", "team4", "parth", "srikanth"]

# file_path = Path(__file__).parent.parent / "streamlitUserPW.pkl"
# with file_path.open("rb") as file:
#     hashed_passwards = pickle.load(file)

# authenticator = stauth.Authenticate(names, usernames, hashed_passwards, "streamlitMain", "abcdef", cookie_expiry_days=0)

# if st.session_state["authentication_status"]:
#     authenticator.logout('Logout', 'sidebar')
#     st.markdown('# Panda Profiling Page')
#     HtmlFile = open("../reports/airplane_data_profiling.html", 'r')
#     source_code = HtmlFile.read() 
#     print(source_code)
#     components.html(source_code, height = 13200)
# else:
#     st.markdown('# Please go to streamlitMain login')