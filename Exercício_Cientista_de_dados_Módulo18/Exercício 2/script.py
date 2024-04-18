import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import statsmodels.formula.api as smf
import statsmodels.api as sm

def Qualitativa (df, y, x):
    # Criando  para 'age' através do pd.crosstab().
    # Nº de saudáveis
    # Nº de doentes
    # Total
    tab = pd.crosstab(df[x], df[y], margins=True, margins_name='Total', dropna=True)

    # Quantidade média de doentes.
    tab['Media_doentes'] = tab[1]/tab['Total']

    # Odds
    tab['Odds_Doentes'] = tab[1]/tab[0]

    # Odds ratio
    tab['RC_vs_total_OddsRatio'] = tab['Odds_Doentes']/tab.loc['Total', 'Odds_Doentes']

    # Logito (LOG(Odds))
    tab['Logito'] = np.log(tab['Odds_Doentes'])

    # Log do Odds ratio - Weight of Evidence (WOE)
    tab['WOE'] = np.log(tab['RC_vs_total_OddsRatio'])

    return tab.rename({0: 'Saudavel', 1: 'Doente'}, axis=1)

def Quantitativa (df, y, x, quebra=5):
    # Categorizando a variável x em grupos com quebra padrão igual a 5.
    cat = pd.qcut(x=df[x], q=quebra, duplicates='drop')

    # Criando  para 'age' através do pd.crosstab().
    # Nº de saudáveis
    # Nº de doentes
    # Total
    tab = pd.crosstab(cat, df[y], margins=True, margins_name='Total', dropna=True)

    # Quantidade média de doentes.
    tab['Media_doentes'] = tab[1]/tab['Total']

    # Odds
    tab['Odds_Doentes'] = tab[1]/tab[0]

    # Odds ratio
    tab['RC_vs_total_OddsRatio'] = tab['Odds_Doentes']/tab.loc['Total', 'Odds_Doentes']

    # Logito (LOG(Odds))
    tab['Logito'] = np.log(tab['Odds_Doentes'])

    # Log do Odds ratio - Weight of Evidence (WOE)
    tab['WOE'] = np.log(tab['RC_vs_total_OddsRatio'])

    # Valor médio da variável Age.
    tab['Media_'+x] = df.groupby(cat)[x].mean()
    tab.loc['Total', 'Media_'+x] = tab['Media_'+x][0:quebra].mean()

    return tab.rename({0: 'Saudavel', 1: 'Doente'}, axis=1)