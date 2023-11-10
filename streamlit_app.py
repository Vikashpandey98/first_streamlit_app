import streamlit as st 

st.title('My Parents New Healthy Dinner')
st.header('Breakfast Menu')
st.text('🥣 Omega 3 and Blueberry Oatmeal')
st.text('🥗Kale, spinach and Rocket Smoothie')
st.text('🐔Hard-Boiled Free-Range eggs')
st.text('🥑🍞Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇') 
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

st.dataframe(my_fruit_list)

st.radio("Pick one", ["cats", "dogs"])



tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")

st.balloons()
st.snow()



st.balloons()
st.snow()
