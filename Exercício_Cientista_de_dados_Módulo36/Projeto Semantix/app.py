import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time
import streamlit as st
import analise

sns.set_theme()

import warnings

warnings.filterwarnings("ignore")

st.title("TESTE")

df = pd.read_csv('./Dados/matches.csv', index_col=0, parse_dates=['Date']).drop(columns='Notes')

st.write(analise.analise(df, 'Result'))