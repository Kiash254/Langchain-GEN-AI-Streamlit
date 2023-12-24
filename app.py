#import streamlit
import streamlit as st
import pandas as pd 
import numpy as np

#create a side bar showing the title "Welome to my app for data analysis"
st.sidebar.title("Welcome to my app for data analysis")
#add a text input to the sidebar
st.sidebar.text_input("Your name", "Type here")
#add a select box to the sidebar
st.sidebar.selectbox("Choose your favorite color", ["Red", "Green", "Blue"])
#add a slider to the sidebar
st.sidebar.slider("Choose a number", 0, 100, 50)
    

#set the title
st.title('My first app')
st.write("Here's our first attempt at using data to create a table:")

#read the data
df = pd.read_csv("data/iris.csv")
#show the data as a table for the first 5 rows 
st.table(df.head(3))

