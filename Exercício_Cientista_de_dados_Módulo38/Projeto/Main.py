import streamlit as st
import script

from streamlit_option_menu import option_menu

import Gráfico, Análise, Home

st.set_page_config(page_title='Projeto Final',
                   page_icon='https://web-summit-avenger.imgix.net/production/logos/original/68de83f411416128ffe8c1a3789a99b5ba538a6f.png?ixlib=rb-3.2.1&fit=fill&fill-color=white',
                   initial_sidebar_state='expanded',
                   layout='wide')

st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

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
                options=['Home', 'Gráficos', 'Análise'],
                icons=['house-fill', 'file-bar-graph-fill', 'rulers'],
                default_index=0,
                styles={
                     "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "gray"},
        "nav-link-selected": {"background-color": "darkcyan"},}
            )

        if 'df_final' not in st.session_state:
            st.session_state['df_final'] = ''

        # Carregando arquivo.
        st.sidebar.file_uploader(':file_folder: Suba seu arquivo CSV ou FTR', type=(['csv', 'ftr', 'xlsx', 'xls']), key='upload')

        try:
            if st.session_state['upload'] is None:
                df = st.session_state['df_final'][0]
                file_name = st.session_state['df_final'][1]
            else:
                df = script.load_data(st.session_state['upload'])
                file_name = st.session_state.get('upload').name
                st.session_state['df_final'] = df, file_name
            
            st.sidebar.success(f'Arquivo "{file_name}" carregado.', icon='✅')

        except:
            st.sidebar.error('Suba um arquivo válido.', icon='⛔')

        if app == "Home":
            Home.app()
        if app == "Gráficos":
            Gráfico.app()    
        if app == "Análise":
            Análise.app()
    
    run()