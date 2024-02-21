import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time
import streamlit as st
from analise import analise
from analise import stats
import openai

sns.set_theme()

import warnings

warnings.filterwarnings("ignore")

st.title("PROJETO Semantix")

df = pd.read_csv('./Dados/matches.csv', index_col=0, parse_dates=['Date']).drop(columns='Notes')
df['Result'] = df['Result'].map({'D': 'Empate', 'L':'Derrota', 'W':'Vitória'})

df_home = df[df['Venue'] == 'Home']
df_away = df[df['Venue'] == 'Away']

st.write(df)
col1, col2, col3 = st.columns(3)

col1.bar_chart(stats(x='Result', df=df_home), color=['#ff0000','#ffaa00', '#00ff00'])
col2.bar_chart(stats(x='Poss', df=df_home), color=['#ff0000','#ffaa00', '#00ff00'])
col3.bar_chart(stats(x='Opponent', df=df_home), color=['#ff0000','#ffaa00', '#00ff00'])

openai.api_key = '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'

completion = openai.chat.completions.create(
                                            model="gpt-3.5-turbo",
                                            messages=[{"role": "user", "content": f'O dataset a seguir corresponde a metricas de partidas de futebol da Premier League. Me informe insights sobre este dataset {df_home}'}])

st.markdown(completion.choices[0].message.content)