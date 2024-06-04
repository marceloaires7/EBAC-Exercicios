import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import script
from pycaret.classification import *

def app():
    st.title(
        f'''
        📐 :red[ANÁLISE]
        ---
        ''')
    try:
        data = st.session_state['data']
        data_unseen = st.session_state['data_unseen']

        st.cache
        clf = setup(data=data.reset_index(drop=True),
                    target='mau',
                    session_id=123,
                    numeric_imputation=-1,
                    remove_outliers=True,
                    pca=True,
                    pca_method='incremental',
                    fix_imbalance=True)
        
        st.write('### Configuração do modelo criado no PyCaret:')
        
        col1, col2, col3, col4 = st.columns([1,1,1,1])

        col1.write(clf._display_container[0][:8])

        col2.write(clf._display_container[0][8:16])
       
        col3.write(clf._display_container[0][16:24])
      
        col4.write(clf._display_container[0][24:])

        st.write('### Lista de modelos utilizados no PyCaret:')

        col1, col2, col3, col4 = st.columns(4)

        col1.write(models().iloc[:9,[0,2]]) 
        col2.write(models().iloc[9:,[0,2]])        
        
        col1, col2 = st.columns(2)
        col1.write('### CrossValidation dos modelos criados do comando:')
        col1.code("lightgbm = createmodel(estimator='lightgbm', fold=5)", language='python')

        lightgbm = script.createmodel(estimator='lightgbm', fold=5)
        col1.write(st.session_state['pullMod'].style.apply(lambda row: ['background-color: yellow'] * len(row) if row.name == 'Mean' else [''] * len(row), axis=1))

        col2.write('### CrossValidation dos modelos tunados do comando:')
        col2.code("tuned_lightgbm = tunemodel(lightgbm, optimize='AUC')", language='python')

        tuned_lightgbm = script.tunemodel(_estimator=lightgbm, fold=5, optimize='AUC')
        col2.write(st.session_state['pullTuned'].style.apply(lambda row: ['background-color: yellow'] * len(row) if row.name == 'Mean' else [''] * len(row), axis=1))


    except ValueError as e:
        st.error('Suba um arquivo válido.', icon='⛔')
        st.error('Indísponível.', icon='⚠️')
        st.write(e)
    