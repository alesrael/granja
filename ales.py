from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak

import pandas as pd

# Supondo que você tenha um DataFrame chamado 'df' com as informações desejadas
# Aqui está um exemplo fictício
data = {'Brinco': [101, 102, 103],
        'Previsão de Cio': ['2024-02-20', '2024-02-21', '2024-02-22'],
        'Idade no Dia da Previsão': [20, 22, 18]}
df = pd.DataFrame(data)

# Nome do arquivo PDF de saída
output_pdf = 'informacoes_laiteiras.pdf'

# Função para criar o PDF
def create_pdf(df, output_pdf):
    # Define um estilo para o título e outro para o corpo do texto
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('Title', parent=styles['Title'], alignment=1, spaceAfter=12)  # Centralizado
    body_style = ParagraphStyle('BodyText', parent=styles['BodyText'], spaceAfter=12, alignment=1, spaceBefore=12)  # Centralizado

    # Criação do documento PDF
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)

    # Lista para armazenar os elementos do PDF
    elements = []

    # Itera sobre as linhas do DataFrame para adicionar informações ao PDF
    for index, row in df.iterrows():
        brinco = str(row['Brinco'])
        previsao_cio = str(row['Previsão de Cio'])
        idade = str(row['Idade no Dia da Previsão'])

        # Adiciona uma quebra de página para a próxima linha do DataFrame (exceto na primeira iteração)
        if index > 0:
            elements.append(PageBreak())

        # Adiciona informações ao PDF
        # Alinha o Brinco no meio da página ocupando 50% da largura
        brinco_paragraph = Paragraph(f'<b>{brinco}</b>', title_style)
        brinco_paragraph.wrapOn(doc, 300, 100)  # 50% da largura da página
        brinco_paragraph.drawOn(doc, doc.width / 4, doc.height / 2)

        # Adiciona a Previsão de Cio de ponta cabeça
        previsao_cio_paragraph = Paragraph(f'<b>Previsão de Cio:</b> {previsao_cio}', body_style)
        previsao_cio_paragraph.wrapOn(doc, 100, 100)
        previsao_cio_paragraph.drawOn(doc, doc.width / 2, doc.height - 50)

        # Adiciona a Idade no Dia da Previsão
        elements.append(Paragraph(f'<b>Idade no Dia da Previsão:</b> {idade}', body_style))

    # Adiciona os elementos ao documento PDF
    doc.build(elements)

# Chama a função para criar o PDF
create_pdf(df, output_pdf)
