import streamlit as st
import time

st.title("LEARNING STREAMLIT")
st.header("Header")
st.markdown("markdown")
st.subheader("subheader")
st.caption("Caption")
st.code("python3 app.py")
st.latex(r'''a+a r^1+a r^2+a r^3''')
st.write("write")
st.image("1.jpg")

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)

st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

st.balloons()

st.subheader("Progress bar")
st.progress(10) 

with st.spinner('Wait for it...'):
    time.sleep(10)

st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

st.sidebar.title("Sidebar")
st.sidebar.button("button")
st.sidebar.write("Writing in sidebar")
