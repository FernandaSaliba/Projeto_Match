from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def gerar_pdf(cep, cpf, convidados, carne, bebida, tipo_entrega, resultado_cep):
    pdf_filename = "resultados_churrasco.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Define a fonte e o tamanho para melhor formatação
    c.setFont("Helvetica", 12)

    # Define as margens e a largura da linha para melhor layout
    margin = 72
    width, height = letter
    width -= 2 * margin
    line_height = 14

    # Função para adicionar texto com quebra de linha
    def add_text(x, y, text):
        lines = text.split('\n')
        for line in lines:
            c.drawString(x, y, line)
            y -= line_height

    # Adiciona texto formatado ao PDF
    c.drawString(margin, height - margin, "Resultados do Churrasco:")
    c.drawString(margin, height - margin - line_height, f"CEP: {cep}")
    c.drawString(margin, height - margin - 2 * line_height, f"CPF: {cpf}")
    c.drawString(margin, height - margin - 3 * line_height, f"Número de Convidados: {convidados}")
    c.drawString(margin, height - margin - 4 * line_height, f"Carne Necessária: {carne:.2f} kg")
    c.drawString(margin, height - margin - 5 * line_height, f"Bebida Necessária: {bebida:.2f} litros")
    c.drawString(margin, height - margin - 6 * line_height, f"Tipo de Entrega: {tipo_entrega}")

    # Adiciona o endereço completo com quebra de linha
    endereco_text = f"Endereço Completo: {resultado_cep.get('endereco_completo', '')}"
    add_text(margin, height - margin - 7 * line_height, endereco_text)

     
    c.save()
    return pdf_filename
