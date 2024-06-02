import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import script
from pycaret.classification import *


def app():
    df = st.session_state['df'][0]
    
    clf = setup(data=data, target='mau', session_id=123)