import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import script


def app():
    df = st.session_state['df'][0]
    st.write(df)