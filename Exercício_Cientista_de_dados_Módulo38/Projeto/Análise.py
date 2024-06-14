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

    st.title('📐 :red[ANÁLISE]')
    
    st.write('Aqui, conduzimos a modelagem e análise de dados utilizando PyCaret. Seguimos uma sequência clara para criar e otimizar modelos preditivos:')
    
    col1, col2 = st.columns(2)

    col1.write('''- **Busca das Variáveis:** Preparamos os datasets.
- **Configuração com setup():** Definimos o ambiente de modelagem.
- **Criação com create_model():** Construímos o modelo inicial com LightGBM.
- **Ajuste com tune_model():** Otimizamos o modelo.''')

    col2.write('''- **Finalização com finalize_model():** Consolidamos o modelo.
- **Visualização com plot_model():** Apresentamos gráficos de desempenho.
- **Salvamento com save_model():** Armazenamos o modelo final.
- **Previsões com predict_model():** Fazemos previsões em novos dados.''')
           
    st.write('''Explore esta página para entender e aplicar cada etapa do processo de modelagem.

--- ''')

    try:

###########################################################
## Definindo as variaveis alojadas no 'st.session_state' ##
###########################################################
        
        if 'pullMod' not in st.session_state:
            st.session_state['pullMod'] = {}
    
        if 'pullTuned' not in st.session_state:
            st.session_state['pullTuned'] = {}

        data = st.session_state['data']
        data_unseen = st.session_state['data_unseen']

#################################################
## Configurando o Modelo com o Pycaret (setup) ##
#################################################

        st.write('### Configuração com setup():')

        st.code('''clf = setup(data=data,
            target='mau',
            session_id=123,
            numeric_imputation=-1)''')

        clf = setup(data=data,
                    target='mau',
                    session_id=123,
                    numeric_imputation=-1)

        
        col1, col2, col3, col4 = st.columns([1,1,1,1])

        col1.write(clf._display_container[0][:8])

        col2.write(clf._display_container[0][8:16])
       
        col3.write(clf._display_container[0][16:24])
      
        col4.write(clf._display_container[0][24:])

        st.write('### Lista de modelos utilizados no PyCaret:')

        col1, col2, col3, col4 = st.columns(4)

        col1.write(models().iloc[:5,[0,2]]) 
        col2.write(models().iloc[5:10,[0,2]])        
        col3.write(models().iloc[10:15,[0,2]]) 
        col4.write(models().iloc[15:,[0,2]])
        
##############################################################################
## Configurando o Modelo com 'create_model' utilizando estimator='lightgbm' ##
##############################################################################
        
        col1, col2 = st.columns(2)
        col1.write('### Criação com create_model():')
        col1.code("lightgbm = create_model(estimator='lightgbm', fold=5)", language='python')

        lightgbm = script.createmodel(estimator='lightgbm', fold=5)
        st.session_state['pullMod'] = lightgbm[1]
        col1.write(st.session_state['pullMod'].style.apply(lambda row: ['background-color: yellow'] * len(row) if row.name == 'Mean' else [''] * len(row), axis=1))

#######################################################################
## Tunando o Modelo com 'tune_model' utilizando estimator='lightgbm' ##
#######################################################################

        col2.write('### Ajuste com tune_model():')
        col2.code("tuned_lightgbm = tune_model(lightgbm, fold=5, optimize='MCC')", language='python')

        tuned_lightgbm = script.tunemodel(_estimator=lightgbm[0], fold=5, optimize='MCC')
        st.session_state['pullTuned'] = tuned_lightgbm[1]
        col2.write(st.session_state['pullTuned'].style.apply(lambda row: ['background-color: yellow'] * len(row) if row.name == 'Mean' else [''] * len(row), axis=1))

##################
## Modelo Final ##
##################
        st.write('### Finalização com finalize_model():')
        st.code('final_lightgbm = finalize_model(tuned_lightgbm)', language='python')
        final_lightgbm = finalize_model(tuned_lightgbm[0])
        st.write(final_lightgbm)
        
############################################
## Plotando gráficos gerados pelo PyCaret ##
############################################
        st.write('### Visualização com plot_model():')

        col1, col2 = st.columns(2)
       
        fig, ax = plt.subplots(figsize=(5,4))
        col1.write('#### CURVA ROC:')
        col1.image(plot_model(final_lightgbm, plot = 'auc', save='./output'), width=550)
        col2.write('#### ESTATÍSTICAS DO KS:')
        col2.image(plot_model(final_lightgbm, plot = 'ks', save='./output'), width=600)
        
        col1, col2 = st.columns(2)
       
        fig, ax = plt.subplots(figsize=(5,4))
        
        col1.write('#### CURVA PRECISION-RECALL:')
        col1.image(plot_model(final_lightgbm, plot = 'pr', save='./output'), width=550)
        col2.write('#### FEATURE IMPORTANCE:')
        col2.image(plot_model(final_lightgbm, plot = 'feature', save='./output'), width=600)
        
        col1, col2 = st.columns(2)
       
        fig, ax = plt.subplots(figsize=(5,4))
        
        col1.write('#### CONFUSION MATRIX:')
        col1.image(plot_model(final_lightgbm, plot = 'confusion_matrix', save='./output'), width=550)

##################################
## Salvamento com save_model(): ##
##################################

        st.write('### Salvamento com save_model():')
        st.code("save_model(final_lightgbm, 'Final_LightGBM_Model')")
        save_model(final_lightgbm, 'Final_LightGBM_Model')
        
####################################
## Previsões com predict_model(): ##
####################################
        col1, col2 = st.columns(2)

        st.write('### Previsões com predict_model():')

        st.code("saved_lightgbm = load_model('Final_LightGBM_Model')")
        saved_lightgbm = load_model('Final_LightGBM_Model')

        st.code("new_prediction = predict_model(saved_lightgbm, data=data_unseen)")
        new_prediction = predict_model(saved_lightgbm, data=data_unseen)

        fig, ax = plt.subplots(figsize=(5,4))
        ct = pd.crosstab(new_prediction['mau'], new_prediction['prediction_label'])
        ax = sns.heatmap(ct, annot=True, cmap="YlGnBu", fmt='d', linewidths=.5, linecolor='black', xticklabels=new_prediction['prediction_label'].map({0: 'Bom', 1: 'Mau'}).unique())
        col1.pyplot(fig)
                
############
## except ##
############

    except ValueError as e:
        st.error('Suba um arquivo válido.', icon='⛔')
        st.error('Indísponível.', icon='⚠️')
        st.write(e)
    