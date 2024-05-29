import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def app():
    st.title('📊 :blue[GRÁFICOS]')

    df = st.session_state['df_final'][0]

##########################################################################################################
# QUALITATIVA

    st.write('## Descritiva básica univariada (Qualitativa e Quantitativa)')

    col1, col2, col3, col4 = st.columns([1, .5, 1, .5])

    uniQuali = col1.selectbox('**Descritiva básica univariada (Qualitativa)**',
                          df.select_dtypes(include='object').columns)

    plt.figure(figsize=(5,4))
    ax = sns.countplot(data=df, x=uniQuali, hue=uniQuali, legend=False, palette="tab10")

    ax.tick_params(axis='x', rotation=270, length=6, width=2, grid_color='r', grid_alpha=0.5)
    ax.set_title(f'Contagem da variável {ax.get_xlabel()}', color='navy')
    ax.set_ylim(ymax=ax.get_ylim()[1]*1.2)
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='left', va='baseline', fontsize=9, color='black', xytext=(0, 5),
                textcoords='offset points', rotation=45)

    col1.pyplot(fig=plt, use_container_width=True)
    col2.write('Contagem:')
    col2.write(df[uniQuali].value_counts()
                            .sort_index()
                            .set_axis(df[uniQuali]
                            .value_counts()
                            .sort_index()
                            .index.astype(str)))

##########################################################################################################
# QUANTITATIVA

    df_cut = df.copy()
    df_cut['idade'] = pd.qcut(df['idade'], 9, precision=0, duplicates='drop')
    df_cut['tempo_emprego'] = pd.qcut(df['tempo_emprego'].fillna(-1), 9, precision=0, duplicates='drop')
    df_cut['renda'] = pd.qcut(df['renda'], 9, precision=0, duplicates='drop')

    # col3.write('#### Descritiva básica univariada (Quantitativa)')

    uniQuanti = col3.selectbox('**Descritiva básica univariada (Quantitativa)**',
                          df_cut.select_dtypes(exclude='object').columns)
    
    plt.figure(figsize=(5,4))
    ax = sns.countplot(data=df_cut, x=uniQuanti, hue=uniQuanti, legend=False, palette="tab10")

    ax.tick_params(axis='x', rotation=270, length=6, width=2, grid_color='r', grid_alpha=0.5)
    ax.set_title(f'Contagem da variável {ax.get_xlabel()}', color='navy')
    ax.set_ylim(ymax=ax.get_ylim()[1]*1.2)
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='left', va='baseline', fontsize=9, color='black', xytext=(0, 5),
                textcoords='offset points', rotation=45)

    col3.pyplot(fig=plt, use_container_width=True)

    col4.write('Contagem:')

    col4.write(df_cut[uniQuanti].value_counts()
                                .sort_index()
                                .set_axis(df_cut[uniQuanti]
                                .value_counts()
                                .sort_index()
                                .index.astype(str)))