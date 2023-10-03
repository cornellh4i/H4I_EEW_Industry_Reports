import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="hello",
    page_icon="👋",
)

st.title("julespapp")
st.write("Hi, I'm Jules!")

state_counties = pd.read_csv('state_counties_corrected.csv')

st.sidebar.success("Select a demo above.")

# Select and display only the "FAC_STATE" and "FAC_COUNTY" columns
selected_columns = ["FAC_STATE", "FAC_COUNTY"]
selected_data = state_counties[selected_columns]
st.write(selected_data)
