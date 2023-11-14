#!/usr/bin/env python
# coding: utf-8

# In[1]:

import datetime
import streamlit as st
import pandas as pd
import requests
import json
import time
import plotly.graph_objects as go
import random
import plotly.io as pio
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.ticker as ticker
import numpy as np
import plotly.express as px 
import streamlit_wordcloud as wordcloud


st.cache(suppress_st_warning=True)  
st.set_page_config(page_title="ECSA BI Dashboard", layout="wide",initial_sidebar_state="collapsed")

# In[2]:
st.title('Introduction')

# In[3]:
st.markdown('This is a first version of a dashboard which will evolve over time and anyone can fork at any given time.')
st.markdown('It is structured as follows:')
st.write('- First, number of offers.')
st.write('- number of staked offers (become ecsa operations).')
st.write('- deadlines met for tasks within offers.')
st.write('- weekly hour limit reached but not breached.')
st.markdown('If there`s any missing information or misleading one, please do not hesitate to reach out on twitter.')

 

tab1, tab2 = st.tabs(["Fake data test","Input data here"])

# In[7]:

with tab1:
    
    
    st.subheader("Test1")
    st.write('')
    st.write('Test1 text.')
    st.write('')
    
    df_initial_data = pd.read_csv('offer_markets_initial_hours.csv')
    fig = px.pie(df_initial_data, values='Q4_weekly_hours', names='Node Affiliation', title='Q4 Projected weekly hours by node affiliation')
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    # Split the interests in the 'Interests' column
    interests_split = df_initial_data['Interests'].str.split(', ')

    # Create a list to store individual interests
    all_interests = [interest for sublist in interests_split.dropna() for interest in sublist]

    # Count the occurrences of each interest
    interest_counts = pd.Series(all_interests).value_counts()

    # Create a DataFrame from the counts
    df_interest_counts = pd.DataFrame({'Interest': interest_counts.index, 'Count': interest_counts.values})

    all_interests_text = ', '.join(df_initial_data['Interests'].dropna())

    # Generate the word cloud
    wordcloud = wordcloud(width=800, height=400, background_color='white').generate(all_interests_text)

    # Plot the word cloud and display it using st.image
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Interests')

    # Save the word cloud image to a BytesIO object
    image_streamlit = st.image(wordcloud.to_image(), caption='Word Cloud of Interests', use_container_width=True)

    # Display the word cloud in the Streamlit app
    st.pyplot(plt)

    
with tab2:
    
    st.subheader('Test2')
    st.write('')
    st.write('Test2 text')
