import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import script
from pycaret.classification import *


def app():
    st.title('📐 :red[ANÁLISE]')
    data = st.session_state['data']
    data_unseen = st.session_state['data_unseen']
    