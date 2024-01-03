import streamlit as st
from PyPDF2 import PdfMerger
import os
from tkinter import filedialog

st.set_page_config(page_title="Mesclar PDFs", page_icon=":smiley:")

def merge_pdfs(uploaded_files, output_path):
    merged_pdf = PdfMerger()

    for file in uploaded_files:
        merged_pdf.append(file)

    output_filename = os.path.join(output_path, 'merged_output.pdf')
    with open(output_filename, 'wb') as output_file:
        merged_pdf.write(output_file)

    return output_filename

def main():
    st.title("Mesclar PDFs")

    uploaded_files = st.file_uploader("Selecione os arquivos PDF para mesclar", type="pdf", accept_multiple_files=True)

    if uploaded_files:
        st.write("Arquivos selecionados:")
        for file in uploaded_files:
            st.write(file.name)

        st.sidebar.subheader("Escolha o diretório para salvar o arquivo mesclado:")
        output_path = st.sidebar.text_input("Caminho do diretório:", "")
        
        if st.sidebar.button("Selecionar diretório"):
            output_path = filedialog.askdirectory()

        if st.button("Mesclar PDFs") and output_path:
            os.makedirs(output_path, exist_ok=True)

            output_filename = merge_pdfs(uploaded_files, output_path)
            st.success(f"PDFs mesclados com sucesso. [Clique aqui para baixar o arquivo mesclado]({output_filename})")

if __name__ == "__main__":
    main()
