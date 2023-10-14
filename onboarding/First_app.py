import streamlit as st
import pandas as pd
import numpy as np

st.title('Brianna\'s first web app!')
st.subheader('Hello! 👋 My name is Brianna and I am a sophmore in the College'  
             + 'of Engineering studying computer science.')

data = pd.read_csv("state_counties_corrected.csv")
data[['FAC_STATE', 'FAC_COUNTY']]