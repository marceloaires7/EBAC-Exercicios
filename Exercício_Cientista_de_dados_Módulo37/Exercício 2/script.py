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

def Legenda(grafico=None, titulo=None): #Fórmula para colocar legenda no gráfico.
    
    ax = plt.gca()  # Obter o eixo atual.
    
    for p in ax.patches: #for para criar a legenda.
        ax.annotate(f'{round(p.get_height(),2)}', #Texto a ser escrito no gráfico.
                    xy=(p.get_x() + p.get_width() / 2, p.get_height()), #Localização do Texto.
                    ha='center', #Alinhamento Horizontal.
                    va='center', #Alinhamento Vertical.
                    xytext= (0,15),
                    textcoords= 'offset points') #Rotação do texto.
    
    plt.title(titulo) #Título do gráfico.