def obter_opcoes_entrega(cep):
    opcoes_entrega = []
    if cep:
        # Verifique o CEP e adicione as opções de entrega com base no CEP aqui
        # Neste exemplo, adicionaremos apenas duas opções fictícias.
        opcoes_entrega.append("1. Entrega padrão")
        opcoes_entrega.append("2. Entrega expressa")
    return opcoes_entrega
