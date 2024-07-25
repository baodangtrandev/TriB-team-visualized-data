import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer


st.set_page_config(
    page_title="TriB team - HCMUT student",
    layout="wide"
)

st.title("TriB Visualization App")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='latin1')
    pyg_app = StreamlitRenderer(df)
    pyg_app.explorer()


