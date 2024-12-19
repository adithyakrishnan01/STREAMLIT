import streamlit as st
import pandas as pd
import numpy as np

st.title("Web App")

x = st.slider("x",min_value=10, max_value=20)
st.title("{} squared is {}". format(x, x*x))

map_data = pd.DataFrame(
    np.array([[8.571032, 76.866333]]), columns=["lat", "lon"]
)
st.map(map_data)
