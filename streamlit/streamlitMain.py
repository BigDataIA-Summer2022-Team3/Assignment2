import streamlit as st
import webbrowser
#from count_airplanes_in_given_image import count_airplanes_in_given_image as caig

st.markdown('# Login Page')

#.text_input("X"), X can not use same key
#button can not use same key
if st.sidebar.button("Reset"):
    st.empty()

fun1 =  st.sidebar.expander("Function 1")
fun1val1 = fun1.text_input("fun1val1")
fun1val2 = fun1.text_input("fun1val2")
if fun1.button("Select1"):
   st.write('Finish1')


fun2 =  st.sidebar.expander("Function 2")
fun2val1 = fun2.text_input("fun2val1")
fun2val2 = fun2.text_input("fun2val2")
if fun2.button("Select2"):
    st.write('Finish2')


fun3 =  st.sidebar.expander("Function 3")
fun3val1 = fun3.text_input("fun3val1")
fun3val2 = fun3.text_input("fun3val2")
if fun3.button("Select3"):
    st.write('Finish3')


fun4 =  st.sidebar.expander("Function 4")
fun4val1 = fun4.text_input("fun4val1")
fun4val2 = fun4.text_input("fun4val2")
if fun4.button("Select4"):
    st.write('Finish4')


fun5 =  st.sidebar.expander("Function 5")
fun5val1 = fun5.text_input("fun5val1")
fun5val2 = fun5.text_input("fun5val2")
if fun5.button("Select5"):
    st.write('Finish5')


fun6 =  st.sidebar.expander("Function 6")
fun6val1 = fun6.text_input("fun6val1")
fun6val2 = fun6.text_input("fun6val2")
if fun6.button("Select6"):
    st.write('Finish6')


fun7 =  st.sidebar.expander("Function 7")
fun7val1 = fun7.text_input("fun7val1")
fun7val2 = fun7.text_input("fun7val2")
if fun7.button("Select7"):
    st.write('Finish7')


if st.sidebar.button("panda profiling"):
    webbrowser.open_new_tab("https://github.com/BigDataIA-Summer2022-Team3/Assignment1/blob/main/reports/airplane_data_profiling.html")