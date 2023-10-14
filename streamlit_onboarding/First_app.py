import streamlit as st
import pandas as pd
import numpy as np

st.title("Owen's First App")
st.write("Hi, I'm Owen! I'm a sophomore at Cornell University. I like hiking, playing piano, painting, baking, and Phoebe Bridgers. I also have a goldendoodle named Luke :)")

csv_data = pd.read_csv("state_counties_corrected.csv")
filtered_data = csv_data[['FAC_STATE', 'FAC_COUNTY']]

filtered_data
