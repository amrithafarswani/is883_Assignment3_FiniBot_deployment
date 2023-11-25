# Import necessary libraries
import streamlit as st
import openai
import os
from io import StringIO
import pandas as pd



# Make sure to add your OpenAI API key in the advanced settings of streamlit's deployment
open_AI_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = open_AI_key

### Here, with some adjustments, copy-paste the code you developed for Question 1 in Assignment 3 
##########################################################################




##########################################################################


# UX goes here. You will have to encorporate some variables from the code above and make some tweaks.

# Streamlit UI

# Header
st.header("Welcome to FiniBot Services!")
st.write("Please upload your spreadsheet using the button below.")
st.write("Download the spreadsheet template [here](link_to_template)")

# File uploader
uploaded_file = st.file_uploader("Upload spreadsheet", type=["csv", "xlsx"])

# Radio button for user type
user_type = st.radio("Select your expertise level:", ('Novice', 'Expert'))

# Display uploaded spreadsheet
if uploaded_file is not None:
   df = pd.read_csv(uploaded_file)  # You can modify this based on the file type
   st.dataframe(df)

    # Perform analysis and display recommendation
        analysis_result = perform_analysis(df, user_type)
        st.markdown(f"## FiniBot's Analysis and Recommendation\n{analysis_result}")


