import streamlit as st
import pandas as pd
#from PyPDF2 import PdfMerger

st.set_page_config(page_title="Home")

# Variaveis
a = st.sidebar.radio('Menu:',["Pagina 1","Pagina 2"])
tabela = pd.read_csv("flush.csv", sep=",")

#trecho para xibir caixa de codigo
st.echo()
with st.echo():
    st.write('Code will be executed and printed')

#st.dataframe(tabela)

#st.dataframe(tabela.style.highlight_max(axis=0))

# st.json({f'foo':'bar','fu':'ba'})
# st.metric(label="Temp", value="273 K", delta="1.2 K")

df = pd.DataFrame(tabela)
df['Brinco'] = df['Brinco'].astype(int)
selected_raça = st.sidebar.selectbox('Selecione a Raça', df['Raça'].unique())

# Filtrar o DataFrame com base na raça selecionada
filtered_df = df[df['Raça'] == selected_raça]

# Mostrar o DataFrame filtrado
st.write(f'DataFrame filtrado para a raça {selected_raça}:')
st.write(filtered_df)

st.dataframe(df)
