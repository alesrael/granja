import streamlit as st
from PyPDF2 import PdfMerger

st.set_page_config(page_title="Unir PDFs", page_icon="3616504.png")

#css e html
st.markdown("""
            <style>
                .st-emotion-cache-9ycgxx {
                    margin-bottom: 0.25rem;
                    display:none;
                }
            </style>
            
            """, unsafe_allow_html=True)

def merge_pdfs(uploaded_files):
    merged_pdf = PdfMerger()

    for file in uploaded_files:
        merged_pdf.append(file)

    output_filename = 'PDFs/MESCLADO.pdf'
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

        if st.button("Mesclar PDFs"):
            output_filename = merge_pdfs(uploaded_files)
            st.success("Para acessar o arquivo digite **pdfs** no prompt do Anaconda")
            #st.success(f"PDFs mesclados com sucesso. [Clique aqui para baixar o arquivo mesclado]({output_filename})")
if __name__ == "__main__":
    main()
