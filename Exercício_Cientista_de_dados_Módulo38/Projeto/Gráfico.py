import streamlit as st

def app():
    st.title('📊 :blue[GRÁFICOS]')

    st.write(st.session_state['df_final'][0])