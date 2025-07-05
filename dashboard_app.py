import streamlit as st
import pandas as pd

st.set_page_config(page_title="NODASIS v11 Dashboard", layout="wide")
st.title("📊 NODASIS v11 – Operator Detection Dashboard")

st.sidebar.success("Select a view above.")

st.markdown("Welcome to **NODASIS v11**. Use the tabs to explore strategy chains, replay memory, Sell/Buy zones, and capital flows.")