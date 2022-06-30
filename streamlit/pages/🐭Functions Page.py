import streamlit as st
#st.session_state
st.sidebar.markdown("# Functions Page")
def fun1():
    st.header("Function 1: Location")
    st.sidebar.header("Function 1: Location")
    fun1val1 = st.sidebar.number_input("x_loc (Pick a number between (0,2560))",0 ,2560 ,step = 100)
    fun1val2 = st.sidebar.number_input("y_loc (Pick a number between (0,2560))",0 ,2560 ,step = 100)
    fun1val3 = st.sidebar.text_input("image_id", max_chars= 50)
    if st.sidebar.button("Select"):
        st.write('Finish1')
    
def fun2():
    st.header("Function 2: Loordinates")
    st.sidebar.header("Function 2: Loordinates")
    fun2val1 = st.sidebar.text_input("image_id", max_chars= 50)
    if st.sidebar.button("Select"):
        st.write('Finish2')
    
def fun3():
    st.header("Function 3: Display")
    st.sidebar.header("Function 3: Display")
    fun3val1 = st.sidebar.text_input("image id", max_chars= 50)
    fun3val2 = st.sidebar.number_input("limit of number (Pick a number between (1,10))",1 ,10)
    if st.sidebar.button("Select"):
        st.write('Finish3')
    
def fun4():
    st.header("Function 4: Count")
    st.sidebar.header("Function 4: Count")
    fun4val1 = st.sidebar.text_input("image id", max_chars= 50)
    if st.sidebar.button("Select"):
        st.write('Finish4')
    
def fun5():
    st.header("Function 5: givenNumber")
    st.sidebar.header("Function 5: givenNumber")
    fun5val1 = st.sidebar.number_input("contain aircraft number (Pick a number between (20,100))",20 ,100 ,step = 10)
    fun5val2 = st.sidebar.number_input("limit of number (Pick a number between (1,10))",1 ,10)
    if st.sidebar.button("Select"):
        st.write('Finish5')
    
def fun6():
    st.header("Function 6: Maximum")
    st.sidebar.header("Function 6: Maximum")
    fun6val1 = st.sidebar.number_input("number of image (Pick a number between (1,10))",1 ,10)
    if st.sidebar.button("Select"):
        st.write('Finish6')
    
def fun7():
    st.header("Function 7: Truncated")
    st.sidebar.header("Function 7: Truncated")
    fun7val1 = st.sidebar.number_input("number of image (Pick a number between (1,10))",1 ,10)
    if st.sidebar.button("Select"):
        st.write('Finish7')
    

funNum = {
    "function1": fun1,
    "function2": fun2,
    "function3": fun3,
    "function4": fun4,
    "function5": fun5,
    "function6": fun6,
    "function7": fun7
}

selectFun = st.sidebar.selectbox("choose function", funNum.keys())
funNum[selectFun]()