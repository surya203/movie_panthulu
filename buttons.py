import streamlit as st

st.title("hello")
# demonstration of streamlit buttons, text input, and slider.
if st.button("click me"):
    st.write("hello")
if st.text_input("enter your name"):
    st.write("hello")
if st.slider("select your age",0,100,25):
    st.write("hello")

# demonstration of streamlit columns and rows.
col1, col2 = st.columns(2)
with col1:
    st.write("hello")