import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer
import numpy as np


st.set_page_config(
    page_title="TriB team - HCMUT student",
    layout="wide"
)

st.title("TriB Visualization App")

selection = st.selectbox("Select your file type", ("*.csv", "*.xlsx", "*.json"))

uploaded_file = st.file_uploader("Choose a file")




if uploaded_file is not None:
    df = None
    if selection == "*.csv":
        df = pd.read_csv(uploaded_file, encoding='latin1')
        pyg_app = StreamlitRenderer(df)
        pyg_app.explorer()
    elif selection == "*.xlsx":
        df = pd.read_excel(uploaded_file)
        st.write("load successfully")
        pyg_app = StreamlitRenderer(df)
        pyg_app.explorer()
    elif selection == "*.json":
        df = pd.read_json(uploaded_file)
        pyg_app = StreamlitRenderer(df)
        pyg_app.explorer()
    


