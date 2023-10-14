import streamlit as st
import pandas as pd
import numpy as np
import os
# os.chdir("OneDrive\Documents\h4i\H4I_EEW_Industry_Reports")
st.write(os.getcwd())


st.title("First App")
st.write("I'm Hubert, a Sophomore in Arts and Sciences studying CS. This is my first semester on Hack4Impact and I'm excited to learn and contribute to the team")

df = pd.read_csv(
    "state_counties_corrected.csv")
selected_columns = ['FAC_STATE', 'FAC_COUNTY']
st.write(df[selected_columns])
