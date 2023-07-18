# Importações de Pacotes:
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import time

# Import CSV 'input_M15_SINASC_RO_2019.csv'
sinasc = pd.read_csv('./MaterialExercicio/input_M15_SINASC_RO_2019.csv')
sinasc['DTNASC'] = pd.to_datetime(sinasc['DTNASC'])

# Layout da Página:
st.set_page_config(page_title= 'Módulo15Tarefa1',
                   page_icon= 'https://s3.amazonaws.com/gupy5/production/companies/39637/career/92146/images/2022-08-23_17-33_logo.jpg',
                   layout= 'wide',
                   initial_sidebar_state="collapsed")

# Print na Tela:
'''
# :violet[Módulo15Tarefa1]
### **:violet[Página 1]**
---
Aqui nós vamos *desenvolver* nosso **primeiro** ambiente no **_Streamlit_**.
'''

st.write('---')

'## :green[:smile: Código 1:]'

x = st.slider(':red[Slider]\n\n:red[Qual é a Raíz Quadrada de:]')  # 👈 this is a widget
st.write(f'A Raíz Quadrada de **:red[{x}] é igual a :red[{x * x}.]**')

y = st.number_input(':blue[Input]\n\n:blue[Qual é a Raíz Quadrada de:]',step=1,min_value=0, max_value=100)
st.write(f'A Raíz Quadrada de **:blue[{y}] é igual a :blue[{y * y}.]**')

st.write('---')

'## :green[:smile: Código 2:]'

st.text_input("Qual é o seu nome:", key="name")

# You can access the value at any point with:
st.write(f'Olá {st.session_state.name}, seja Bem-vindo.')

st.write('---')

'## :green[:smile: Código 3:]'

if st.checkbox('Tabela SINASC Rondônia (Exemplo).'):
    st.write(sinasc.head())

st.write('---')

'## :green[:smile: Código 4:]'

df = pd.DataFrame({
    'column': ['Brasília', 'São Paulo', 'Rio de Janeiro', 'Salvador']
    })

option = st.selectbox(
    'Qual cidade você gosta mais?',
     df['column'])

st.write(f'Cidade Preferida: **:blue[{option}.]**')

st.write('---')

'## :green[:smile: Código 5:]'

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Carregando...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Carregando...Tudo pronto!')

st.subheader('Uber Raw data')
st.write(data)

st.write('---')

'## :green[:smile: Código 6:]'

st.subheader('Mapa de Brasília com marcações aleatórias:')
map_data = pd.DataFrame(
    np.random.randn(300, 2) / [50, 50] + [-15.79, -47.89],
    columns=['lat', 'lon'])

st.map(map_data)

st.write('---')

'## :green[:smile: Código 7:]'

def get_usuario():
    return 'João'

with st.echo():
    # Tudo dentro deste bloco de código será Visualizado
    # e Executado na tela, inclusive este comentário (#).

    def get_pontuacao():
        return '!!!'

    ola = "Olá, "
    usuario = get_usuario()
    pontuacao = get_pontuacao()

    st.write(ola, usuario, pontuacao)

# Agora o que está fora do st.echo() não será Visualizado.
st.write('Feito!')