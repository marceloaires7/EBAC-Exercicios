import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
from sklearn.metrics import accuracy_score, roc_auc_score
from scipy.stats import t
from scipy.stats import ks_2samp
from pycaret.classification import *
import script

# Dicionário dos Meses.

meses = {1:  'Jan',
         2:  'Fev',
         3:  'Mar',
         4:  'Abr',
         5:  'Mai',
         6:  'Jun',
         7:  'Jul',
         8:  'Ago',
         9:  'Set',
         10: 'Out',
         11: 'Nov',
         12: 'Dez'}

# Função para ler os dados
@st.cache_data
def load_data(file_data):
    try:
        df = pd.read_feather(file_data)
        df.set_index(keys='data_ref', inplace=True)
        df.index = df.index.month.map(script.meses) + '_' + df.index.year.astype(str)
        df.drop(columns='index', inplace=True)
        return df
    except:
        return pd.read_csv(file_data)
    
@st.cache_data
def analise(data, y):
    analise = pd.DataFrame({'dtype': data.dtypes,
                            'contagem': data.count(),
                            'missing': data.isna().sum(),
                            'nunique': data.nunique(),
                            'papel': ['Resposta' if i == 'mau' else 'Covariavel' for i in data.dtypes.index]})

    return (analise.rename_axis('Variáveis')
                   .sort_values(by=['papel', 'nunique'],
                                ascending=False))

@st.cache_data
def IV(variavel, resposta):
    tab = pd.crosstab(variavel, resposta, margins=True, margins_name='total')

    rótulo_evento = tab.columns[0]
    rótulo_nao_evento = tab.columns[1]

    tab['pct_evento'] = tab[rótulo_evento]/tab.loc['total',rótulo_evento]
    tab['ep'] = tab[rótulo_evento]/tab.loc['total',rótulo_evento]
    
    tab['pct_nao_evento'] = tab[rótulo_nao_evento]/tab.loc['total',rótulo_nao_evento]
    tab['woe'] = np.log(tab.pct_evento/tab.pct_nao_evento)
    tab['iv_parcial'] = (tab.pct_evento - tab.pct_nao_evento)*tab.woe
    return tab['iv_parcial'].sum()

@st.cache_data
def biv_discreta(var, df):
    df['bom'] = 1-df.mau
    g = df.groupby(var)

    biv = pd.DataFrame({'qt_bom': g['bom'].sum(),
                        'qt_mau': g['mau'].sum(),
                        'mau':g['mau'].mean(), 
                        var: g['mau'].mean().index, 
                        'cont':g[var].count()})
    
    biv['ep'] = (biv.mau*(1-biv.mau)/biv.cont)**.5
    biv['mau_sup'] = biv.mau+t.ppf([0.975], biv.cont-1)*biv.ep
    biv['mau_inf'] = biv.mau+t.ppf([0.025], biv.cont-1)*biv.ep
    
    biv['logit'] = np.log(biv.mau/(1-biv.mau))
    biv['logit_sup'] = np.log(biv.mau_sup/(1-biv.mau_sup))
    biv['logit_inf'] = np.log(biv.mau_inf/(1-biv.mau_inf))

    tx_mau_geral = df.mau.mean()
    woe_geral = np.log(df.mau.mean() / (1 - df.mau.mean()))

    biv['woe'] = biv.logit - woe_geral
    biv['woe_sup'] = biv.logit_sup - woe_geral
    biv['woe_inf'] = biv.logit_inf - woe_geral

    fig, ax = plt.subplots(2,1, figsize=(8,6))
    ax[0].plot(biv[var], biv.woe, ':bo', label='woe')
    ax[0].plot(biv[var], biv.woe_sup, 'o:r', label='limite superior')
    ax[0].plot(biv[var], biv.woe_inf, 'o:r', label='limite inferior')
    
    num_cat = biv.shape[0]
    ax[0].set_xlim([-.3, num_cat-.7])

    ax[0].set_ylabel("Weight of Evidence")
    ax[0].legend(bbox_to_anchor=(.83, 1.17), ncol=3)
    
    ax[0].set_xticks(list(range(num_cat)))
    ax[0].set_xticklabels(biv[var], rotation=15)
    
    ax[1] = biv.cont.plot.bar()
    return biv

@st.cache_data
def biv_continua(var, ncat, df):
    df['bom'] = 1-df.mau
    cat_srs, bins = pd.qcut(df[var], ncat, retbins=True, precision=0, duplicates='drop')
    g = df.groupby(cat_srs, observed=False)

    biv = pd.DataFrame({'qt_bom': g['bom'].sum(),
                        'qt_mau': g['mau'].sum(),
                        'mau':g['mau'].mean(), 
                        var: g[var].mean(),     
                        'cont':g[var].count()})
    
    biv['ep'] = (biv.mau*(1-biv.mau)/biv.cont)**.5
    biv['mau_sup'] = biv.mau+t.ppf([0.975], biv.cont-1)*biv.ep
    biv['mau_inf'] = biv.mau+t.ppf([0.025], biv.cont-1)*biv.ep
    
    biv['logit'] = np.log(biv.mau/(1-biv.mau))
    biv['logit_sup'] = np.log(biv.mau_sup/(1-biv.mau_sup))
    biv['logit_inf'] = np.log(biv.mau_inf/(1-biv.mau_inf))

    tx_mau_geral = df.mau.mean()
    woe_geral = np.log(df.mau.mean() / (1 - df.mau.mean()))

    biv['woe'] = biv.logit - woe_geral
    biv['woe_sup'] = biv.logit_sup - woe_geral
    biv['woe_inf'] = biv.logit_inf - woe_geral

    fig, ax = plt.subplots(2,1, figsize=(8,6))
    ax[0].plot(biv[var], biv.woe, ':bo', label='woe')
    ax[0].plot(biv[var], biv.woe_sup, 'o:r', label='limite superior')
    ax[0].plot(biv[var], biv.woe_inf, 'o:r', label='limite inferior')
    
    num_cat = biv.shape[0]

    ax[0].set_ylabel("Weight of Evidence")
    ax[0].legend(bbox_to_anchor=(.83, 1.17), ncol=3)
    
    ax[1] = biv.cont.plot.bar()
    return biv

