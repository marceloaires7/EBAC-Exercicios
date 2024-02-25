import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time
import streamlit

def analise(data, y):
    analise = pd.DataFrame({'dtype': data.dtypes,
                            'contagem': data.count(),
                            'missing': data.isna().sum(),
                            'nunique': data.nunique(),
                            'papel': 'covariavel'})
    analise.loc[analise.index == y, 'papel'] = 'resposta'
    return analise

def stats(x, df):
    team_stats = (pd.crosstab(columns=df['Result'], index=df[x]).sort_values(by=['Vitória', 'Empate', 'Derrota'], ascending= False))

    return team_stats