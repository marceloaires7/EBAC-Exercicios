import streamlit as st
import script
import seaborn as sns
import matplotlib.pyplot as plt

from streamlit_option_menu import option_menu

import Gráfico, Análise, Home

st.set_page_config(page_title='Projeto Final',
                   page_icon='https://web-summit-avenger.imgix.net/production/logos/original/68de83f411416128ffe8c1a3789a99b5ba538a6f.png?ixlib=rb-3.2.1&fit=fill&fill-color=white',
                   initial_sidebar_state='expanded',
                   layout='wide')

st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)

st.sidebar.image(image='https://afubesp.org.br/wp-content/uploads/2022/07/logo_ebac-960x640.png',
                 caption='Aluno: Marcelo Aires Coelho Otsuki (Cientista de Dados)')

class Multiapp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run():

        with st.sidebar:
            app = option_menu(
                menu_title='MENU',
                menu_icon='list',
                options=['Home', 'Gráficos', 'Modelagem/Análise'],
                icons=['house-fill', 'file-bar-graph-fill', 'rulers'],
                default_index=0,
                styles={
                     "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "gray"},
        "nav-link-selected": {"background-color": "darkcyan"},}
            )

        if 'df' not in st.session_state:
            st.session_state['df'] = ''

        if 'data' not in st.session_state:
            st.session_state['data'] = ''

        if 'data_unseen' not in st.session_state:
            st.session_state['data_unseen'] = ''

        # Carregando arquivo.
        st.sidebar.file_uploader(':file_folder: Suba seu arquivo CSV ou FTR', type=(['csv', 'ftr', 'xlsx', 'xls']), key='upload')

        try:
            if st.session_state['upload'] is None:
                df = st.session_state['df'][0]
                # df.fillna({'tempo_emprego': -1}, inplace=True)
                file_name = st.session_state['df'][1]
            else:
                df = script.load_data(st.session_state['upload'])
                # df.fillna({'tempo_emprego': -1}, inplace=True)
                file_name = st.session_state.get('upload').name
                st.session_state['df'] = df, file_name

                data = df.reset_index().sample(frac=.95, random_state=42)
                data_unseen = df.reset_index().drop(data.index)
                data.set_index(keys='data_ref', inplace=True)
                data_unseen.set_index(keys='data_ref', inplace=True)

                st.session_state['data'] = data
                st.session_state['data_unseen'] = data_unseen

            st.sidebar.success(f'Arquivo "{file_name}" carregado.', icon='✅')

        except:
            st.sidebar.error('Suba um arquivo válido.', icon='⛔')
            

        if app == "Home":
            Home.app()
        if app == "Gráficos":
            Gráfico.app()    
        if app == "Modelagem/Análise":
            Análise.app()
    
    run()