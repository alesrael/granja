from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
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
    c = canvas.Canvas(output_pdf, pagesize=letter)

    # Itera sobre as linhas do DataFrame para adicionar informações ao PDF
    for index, row in df.iterrows():
        brinco = str(row['Brinco'])
        previsao_cio = str(row['Previsão de Cio'])
        idade = str(row['Idade no Dia da Previsão'])

        # Adiciona informações ao PDF
        c.drawString(100, 700, f'Brinco: {brinco}')
        c.drawString(100, 680, f'Previsão de Cio: {previsao_cio}')
        c.drawString(100, 660, f'Idade no Dia da Previsão: {idade}')

        # Adiciona uma quebra de página para a próxima linha do DataFrame
        c.showPage()

    # Salva o PDF
    c.save()

# Chama a função para criar o PDF
create_pdf(df, output_pdf)
