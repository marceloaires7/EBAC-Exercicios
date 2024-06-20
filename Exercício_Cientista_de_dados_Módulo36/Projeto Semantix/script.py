import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time

Teams =          {'Arsenal'                : 1,
                  'AstonVilla'             : 2,
                  'Bournemouth'            : 3,
                  'Brentford'              : 4,
                  'BrightonandHoveAlbion'  : 5,
                  'Burnley'                : 6,
                  'Chelsea'                : 7,
                  'CrystalPalace'          : 8,
                  'Everton'                : 9,
                  'Fulham'                 : 10,
                  'Liverpool'              : 11,
                  'LutonTown'              : 12,
                  'ManchesterCity'         : 13,
                  'ManchesterUnited'       : 14,
                  'NewcastleUnited'        : 15,
                  'NottinghamForest'       : 16,
                  'SheffieldUnited'        : 17,
                  'TottenhamHotspur'       : 18,
                  'WestHamUnited'          : 19,
                  'WolverhamptonWanderers' : 20}

Teams_Opponent = {'Arsenal'         : 1, 
                  'Aston Villa'     : 2,     
                  'Bournemouth'     : 3,     
                  'Brentford'       : 4,   
                  'Brighton'        : 5,  
                  'Burnley'         : 6, 
                  'Chelsea'         : 7, 
                  'Crystal Palace'  : 8,        
                  'Everton'         : 9, 
                  'Fulham'          : 10, 
                  'Liverpool'       : 11,   
                  'Luton Town'      : 12,    
                  'Manchester City' : 13,         
                  'Manchester Utd'  : 14,        
                  'Newcastle Utd'   : 15,       
                  "Nott'ham Forest" : 16,         
                  'Sheffield Utd'   : 17, 
                  'Tottenham'       : 18,
                  'West Ham'        : 19,
                  'Wolves'          : 20}

Matchweek =      {'Matchweek 1': 1,
                  'Matchweek 2': 2,
                  'Matchweek 3': 3,
                  'Matchweek 4': 4,
                  'Matchweek 5': 5,
                  'Matchweek 6': 6,
                  'Matchweek 7': 7,
                  'Matchweek 8': 8,
                  'Matchweek 9': 9,
                  'Matchweek 10': 10,
                  'Matchweek 11': 11,
                  'Matchweek 12': 12,
                  'Matchweek 13': 13,
                  'Matchweek 14': 14,
                  'Matchweek 15': 15,
                  'Matchweek 16': 16,
                  'Matchweek 17': 17,
                  'Matchweek 18': 18,
                  'Matchweek 19': 19,
                  'Matchweek 20': 20,
                  'Matchweek 21': 21,
                  'Matchweek 22': 22,
                  'Matchweek 23': 23,
                  'Matchweek 24': 24}

weekday =        {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu':3, 'Fri': 4, 'Sat': 5, 'Sun': 6}

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