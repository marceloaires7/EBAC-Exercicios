# Importações de Pacotes:
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

##############################################################

# Set no tema do seaborn para melhorar o visual dos plots
custom_params = {"axes.spines.right": False, "axes.spines.top": False}
sns.set_theme(style='ticks', rc=custom_params, palette='tab10')

##############################################################

# Layout da Página:
st.set_page_config(page_title= 'Projeto Final',
                   page_icon= 'https://web-summit-avenger.imgix.net/production/logos/original/68de83f411416128ffe8c1a3789a99b5ba538a6f.png?ixlib=rb-3.2.1&fit=fill&fill-color=white',
                   layout= 'wide',
                   initial_sidebar_state='expanded')

##############################################################

file = 

##############################################################

# Função para ler os dados
@st.cache_data(show_spinner=True)
def load_data(file_data):
    try:
        return pd.read_feather(file_data)
    except:
        return pd.read_csv(file_data, sep=';')

##############################################################

# Tratamento dos Dados
#renda = (renda.drop(columns=['index'], axis=1)
#
#                    .set_index(keys='data_ref').copy()
#                    .assign(tempo_emprego = lambda x: x['tempo_emprego'].fillna(x['tempo_emprego'].median())))


##############################################################

'''
# 💼 :green[Projeto Final]
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
#st.write(script.analise(renda, 'mau'))

##############################################################

'''
---

### Amostra dos Dados:
'''
# st.write(f"**Linhas: {renda.shape[0]} / Colunas: {renda.shape[1]+1}**")
# st.write(renda)