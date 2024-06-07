import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import script
from pycaret.classification import *

####################################
## Aplicativo da página 'Análise' ##
####################################

def app():

############################################
## Título e descrição da página 'Análise' ##
############################################

    st.title(
        f'''
        📐 :red[ANÁLISE]
        ---
        ''')
    try:

###########################################################
## Definindo as variaveis alojadas no 'st.session_state' ##
###########################################################
        
        if 'pullMod' not in st.session_state:
            st.session_state['pullMod'] = {}
    
        if 'pullTuned' not in st.session_state:
            st.session_state['pullTuned'] = {}

        data = st.session_state['data'][['renda', 'qtd_filhos', 'posse_de_veiculo', 'posse_de_imovel', 'estado_civil', 'sexo', 'tempo_emprego', 'mau']].sample(50000, random_state=42)
        data_unseen = st.session_state['data_unseen']

#################################################
## Configurando o Modelo com o Pycaret (setup) ##
#################################################

        clf = setup(data=data.reset_index(drop=True),
                    target='mau',
                    session_id=123,
                    numeric_imputation=-1,
                    remove_outliers=True,
                    normalize=True,
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
        
##############################################################################
## Configurando o Modelo com 'create_model' utilizando estimator='lightgbm' ##
##############################################################################
        
        col1, col2 = st.columns(2)
        col1.write('### CrossValidation dos modelos criados do comando:')
        col1.code("lightgbm = createmodel(estimator='lightgbm', fold=5)", language='python')

        lightgbm = script.createmodel(estimator='lightgbm', fold=5)
        st.session_state['pullMod'] = lightgbm[1]
        col1.write(st.session_state['pullMod'].style.apply(lambda row: ['background-color: yellow'] * len(row) if row.name == 'Mean' else [''] * len(row), axis=1))

#######################################################################
## Tunando o Modelo com 'tune_model' utilizando estimator='lightgbm' ##
#######################################################################

        col2.write('### CrossValidation dos modelos tunados do comando:')
        col2.code("tuned_lightgbm = tunemodel(lightgbm, optimize='AUC', fold=5)", language='python')

        tuned_lightgbm = script.tunemodel(_estimator=lightgbm[0], fold=5, optimize='Accuracy')
        st.session_state['pullTuned'] = tuned_lightgbm[1]
        col2.write(st.session_state['pullTuned'].style.apply(lambda row: ['background-color: yellow'] * len(row) if row.name == 'Mean' else [''] * len(row), axis=1))
        
############################################
## Plotando gráficos gerados pelo PyCaret ##
############################################

        col1, col2 = st.columns(2)
       
        fig, ax = plt.subplots(figsize=(5,4))
        col1.write('### CURVA ROC:')
        col1.image(plot_model(tuned_lightgbm[0], plot = 'auc', save='./output'), width=550)
        col2.write('### ESTATÍSTICAS DO KS:')
        col2.image(plot_model(tuned_lightgbm[0], plot = 'ks', save='./output'), width=600)
        
        col1, col2 = st.columns(2)
       
        fig, ax = plt.subplots(figsize=(5,4))
        
        col1.write('### CURVA PRECISION-RECALL:')
        col1.image(plot_model(tuned_lightgbm[0], plot = 'pr', save='./output'), width=550)
        col2.write('### FEATURE IMPORTANCE:')
        col2.image(plot_model(tuned_lightgbm[0], plot = 'feature', save='./output'), width=600)
        
        col1, col2 = st.columns(2)
       
        fig, ax = plt.subplots(figsize=(5,4))
        
        col1.write('### CONFUSION MATRIX:')
        col1.image(plot_model(tuned_lightgbm[0], plot = 'confusion_matrix', save='./output'), width=550)

##################
## Modelo Final ##
##################
    
        st.write(predict_model(tuned_lightgbm[0]))
        st.write(tuned_lightgbm)

############
## except ##
############

    except ValueError as e:
        st.error('Suba um arquivo válido.', icon='⛔')
        st.error('Indísponível.', icon='⚠️')
        st.write(e)
    