@st.cache_data
def print_metricas(dados, PD='PD', CLASSE_PRED='classe_predita', RESP='mau'):

    #Acuracia
    acc = accuracy_score(dados[RESP], dados[CLASSE_PRED])

    #AUC
    auc = roc_auc_score(dados[RESP], dados[PD])

    #Gini
    gini = 2 * auc - 1

    #KS
    ks = ks_2samp(dados.loc[dados[RESP] == 1, PD], dados.loc[dados[RESP] != 1,
                                                             PD]).statistic

    print('KS:       {0:.2f}%'.format(ks * 100))
    print('AUC:      {0:.2f}%'.format(auc * 100))
    print('GINI:     {0:.2f}%'.format(gini * 100))
    print('Acurácia: {0:.2f}%\n'.format(acc * 100))

    return None

@st.cache_data
def graficoQuali(uniQuali):
    df = st.session_state['df'][0].copy()

    fig, ax = plt.subplots(figsize=(5,4))
    ax = sns.countplot(data=df.sort_values(by=uniQuali), x=uniQuali, hue=uniQuali, legend=False, palette="tab10")
    plt.ylabel('Contagem')
    
    ax.tick_params(axis='x', rotation=270, length=6, width=2, grid_color='r', grid_alpha=0.5)
    ax.set_title(f'Contagem da variável {ax.get_xlabel()}', color='navy')
    ax.set_ylim(ymax=ax.get_ylim()[1]*1.2)
    
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='left', va='baseline', fontsize=9, color='black', xytext=(0, 5),
                textcoords='offset points', rotation=45)    
    
    return fig

@st.cache_data
def graficoQuanti(uniQuanti):
    df = st.session_state['df'][0].copy()
    df['idade'] = pd.qcut(df['idade'], 9, precision=0, duplicates='drop')
    df['tempo_emprego'] = pd.qcut(df['tempo_emprego'], 9, precision=0, duplicates='drop')
    df['renda'] = pd.qcut(df['renda'], 9, precision=0, duplicates='drop')
    
    fig, ax = plt.subplots(figsize=(5,4))
    ax = sns.countplot(data=df.reset_index().sort_values(by=uniQuanti), x=uniQuanti, hue=uniQuanti, legend=False, palette="tab10")
    plt.ylabel('Contagem')

    ax.tick_params(axis='x', rotation=270, length=6, width=2, grid_color='r', grid_alpha=0.5)
    ax.set_title(f'Contagem da variável {ax.get_xlabel()}', color='navy')
    ax.set_ylim(ymax=ax.get_ylim()[1]*1.2)
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='left', va='baseline', fontsize=9, color='black', xytext=(0, 5),
                textcoords='offset points', rotation=45)
        
    return fig, df

@st.cache_data
def graficoBivar(UniQuali1, UniQuali2):
    df = st.session_state['df'][0].copy()

    fig, ax = plt.subplots(figsize=(5,4))

    ct = pd.crosstab(df[UniQuali1], df[UniQuali2])
    sns.heatmap(ct, annot=True, cmap="YlGnBu", fmt='d', linewidths=.5, linecolor='black')
    ax.set_title(f'Contagem da variável {UniQuali1} por {UniQuali2}', color='navy')  
    
    return fig, ct

@st.cache_data
def graficoBivar2(UniQuanti1, UniQuanti2):
    df = st.session_state['df'][0].copy().fillna({'tempo_emprego': -1})

    fig, ax = plt.subplots(figsize=(5,4))

    ax = sns.scatterplot(data=df.reset_index(), x=df.reset_index()[UniQuanti1], y=df.reset_index()[UniQuanti2])
    ax.set_title(f'Contagem da variável {UniQuanti1} por {UniQuanti2}', color='navy')  
    
    df_cut = df.copy()
    df_cut['idade'] = pd.qcut(df_cut['idade'], 5, precision=0, duplicates='drop')
    df_cut['tempo_emprego'] = pd.qcut(df_cut['tempo_emprego'], 5, precision=0, duplicates='drop')
    df_cut['renda'] = pd.qcut(df_cut['renda'], 5, precision=0, duplicates='drop')

    return fig, df_cut.astype(str)

@st.cache_data
def createmodel(estimator, fold):
    
    modelo = create_model(estimator=estimator, fold=fold)
    pullMod = pull()
    return modelo, pullMod

@st.cache_data
def tunemodel(_estimator, fold, optimize):
    
    modelo = tune_model(estimator=_estimator, fold=fold, optimize=optimize)
    pullTuned = pull()
    return modelo, pullTuned