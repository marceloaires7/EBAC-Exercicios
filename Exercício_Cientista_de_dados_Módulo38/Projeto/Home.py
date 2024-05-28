import streamlit as st
import pandas as pd
import os
import warnings
import script


# Função para ler os dados
@st.cache_data(show_spinner=True)
def load_data(file_data):
    try:
        return pd.read_feather(file_data)
    except:
        return pd.read_csv(file_data, sep=';')

# Aplicativo da aba 'Home'
def app():

    # Descrição da aba 'Home'
    st.markdown(f'''
                 # 💼 :green[Projeto Final]
                 ### **Previsão de Renda**
                 ---
                 ### Entendimento do negócio:
                 A análise para a concessão de cartões de crédito é um assunto de extrema importância no setor financeiro. Para que o limite de crédito seja liberado, o banco ou algum outro tipo de industria financeira, utilizam informações pessoais e dados fornecidos pelos candidato para prever a probabilidade de inadimplência futura e comportamento de endividamento com o cartão.
 
                 Vamos utlizar desses dados fornecidos em um desafio do site [Kaggle](https://www.kaggle.com/), uma plataforma que promove desafios de ciência de dados, oferecendo prêmios em dinheiro para os melhores colocados. O link original está [aqui](https://www.kaggle.com/rikdifos/credit-card-approval-prediction).
 
                 O objetivo será construir o melhor modelo preditivo para identificar o perfil de renda do cliente, e assim tentar prever a renda de novos clientes.
 
                 ---
                 ''')
    
    # Carregando arquivo.
    
    df = st.file_uploader(':file_folder: Suba seu arquivo CSV ou FTR', type=(['csv', 'ftr', 'xlsx', 'xls']))
    try:
        df = load_data(df)
        st.success('Arquivo carregado.')
        st.markdown('''### Lista de Variáveis com Quantidade e Tipo:''')
        st.write(script.analise(df, 'mau'))
        st.markdown('''### Amostra dos Dados:''')
        st.write(f"**Linhas: {df.shape[0]} / Colunas: {df.shape[1]+1}**")
        st.write(df)
    except:
        st.error('Suba um arquivo.')
        st.markdown('''### Lista de Variáveis com Quantidade e Tipo:''')
        st.error('Indísponível.')
        st.markdown('''### Amostra dos Dados:''')
        st.error('Indísponível.')