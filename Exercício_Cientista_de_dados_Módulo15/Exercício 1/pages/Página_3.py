# Importações de Pacotes:
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import time

# Layout da Página:
st.set_page_config(page_title= 'Módulo15Tarefa1',
                   page_icon= 'https://s3.amazonaws.com/gupy5/production/companies/39637/career/92146/images/2022-08-23_17-33_logo.jpg',
                   layout= 'wide',
                   initial_sidebar_state="collapsed")

# Print na Tela:
'''
# :violet[Módulo15Tarefa1]
### **:violet[Página 3]**
---
Aqui nós vamos *desenvolver* nosso **primeiro** ambiente no **_Streamlit_**.
'''

st.write('---')

'## :green[:smile: Código 15:]'
'**Diferentes tipos de avisos:**'
st.error('Caixa de Texto de Error.', icon="🚨")
st.warning('Caixa de Texto de Aviso.', icon="⚠️")
st.info('Caixa de Texto de Informação.', icon="ℹ️")
st.success('Caixa de Texto de Sucesso.', icon="✅")

st.write('---')

'## :green[:smile: Código 16:]'
'**Utilização do código, para obter ajuda e mais informações sobre:**'
st.code("st.help(np.sum)", language="python")
st.help(np.sum)

st.write('---')

'## :green[:smile: Código 17:]'
'**Retorna paramentos em QUERY:**'
st.experimental_get_query_params()
{"show_map": ["True"], "selected": ["asia", "america"]}

st.write('---')

'## :green[:smile: Código 18:]'
'**Exemplo de botão:**'
if st.button('Botão'):
    st.write('Botão foi clicado!')
    if st.button('Voltar'):
        # Isso nunca vai ser executado.
        st.write('Botão 2 foi clicado!')

st.write('---')

'## :green[:smile: Código 19:]'
'**Imagem com funçãod de botão (Clique):**'
with st.echo():
    st.title("DOG")

    st.markdown("[![Click me](https://cdn-icons-png.flaticon.com/128/2454/2454302.png)](https://streamlit.io)")

st.write('---')

'## :green[:smile: Código 20:]'

color = st.color_picker('**Selecionar cores:**', '#00f900')
st.write('**A cor escolhida foi %s**' % color)

st.write('---')

'# :blue[:sunglasses: FIM :sunglasses:]'

