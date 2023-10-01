# Imports
import pandas            as pd
import streamlit         as st
import seaborn           as sns
import matplotlib.pyplot as plt
from PIL                 import Image
from io                  import BytesIO

# Set no tema do seaborn para melhorar o visual dos plots
custom_params = {"axes.spines.right": False, "axes.spines.top": False}
sns.set_theme(style="ticks", rc=custom_params)

# Função para ler os dados
@st.cache(show_spinner=True, allow_output_mutation=True)
def load_data(file_data):
    try:
        return pd.read_csv(file_data, sep=';')
    except:
        return pd.read_excel(file_data)
    
# Função para filtrar baseado na multiseleção de categorias
@st.cache(allow_output_mutation=True)
def multiselect_filter(relatorio, col, selecionados):
    if 'all' in selecionados:
        return relatorio
    else:
        return relatorio[relatorio[col].isin(selecionados)].reset_index(drop=True)
    
# Função para converter o df para csv
@st.cache
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

# Função para converter o df para excel
@st.cache
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data

# Função principal da aplicação
def main():
    # Configuração inicial da página da aplicação
    st.set_page_config(page_title= 'Análise Telemarketing',
                       page_icon= '../img/telmarketing_icon.png',
                       layout='wide',
                       initial_sidebar_state='expanded'
                      )

    # Título principal da aplicação
    st.write('# Análise Telemarketing')
    st.markdown("---")

if __name__ == '__main__':
	main()