import streamlit as st
import pandas as pd
import os
import warnings
import script
import matplotlib.pyplot as plt

#################################
## Aplicativo da página 'Home' ##
#################################

def app():

#########################################
## Título e descrição da página 'Home' ##
#########################################

    st.markdown(f'''
                 <div style="text-align:center">
                    <img src="https://raw.githubusercontent.com/marceloaires7/EBAC-Exercicios/main/Exercício_Cientista_de_dados_Módulo38/Projeto/output/ebac_logo-data_science.png" alt="ebac_logo-data_science" width="100%">
                 </div>
                
                 # 💼 :green[Projeto Final - Cientista de Dados]
                 ### Streamlit VI & Pycaret - Previsão de Renda
                 ##### Aluno: [Marcelo Aires Coelho Otsuki ![LinkedIn](https://raw.githubusercontent.com/marceloaires7/EBAC-Exercicios/main/Exercício_Cientista_de_dados_Módulo38/Projeto/output/linkedin.png)](https://www.linkedin.com/in/marceloaco/)
                 ##### Data: Maio/2024
                 ---
                 ### Entendimento do negócio:
                 A análise para a concessão de cartões de crédito é um assunto de extrema importância no setor financeiro. Para que o limite de crédito seja liberado, o banco ou algum outro tipo de industria financeira, utilizam informações pessoais e dados fornecidos pelos candidato para prever a probabilidade de inadimplência futura e comportamento de endividamento com o cartão.

                 Vamos utlizar dados parecidos com o que encontramos no desafio do site [Kaggle](https://www.kaggle.com/), uma plataforma que promove desafios de ciência de dados, oferecendo prêmios em dinheiro para os melhores colocados. O link original está [aqui](https://www.kaggle.com/rikdifos/credit-card-approval-prediction). Porém utilizaremos dados fornecidos pela própria EBAC, em que há informações complementares em Português e com maior número de informações.
 
                 O objetivo será construir o melhor modelo preditivo, utilizando o Pycaret, para identificar o perfil de renda do cliente, e dizer se esse cliente é um potencial cliente inadimplente, considerado na variável respota como "mau" == True.
 
                 ---
                 ''', unsafe_allow_html=True)

################################################################
## Importando as variáveis criadas no Main.py e analisando-as ##
################################################################

    try:

        df = st.session_state['df'][0]
        data = st.session_state['data']
        data_unseen = st.session_state['data_unseen']

        st.markdown('''### Amostra dos Dados:''')
        st.write(f"**Linhas: {df.shape[0]} / Colunas: {df.shape[1]+1}**")
        st.write(df.head())

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

        st.write('### Separação do Dataset:')
        col1, col2 = st.columns([1,1])

        col1.write(
            f'''
             ##### Conjunto de dados para modelagem (treino e teste):
             **data:**

             Linhas: {data.shape[0]} / Colunas: {data.shape[1]}
             ''')
        col1.write(script.analise(data=data, y='mau'))

        col2.write(
            f'''
             ##### Conjunto de dados não usados no treino/teste, apenas como validação:
             **data_unseen:**

             Linhas: {data_unseen.shape[0]} / Colunas: {data_unseen.shape[1]}
             ''')
        col2.write(script.analise(data=data_unseen, y='mau'))

############
## except ##
############
        
    except:
        
        st.error('Suba um arquivo válido.', icon='⛔')
        st.error('Indísponível.', icon='⚠️')