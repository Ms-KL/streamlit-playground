# Documentation Example
# https://docs.streamlit.io/library/get-started/create-an-app

# Import Libraries
import streamlit as st
import pandas as pd
import numpy as np


#--- KRISTY HEADER
st.title("Kristy's Streamlit Playground")
st.write('''This is a playground for me to learn how to use Streamlit via the documentation. I plan on using this to create a dashboard for my data science projects.''')

#--- APP CONTENT
st.title('Uber pickups in NYC')

#--- APP DATA
# add code to script to enable fetching data
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data 
def load_data(nrows):
    '''

    This function:
    - downloads data using read_csv
    - converts the data into a pandas data-frame
    - converts the data column from string to datetime format

    cache_data:
    - checks the input parameters
    - checks the function body
    - checks the function output
    - the cache_data compares the input parameters and function body to the previous run and if they are the same, it will not run the function again, but will return the previous output.
    - if the input parameters or function body are different, the function will run again and the output will be saved for the next run.

    Parameters:
    * Specifies number of rows to load into data from

    '''
    data = pd.read_csv(DATA_URL, nrows=nrows) # download data from csv, convert to data using a the number of required of rows passed into the parameter

    lowercase = lambda x: str(x).lower()
    # convert the string to all lowercase

    data.rename(lowercase, axis='columns', inplace=True)
    # renames the data columns to lowercase

    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    # converts the date column to datetime format

    return data


#--- RUN THE DATA FUNCTION

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')

# Load 10,000 rows of data into the dataframe.
data = load_data(10000)

# Notify the reader that the data was successfully loaded.
# data_load_state.text('Loading data...done!') 
data_load_state.text("Done! (using st.cache_data)")

#--- APP DATA EXPLORATION
st.subheader('Raw data')
st.write(data)

#--- HISTOGRAM

st.subheader('Number of pickups by hour')

# numpy function to generate a histogram that breaks the data into 24 bins (one for each hour of the day). This is the data we will plot:
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

# draw the histogram
st.bar_chart(hist_values)

# #--- MAP
# st.subheader('Map of all pickups')

# # plot the data on a map
# st.map(data)

# --- MAP WITH FILTER
hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)