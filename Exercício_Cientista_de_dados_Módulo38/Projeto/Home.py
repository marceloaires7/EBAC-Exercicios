import streamlit as st
import pandas as pd
import os
import warnings
import script
import matplotlib.pyplot as plt

# Aplicativo da aba 'Home'
def app():

    # Descrição da aba 'Home'
    st.markdown(f'''
                 <div style="text-align:center">
                    <img src="https://raw.githubusercontent.com/marceloaires7/EBAC-Exercicios/main/Exercício_Cientista_de_dados_Módulo38/Projeto/ebac_logo-data_science.png" alt="ebac_logo-data_science" width="100%">
                 </div>
                
                 # 💼 :green[Projeto Final - Cientista de Dados]
                 ### Streamlit VI & Pycaret - Previsão de Renda
                 ##### Aluno: Marcelo Aires Coelho Otsuki[<div><img src="https://raw.githubusercontent.com/marceloaires7/EBAC-Exercicios/main/Exercício_Cientista_de_dados_Módulo38/Projeto/linkedin.png" width="2%"></div>](https://www.linkedin.com/in/marceloaco/)
                 ##### Data: Maio/2024
                 ---
                 ### Entendimento do negócio:
                 A análise para a concessão de cartões de crédito é um assunto de extrema importância no setor financeiro. Para que o limite de crédito seja liberado, o banco ou algum outro tipo de industria financeira, utilizam informações pessoais e dados fornecidos pelos candidato para prever a probabilidade de inadimplência futura e comportamento de endividamento com o cartão.

                 Vamos utlizar dados parecidos com o que encontramos no desafio do site [Kaggle](https://www.kaggle.com/), uma plataforma que promove desafios de ciência de dados, oferecendo prêmios em dinheiro para os melhores colocados. O link original está [aqui](https://www.kaggle.com/rikdifos/credit-card-approval-prediction). Porém utilizaremos dados fornecidos pela própria EBAC, em que há informações complementares em Português e com maior número de informações.
 
                 O objetivo será construir o melhor modelo preditivo para identificar o perfil de renda do cliente, e dizer se esse cliente é um potencial cliente inadimplente, considerado na variável respota como "mau" == True.
 
                 ---
                 ''', unsafe_allow_html=True)
    
    if 'df_final' not in st.session_state:
        st.session_state['df_final'] = ''

    # Carregando arquivo.
    st.file_uploader(':file_folder: Suba seu arquivo CSV ou FTR', type=(['csv', 'ftr', 'xlsx', 'xls']), key='upload')
    
    try:
        if st.session_state['upload'] is None:
            df = st.session_state['df_final'][0]
            file_name = st.session_state['df_final'][1]
        else:
            df = script.load_data(st.session_state['upload'])
            file_name = st.session_state.get('upload').name
            st.session_state['df_final'] = df, file_name
        
        st.success(f'Arquivo "{file_name}" carregado.', icon='✅')

        st.markdown('''### Amostra dos Dados:''')
        st.write(f"**Linhas: {df.shape[0]} / Colunas: {df.shape[1]+1}**")
        st.write(df)


        col4, col5 = st.columns([1, 1])

        col4.markdown('''### Lista de Variáveis com Quantidade e Tipo:''')
        col4.write(script.analise(df, 'mau'))

        col5.markdown('''### Variável resposta 'mau':''')
        fig, ax = plt.subplots(figsize=(2.5,2.5))
        ax.pie(df.mau.value_counts(),
            explode=(0, 0.3),
            labels=['bom', 'mau'],
            autopct='%1.2f%%',
            shadow=True,
            startangle=140)
        col5.pyplot(fig, use_container_width=False)

    except:
        st.error('Suba um arquivo válido.', icon='⛔')
        st.error('Indísponível.', icon='⚠️')