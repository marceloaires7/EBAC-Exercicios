# Importações de Pacotes:
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import time
import renda_grafico

##############################################################

# Import CSV 'previsao_de_renda.csv'
renda = pd.read_csv('./input/previsao_de_renda.csv', parse_dates=['data_ref'])
renda['data_ref'] = pd.to_datetime(renda['data_ref'])

##############################################################

# Tratamento dos Dados
renda = (renda.drop_duplicates(subset='id_cliente',
                                             keep='first',
                                             ignore_index=True)
                     .drop(columns=['Unnamed: 0',
                                           'id_cliente'],
                                           axis=1)
                     .set_index(keys='data_ref').copy()
                     .assign(tempo_emprego = lambda x: x['tempo_emprego'].fillna(x['tempo_emprego'].median())))

##############################################################

# Lista das Variáveis com Quantidades e Tipo.
variaveis = (renda.columns.to_frame()
                          .rename(columns={0: 'Quantidade'})
                          .rename_axis('Variáveis')
                          .assign(Quantidade = lambda x: renda[x.index].nunique())
                          .assign(Tipo = renda.dtypes)
                          .sort_values(by=['Quantidade'], ascending=False))

##############################################################

# Layout da Página:
st.set_page_config(page_title= 'Projeto 2',
                   page_icon= 'https://s3.amazonaws.com/gupy5/production/companies/39637/career/92146/images/2022-08-23_17-33_logo.jpg',
                   layout= 'wide')

##############################################################

'''
# :green[Projeto 2]
### **Previsão de Renda**
'''

##############################################################

'''
---
### COUNTPLOT DAS VARIÁVEIS (Após tratamento):
'''

##############################################################

fig, ax = plt.subplots(nrows=6,
                       ncols=2,
                       figsize=(20,40))

plt.subplots_adjust(hspace=1)

##############################################################

sns.countplot(x=renda.index,data=renda, ax=ax[0,0])
ax[0,0].set_title('data_ref')
ax[0,0].tick_params(axis='x',
                    rotation=90)

##############################################################

sns.countplot(x='sexo',data=renda, ax=ax[0,1])
ax[0,1].set_title('sexo')

##############################################################

sns.countplot(x='posse_de_veiculo',data=renda, ax=ax[1,0])
ax[1,0].set_title('posse_de_veiculo')

##############################################################

sns.countplot(x='posse_de_imovel',data=renda, ax=ax[1,1])
ax[1,1].set_title('posse_de_imovel')

##############################################################

sns.countplot(x='qtd_filhos',data=renda, ax=ax[2,0])
ax[2,0].set_title('qtd_filhos')

##############################################################

sns.countplot(x='tipo_renda',data=renda, ax=ax[2,1])
ax[2,1].set_title('tipo_renda')

##############################################################

sns.countplot(x='educacao',data=renda, ax=ax[3,0])
ax[3,0].set_title('educacao')

##############################################################

sns.countplot(x='estado_civil',data=renda, ax=ax[3,1])
ax[3,1].set_title('estado_civil')

##############################################################

sns.countplot(x='tipo_residencia',data=renda, ax=ax[4,0])
ax[4,0].set_title('tipo_residencia')

##############################################################

sns.countplot(x='idade',data=renda, ax=ax[4,1])
ax[4,1].set_title('idade')
ax[4,1].tick_params(axis='x',
                    rotation=90)

##############################################################

sns.countplot(x='qt_pessoas_residencia',data=renda, ax=ax[5,0])
ax[5,0].set_title('qt_pessoas_residencia')

##############################################################

ax[5,1].remove()

##############################################################

st.pyplot(plt)