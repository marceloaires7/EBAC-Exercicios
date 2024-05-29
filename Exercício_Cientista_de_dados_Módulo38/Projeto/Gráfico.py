import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.title('📊 :blue[GRÁFICOS]')

    df = st.session_state['df_final'][0]

    col1, col2, col3 = st.columns([1, 1, 1])

    option = col1.selectbox('Qual cidade você gosta mais?',
                          df.select_dtypes(include='object').columns)

    plt.figure(figsize=(5,4))
    ax = sns.countplot(data=df, x=option, hue=option, legend=False, palette="tab10")

    ax.tick_params(axis='x', rotation=270, length=6, width=2, grid_color='r', grid_alpha=0.5)
    ax.set_title(f'Contagem da variável {ax.get_xlabel()}', color='navy')
    ax.set_ylim(ymax=ax.get_ylim()[1]*1.2)
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='left', va='baseline', fontsize=9, color='black', xytext=(0, 5),
                textcoords='offset points', rotation=45)
        
    col1, col2, col3 = st.columns([1, .8, .8])

    col1.pyplot(fig=plt, use_container_width=True)