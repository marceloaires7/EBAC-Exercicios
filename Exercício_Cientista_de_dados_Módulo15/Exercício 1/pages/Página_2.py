# Importações de Pacotes:
import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import time
import plotly.figure_factory as ff
from bokeh.plotting import figure

# Layout da Página:
st.set_page_config(page_title= 'Módulo15Tarefa1',
                   page_icon= 'https://s3.amazonaws.com/gupy5/production/companies/39637/career/92146/images/2022-08-23_17-33_logo.jpg',
                   layout= 'wide',
                   initial_sidebar_state="collapsed")

# Print na Tela:
'''
# :violet[Módulo15Tarefa1]
### **:violet[Página 2]**
---
Aqui nós vamos *desenvolver* nosso **primeiro** ambiente no **_Streamlit_**.
'''

st.write('---')

'## :green[:smile: Código 8:]'

'**Print de Código (linguagem python):**'

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

st.write('---')

'## :green[:smile: Código 9:]'

st.write('**Print de Fórmulas Matemáticas:**')

col1, col2, col3 = st.columns(3)
col1.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.write('---')

'## :green[:smile: Código 10:]'

st.slider("**st.slider de 0 á 100 com 2 pontos de seleção:**", 0, 100, (25, 75))

st.write('---')

'## :green[:smile: Código 11:]'
st.write('**Métricas com indicadores de subida e queda:**')

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
col1.metric("Temperatura", "40 °C", "5.2 °C")
col2.metric("Vento", "14 km/h", "-8%")
col3.metric("Umidade", "86%", "4%")

st.write('---')

'## :green[:smile: Código 12:]'
'**DataFrame em formato de Tabela com informações numéricas e gráficas:**'
df = pd.DataFrame(
    {
        "name": ["Google", "Yahoo", "DuckDuckGo"],
        "url": ["https://www.google.com.br/", "https://www.yahoo.com.br/", "https://www.duckduckgo.com/"],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        "name": "Site de Buscas",
        "stars": st.column_config.NumberColumn(
            "Pontuação",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("Endereço do Site"),
        "views_history": st.column_config.LineChartColumn(
            "Visualizações (últimos 30 dias)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)

st.write('---')

'## :green[:smile: Código 13:]'
'**Tabela Editável (podendo adicionar dados novos):**'
df = pd.DataFrame(
    [
       {"Comando": "st.selectbox", "Avaliação": 4, "is_widget": True},
       {"Comando": "st.balloons", "Avaliação": 5, "is_widget": False},
       {"Comando": "st.time_input", "Avaliação": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(
    df,
    column_config={
        "Comando": "Streamlit Comando",
        "Avaliação": st.column_config.NumberColumn(
            help="Qual é sua nota de 1 á 5 ?",
            min_value=1,
            max_value=5,
            step=1,
            format="%d ⭐"
        ),
        "is_widget": "Widget ?"
    },
    hide_index=True,
    num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["Avaliação"].idxmax()]["Comando"]
st.markdown(f"Seu comando favorito é **{favorite_command}** 🎈")

st.write('---')

'## :green[:smile: Código 14:]'
'**Plotagem de Gráficos:**'
col1, col2, col3 = st.columns(3)
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
col1.write('**Gráfico 1:**')
col1.area_chart(chart_data)

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
col2.write('**Gráfico 2:**')
col2.plotly_chart(fig, use_container_width=True)

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)
col3.write('**Gráfico 3:**')
col3.bokeh_chart(p, use_container_width=True)