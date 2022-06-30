import streamlit as st
import streamlit.components.v1 as components

st.markdown('# Panda Profiling Page')

HtmlFile = open("../reports/airplane_data_profiling.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height = 13150)