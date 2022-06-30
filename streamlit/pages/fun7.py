import streamlit as st
#st.session_state
st.sidebar.markdown("# function7")
fun1val1 = st.text_input("val1")
fun1val2 = st.text_input("val2")
if st.button("Select"):
    st.write('Finish')