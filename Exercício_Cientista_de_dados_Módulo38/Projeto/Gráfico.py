import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import script

def app():

    st.title('📊 :blue[GRÁFICOS]')

    try:

        df = st.session_state['df'][0]

        st.write('## Descritiva básica univariada (Qualitativa e Quantitativa)')

        col1, col2, col3, col4 = st.columns([1, .5, 1, .5])

    ##########################################################################################################
    # QUALITATIVA

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

    ##########################################################################################################
    # QUANTITATIVA

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
        
    ##########################################################################################################
    # Descritiva bivariada (Qualitativa)

        st.markdown('''
                    ---
                    ## Descritiva bivariada (Qualitativa)''')
        
        col1, col2, col3, col4 = st.columns([.4, 0.001, 1, 1.4])

        UniQuali1 = col1.selectbox('**BIVARIADA 1:**', df.select_dtypes(include='object').columns, key='Bivariada1')
        UniQuali2 = col1.selectbox('**BIVARIADA 2:**', df.select_dtypes(include='object').columns, key='Bivariada2')

        for i in df.select_dtypes(include='object').columns:
            for j in df.select_dtypes(include='object').columns:
                st.session_state['graficos'][i+j] = script.graficoBivar(UniQuali1=i,
                                                                        UniQuali2=j)
        # fig, ax = plt.subplots(figsize=(5,4))
        # ct = pd.crosstab(df[UniQuali1], df[UniQuali2])
        # sns.heatmap(ct, annot=True, cmap="YlGnBu", fmt='d', linewidths=.5, linecolor='black')
        # ax.set_title(f'Contagem da variável {UniQuali1} por {UniQuali2}', color='navy')  
        # st.write(st.session_state['graficos'][UniQuali1+UniQuali2])
        col3.pyplot(fig=st.session_state['graficos'][UniQuali1+UniQuali2][0])
        col4.write(st.session_state['graficos'][UniQuali1+UniQuali2][1])
        
    ##########################################################################################################
    # Descritiva bivariada (Quantitativa)
        st.markdown('''
            ---
            ## Descritiva bivariada (Qualitativa)''')

        col1, col2 = st.columns([1, 1])
        fig, ax = plt.subplots(figsize=(5,4))

        correlation_matrix = df.select_dtypes(include='number').corr()

        ax = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        ax.set_title("Heatmap")

        col1.pyplot(plt)
        col2.write(correlation_matrix)
    except:
        # Handle the specific ValueError exception
        st.error('Suba um arquivo válido.', icon='⛔')
        st.error('Indísponível.', icon='⚠️')