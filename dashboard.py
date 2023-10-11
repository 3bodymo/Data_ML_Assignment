import streamlit as st
from src.components.training import render_training_section
from src.components.inference import render_inference_section
from src.components.eda import render_eda_section

st.title("Resume Classification Dashboard")
st.sidebar.title("Dashboard Modes")

sidebar_options = st.sidebar.selectbox(
    "Options",
    ("EDA", "Training", "Inference")
)

if sidebar_options == "EDA":
    render_eda_section()
elif sidebar_options == "Training":
    render_training_section()
else:
    render_inference_section()
