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
my_fruit_list = my_fruit_list.set_index('Fruit')
st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','strawberries'])
st.dataframe(my_fruit_list)








