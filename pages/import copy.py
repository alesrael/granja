# Código Streamlit completo
import streamlit as st
import pandas as pd
import re

# Configurar a página
st.title('Importar planilha com dados brutos')
# Adicionar widget de upload de arquivo Excel
arquivo_excel = st.file_uploader('Escolha um arquivo Excel (xls ou xlsx)', type=['xls', 'xlsx'])


# Verificar se o arquivo foi enviado
if arquivo_excel is not None:
    # Ler o arquivo Excel e criar um DataFrame
    try:
        conteiner = st.container(border=True)
        col1, col2 = st.columns(2)
        
        df = pd.read_excel(arquivo_excel, skiprows=3)
        colunas_a = ['Leitoa', 'Data de Entrada', 'Data de Nascimento', 'Raça']
        df = df[colunas_a]
        separadores = ['x', '-', '*', 'X']
        df = df.dropna()
        # Criando uma expressão regular para dividir com base na lista de caracteres
        padrao = '|'.join(map(re.escape, separadores))  # Cria um padrão regex para divisão

        
        # Dividindo a coluna 'Nomes' com base na lista de caracteres
        df[['Brinco', 'Correspondente', 'Tatuagem']] = df['Leitoa'].str.split(padrao, expand=True)
        
        
        colunas_uteis = ['Leitoa', 'Data de Entrada', 'Data de Nascimento', 'Raça','Brinco', 'Correspondente','Tatuagem']
        df = df[df['Leitoa'] != "Leitoa"]
        
        df.loc[df['Brinco'].str.startswith('BMB'), 'Tatuagem'] = df['Brinco']

        colunas_b = ['Brinco', 'Tatuagem', 'Correspondente', 'Data de Nascimento', 'Data de Entrada', 'Raça']
        
        colunas_a_remover = ['Brinco', 'Tatuagem', 'Correspondente']
        
        for coluna in colunas_a_remover:
            df[coluna] = df[coluna].str.replace('BMB', '').str.replace('W', '').str.replace('S', '')

        
        df = df[colunas_b]
        
        linhas_com_valores_em_branco = df[df.isna().any(axis=1)]
        
        contem_branco = df.isnull().values.any()
        if contem_branco:
            st.write("Linhas com algum valor em branco:")
            st.dataframe(linhas_com_valores_em_branco, use_container_width=True, hide_index=True)

        st.link_button("Ir para planilha", "https://docs.google.com/spreadsheets/d/1Luu42-A8elsomwMMCfbLBKjEG8H8LaSnKPMK0QcDgS8/edit#gid=1382343527", type="primary")

        # Exibir o DataFrame
        contagem = df['Brinco'].count()
        st.info(f'Quantidade de leitoas: **{contagem}**')
        st.data_editor(df.style.highlight_null(), use_container_width=True, hide_index=True)
        

        ales = st.button("Download")
        
        if ales:
            df.to_csv('seu_arquivo.csv', index=False)
            st.write("Seu arquivo foi salvo como 'eu_aqruivo.csv'")
        
        
    except Exception as e:
        st.error(f"Erro ao ler o arquivo Excel: {e}")

        
        
        
        
        
