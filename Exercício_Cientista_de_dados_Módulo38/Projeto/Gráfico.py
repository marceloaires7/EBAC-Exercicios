import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import script

def app():

    ##################################
    ## Título e descrição da página ##
    ##################################

    st.title(
        f'''
        📊 :blue[GRÁFICOS]
        ---
        ''')

    try:

    #########################################
    ## Definindo DataFrame 'df' na página. ##
    #########################################

        df = st.session_state['df'][0]

    ################################################
    ## Descritiva básica univariada (Qualitativa) ##
    ################################################

        st.write('## Descritiva básica univariada (Qualitativa e Quantitativa)')

        col1, col2, col3, col4 = st.columns([1, .5, 1, .5])

        uniQuali = col1.selectbox('**QUALITATIVA:**', df.select_dtypes(include='object').columns, key='Qualitativa')

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

    #################################################
    ## Descritiva básica univariada (Quantitativa) ##
    #################################################

        uniQuanti = col3.selectbox('**QUANTITATIVA:**', df.select_dtypes(exclude='object').columns, key='Quantitativa')
        
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
        
    ########################################
    ## Descritiva bivariada (Qualitativa) ##
    ########################################

        st.markdown('''
                    ---
                    ## Descritiva bivariada (Qualitativa)''')
        
        col1, col2 = st.columns([1 , 1.3])

        UniQuali1 = col1.selectbox('**LINHA:**', df.select_dtypes(include='object').columns, key='Bivariada1')
        UniQuali2 = col2.selectbox('**COLUNA:**', df.select_dtypes(include='object').columns, key='Bivariada2')

        for i in df.select_dtypes(include='object').columns:
            for j in df.select_dtypes(include='object').columns:
                if i+j not in st.session_state['graficos']:
                   st.session_state['graficos'][i+j] = script.graficoBivar(UniQuali1=i, UniQuali2=j)
                    
        col1.pyplot(fig=st.session_state['graficos'][UniQuali1+UniQuali2][0])
        col2.write(st.session_state['graficos'][UniQuali1+UniQuali2][1])
        
    #########################################
    ## Descritiva bivariada (Quantitativa) ##
    #########################################

        st.markdown('''
                    ---
                    ## Descritiva bivariada (Quantitativa)''')

        col1, col2 = st.columns([1, 1])
                
        UniQuanti1 = col1.selectbox('**LINHA:**', df.select_dtypes(exclude='object').columns, key='Bivariada3')
        UniQuanti2 = col2.selectbox('**COLUNA:**', df.select_dtypes(exclude='object').columns, key='Bivariada4')

        for i in df.select_dtypes(exclude='object').columns:
            for j in df.select_dtypes(exclude='object').columns:
                if i+j not in st.session_state['graficos']:
                    st.session_state['graficos'][i+j] = script.graficoBivar2(UniQuanti1=i, UniQuanti2=j)

        df_cut = st.session_state['graficos'][UniQuanti1+UniQuanti2][1]

        col1.pyplot(fig=st.session_state['graficos'][UniQuanti1+UniQuanti2][0])
        col2.write(pd.crosstab(index=df_cut[UniQuanti1], columns=df_cut[UniQuanti2]))

    except:
        st.error('Suba um arquivo válido.', icon='⛔')
        st.error('Indísponível.', icon='⚠️')