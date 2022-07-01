import streamlit as st
import streamlit.components.v1 as components

st.markdown('# A Group 3 Home Page')

st.markdown('# Welcome!')

HtmlFile = open("../reports/api_describe_guide.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height = 13150, width = 1000) 