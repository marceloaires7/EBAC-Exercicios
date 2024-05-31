import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import script

def app():
    df = st.session_state['df_final'][0]

    st.title('📊 :blue[GRÁFICOS]')

    st.write('## Descritiva básica univariada (Qualitativa e Quantitativa)')

    col1, col2, col3, col4 = st.columns([1, .5, 1, .5])

##########################################################################################################
# QUALITATIVA

    uniQuali = col1.selectbox('**QUALITATIVA:**', df.select_dtypes(include='object').columns)

    if 'graficos' not in st.session_state:
        st.session_state['graficos'] = {}

    for i in df.select_dtypes(include='object').columns:
        st.session_state['graficos'][i] = script.graficoQuali(uniQuali=i)

    col1.pyplot(fig=st.session_state['graficos'][uniQuali], use_container_width=True)

    col2.write('Contagem:')
    col2.write(df[uniQuali].value_counts()
                           .sort_index()
                           .set_axis(df[uniQuali]
                           .value_counts()
                           .sort_index()
                           .index.astype(str)))

##########################################################################################################
# QUANTITATIVA

    uniQuanti = col3.selectbox('**QUANTITATIVA:**', df.select_dtypes(exclude='object').columns)
    
    for i in df.select_dtypes(exclude='object').columns:
        st.session_state['graficos'][i] = script.graficoQuanti(uniQuanti=i)

    col3.pyplot(fig=st.session_state['graficos'][uniQuanti][0], use_container_width=True)

    df_cut = st.session_state['graficos'][uniQuanti][1]
    col4.write('Contagem:')
    col4.write(df_cut[uniQuanti].value_counts()
                                .sort_index()
                                .set_axis(df_cut[uniQuanti]
                                .value_counts()
                                .sort_index()
                                .index.astype(str)))
    
##########################################################################################################
# 