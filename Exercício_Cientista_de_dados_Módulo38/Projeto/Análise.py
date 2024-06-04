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
                    pca=True)
        
        st.write('### Modelos utilizados no PyCaret:')

        col1, col2, col3, col4 = st.columns(4)

        col1.write(models().iloc[:9,[0,2]]) 
        col2.write(models().iloc[9:,[0,2]])        
        
    except ValueError as e:
        st.error('Suba um arquivo válido.', icon='⛔')
        st.error('Indísponível.', icon='⚠️')
        st.write(e)
    