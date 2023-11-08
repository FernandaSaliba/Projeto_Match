from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def gerar_pdf(cep, cpf, convidados, carne, bebida, tipo_entrega, resultado_cep):
    pdf_filename = "resultados_churrasco.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.drawString(72, 750, "Resultados do Churrasco:")
    c.drawString(72, 725, f"CEP: {cep}")
    c.drawString(72, 705, f"CPF: {cpf}")
    c.drawString(72, 685, f"Número de Convidados: {convidados}")
    c.drawString(72, 665, f"Carne Necessária: {carne:.2f} kg")
    c.drawString(72, 645, f"Bebida Necessária: {bebida:.2f} litros")
    c.drawString(72, 625, f"Tipo de Entrega: {tipo_entrega}")
    c.drawString(72, 605, f"Endereço Completo: {resultado_cep.get('endereco_completo', '')}")
    c.save()
    return pdf_filename
