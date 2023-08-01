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
---
### Entendimento do negócio:
A análise para a concessão de cartões de crédito é um assunto de extrema importância no setor financeiro. Para que o limite de crédito seja liberado, o banco ou algum outro tipo de industria financeira, utilizam informações pessoais e dados fornecidos pelos candidato para prever a probabilidade de inadimplência futura e comportamento de endividamento com o cartão.

Vamos utlizar desses dados fornecidos em um desafio do site [Kaggle](https://www.kaggle.com/), uma plataforma que promove desafios de ciência de dados, oferecendo prêmios em dinheiro para os melhores colocados. O link original está [aqui](https://www.kaggle.com/rikdifos/credit-card-approval-prediction).

O objetivo será construir o melhor modelo preditivo para identificar o perfil de renda do cliente, e assim tentar prever a renda de novos clientes.
'''

##############################################################

'''
---

### Lista de Variáveis com Quantidade e Tipo:
'''
st.write(variaveis)

##############################################################

'''
---

### Amostra dos Dados:
'''
st.write(f"**Linhas: {renda.shape[0]} / Colunas: {renda.shape[1]+1}**")
st.write(renda)