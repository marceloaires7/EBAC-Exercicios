# %% Importações de Pacotes:
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import time
import script

##############################################################

# Set no tema do seaborn para melhorar o visual dos plots
custom_params = {"axes.spines.right": False, "axes.spines.top": False}
sns.set_theme(style='ticks', rc=custom_params, palette='tab10')

##############################################################

# %% Import CSV 'credit_scoring.ftr'
renda = pd.read_feather('./input/credit_scoring.ftr')
renda['data_ref'] = pd.to_datetime(renda['data_ref'])


##############################################################

# %% Tratamento dos Dados
renda = (renda.drop(columns=['index'], axis=1)

                    .set_index(keys='data_ref').copy()
                    .assign(tempo_emprego = lambda x: x['tempo_emprego'].fillna(x['tempo_emprego'].median())))

##############################################################

# %% Lista das Variáveis com Quantidades e Tipo.
variaveis = (renda.columns.to_frame()
                          .rename(columns={0: 'Quantidade'})
                          .rename_axis('Variáveis')
                          .assign(Quantidade = lambda x: renda[x.index].nunique())
                          .assign(Tipo = renda.dtypes)
                          .sort_values(by=['Quantidade'], ascending=False))

##############################################################

'''
# :green[Projeto Final]
### **Previsão de Renda**
'''

##############################################################

'''
---
### BARPLOT VARIÁVEIS x 'renda' (Após tratamento):
'''

##############################################################

fig, ax = plt.subplots(nrows=5,
                       ncols=2,
                       figsize=(20,40))

plt.subplots_adjust(hspace=1)

##############################################################

sns.barplot(x=renda.index,
            y='renda',
            data=renda,
            ax=ax[0,0])
ax[0,0].set_title("'data_ref' x 'renda'")
ax[0,0].tick_params(axis='x',
                    rotation=90)

##############################################################

sns.barplot(x='sexo',
            y='renda',
            data=renda,
            ax=ax[0,1])
ax[0,1].set_title("'sexo' x 'renda'")

##############################################################

sns.barplot(x='posse_de_veiculo',
            y='renda',
            data=renda,
            ax=ax[1,0])
ax[1,0].set_title("'posse_de_veiculo' x 'renda'")

##############################################################

sns.barplot(x='posse_de_imovel',
            y='renda',
            data=renda,
            ax=ax[1,1])
ax[1,1].set_title("'posse_de_imovel' x 'renda'")

##############################################################

sns.barplot(x='qtd_filhos',
            y='renda',
            data=renda,
            ax=ax[2,0])
ax[2,0].set_title("'qtd_filhos' x 'renda'")

##############################################################

sns.barplot(x='tipo_renda',
            y='renda',
            data=renda,
            ax=ax[2,1])
ax[2,1].set_title("'tipo_renda' x 'renda'")

##############################################################

sns.barplot(x='educacao',
            y='renda',
            data=renda,
            ax=ax[3,0])
ax[3,0].set_title("'educacao' x 'renda'")

##############################################################

sns.barplot(x='estado_civil',
            y='renda',
            data=renda,
            ax=ax[3,1])
ax[3,1].set_title("'estado_civil' x 'renda'")

##############################################################

sns.barplot(x='tipo_residencia',
            y='renda',
            data=renda,
            ax=ax[4,0])
ax[4,0].set_title("'tipo_residencia' x 'renda'")

##############################################################

sns.barplot(x='qt_pessoas_residencia',
            y='renda',
            data=renda,
            ax=ax[4,1])
ax[4,1].set_title("'qt_pessoas_residencia' x 'renda'")

##############################################################

st.pyplot(plt)