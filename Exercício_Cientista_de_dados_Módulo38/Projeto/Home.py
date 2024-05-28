import streamlit as st
import pandas as pd
import os
import warnings
import script
import matplotlib.pyplot as plt

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
    col1, col2, col3 = st.columns([2.5, 1.2, 4])


    if 'df' not in st.session_state:
        fl = col1.file_uploader(':file_folder: Suba seu arquivo CSV ou FTR', type=(['csv', 'ftr', 'xlsx', 'xls']))
        st.session_state['df'] = load_data(fl)

    try:
        
        df = st.session_state['df']

        col2.success('Arquivo carregado.', icon='✅')

        fig, ax = plt.subplots(figsize=(2.5,2.5))
        ax.pie(df.mau.value_counts(),
        explode=(0, 0.3),
        labels=['bom', 'mau'],
        autopct='%1.2f%%',
        shadow=True,
        startangle=140)

        st.markdown('''### Amostra dos Dados:''')
        st.write(f"**Linhas: {df.shape[0]} / Colunas: {df.shape[1]+1}**")
        st.write(df)

        col4, col5 = st.columns([1, 1])

        col4.markdown('''### Lista de Variáveis com Quantidade e Tipo:''')
        col4.write(script.analise(df, 'mau'))

        col5.markdown('''### Variável resposta 'mau':''')
        col5.pyplot(fig, use_container_width=False)

    except:
        col2.error('Suba um arquivo.', icon='⛔')
        st.markdown('''### Amostra dos Dados:''')
        st.error('Indísponível.', icon='⚠️')

        col4, col5 = st.columns([1, 1])

        col4.markdown('''### Lista de Variáveis com Quantidade e Tipo:''')
        col4.error('Indísponível.', icon='⚠️')

        col5.markdown('''### Variável resposta 'mau':''')
        col5.error('Indísponível.', icon='⚠️')






