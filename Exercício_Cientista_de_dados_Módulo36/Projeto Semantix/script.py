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

def get_dict(df, i, coluna, dict):
    x = df.loc[df[coluna] == i, coluna].map({valor: chave for chave, valor in dict.items()}).to_list()
    if x == []:
        y = df[coluna].map({valor: chave for chave, valor in dict.items()})
        x = y.loc[y == i]
        x = x.map(dict).to_list()
    return x

def Legenda(grafico=None, rotacao=None, titulo=None): #Fórmula para colocar legenda no gráfico.
    
    ax = plt.gca()  # Obter o eixo atual.
    
    for p in ax.patches: #for para criar a legenda.
        ax.annotate(f'{round(p.get_height(),2)}', #Texto a ser escrito no gráfico.
                    xy=(p.get_x() + p.get_width() / 2, p.get_height()), #Localização do Texto.
                    ha='center', #Alinhamento Horizontal.
                    va='center', #Alinhamento Vertical.
                    xytext= (0,15),
                    textcoords= 'offset points',
                    rotation=rotacao) #Rotação do texto.
    
    plt.title(titulo) #Título do gráfico.