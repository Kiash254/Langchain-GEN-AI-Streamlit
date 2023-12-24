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
st.subheader('Data Analysis with Streamlit for Dashboard visualization')
st.write("Here's our first attempt at using data to create a table:")
#read the data
df = pd.read_csv("data/iris.csv")
#show the data as a table for the first 5 rows 
st.table(df.head(3))

#use matplotlib to plot a histogram of the data
import matplotlib.pyplot as plt
import seaborn as sns
#set the style of the plot
sns.set_style("darkgrid")
#plot the histogram
fig, ax = plt.subplots()
ax = sns.histplot(data=df, x="SepalLengthCm", kde=True)
#set the title
plt.title("Histogram of sepal length")
#set the x-axis label
plt.xlabel("Sepal length")
#set the y-axis label
plt.ylabel("Frequency")
#show the plot
st.pyplot(fig)

#create a scatter plot
fig, ax = plt.subplots()
ax = sns.scatterplot(data=df, x="SepalLengthCm", y="SepalWidthCm", hue="Species")
#set the title
plt.title("Scatter plot of sepal length and width")
#set the x-axis label
plt.xlabel("Sepal length")
#set the y-axis label
plt.ylabel("Sepal width")
#show the plot
st.pyplot(fig)

#create a bar chart
fig, ax = plt.subplots()
ax = sns.barplot(data=df, x="Species", y="SepalLengthCm")
#set the title
plt.title("Bar chart of sepal length")
#set the x-axis label
plt.xlabel("Species")
#set the y-axis label
plt.ylabel("Sepal length")
#show the plot
st.pyplot(fig)

    
#create a line chart
fig, ax = plt.subplots()
ax = sns.lineplot(data=df, x="SepalLengthCm", y="SepalWidthCm")
#set the title
plt.title("Line chart of sepal length and width")
#set the x-axis label
plt.xlabel("Sepal length")
#set the y-axis label
plt.ylabel("Sepal width")
#show the plot
st.pyplot(fig)

#create a box plot
fig, ax = plt.subplots()
ax = sns.boxplot(data=df, x="Species", y="SepalLengthCm")
#set the title
plt.title("Box plot of sepal length")
#set the x-axis label
plt.xlabel("Species")
#set the y-axis label
plt.ylabel("Sepal length")
#show the plot
st.pyplot(fig)

#create a violin plot
fig, ax = plt.subplots()
ax = sns.violinplot(data=df, x="Species", y="SepalLengthCm")
#set the title
plt.title("Violin plot of sepal length")
#set the x-axis label
plt.xlabel("Species")
#set the y-axis label
plt.ylabel("Sepal length")
#show the plot
st.pyplot(fig)

#create a pie chart
fig, ax = plt.subplots()
ax = df["Species"].value_counts().plot.pie(autopct="%1.1f%%")
#set the title
plt.title("Pie chart of species")
#show the plot
st.pyplot(fig)

#create a heatmap   
fig, ax = plt.subplots()
ax = sns.heatmap(df.corr(), annot=True)
#set the title
plt.title("Heatmap of correlation matrix")  
#show the plot
st.pyplot(fig)
