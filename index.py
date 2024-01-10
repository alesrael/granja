import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Home", layout="wide")

# Variaveis
#a = st.sidebar.radio('Menu:',["Pagina 1","Pagina 2"])
tabela = pd.read_csv("Leitoas-2024-01-08.csv", sep=",")

df = pd.DataFrame(tabela)

raca_unica = df['Raça'].unique()
raca = st.sidebar.multiselect('Selecione a Raça', raca_unica)

df['Ultimo cio'] = pd.to_datetime(df['Ultimo cio'])

# Adicionar filtro de data no Streamlit
data_inicio = st.sidebar.date_input('Selecione a data de início:', format="DD/MM/YYYY")
data_fim = st.sidebar.date_input('Selecione a data de fim:', format="DD/MM/YYYY")

# Filtrar o DataFrame com base nas datas selecionadas
df = df[(df['Ultimo cio'] >= pd.to_datetime(data_inicio)) & (df['Ultimo cio'] <= pd.to_datetime(data_fim))]

# Filtrar o DataFrame com base na raça selecionada
df = df[df['Raça'].isin(raca)]

idade = st.sidebar.number_input("Idade maior que:", value=225)
df = df[df['Idade']>= idade]

#reseta o indice da tabela
df = df.reset_index(drop=True)

# Mostrar o DataFrame filtrado
st.write(f'DataFrame filtrado para a raça {raca}:')
st.write(df, use_column_width=True)

cores_por_raça = {
                    'TLLZZ - TN70': 'blue',
                    'TZZZZ - AVÓ':'red'
}

plotgrafico = px.scatter(tabela, x="Idade", y="TSI", color="Raça", color_discrete_map=cores_por_raça)
st.plotly_chart(plotgrafico, use_container_width=True)