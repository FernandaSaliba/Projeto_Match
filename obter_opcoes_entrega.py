def obter_opcoes_entrega(cep):
    opcoes_entrega = []
    if cep:
        opcoes_entrega.append("1. Entrega padrão")
        opcoes_entrega.append("2. Entrega expressa")
    return opcoes_entrega
