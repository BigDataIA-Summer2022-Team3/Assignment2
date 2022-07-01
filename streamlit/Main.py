import streamlit as st
import webbrowser
import streamlit.components.v1 as components
#from count_airplanes_in_given_image import count_airplanes_in_given_image as caig

st.markdown('# Login Page')



#.text_input("X"), X can not use same key
#button can not use same key
if st.sidebar.button("Reset"):
    st.empty()

if st.sidebar.button("panda profiling"):
    webbrowser.open_new_tab("https://github.com/BigDataIA-Summer2022-Team3/Assignment1/blob/main/reports/airplane_data_profiling.html")
    st.empty() 
